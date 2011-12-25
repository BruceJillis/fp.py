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
			symtab[combinator.name()] = combinator
		return ast.tree

def transform(ast, prettyprint):
	"perform transformations on the supplied ast"
	def show(msg, ast):
		if prettyprint:
			print msg
			print
			prettyprinter.visit(ast)
			print '-' * 40
			print

	show('before', ast)
	# lambdasplitter.visit(ast)
	# show('lambda splitter', ast)
	lambdalifter.visit(ast)
	show('lambda lifter', ast)
	caselifter.visit(ast)
	show('case / pack lifter', ast)
	return ast

def printcode(name):
	'small helper function to easily and quickly print the gmachine code for a combinator'
	print '%s = %s' % (name, str(symtab[name].code))

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
parser.add_argument('--print-code', action='append', dest="printcode", default=[], help="print gmachine instructions for the supplied combinators")
parser.add_argument('--show-transformations', action='store_true', dest="show_transformations", default=[], help="prettyprint the program before, during and after the transformation step")
args = parser.parse_args()

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

# do actual work: compile all the supplied files including the include directories (recursively if necessary)
# do this in two phases to make sure we have all needed info (we need to know all combinators in a file, and
# across files) before we start compilation
if len(args.file) == 0:
	parser.error("no files supplied")
asts = []
if not args.no_includes:
	for filename in files(args.include, '*.core'):
		ast = parse(filename)
		ast = transform(ast, args.show_transformations)
		identification.visit(ast)
		asts.append(ast)
for filename in args.file:
	ast = parse(filename)
	# prettyprinter.visit(ast)
	ast = transform(ast, args.show_transformations)
	identification.visit(ast)
	# prettyprinter.visit(ast)
	asts.append(ast)
print ast.toStringTree()
# compile all the asts (files)
for ast in asts:
	codegeneration.visit(ast)
# print any code sequences the user wants to see
for combinator in args.printcode:
	printcode(combinator)

print symtab.data['main'].code
print
print symtab.data['$sc1'].code

# construct initial state and run the resulting program
state = State(symtab)
print	'result:', run(state, args.verbose)

# output stats for the execution of the program
if args.verbose or args.stats:
	print '\n--'
	print state.stats