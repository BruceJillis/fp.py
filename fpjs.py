import argparse
import os
import glob

import antlr3
import antlr3.extras
import antlr3.tree

from common import Information, Code, Environment
from gmachine import GMachine

from CoreLexer import CoreLexer
from CoreParser import CoreParser
from CoreAnalyzer import CoreAnalyzer
from CoreCompiler import CoreCompiler

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

def process(filename, info, code):
	if not os.path.exists(filename):
		raise Exception('file not found: %s.' % (filename))
	with open(filename) as f:
		stream = antlr3.ANTLRInputStream(f)
		lexer = CoreLexer(stream)
		tokens = antlr3.CommonTokenStream(lexer)
		parser = CoreParser(tokens)
		ast = parser.start()
		tokens = antlr3.tree.CommonTreeNodeStream(ast.tree)
		analyzer = CoreAnalyzer(tokens)
		analyzer.start(info)
		tokens = antlr3.tree.CommonTreeNodeStream(ast.tree)
		compiler = CoreCompiler(tokens)
		compiler.start(info, code)

parser = argparse.ArgumentParser(description='Compiler for the functional language FP.')
parser.add_argument('files', nargs='+', help='.core files to compile')
parser.add_argument('-i', '--include', action='store_true', dest="include", default=[os.path.join('core', 'runtime')], help="include .cor files in these directories.")
parser.add_argument('-r', '--recursive', action='store_true', dest="recursive", help="scan all directories recursively.")
parser.add_argument('-m', '--minimize', action='store_true', dest="minimize", help="minimize all generated .js files.")
parser.add_argument('-b', '--bundle', action='store_true', dest="bundle", help="bundle all .js files.")
parser.add_argument('-c', '--core', action='store_const', const='core', dest="language", default="core", help="set compiler to expect Core input (default).")
args = parser.parse_args()

if len(args.files) == 0:
	parser.error();

info = Information()
code = Code()

# do actual work, compile all the files from the include directories (recursively if necessary)
for filename in files(args.include, '*.cor'):
	process(filename, info, code)
# compile actual files
for filename in args.files:
	process(filename, info, code)

# evaluate the generated code
print code.combinators['Y'][0]
result = []
for instr in code.combinators['Y'][0]:
	result.append(code.to_str(instr))
print ', '.join(result)
gm = GMachine(code)
print gm.run()
print gm.stats