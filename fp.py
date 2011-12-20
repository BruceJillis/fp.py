import argparse, os, glob, antlr3, sys
from CoreLexer import CoreLexer
from CoreParser import CoreParser
from visitors import Identification, CodeGeneration, PrettyPrinter
from transforms import CaseLifter, LambdaLifter, LambdaSplitter
from gmachine import State, SymbolTable, run

def files(paths, pattern, recursive = False):
	"generate all files corresponding to a glob pattern in all paths. if recursive is True then do this recursively for paths found during traversal."
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
	'parse a file into an ast'
	if not os.path.exists(filename):
		raise Exception('file not found: %s.' % (filename))
	with open(filename) as f:
		stream = antlr3.ANTLRInputStream(f)
		lexer = CoreLexer(stream)
		tokens = antlr3.CommonTokenStream(lexer)
		parser = CoreParser(tokens)
		ast = parser.program()
		for combinator in ast.tree.combinators():
			symtab.combinators[combinator.name()] = True
		return ast.tree

def transform(ast):
	"perform transformations on the supplied ast"
	lambdasplitter.visit(ast)
	lambdalifter.visit(ast)
	caselifter.visit(ast)
	return ast

def printcode(name):
	'small helper function to easily and quickly print the gmachine code for a combinator'
	print '%s = %s' % (name, str(symtab[name][SymbolTable.CODE]))

# define the command line parser
parser = argparse.ArgumentParser(description='Compiler for the miranda-style functional language FP.')
parser.add_argument('file', nargs='*', help='.core file to compile and evaluate')
parser.add_argument('--include', action='append', dest="include", default=[os.path.join('core', 'runtime')], help="include .core files in these directories (default: core/runtime/*.core)")

# debug options
debug = parser.add_argument_group('debug', 'commandline options used during development on FPJS itself')
debug.add_argument('-v', '--verbose', action='store_true', dest="verbose", help="output a lot of information on the internals of the systems")
debug.add_argument('--stats', action='store_true', dest="stats", help="output stats for the execution of the program (nr. of steps, heap space used, pop/push/peeks, etc)")
debug.add_argument('--test', action='store_true', dest="test", default=False, help="run testsuite and report results")
debug.add_argument('--coverage', action='store_true', dest="coverage", default=False, help="run test, record code coverage and report results")
debug.add_argument('--show-missing', action='store_true', dest="show_missing", default=False, help="show line numbers that were not covered by the testsuite in the --coverage report")
debug.add_argument('--no-includes', action='store_true', dest="no_includes", default=False, help="do not include any external files (--include) except those supplied as positional arguments")
args = parser.parse_args()

# handle coverage command line argument
if args.coverage:
	import coverage
	args.test = True
	if len(sys.argv) > 2:
		sys.argv = [sys.argv[1]] + sys.argv[2:]
	cov = coverage.coverage(auto_data=True, include=["visitors.py", "gmachine.py", "transforms.py"])
	cov.start()
	# fall through to the test code

# run test suite
if args.test:
	import unittest
	# run test suite and exit
	unittest.main(module="tests", argv=sys.argv[1:], exit=not args.coverage)

# finish up coverage handling, show the report
if args.coverage:
	cov.stop()
	cov.report(file=sys.stdout, show_missing=args.show_missing, ignore_errors=True)
	exit()

# symbol table for global registration of info 
symtab = SymbolTable()

# phases of the compiler
identification = Identification(symtab)
codegeneration = CodeGeneration(symtab)

# transformations
caselifter = CaseLifter(symtab)
lambdasplitter = LambdaSplitter()
lambdalifter = LambdaLifter(symtab)

# misc
prettyprinter = PrettyPrinter()


# do actual work: compile all the supplied files including the include directories (recursively if necessary)
# do this in two phases to make sure we have all needed info (we need to know all combinators in a file, and 
# across files) before we start compilation
if len(args.file) == 0:
	parser.error("no files supplied")
asts = []
if not args.no_includes:
	for filename in files(args.include, '*.core'):
		ast = parse(filename)
		ast = transform(ast)
		identification.visit(ast)
		asts.append(ast)
for filename in args.file:
	ast = parse(filename)
	# prettyprinter.visit(ast)
	ast = transform(ast)
	identification.visit(ast)
	# prettyprinter.visit(ast)
	asts.append(ast)
# compile all the asts (files)
for ast in asts:
	codegeneration.visit(ast)
# construct initial state and run the resulting program
state = State(symtab)
#printcode('main')
print	run(state, args.verbose)

# output stats for the execution of the program
if args.verbose or args.stats:
	print '\n--'
	print state.stats