import unittest
import coverage
import argparse, os, glob, antlr3, sys
from CoreLexer import CoreLexer
from CoreParser import CoreParser
from visitors import Identification, CodeGeneration
from gmachine import State, SymbolTable, run

# define the command line parser
parser = argparse.ArgumentParser(description='Compiler for the miranda-style functional language FP.')
parser.add_argument('file', nargs='*', help='.core file to compile and evaluate')
parser.add_argument('--include', action='append', dest="include", default=[os.path.join('core', 'runtime')], help="include .core files in these directories (default: core/runtime/*.core)")
debug = parser.add_argument_group('debug', 'commandline options used during development on FPJS itself')
debug.add_argument('-v', '--verbose', action='store_true', dest="verbose", help="output a lot of information on the internals of the systems")
debug.add_argument('--stats', action='store_true', dest="stats", help="output stats for the execution of the program (nr. of steps, heap space used, pop/push/peeks, etc)")
debug.add_argument('--test', action='store_true', dest="test", default=False, help="run testsuite and report results")
debug.add_argument('--coverage', action='store_true', dest="coverage", default=False, help="run test, and record code coverage. report results")
debug.add_argument('--show-missing', action='store_true', dest="show_missing", default=False, help="show line numbers that were not covered by the testsuite in the --coverage report")
debug.add_argument('--no-includes', action='store_true', dest="no_includes", default=False, help="do not include any external files (--include) except those supplied on the commandline")
args = parser.parse_args()

if args.coverage:
	args.coverage = True
	cov = coverage.coverage(auto_data=True, include=["visitors.py", "gmachine.py", "common.py"])
	cov.start()

if args.test:
	# run test suite and exit
	unittest.main('CoreTest', 'CoreTest', sys.argv[1:])

if args.coverage:
	cov.stop()
	cov.report(file=sys.stdout, show_missing=args.show_missing, ignore_errors=True)
	exit()

if len(args.file) == 0:
	parser.error("no files supplied");

def files(paths, pattern, recursive = False):
	"generate all files corresponding to glob pattern in all paths. if recursive then do this recursively"
	while len(paths) > 0:
		# while we have paths to scan
		path, paths = paths[:1][0], paths[1:]
		for filename in glob.glob(os.path.join(path, pattern)):
			# yield all filenames corresponding to pattern
			yield filename
		if recursive:
			# find all immediate subpaths and append them to the list of paths to scan
			for subpath in os.listdir(path):
				if os.path.isdir(os.path.join(path, subpath)):
					paths.append(os.path.join(path, subpath))
	raise StopIteration

def parse(filename):
	'parse an file into an ast'
	if not os.path.exists(filename):
		raise Exception('file not found: %s.' % (filename))
	with open(filename) as f:
		stream = antlr3.ANTLRInputStream(f)
		lexer = CoreLexer(stream)
		tokens = antlr3.CommonTokenStream(lexer)
		parser = CoreParser(tokens)
		ast = parser.program()
		return ast.tree

def process(filename):
	'deprecated: small helper function that defines the compiler stages. parse the file, process the ast'
	ast = parse(filename)
	identification.visit(ast)
	codegeneration.visit(ast)

def printcode(name):
	'small helper function to easily and quickly print the gmachine code for a combinator'
	print '%s = %s' % (name, str(symtab[name][SymbolTable.CODE]))

# symbol table for global registration of info 
symtab = SymbolTable()

# phases of the compiler
identification = Identification(symtab)
codegeneration = CodeGeneration(symtab)

# do actual work: compile all the supplied files including the include directories (recursively if necessary)
# do this in two phases to make sure we have all needed info (we need to know all combinators in a file, and 
# across files) before we start compilation
asts = []
if not args.no_includes:
	for filename in files(args.include, '*.core'):
		ast = parse(filename)
		identification.visit(ast)
		asts.append(ast)
for filename in args.file:
	ast = parse(filename)
	identification.visit(ast)
	asts.append(ast)
# compile all the asts (files)
for ast in asts:
	# print ast.toStringTree()
	codegeneration.visit(ast)
# construct initial state and run the resulting program
state = State(symtab)
# printcode('main')
print	run(state, args.verbose)

# output stats for the execution of the program
if args.verbose or args.stats:
	print '\n--'
	print state.stats