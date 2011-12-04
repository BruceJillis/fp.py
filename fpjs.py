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

class GMachine:
	def __init__(self, code):
		self._code = code
		self.code = [(Code.PUSH_GLOBAL, 'main'), (Code.UNWIND,)]
		self.stack = []
		self.globals = Globals()
		self.heap = Heap(code, self.globals)
		self.stats = Statistics(self)

	def print_code(self):
		result = []
		for instr in self.code:
			result.append(self._code.to_str(instr))
		print ', '.join(result)

	def print_stack(self):
		result = []
		for addr in self.stack:
			result.append("[%s:%s]" % (str(addr), str(self.heap[addr])))
		print ', '.join(result)

	def print_heap(self):
		result = []
		for addr in self.heap.iter():
			result.append("<%s:%s>" % (str(addr), str(self.heap[addr])))
		print '\n'.join(result)

	def run(self):
		self.stats.start()
		while len(self.code) > 0:
			print "-------\nstep", self.stats.steps
			print "code :",
			self.print_code()
			print "stack:",			
			self.print_stack()
			print "heap:"		
			self.print_heap()
			print '=======\n'
			i, self.code = self.code[:1][0], self.code[1:]
			if i[0] == Code.PUSH_GLOBAL:
				a = self.globals[i[1]]
				self.stack.append(a)
			elif i[0] == Code.PUSH_INT:
				if str(i[1]) in self.globals:
					a = self.globals[str(i[1])]
				else:
					a = self.heap.alloc(NNum(i[1]))
					self.globals[str(i[1])] = a
				self.stack.append(a)
			elif i[0] == Code.PUSH:
				a = self.stack[-(i[1]+2):][0]
				a = self.heap[a].a2
				self.stack.append(a)
			elif i[0] == Code.APPLY:
				a1 = self.stack.pop()
				a2 = self.stack.pop()
				a = self.heap.alloc(NApply(a1, a2))
				self.stack.append(a)
			elif i[0] == Code.UNWIND:
				a = self.stack[-1:][0]
				o = self.heap[a]
				if o.__class__ == NGlobal:
					n = o.nargs
					while n > 0:
						n -= 1
					self.code = o.code
				elif o.__class__ == NApply:
					self.stack.append(o.a1)
					self.code = [(Code.UNWIND,)] + self.code
				elif o.__class__ == NNum:
					self.code = []
					self.stack.append(o)
					break
			elif i[0] == Code.SLIDE:
				a = self.stack.pop()
				i = i[1]
				while i >= 1:
					self.stack.pop()
					i -= 1
				self.stack.append(a)					
			else:
				raise Exception('unknown instruction: ' + str(i))
			self.stats.step()
		self.stats.stop()
		return self.stack.pop()

# evaluate the generated code
gm = GMachine(code)
print gm.run()
print gm.stats