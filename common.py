import time

class	Environment:
	def	__init__(self):
		self.mapping	=	{}
		self.index	=	0

	def	add(self,	param):
		self.mapping[param] = self.index
		self.index	+= 1

	def	get(self,	param):
		if	not	param	in self.mapping:
			exit('unknown	local	var: ' + param)
		return	self.mapping[param]

	def	count(self):
		return	self.index

	def increment(self):
		result = Environment()
		result.index = self.index
		for k in self.mapping:
			result.mapping[k] = self.mapping[k] + 1
		return result

class Code:
	PUSH = 1
	PUSH_GLOBAL = 2
	PUSH_INT = 3
	UNWIND = 4
	SLIDE = 5
	APPLY = 6

	def __init__(self):
		self.combinators = {}
		self.instructions = []

	def store(self, name, env):
		if name in self.combinators:
			raise Exception('duplicate combinator names: ' + name)
		self.combinators[name] = (self.instructions, env)
		self.instructions = []

	def to_str(self, instr):
		str = None
		if instr[0] == self.PUSH:
			str = "PUSH %s" % (instr[1])
		if instr[0] == self.PUSH_GLOBAL:
			str = "PUSHG %s" % (instr[1])
		if instr[0] == self.PUSH_INT:
			str = "PUSHI %s" % (instr[1])
		if instr[0] == self.UNWIND:
			str = "UNWIND"
		if instr[0] == self.SLIDE:
			str = "SLIDE %s" % (instr[1])
		if instr[0] == self.APPLY:
			str = "APPLY"
		return "%s" % (str)

	def Apply(self):
		self.instructions.append((Code.APPLY,))

	def Slide(self, value):
		self.instructions.append((Code.SLIDE, value))

	def Unwind(self):
		self.instructions.append((Code.UNWIND,))

	def Push(self, index, name):
		self.instructions.append((Code.PUSH, index))

	def PushInt(self, value):
		self.instructions.append((Code.PUSH_INT, int(value)))

	def PushGlobal(self, name):
		self.instructions.append((Code.PUSH_GLOBAL, name))

	def __str__(self):
		result = ''
		for i in self.instructions:
			result += '%s\n' % (str(i))
		return result

class Information:
	def __init__(self):
		self.combinators = {}
	
	def combinator(self, name, params):
		if name in self.combinators:
			raise Exception('duplicate combinator names: ' + name)
		self.combinators[name] = params

class Node:
	pass

class NGlobal(Node):
	def __init__(self, nargs, code, name):
		self.nargs = int(nargs)
		self.code = code
		self.name = name
	
	def __repr__(self):
		return 'NGlobal(%s, %s)' % (self.nargs, self.name)

class NApply(Node):
	def __init__(self, a1, a2):
		self.a1 = a1
		self.a2 = a2

	def __repr__(self):
		return 'NApply(%s, %s)' % (repr(self.a1), repr(self.a2))

class NNum(Node):
	def __init__(self, value):
		self.value = int(value)

	def __repr__(self):
		return 'NNum(%s)' % (self.value)

class Heap:
	def __init__(self, code, globals):
		self.index = 0
		self._heap = {}
		for c in code.combinators:
			co = code.combinators[c]
			a = self.alloc(NGlobal(co[1].count(), co[0], c))
			globals[c] = a

	def size(self):
		return len(self._heap.keys()) 

	def iter(self):
		return self._heap.keys()

	def __getitem__(self, name):
		return self._heap[name]

	def alloc(self, obj):
		result = self.index
		self._heap[result] = obj
		self.index += 1
		return result

class Globals:
	def __init__(self):
		self._heap = {}

	def __setitem__(self, name, value):
		self._heap[name] = value

	def __getitem__(self, name):
		if name in self._heap:
			return self._heap[name]
		raise StopIteration

class Statistics:
	def __init__(self, machine):
		self.machine = machine
		self.steps = 0
		self._start = 0
		self._stop = 0
	
	def step(self):
		self.steps += 1

	def start(self):
		self._start = time.time()
	
	def stop(self):
		self._stop = time.time()
	
	def __str__(self):
		result = "";
		result += 'steps: %s \n' % (self.steps)
		result += 'time : %2.2f sec \n' % (self._stop - self._start)
		result += 'heap : %s cells \n' % (self.machine.heap.size())
		return result