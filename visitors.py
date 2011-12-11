from common import *
from gmachine import Code, SymbolTable

class Visitor(object):
	debug = False

	def visit(self, node, *args, **kwargs):
		method = None
		for cls in node.__class__.__mro__:
			method_name = 'visit_' + cls.__name__
			method = getattr(self, method_name, None)
			if method:
				break
		if not method:
			method = self.fallback
		return method(node, *args, **kwargs)

	def fallback(self, node, *args, **kwargs):
		'generic method to direct a visitor over the children of the current node if the children property is present. prints node name if debug is set to True'
		if self.debug:
			print 'fallback ' + node.__class__.__name__
			print node.toStringTree()
		if hasattr(node, 'children'):
			for child in node.children:
				self.visit(child, *args, **kwargs)

class Identification(Visitor):
	"identify variables, check if program is obeys all scoping rules."
	def __init__(self, symtab):
		self.symtab = symtab

	def visit_CombinatorNode(self, combinator):
		if combinator.name() in self.symtab:
			raise SyntaxError('%s already defined' % combinator.name())
		self.symtab.enter(combinator.name())
		for parameter in combinator.children[1:-1]:
			self.symtab[str(parameter)] = parameter
		self.symtab[SymbolTable.COUNT] = len(combinator.children[1:-1])
		self.visit(combinator.children[-1])
		self.symtab.leave()

	def visit_ApplicationNode(self, application, *args, **kwargs):
		self.visit(application.children[1])
		self.visit(application.children[0])

	def visit_IdentifierNode(self, identifier):
		if not str(identifier) in self.symtab:
			raise SyntaxError('"%s" is not defined' % identifier)

	def visit_LetNode(self, let):
		self.symtab.enter(let)
		for definition in let.children[0:-1]:
			self.symtab[definition.name()] = definition
			self.visit(definition.children[-1])
		self.symtab[SymbolTable.COUNT] = len(let.children[0:-1])
		self.visit(let.children[-1])
		self.symtab.leave()

	def visit_LetRecNode(self, letrec):
		self.symtab.enter(letrec)
		for definition in letrec.children[0:-1]:
			self.symtab[definition.name()] = definition
		for definition in letrec.children[0:-1]:
			self.visit(definition.children[-1])
		self.symtab[SymbolTable.COUNT] = len(letrec.children[0:-1])
		self.visit(letrec.children[-1])
		self.symtab.leave()


class CodeGeneration(Visitor):
	"generate GMachine code for the supplied program."

	# inner class Environment is only used during code generation to maintain stack indices
	class	Environment:
		def	__init__(self):
			self.mapping	=	{}
			self.index	=	0

		def	add(self,	param):
			self.mapping[param] = self.index
			self.index	+= 1

		def	add_at(self,	param, at):
			self.mapping[param] = at

		def	get(self,	param):
			if	not	param	in self.mapping:
				exit('unknown local var: %s ' % (param))
			return	self.mapping[param]

		def	count(self):
			return len(self.mapping.keys())
		
		def merge_from(self, env, frm):
			for m in env.mapping:
				self.add_at(m, frm)
				frm -= 1

		def increment(self, amount = 1):
			"clone and increment this environment"
			result = CodeGeneration.Environment()
			result.index = self.index
			for k in self.mapping:
				result.mapping[k] = self.mapping[k] + amount
			return result

		def clone(self):
			"clone this environment so changes wont affect the master environment"
			result = CodeGeneration.Environment()
			result.index = self.index
			for k in self.mapping:
				result.mapping[k] = self.mapping[k]
			return result		

	def __init__(self, symtab):
		self.symtab = symtab

	def visit_ProgramNode(self, program):
		for combinator in program.children:
			self.visit(combinator)

	def visit_CombinatorNode(self, combinator):
		self.code = Code()
		env = CodeGeneration.Environment()
		self.symtab.enter(combinator.name())
		for parameter in combinator.children[1:-1]:
			env.add(str(parameter))
		d = env.index
		self.visit(combinator.children[-1], env = env)
		self.code.Update(d)
		self.code.Pop(d)
		self.code.Unwind()
		self.symtab[SymbolTable.CODE] = self.code
		self.symtab.leave()

	def visit_LetNode(self, let, **kwargs):
		self.symtab.enter(let)
		env, n = kwargs['env'].increment(self.symtab[SymbolTable.COUNT]), 0
		for definition in let.children[0:-1]:
			env.add_at(definition.name(), self.symtab[SymbolTable.COUNT] - (n + 1))
			_env, n = kwargs['env'].increment(n), n + 1
			self.visit(definition.children[1], env = _env)
		self.visit(let.children[-1], env = env)
		self.code.Slide(self.symtab[SymbolTable.COUNT])
		self.symtab.leave()

	def visit_LetRecNode(self, letrec, **kwargs):
		self.symtab.enter(letrec)
		self.code.Alloc(self.symtab[SymbolTable.COUNT])
		env, n = kwargs['env'].increment(self.symtab[SymbolTable.COUNT]), 0
		for definition in letrec.children[0:-1]:
			env.add_at(definition.name(), self.symtab[SymbolTable.COUNT] - (n + 1))
			n += 1
		u = self.symtab[SymbolTable.COUNT] - 1
		for definition in letrec.children[0:-1]:
			self.visit(definition.children[-1], env = env)
			self.code.Update(u)
			u -= 1
		self.visit(letrec.children[-1], env = env)
		self.code.Slide(self.symtab[SymbolTable.COUNT])
		self.symtab.leave()

	def visit_ApplicationNode(self, application, **kwargs):
		self.visit(application.children[1], env = kwargs['env'])
		env = kwargs['env'].increment(1)
		self.visit(application.children[0], env = env)
		self.code.Apply()

	def visit_AddNode(self, node, *args, **kwargs):
		self.visit(node.children[1], *args, **kwargs)
		self.visit(node.children[0], *args, **kwargs)
		self.code.PushGlobal('+')
		self.code.Apply()
		self.code.Apply()

	def visit_MulNode(self, node, *args, **kwargs):
		self.visit(node.children[1], *args, **kwargs)
		self.visit(node.children[0], *args, **kwargs)
		self.code.PushGlobal('*')
		self.code.Apply()
		self.code.Apply()

	def visit_IdentifierNode(self, identifier, **kwargs):
		name = str(identifier)
		node = self.symtab[name]
		if isinstance(node, ASTNode):
			self.code.Push(kwargs['env'].get(name))
		else:
			self.code.PushGlobal(name)

	def visit_NumberNode(self, number, **kwargs):
		self.code.PushInt(number.value())