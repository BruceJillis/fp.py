# State

class State:
	"State represents a G-machine state"
	def __init__(self, code, stats):
		self.code = []
		self.globals = Globals(code)
		self.stack = Stack()
		self.heap = Heap()
		self.stats = stats
	
	def result(self):
		return self.stack.pop()

# State Components

class Stats:
	pass

class Globals:
	pass

class Heap:
	pass

class Stack:
	pass

# Nodes

class Node:
	"base node for all runtime value representations"
	pass

class NGlobal(Node):
	"represents an combinator at runtime"
	def __init__(self, n, code, name):
		self.n = int(n)
		self.code = code
		self.name = name
	
	def __repr__(self):
		return 'NGlobal(%s, %s)' % (self.n, self.name)

class NApply(Node):
	"represents an application of two expressions at runtime"
	def __init__(self, a1, a2):
		self.a1 = a1
		self.a2 = a2

	def __repr__(self):
		return 'NApply(%s, %s)' % (repr(self.a1), repr(self.a2))

class NNum(Node):
	"represents a number at runtime"
	def __init__(self, value):
		self.value = int(value)

	def __repr__(self):
		return 'NNum(%s)' % (self.value)

class NInd(Node):
	"represents an indirection at runtime"
	def __init__(self, a):
		self.a = int(a)

	def __repr__(self):
		return 'NInd(%s)' % (self.a)

class GMachine:
	def run(self, state):
		while len(state.code) > 0:
			pass
		return state.result()