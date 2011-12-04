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
		return self._heap[name]

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
				a = self.heap.alloc(NNum(i[1]))
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