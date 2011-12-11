import argparse, os, glob

import antlr3
from CoreLexer import CoreLexer
from CoreParser import CoreParser
from common import SymbolTable
from visitors import Identification, CodeGeneration
from gmachine import State, run

# define the command line parser
parser = argparse.ArgumentParser(description='Compiler for the miranda-style functional language FP.')
parser.add_argument('file', nargs='+', help='.core file to compile and evaluate')
parser.add_argument('-i', '--include', action='append', dest="include", default=[os.path.join('core', 'runtime')], help="include .core files in these directories.")
parser.add_argument('-n', '--no-includes', action='store_true', dest="no_includes", default=False, help="override including external files (usefull for debugging).")
parser.add_argument('-v', '--verbose', action='store_true', dest="verbose", help="output a lot of information on the internals of the system.")
parser.add_argument('--stats', action='store_true', dest="stats", help="output stats for the execution of the program (nr. of steps, heap space used, pop/push/peeks, etc).")
args = parser.parse_args()

# we need at least 1 file to be supplied
if len(args.file) == 0:
	parser.error();

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
	'small helper function that defines the compiler stages. parse the file, process the ast'
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

# do actual work, compile all the supplied files including the include directories (recursively if necessary)
for filename in files(args.include, '*.core'):
	process(filename)
for filename in args.file:
	process(filename)
# construct initial state and run the resulting program
state = State(symtab)
printcode('Y')
printcode('K')
printcode('main')
print	run(state, args.verbose)

# output stats for the execution of the program
if args.verbose or args.stats:
	print '\n--'
	print state.stats