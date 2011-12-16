import unittest, os, antlr3, StringIO, random
from CoreLexer import CoreLexer
from CoreParser import CoreParser
from visitors import Identification, CodeGeneration
from gmachine import Heap, State, SymbolTable

class HeapTest(unittest.TestCase):
	def setUp(self):
		self.symtab = SymbolTable()
		self.state = State(self.symtab)
		self.heap = self.state.heap

	def test_store(self):
		a = self.heap.store('test')
		self.assertEqual(self.heap[a], 'test')

	def test_store_contains(self):
		a = self.heap.store('test')
		self.assertTrue(a in self.heap)

	@unittest.expectedFailure
	def test_store_free(self):
		a = self.heap.store('test')
		self.heap.free(a)
		self.assertEqual(self.heap[a], 'test')

class StackTest(unittest.TestCase):
	def setUp(self):
		self.symtab = SymbolTable()
		self.state = State(self.symtab)
		self.stack = self.state.stack

	def test_push(self):
		self.stack.push('test')
		self.assertEqual(self.stack.pop(), 'test')

	def test_push1(self):
		self.stack.push('test1')
		self.stack.push('test2')
		self.assertEqual(self.stack.pop(), 'test2')
		self.assertEqual(self.stack.pop(), 'test1')

	def test_push2(self):
		self.stack.push(1)
		self.assertEqual(self.stack.peek(), 1)
		self.assertEqual(self.stack.pop(), 1)

	def test_push3(self):
		self.stack.push(1)
		self.assertEqual(self.stack.peek(), 1)
		self.stack.push(2)
		self.assertEqual(self.stack.peek(), 2)
		self.assertEqual(self.stack.pop(), 2)
		self.assertEqual(self.stack.pop(), 1)

	def test_append(self):
		self.stack.append([1,2,3])
		self.assertEqual(self.stack.pop(), 3)
		self.assertEqual(self.stack.pop(), 2)
		self.assertEqual(self.stack.pop(), 1)

	def test_bottom(self):
		self.stack.append([1,2,3])
		self.assertEqual(self.stack.bottom(), 1)
		self.assertEqual(self.stack.pop(), 3)
		self.assertEqual(self.stack.pop(), 2)
		self.assertEqual(self.stack.pop(), 1)

	def test_empty(self):
		self.assertTrue(self.stack.empty())
		self.stack.append([1])
		self.assertFalse(self.stack.empty())
		self.stack.push(2)
		self.assertFalse(self.stack.empty())
		self.assertEqual(self.stack.pop(), 2)
		self.assertFalse(self.stack.empty())
		self.assertEqual(self.stack.pop(), 1)
		self.assertTrue(self.stack.empty())

	def test_size(self):
		self.assertTrue(self.stack.empty())
		self.stack.append([1])
		self.stack.push(2)
		self.assertEqual(len(self.stack), 2)
		self.assertEqual(self.stack.pop(), 2)
		self.assertEqual(self.stack.pop(), 1)
		self.assertTrue(self.stack.empty())

class DumpTest(unittest.TestCase):
	def setUp(self):
		self.symtab = SymbolTable()
		self.state = State(self.symtab)
		self.dump = self.state.dump

	def test_push(self):
		self.dump.push(1)
		self.assertEqual(self.dump.pop(), 1)

	def test_empty(self):
		self.dump.push(1)
		self.assertEqual(self.dump.pop(), 1)
		self.assertTrue(self.dump.empty())

	def test_empty2(self):
		self.dump.push(1)
		self.assertFalse(self.dump.empty())
		self.assertEqual(self.dump.pop(), 1)
		self.assertTrue(self.dump.empty())