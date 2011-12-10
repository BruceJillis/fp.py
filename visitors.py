from common import Code

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
				self.visit(child)

class Identification(Visitor):
	"identify variables, check if program is obeys all scoping rules."
	def __init__(self, symtab):
		self.symtab = symtab

	def visit_CombinatorNode(self, combinator):
		if combinator.name() in self.symtab:
			raise SyntaxError('%s already defined' % combinator.name())
		self.symtab.enter(combinator.name())
		for parameter in combinator.parameters():
			self.symtab[str(parameter)] = parameter
		self.visit(combinator.children[-1])
		self.symtab.leave()

	def visit_IdentifierNode(self, identifier):
		if not str(identifier) in self.symtab:
			raise SyntaxError('"%s" is not defined' % identifier)

	def visit_LetNode(self, let):
		self.symtab.enter(let)
		for definition in let.children[0:-1]:
			self.symtab[definition.name()] = definition
			self.visit(definition.children[-1])
		self.visit(let.children[-1])
		self.symtab.leave()

	def visit_LetRecNode(self, letrec):
		self.symtab.enter(letrec)
		for definition in letrec.children[0:-1]:
			self.symtab[definition.name()] = definition
		for definition in letrec.children[0:-1]:
			self.visit(definition.children[-1])
		self.visit(letrec.children[-1])
		self.symtab.leave()


class CodeGeneration(Visitor):
	"generate GMachine code for the supplied program."
	def __init__(self, symtab):
		self.symtab = symtab

	def visit_ProgramNode(self, program):
		self.code = Code()
		for combinator in program.children:
			self.visit(combinator)

	def visit_CombinatorNode(self, combinator):
		self.symtab.enter(combinator.name())