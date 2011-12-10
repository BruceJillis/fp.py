import argparse, os, glob

import antlr3
from CoreLexer import CoreLexer
from CoreParser import CoreParser
from common import SymbolTable
from visitors import *
from gmachine import State, Stats, run

parser = argparse.ArgumentParser(description='Compiler for the miranda-style functional language FP.')
parser.add_argument('file', nargs='+', help='.core file to compile and evaluate')

parser.add_argument('-v', '--verbose', action='store_true', dest="verbose", help="output a lot of information on the internals of the system.")
args = parser.parse_args()

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
	if not os.path.exists(filename):
		raise Exception('file not found: %s.' % (filename))
	with open(filename) as f:
		stream = antlr3.ANTLRInputStream(f)
		lexer = CoreLexer(stream)
		tokens = antlr3.CommonTokenStream(lexer)
		parser = CoreParser(tokens)
		ast = parser.program()
		return ast.tree

# symbol table for global registration of info 
symtab = SymbolTable()
stats = Stats()

# phases of the compiler
identification = Identification(symtab)
codegeneration = CodeGeneration(symtab)

# do actual work, compile all the supplied files including the include directories (recursively if necessary)
for filename in args.file:
	ast = parse(filename)
	identification.visit(ast)
	codegeneration.visit(ast)

def printcode(name):
	print name, str(symtab[name]['__code__'])

state = State(symtab, stats)
print	run(state, args.verbose)