import argparse, os, glob

import antlr3
from CoreLexer import CoreLexer
from CoreParser import CoreParser

parser = argparse.ArgumentParser(description='Compiler for the miranda-style functional language FP.')
parser.add_argument('file', nargs='+', help='.core file to compile and evaluate')
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
			# find all immediate subpaths and append them to the list of path to scan
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

# do actual work, compile all the supplied files including the include directories (recursively if necessary)
for filename in args.file:
	ast = parse(filename)