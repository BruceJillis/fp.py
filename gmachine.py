from common import SymbolTable
from collections import defaultdict
import time

# Code
class Code:
	"this class represents a sequence of G-machine instructions" 

	PUSH   = 1
	PUSHG  = 2
	PUSHI  = 3
	UNWIND = 4
	APPLY  = 5
	UPDATE = 6
	POP    = 7
	SLIDE  = 8
	ALLOC  = 9
	EVAL   = 10

	ADD = 11
	SUB = 12
	MUL = 13
	DIV = 14
	NEG = 15

	EQ = 16
	NEQ = 17
	LT = 18
	LTE = 19
	GT = 20
	GTE = 21
	
	COND = 22

	def __init__(self):
		self.instructions = []
	
	# factory functions for all instructions

	def Alloc(self, value):
		self.instructions.append((Code.ALLOC, int(value)))

	def Slide(self, value):
		self.instructions.append((Code.SLIDE, int(value)))

	def Update(self, value):
		self.instructions.append((Code.UPDATE, int(value)))

	def Pop(self, value):
		self.instructions.append((Code.POP, int(value)))

	def Apply(self):
		self.instructions.append((Code.APPLY,))

	def Unwind(self):
		self.instructions.append((Code.UNWIND,))

	def Eval(self):
		self.instructions.append((Code.EVAL,))

	def Add(self):
		self.instructions.append((Code.ADD,))

	def Push(self, index, name = ''):
		self.instructions.append((Code.PUSH, index))

	def PushInt(self, value):
		self.instructions.append((Code.PUSHI, int(value)))

	def PushGlobal(self, name):
		self.instructions.append((Code.PUSHG, name))

	def __repr__(self):
		return str(self)

	def __str__(self):
		result = ''
		for i in self.instructions:
			result += '%s\n' % (code_to_str(i))
		return result

def code_to_str(instr):
	"small helper function to prettyprint a instruction without needing a Code instance"
	str = None
	if instr[0] == Code.PUSH:
		str = "PUSH %s" % (instr[1])
	if instr[0] == Code.PUSHG:
		str = "PUSHG %s" % (instr[1])
	if instr[0] == Code.PUSHI:
		str = "PUSHI %s" % (instr[1])
	if instr[0] == Code.UNWIND:
		str = "UNWIND"
	if instr[0] == Code.UPDATE:
		str = "UPDATE %s" % (instr[1])
	if instr[0] == Code.POP:
		str = "POP %s" % (instr[1])
	if instr[0] == Code.SLIDE:
		str = "SLIDE %s" % (instr[1])
	if instr[0] == Code.ALLOC:
		str = "ALLOC %s" % (instr[1])
	if instr[0] == Code.APPLY:
		str = "APPLY"
	if instr[0] == Code.EVAL:
		str = "EVAL"
	if instr[0] == Code.ADD:
		str = "ADD"
	if instr[0] == Code.SUB:
		str = "SUB"
	if instr[0] == Code.MUL:
		str = "MUL"
	if instr[0] == Code.DIV:
		str = "DIV"
	if instr[0] == Code.NEG:
		str = "NEG"
	if instr[0] == Code.EQ:
		str = "EQ"
	if instr[0] == Code.NEQ:
		str = "NEQ"
	if instr[0] == Code.LT:
		str = "LT"
	if instr[0] == Code.LTE:
		str = "LTE"
	if instr[0] == Code.GT:
		str = "GT"
	if instr[0] == Code.GTE:
		str = "GTE"
	if instr[0] == Code.COND:
		str = "COND %s %s" % (instr[1], instr[2])
	return "%s" % (str)

# State

class State:
	"State represents a G-machine state"
	def __init__(self, symtab):
		self.stats = Stats(self)
		self.symtab = symtab
		self.code = [(Code.PUSHG, 'main'), (Code.UNWIND,)]
		self.stack = Stack(self)
		self.heap = Heap(self)
		self.globals = Globals(self, symtab)
	
	def result(self):
		return self.stack.pop()

# State Components

class Stats:
	def __init__(self, state):
		self.state = state
		self._steps = 0
		self._start = 0
		self._stop = 0
		self._counts = defaultdict(int)
	
	def step(self):
		self._steps += 1

	def start(self):
		self._start = time.time()
	
	def stop(self):
		self._stop = time.time()
	
	def count(self, name):
		self._counts[name] += 1

	def __str__(self):
		result = "";
		result += 'steps  : %s \n' % (self._steps)
		result += 'time   : %2.2f sec \n' % (self._stop - self._start)
		result += 'heap   : %s cells \n' % (self.state.heap.size())
		result += 'counts : '
		for count in self._counts:
			result += '%s = %s, ' % (count, self._counts[count])
		result = result[0:-2]
		return result

class Globals:
	def __init__(self, state, symtab):
		self.state = state
		self.data = {}
		for name in symtab.root:
			if name != SymbolTable.PARENT:
				self.state.stats.count('globals')
				symbol = symtab.root[name]
				count, code = symbol[SymbolTable.COUNT], symbol[SymbolTable.CODE]
				self.data[name] = state.heap.store(NGlobal(count, code, name))

	def __setitem__(self, name, address):
		self.state.stats.count('globals')
		self.data[name] = address

	def __getitem__(self, name):
		return self.data[name]

	def __contains__(self, name):
		return name in self.data

class Heap:
	def __init__(self, state):
		self.state = state
		self.data = {}
		self.index = 0
	
	def store(self, value):
		self.state.stats.count('store')
		index = self.index
		self.data[index] = value
		self.index += 1
		return index
	
	def size(self):
		return len(self.data.keys())

	def __setitem__(self, address, value):
		self.data[address] = value

	def __getitem__(self, name):
		return self.data[name]

	def __contains__(self, name):
		return name in self.data

	def __str__(self):
		result = ''
		for a in self.data:
			result += '  %s = ' % a + str(self.state.heap[a]) + ',\n'
		return 'heap: [\n' + result[0:-2] + '\n]'

class Stack:
	def __init__(self, state):
		self.state = state
		self.stack = []

	def push(self, obj):
		self.state.stats.count('push')
		self.stack.append(obj)

	def pop(self):
		self.state.stats.count('pop')
		return self.stack.pop()

	def peek(self, n = 0):
		self.state.stats.count('peek')
		return self.stack[-(n+1)]
	
	def append(self, list):
		self.stack += list

	def __str__(self):
		result = ''
		for a in self.stack:
			result += ', %s:%s' % (a, str(self.state.heap[a]))
		return 'stack: [' + result[2:] + ']'

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

def run(state, verbose=False):
	state.stats.start()
	while len(state.code) > 0:
		i, state.code = state.code[:1][0], state.code[1:]
		if verbose:
			print '--'
			print code_to_str(i)
			# print 'code: ' + str(map(code_to_str, state.code))
			print state.stack
			print state.heap

		# PUSH
		if i[0] == Code.PUSH:
			an = state.stack.peek(i[1])
			state.stack.push(an)

		# PUSHG
		elif i[0] == Code.PUSHG:
			a = state.globals[i[1]]
			state.stack.push(a)
		
		# PUSHI
		elif i[0] == Code.PUSHI:
			key = str(i[1])
			if not key in state.globals:
				a = state.heap.store(NNum(i[1]))
				state.globals[key] = a
			else:
				a = state.globals[key]
			state.stack.push(a)

		# APPLY
		elif i[0] == Code.APPLY:
			a1 = state.stack.pop()
			a2 = state.stack.pop()
			a = state.heap.store(NApply(a2, a1))
			state.stack.push(a)

		# SLIDE
		elif i[0] == Code.SLIDE:
			a0 = state.stack.pop()
			for _ in range(1, i[1] + 1):
				a = state.stack.pop()
			state.stack.push(a0)
		
		# POP
		elif i[0] == Code.POP:
			for j in range(0, i[1]):
				state.stack.pop()

		# ALLOC
		elif i[0] == Code.ALLOC:
			for j in range(i[1]):
				print i, i[1]
				ai = state.heap.store(NInd(null))
				state.stack.push(ai)

		# UPDATE
		elif i[0] == Code.UPDATE:
			a = state.stack.pop()
			an = state.stack.peek(i[1])
			state.heap[an] = NInd(a)

		# UNWIND
		elif i[0] == Code.UNWIND:
			a = state.stack.peek()
			n = state.heap[a]
			c = n.__class__
			if c == NGlobal:
				aa = []
				for i in range(0,	n.n + 1):
					ai = state.stack.pop()
					if i > 0:
						aa.insert(0, state.heap[ai].a1)
				state.stack.push(ai)
				state.stack.append(aa)
				state.code = n.code.instructions						
			elif c == NApply:
				state.stack.push(n.a2)
				state.code.append((Code.UNWIND,))
			elif c == NInd:
				state.stack.pop()
				state.stack.push(n.a)
				state.code.append((Code.UNWIND,))
			elif c == NNum:
				state.code = []
				break

		else:
			pass; # raise Exception('unknown instruction')
		state.stats.step()
	state.stats.stop()
	return state.heap[state.result()]