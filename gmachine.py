from common import Code
import time

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

	def __setitem__(self, name, value):
		self._heap[name] = value

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

class GMachine:
	def __init__(self, code):
		self._code = code
		self.code = [(Code.PUSH_GLOBAL, 'main'), (Code.EVAL,)]
		self.stack = []
		self.globals = Globals()
		self.dump = [] # stack of stacks
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

	def print_dump(self):
		result = []
		for (i,s) in self.dump:
			result.append("<%s:%s>" % (str(i), str(s)))
		print '\n'.join(result)

	def run(self, verbose = False):
		self.stats.start()
		while len(self.code) > 0:
			if verbose:
				print "-------\nstep", self.stats.steps
				print "code :",
				self.print_code()
				print "stack:",			
				self.print_stack()
				print "heap:"		
				self.print_heap()
				print "dump:"		
				self.print_dump()
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
				a = self.stack[-(i[1]+1):][0]
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
					# UNWIND a:NGlobal
					aas = []
					for n in range(o.n + 1):
						an = self.stack.pop()
						if n > 0:
							aas.append(self.heap[an].a2)
					self.stack.append(an)
					aas.reverse()
					self.stack += aas
					self.code = o.code
				elif o.__class__ == NApply:
					# UNWIND a:NApply
					self.stack.append(o.a1)
					self.code = [i] + self.code
				elif o.__class__ == NInd:
					# UNWIND a:NInd
					self.stack.pop()
					self.stack.append(o.a)
					self.code = [i] + self.code
				elif o.__class__ == NNum:
					# UNWIND a:NNum
					if len(self.dump) == 0:
						# machine has terminated
						self.stack.append(o)
						break
					else:
						di, self.dump = self.dump[:1][0], self.dump[1:]
						self.code = di[0]
						self.stack = di[1] + [a]
			elif i[0] == Code.UPDATE:
				a = self.stack.pop()
				an = self.stack[-(i[1]+1):][0]
				self.heap[an] = NInd(a)				
			elif i[0] == Code.POP:
				for n in range(i[1]):
					self.stack.pop()
			elif i[0] == Code.SLIDE:
				a = self.stack.pop()
				i = i[1]
				while i >= 1:
					self.stack.pop()
					i -= 1
				self.stack.append(a)
			elif i[0] == Code.ALLOC:
				a = []
				for i in range(i[1]):
					a.append(self.heap.alloc(NInd(None)))
				a.reverse()
				for aa in a:
					self.stack.append(a);
			elif i[0] == Code.EVAL:
				a = self.stack.pop()
				self.dump.append((self.code, self.stack))
				self.code, self.stack = [(Code.UNWIND,)], [a]
			elif i[0] == Code.ADD or i[0] == Code.SUB or i[0] == Code.MUL or i[0] == Code.DIV or i[0] == Code.EQ or i[0] == Code.NEQ or i[0] == Code.LT or i[0] == Code.LTE or i[0] == Code.GT or i[0] == Code.GTE:
				a0 = self.stack.pop()
				n0 = self.heap[a0]
				a1 = self.stack.pop()
				n1 = self.heap[a1]
				result = None

				def tobool(n):
					if n: return 1
					return 0

				if i[0] == code.ADD:
					result = n0 + n1
				elif i[0] == code.SUB:
					result = n0 - n1
				elif i[0] == code.MUL:
					result = n0 * n1
				elif i[0] == code.DIV:
					result = n0 / n1
				elif i[0] == code.EQ:
					result = tobool(n0 == n1)
				elif i[0] == code.NEQ:
					result = tobool(n0 != n1)
				elif i[0] == code.LT:
					result = tobool(n0 < n1)
				elif i[0] == code.LTE:
					result = tobool(n0 <= n1)
				elif i[0] == code.GT:
					result = tobool(n0 > n1)
				elif i[0] == code.GTE:
					result = tobool(n0 >= n1)
				a = self.heap.alloc(NNum(result))
				self.stack.append(a)
			elif i[0] == Code.NEG:
				a = self.stack.pop()
				n = self.heap[a]
				a = self.heap.alloc(NNum(-n))
				self.stack.append(a)
			elif i[0] == Code.COND:
				pass
			else:
				raise Exception('unknown instruction: ' + str(i))
			self.stats.step()
		self.stats.stop()
		return self.stack.pop()