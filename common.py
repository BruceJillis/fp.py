class	Environment:
	def	__init__(self):
		self.mapping	=	{}
		self.index	=	0

	def	add(self,	param):
		self.mapping[param] = self.index
		self.index	+= 1

	def	addat(self,	param, at):
		self.mapping[param] = at

	def	get(self,	param):
		if	not	param	in self.mapping:
			exit('unknown local var: %s ' % (param))
		return	self.mapping[param]

	def	count(self):
		return len(self.mapping.keys())

	def increment(self, amount = 1):
		result = Environment()
		result.index = self.index
		for k in self.mapping:
			result.mapping[k] = self.mapping[k] + amount
		return result

class Code:
	PUSH = 1
	PUSH_GLOBAL = 2
	PUSH_INT = 3
	UNWIND = 4
	APPLY = 5
	UPDATE = 6
	POP = 7
	SLIDE = 8
	ALLOC = 9

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
		if instr[0] == self.UPDATE:
			str = "UPDATE %s" % (instr[1])
		if instr[0] == self.POP:
			str = "POP %s" % (instr[1])
		if instr[0] == self.SLIDE:
			str = "SLIDE %s" % (instr[1])
		if instr[0] == self.ALLOC:
			str = "ALLOC %s" % (instr[1])
		if instr[0] == self.APPLY:
			str = "APPLY"
		return "%s" % (str)

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
		self.current = None
		self.combinators = {}
		self.letrecs = {}
	
	def combinator(self, name, params):
		if name in self.combinators:
			raise Exception('duplicate combinator name: %s ' % (name))
		if params == None:
			params = []
		self.combinators[name] = params
	
	def params(self, name):
		if not name in self.combinators:
			raise Exception('unknown combinator: %s' % (name) )
		return self.combinators[name]

	def letrec(self, name, param = None):
		if param == None:
			return self.letrecs[name]
		if not name in self.letrecs:
			self.letrecs[name] = []
		self.letrecs[name].append(param)