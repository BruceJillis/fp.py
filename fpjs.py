import argparse
import os
import glob

import antlr3
import antlr3.extras
import antlr3.tree

from common import *

from CoreLexer import CoreLexer
from CoreParser import CoreParser
from CoreAnalyzer import CoreAnalyzer
from CoreCompiler import CoreCompiler

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

def compile(filename, info, code):
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

def files(paths, pattern):
	for path in paths:
		for filename in glob.glob(os.path.join(path, pattern)):
			yield filename
	raise StopIteration

def process(filename, info, code):
	if os.path.exists(filename):
		file = compile(filename, info, code)

info = Information()
code = Code()

# do actual work, compile all the files from the include directories (recursively if necessary)
for filename in files(args.include, '*.cor'):
	process(filename, info, code)
# compile actual files
for filename in args.files:
	process(filename, info, code)

# evaluate the generated code
gm = GMachine(code)
print gm.run()
print gm.stats