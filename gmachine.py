from collections import defaultdict
import time

# Symbol Table
class SymbolTable:
	"the symbol table maintains a tree of scope's such that we can re-enter scopes in different phases of the compiler and lookup / enrich the information present."
	# reserved field names

	# name of the field containing the back pointer to the parent, None for the root node
	PARENT = '__parent__'
	# name of the field containing code for combinators
	CODE = '__code__'
	# contains a count
	COUNT = '__count__'

	def __init__(self):
		self.tree = {}
		self.root = self.tree
		self.tree[SymbolTable.PARENT] = None
		self.precompiled()
		self.combinators = {}
	
	def binary(self, symbol, field):
		c = Code()
		c.Push(1)
		c.Eval()
		c.Push(1)
		c.Eval()
		if not hasattr(c, field):
			raise Exception('binary operator %s instruction not found on Code: %s' % (symbol, field))
		m = getattr(c, field)
		m()
		c.Update(2)
		c.Pop(2)
		c.Unwind()
		self.root[symbol] = {
			SymbolTable.COUNT: 2,
			SymbolTable.CODE: c,
		}

	def precompiled(self):
		self.binary('&', 'And')
		self.binary('|', 'And')
		self.binary('+', 'Add')
		self.binary('-', 'Sub')
		self.binary('*', 'Mul')
		self.binary('/', 'Div')
		self.binary('==', 'Eq')
		self.binary('!=', 'Neq')
		self.binary('<', 'Lt')
		self.binary('<=', 'Lte')
		self.binary('>', 'Gt')
		self.binary('>=', 'Gte')
		# 'negate'
		c = Code()
		c.Push(0)
		c.Eval()
		c.Neg()
		c.Update(1)
		c.Pop(1)
		c.Unwind()
		self.root['negate'] = {
			SymbolTable.COUNT: 1,
			SymbolTable.CODE: c,
		}
		
	def enter(self, context):
		'enter a new scope'
		key = str(context)
		if not key in self.tree:
			self.tree[key] = {}
		parent = self.tree
		self.tree = self.tree[key]
		self.tree[SymbolTable.PARENT] = parent

	def leave(self):
		'leave current scope'
		if self.tree[SymbolTable.PARENT] == None:
			raise Error('cannot pop root scope!')
		self.tree = self.tree[SymbolTable.PARENT]

	def __setitem__(self, key, value):
		self.tree[key] = value

	def __getitem__(self, key):
		if key in self.tree:
			return self.tree[key]
		tree = self.tree[SymbolTable.PARENT]
		while tree != None:
			if key in tree:
				return tree[key]
			tree = tree[SymbolTable.PARENT]
		raise KeyError(key)

	def __contains__(self, key):
		"return True if this or a parent scope contains key"
		if key in self.tree:
			return True
		tree = self.tree[SymbolTable.PARENT]
		while tree != None:
			if key in tree:
				return True
			tree = tree[SymbolTable.PARENT]
		return False

	def __len__(self, key):
		return len(self.tree.keys())
	
	def prettyprint(self, tree, indent = 0):
		"prettyprint the tree"
		try:
			result = '\n'
			for k in tree:
				if k != SymbolTable.PARENT:
					result += (indent * '   ') + '%s = %s\n' % (k, self.prettyprint(tree[k], indent+1))
			return result
		except:
			return str(tree)

	def __str__(self):
		return self.prettyprint(self.root)

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

	PACK = 23
	CASE = 24
	SPLIT = 25

	AND = 26
	OR = 27
	
	PRINT = 28

	def __init__(self):
		self.instructions = []
		
	# factory functions for all instructions
	def Pack(self, tag, arity):
		self.instructions.append((Code.PACK, tag, arity))

	def Case(self, cases):
		self.instructions.append((Code.CASE, cases))

	def Split(self, n):
		self.instructions.append((Code.SPLIT, n))

	def Alloc(self, value):
		self.instructions.append((Code.ALLOC, value))

	def Slide(self, value):
		self.instructions.append((Code.SLIDE, value))

	def Update(self, value):
		self.instructions.append((Code.UPDATE, value))

	def Pop(self, value):
		self.instructions.append((Code.POP, value))

	def Apply(self):
		self.instructions.append((Code.APPLY,))

	def Print(self):
		self.instructions.append((Code.PRINT,))

	def Unwind(self):
		self.instructions.append((Code.UNWIND,))

	def Eval(self):
		self.instructions.append((Code.EVAL,))

	def And(self):
		self.instructions.append((Code.AND,))

	def Or(self):
		self.instructions.append((Code.OR,))

	def Add(self):
		self.instructions.append((Code.ADD,))

	def Sub(self):
		self.instructions.append((Code.SUB,))

	def Mul(self):
		self.instructions.append((Code.MUL,))

	def Div(self):
		self.instructions.append((Code.DIV,))

	def Neg(self):
		self.instructions.append((Code.NEG,))

	def Cond(self, c1, c2):
		self.instructions.append((Code.COND, c1, c2))

	def Eq(self):
		self.instructions.append((Code.EQ,))

	def Neq(self):
		self.instructions.append((Code.NEQ,))

	def Lt(self):
		self.instructions.append((Code.LT,))

	def Lte(self):
		self.instructions.append((Code.LTE,))

	def Gt(self):
		self.instructions.append((Code.GT,))

	def Gte(self):
		self.instructions.append((Code.GTE,))

	def Push(self, index, name = ''):
		self.instructions.append((Code.PUSH, index))

	def PushI(self, value):
		self.instructions.append((Code.PUSHI, value))

	def PushG(self, name):
		self.instructions.append((Code.PUSHG, name))

	def clear(self):
		self.instructions = []

	def clone(self):
		result = Code()
		result.instructions = [i for i in self.instructions]
		return result

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
		str = "P %s" % (instr[1])
	elif instr[0] == Code.PUSHG:
		str = "PG %s" % (instr[1])
	elif instr[0] == Code.PUSHI:
		str = "PI %s" % (instr[1])
	elif instr[0] == Code.UNWIND:
		str = "UNWIND"
	elif instr[0] == Code.UPDATE:
		str = "UPDATE %s" % (instr[1])
	elif instr[0] == Code.POP:
		str = "POP %s" % (instr[1])
	elif instr[0] == Code.SLIDE:
		str = "SLIDE %s" % (instr[1])
	elif instr[0] == Code.ALLOC:
		str = "ALLOC %s" % (instr[1])
	elif instr[0] == Code.APPLY:
		str = "AP"
	elif instr[0] == Code.PACK:
		str = "PACK %s %s" % (instr[1], instr[2])
	elif instr[0] == Code.CASE:
		str = "CASE [\n" 
		for c in instr[1]:
			str += '   %s -> ' % c + ', '.join(map(code_to_str, instr[1][c].instructions)) + ',\n'
		str = str[0:-2] + '\n]'
	elif instr[0] == Code.SPLIT:
		str = "SPLIT %s" % (instr[1])
	elif instr[0] == Code.EVAL:
		str = "EVAL"
	elif instr[0] == Code.AND:
		str = "AND"
	elif instr[0] == Code.OR:
		str = "OR"
	elif instr[0] == Code.ADD:
		str = "ADD"
	elif instr[0] == Code.SUB:
		str = "SUB"
	elif instr[0] == Code.MUL:
		str = "MUL"
	elif instr[0] == Code.DIV:
		str = "DIV"
	elif instr[0] == Code.NEG:
		str = "NEG"
	elif instr[0] == Code.EQ:
		str = "EQ"
	elif instr[0] == Code.NEQ:
		str = "NEQ"
	elif instr[0] == Code.LT:
		str = "LT"
	elif instr[0] == Code.LTE:
		str = "LTE"
	elif instr[0] == Code.GT:
		str = "GT"
	elif instr[0] == Code.GTE:
		str = "GTE"
	elif instr[0] == Code.PRINT:
		str = "PRINT"
	elif instr[0] == Code.COND:
		str = "[COND %s | %s]" % (instr[1], instr[2])
		str = str.replace('\n', '')
	return "%s" % (str)

# State

class State:
	"State represents a G-machine state"
	def __init__(self, symtab):
		self.symtab = symtab
		self.stats = Stats(self)
		self.code = [(Code.PUSHG, 'main'), (Code.EVAL,), (Code.PRINT,)]
		self.stack = Stack(self)
		self.heap = Heap(self)
		self.globals = Globals(self, symtab)
		self.dump = Dump(self)
		self.output = None
	
	def gc(self):
		"mark and scan garbage collector"
		roots = []
		self.stats.count('gc.collections')
		# identify all the roots
		for addr in self.stack.stack:
			roots.append(addr)
		for addr in self.globals.data:
			roots.append(self.globals[addr])
		for item in self.dump.stack:
			for addr in item[0].stack:
				roots.append(addr)
		# start marking
		for addr in roots:
			self.mark(addr)
		# free all unmarked nodes
		self.free()
		
	def mark(self, addr):
		"mark an address recursively (look through apply/indirection nodes)"
		addrs = [addr]
		while len(addrs) > 0:
			addr, addrs = addrs[:1][0], addrs[1:]
			node = self.heap[addr]
			if node.mark:
				continue
			node.mark = True
			if node.__class__ == NApply:
				addrs.append(node.a1)
				addrs.append(node.a2)
			if node.__class__ == NInd:
				addrs.append(node.a)
	
	def free(self):
		"free no longer referenced memory after marking it, reset mark to False"
		for addr in self.heap.data.keys():
			if not self.heap[addr].mark:
				self.heap.free(addr)
			else:
				self.heap[addr].mark = False

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
	
	def free(self, addr):
		self.state.stats.count('free')
		del self.data[addr]

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
		return result[0:-2]

class Stack:
	def __init__(self, state):
		self.state = state
		self.stack = []

	def push(self, obj):
		self.state.stats.count('stack.push')
		self.stack.append(obj)

	def pop(self, n = None):
		if n == None:
			self.state.stats.count('stack.pop')
			return self.stack.pop()
		else:
			if n != 0:
				del self.stack[-(n):]

	def peek(self, n = 0):
		self.state.stats.count('stack.peek')
		return self.stack[-(n+1)]
	
	def append(self, list):
		self.stack += list
	
	def bottom(self):
		return self.stack[0]

	def empty(self):
		return len(self.stack) == 0

	def __len__(self):
		return len(self.stack)

	def __str__(self):
		result = ''
		for a in self.stack:
			result += ', %s:%s \n' % (a, str(self.state.heap[a]))
		return result[2:]

class Dump(Stack):
	def push(self, obj):
		self.state.stats.count('dump.push')
		self.stack.append(obj)

	def pop(self):
		self.state.stats.count('dump.pop')
		return self.stack.pop()

	def to_str_stack(self, stack):
		result = ''
		for a in stack.stack[0:2]:
			result += ', %s:%s' % (a, str(self.state.heap[a]))
		return result[2:] + ' ..'

	def to_str_code(self, code):
		return ' '.join(map(code_to_str, code[0:2])) + ' ..'

	def __str__(self):
		result = ''
		for o in self.stack:
			result += ', (%s, %s)' % (self.to_str_stack(o[0]), self.to_str_code(o[1]))
		return result[2:]

# Nodes

class Node:
	"base node for all runtime value representations"
	mark = False

class NGlobal(Node):
	"represents an combinator at runtime"
	def __init__(self, n, code, name):
		self.n = int(n)
		self.code = code
		self.name = name
	
	def __repr__(self):
		return 'NGlob(%s, %s)' % (self.n, self.name)

class NApply(Node):
	"represents an application of two expressions at runtime"
	def __init__(self, a1, a2):
		self.a1 = a1
		self.a2 = a2

	def __repr__(self):
		return 'NAp(%s, %s)' % (repr(self.a1), repr(self.a2))

class NNum(Node):
	"represents a number at runtime"
	def __init__(self, value):
		self.value = int(value)

	def __repr__(self):
		return 'NNum(%s)' % (self.value)

class NInd(Node):
	"represents an indirection at runtime"
	def __init__(self, a):
		self.a = None
		if a != None:
			assert(int(a))
			self.a = a

	def __repr__(self):
		return 'NInd(%s)' % (self.a)

class NConstr(Node):
	"represents a constructor at runtime"
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return 'NConstr(%s, %s)' % (self.a, self.b)

def run(state, verbose=False):
	def cache(n):
		key = str(n)
		if not key in state.globals:
			state.globals[key] = state.heap.store(NNum(n))
		return state.globals[key]

	state.stats.start()
	while len(state.code) > 0:
		i, state.code = state.code[:1][0], state.code[1:]
		if verbose:
			print '--'
			print code_to_str(i)
			print 'code  : ' + ' '.join(map(code_to_str, state.code))
			print 'stack : [%s]' % state.stack
			print 'dump  : [%s]' % state.dump
			print 'heap  :  [\n%s\n]' % state.heap

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
			state.stack.push(cache(i[1]))

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
			state.stack.pop(i[1])

		# ALLOC
		elif i[0] == Code.ALLOC:
			for j in range(i[1]):
				ai = state.heap.store(NInd(None))
				state.stack.push(ai)

		# UPDATE
		elif i[0] == Code.UPDATE:
			a = state.stack.pop()
			an = state.stack.peek(i[1])
			state.heap[an] = NInd(a)

		# DYADIC
		elif i[0] in [Code.ADD, Code.SUB, Code.MUL, Code.DIV]:
			a0 = state.stack.pop() 
			n0 = state.heap[a0].value
			a1 = state.stack.pop()
			n1 = state.heap[a1].value
			if i[0] == Code.ADD:
				n = n0 + n1
			elif i[0] == Code.SUB:
				n = n0 - n1
			elif i[0] == Code.MUL:
				n = n0 * n1
			elif i[0] == Code.DIV:
				n = n0 / n1
			state.stack.push(cache(n))
		
		# NEG
		elif i[0] == Code.NEG:
			a = state.stack.pop()
			state.stack.push(cache(-state.heap[a].value))

		# COND
		elif i[0] == Code.COND:
			a = state.stack.pop()
			if state.heap[a].value == 1:
				state.code = i[1].instructions + state.code
			elif state.heap[a].value == 0:
				state.code = i[2].instructions + state.code

		# BOOLEAN
		elif i[0] in [Code.AND, Code.OR]:
			a0 = state.stack.pop() 
			n0 = False
			if state.heap[a0].a == 1:
				n0 = True
			a1 = state.stack.pop()
			n1 = False
			if state.heap[a1].a == 1:
				n1 = True
			n = 2
			if i[0] == Code.AND:
				if n0 and n1:
					n = 1
			elif i[0] == Code.OR:
				if n0 or n1:
					n = 1
			state.stack.push(state.heap.store(NConstr(n, [])))

		# COMPARISON
		elif i[0] in [Code.AND, Code.OR, Code.EQ, Code.NEQ, Code.LT, Code.LTE, Code.GT, Code.GTE]:
			a0 = state.stack.pop() 
			n0 = state.heap[a0].value
			a1 = state.stack.pop()
			n1 = state.heap[a1].value
			n = 2
			if i[0] == Code.EQ:
				if n0 == n1:
					n = 1
			elif i[0] == Code.NEQ:
				if n0 != n1:
					n = 1
			elif i[0] == Code.LT:
				if n0 < n1:
					n = 1
			elif i[0] == Code.LTE:
				if n0 <= n1:
					n = 1
			elif i[0] == Code.GT:
				if n0 > n1:
					n = 1
			elif i[0] == Code.GTE:
				if n0 >= n1:
					n = 1
			state.stack.push(state.heap.store(NConstr(n, [])))

		# EVAL
		elif i[0] == Code.EVAL:
			a = state.stack.pop()
			state.dump.push((state.stack, state.code))
			state.stack = Stack(state)
			state.stack.push(a)
			state.code = [(Code.UNWIND,)]

		# PACK
		elif i[0] == Code.PACK:
			aa = []
			for _ in range(i[2]):
				aa.append(state.stack.pop())
			a = state.heap.store(NConstr(i[1], aa))				
			state.stack.push(a)

		# CASE
		elif i[0] == Code.CASE:
			state.code = i[1][n.a].instructions + state.code

		# SPLIT
		elif i[0] == Code.SPLIT:
			state.stack.pop()
			state.stack.append(n.b)

		# PRINT
		elif i[0] == Code.PRINT:
			a = state.stack.pop()
			n = state.heap[a]
			c = n.__class__
			if c == NNum:
				if state.output == None:
					state.output = n.value
				else:
					state.output.append(n.value)
			elif c == NConstr:
				if n.a == 1:
					state.output = True
				elif n.a == 2:
					state.output = False
				elif n.a == 4:
					if state.output == None:
						state.output = 'nil'
					else:
						state.output.append('nil')
				elif n.a == 3:
					if state.output == None:
						state.output = []
					state.stack.append(n.b)
					c = Code()
					for _ in range(len(n.b)):
						c.Eval()
						c.Print()
					state.code = c.instructions + state.code

		# UNWIND
		elif i[0] == Code.UNWIND:
			a = state.stack.peek()
			n = state.heap[a]
			c = n.__class__
			if c == NGlobal:
				if n.name == 'abort':
					raise Exception('user abort')
				k = len(state.stack) - 1
				if k >= n.n:
					aa = []
					for i in range(0,	n.n + 1):
						ai = state.stack.pop()
						if i > 0:
							aa.insert(0, state.heap[ai].a1)
					state.stack.push(ai)
					state.stack.append(aa)
					state.code = n.code.instructions
				else:
					# evaluate top of the stack to WHNF
					a = state.stack.bottom()
					item = state.dump.pop()
					state.stack = item[0]
					state.stack.push(a)
					state.code = item[1]
			elif c == NApply:
				state.stack.push(n.a2)
				state.code.append((Code.UNWIND,))
			elif c == NInd:
				state.stack.pop()
				state.stack.push(n.a)
				state.code.append((Code.UNWIND,))
			elif c == NConstr:
				item = state.dump.pop()
				a = state.stack.pop()
				state.stack = item[0]
				state.stack.push(a)
				state.code = item[1]
			elif c == NNum:
				if state.dump.empty():
					# we are done, return
					state.code = []
					break
				else:
					# top of the stack is in WHNF so restore old context
					item = state.dump.pop()
					a = state.stack.pop()
					state.stack = item[0]
					state.stack.push(a)
					state.code = item[1]
		else:
			raise Exception('unknown instruction')
		allocs = state.stats._counts['store']
		if (allocs > 0) and (allocs % 50000) == 0:
			# run the gc 
			state.gc()
		state.stats.step()
	state.stats.stop()
	return state.output