import unittest, os, antlr3, StringIO, random
from CoreLexer import CoreLexer
from CoreParser import CoreParser
from visitors import Identification, CodeGeneration
from gmachine import State, SymbolTable, run

class CoreTest(unittest.TestCase):
	def setUp(self):
		self.reset()
	
	def reset(self):
		'reset the compiler'
		self.asts = []
		self._loaded = {}
		self.symtab = SymbolTable()
		self.id = Identification(self.symtab)
		self.cg = CodeGeneration(self.symtab)

	def load(self, filename):
		'load function list definitions'
		if filename in self._loaded:
			return
		ast = self.parse(filename)
		self.id.visit(ast)
		self.asts.append(ast)
		self._loaded[filename] = True

	def prelude(self):
		'load prelude definitions'
		self.load("core\\runtime\\prelude.core")

	def lists(self):
		'load functional-lists definitions'
		self.load("core\\tests\\lists.core")
		self.prelude()

	def compile(self, ast):
		for a in self.asts:
			self.cg.visit(a)
		self.cg.visit(ast)

	def parse(self, filename):
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

	def parse_str(self, content):
		stream = antlr3.ANTLRInputStream(StringIO.StringIO(content))
		lexer = CoreLexer(stream)
		tokens = antlr3.CommonTokenStream(lexer)
		parser = CoreParser(tokens)
		ast = parser.program()
		return ast.tree

	def run_str(self, content):
		ast = self.parse_str(content)
		self.id.visit(ast)
		self.compile(ast)
		state = State(self.symtab)
		return run(state), state
	
	def test_basic1(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = I %s" % (p));
		self.assertEqual(ans.value, p)

	def test_basic2(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("id = S K K; main = id %s" % (p));
		self.assertEqual(ans.value, p)

	def test_basic3(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("id = S K K; main = twice twice twice id %s" % (p));
		self.assertEqual(ans.value, p)

	def test_basic4(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = twice (I I I) %s" % (p));
		self.assertEqual(ans.value, p)

	def test_let1(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = let id1 = I I I in id1 id1 %s" % (p));
		self.assertEqual(ans.value, p)

	def test_let2(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = let a = 1, b = 2, c = 3, d = %s in K (K d a) b" % (p));
		self.assertEqual(ans.value, p)

	def test_let3(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = let a = 1, b = 2, c = 3, d = %s in K (K a a) b" % (p));
		self.assertEqual(ans.value, 1)

	def test_let4(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = let a = 1, b = 2, c = 3, d = %s in K (K b c) b" % (p));
		self.assertEqual(ans.value, 2)

	def test_let5(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = let a = 1, b = 2, c = 3, d = %s in K (K c a) d" % (p));
		self.assertEqual(ans.value, 3)

	def test_let6(self):
		self.reset()
		self.prelude()
		p = random.randint(0, 99999)
		ans, state = self.run_str("main = let a = %s in (let b = 1 in K a b)" % (p));
		self.assertEqual(ans.value, p)

	def test_lists(self):
		self.reset()
		self.load("core\\tests\\lists.core")
		self.assertEqual(len(self.symtab.root), 16)
		self.assertEqual(self.symtab.root.keys(), ['<=', '>=', 'nil', 'abort', '==', '+', '*', '-', 'tl', 'cons', 'hd', 'negate','if', '<', '__parent__', '>'])
		self.assertEqual(self.symtab.root['tl'][SymbolTable.COUNT], 1)
		self.assertEqual(self.symtab.root['hd'][SymbolTable.COUNT], 1)
		self.assertEqual(self.symtab.root['nil'][SymbolTable.COUNT], 2)
		self.assertEqual(self.symtab.root['cons'][SymbolTable.COUNT], 4)
		self.assertEqual(self.symtab.root['abort'][SymbolTable.COUNT], 0)

	def test_infinite(self):
		self.reset()
		self.lists()
		p = random.randint(0, 99999)
		ans, state = self.run_str("""
infinite x = cons x (infinite x);
main = hd (tl (tl (infinite %s)))
""" % (p))
		self.assertEqual(self.symtab.root['infinite'][SymbolTable.COUNT], 1)
		self.assertEqual(ans.value, p)

#	def test_infinite2(self):
#		pass
#		self.reset()
#		self.lists()
#		p = random.randint(0, 99999)
#		ans = self.run_str("""
#infinite x = letrec xs = cons x xs in xs;
#main = hd (tl (tl (infinite %s)))
#""" % (p))
#		self.assertEqual(self.symtab.root['infinite'][SymbolTable.COUNT], 1)
#		self.assertEqual(ans.value, p)