from common import *
from collections import defaultdict
from CoreParser import PROGRAM, COMBINATOR, APPLICATION, ID

class Transformer(object):
	"visitor geared towards transforming the tree being walked"
	debug = False

	def visit(self, node, **data):
		method = None
		for cls in node.__class__.__mro__:
			method_name = 'visit_' + cls.__name__
			method = getattr(self, method_name, None)
			if method:
				break
		if not method:
			# the fallback is defined on Visitor and thus will always be present
			method = self.fallback
		return method(node, **data)

	def fallback(self, node, **data):
		'generic method to direct a visitor over the children of the current node if the children property is present. prints node name if debug is set to True'
		if self.debug:
			# if we are in debug mode print that we end up here (handy during development)
			print 'fallback ' + node.__class__.__name__
			print node.toStringTree()
		if hasattr(node, 'children'):
			# call and collect results for all children
			result = []
			for child in node.children:
				ans = self.visit(child, **data)
				result.append(ans)
			return result

class FreeVariables(Transformer):
	def __init__(self, symtab):
		self.symtab = symtab
		self.bound = {}
		for c in symtab.combinators:
			self.bound[c] = True
		self.vars = []

	def variables(self):
		return self.vars

	def visit_CombinatorNode(self, node, **data):
		for p in node.parameters():
			self.bound[str(p)] = True
		self.visit(node.body(), **data)

	def visit_CaseNode(self, node, **data):
		self.visit(node.condition(), **data)
		for a in node.alternatives():
			self.visit(a, **data)

	def visit_AlternativeNode(self, node, **data):
		for p in node.parameters():
			self.bound[str(p)] = True
		self.visit(node.body(), **data)		

	def visit_IdentifierNode(self, node):		
		if not str(node) in self.symtab.combinators and not str(node) in self.bound:
			self.vars.append(node)

class CompositeTransformer(Transformer):
	"specialization of of transformer allowing it to be composed of multiple mutually recursive schemes"
	def __init__(self):
		self.active = None
		self.schemes = {}

	def __setitem__(self, key, scheme):
		self.schemes[key] = scheme

	def __getitem__(self, key):
		return self.schemes[key]

	def select(self, scheme):
		self.active = self.schemes[scheme]

	def visit(self, node, **data):
		'direct a visitor over a composite using the classname to select to concrete method to call (instead of an accept method on each class)'
		method = None
		for cls in node.__class__.__mro__:
			method_name = 'visit_' + cls.__name__
			method = getattr(self.active, method_name, None)
			if method:
				break
		if not method:
			method = self.active.fallback
		return method(node, **data)

	def fallback(self, node, **data):
		'generic method to direct a transformer over the children of the current node if the children property is present. prints node name if debug is set to True'
		if self.debug:
			print 'fallback ' + node.__class__.__name__
			print node.toStringTree()
		if hasattr(node, 'children'):
			for child in node.children:
				self.visit(child, **data)

class CaseLifter(CompositeTransformer):
	def __init__(self, symtab):
		super(CaseLifter, self).__init__()
		self.symtab = symtab
		self['S'] = CaseLifterS(self)
		self['E'] = CaseLifterE(self)
		self['C'] = CaseLifterC(self)
		self['A'] = CaseLifterA(self)
		self.select('S')

class TransformationScheme(Transformer):
	def __init__(self, facade):
		super(TransformationScheme, self).__init__()
		self.facade = facade
		self.names = defaultdict(int)

	def select(self, scheme):
		self.facade.select(scheme)

	def visit(self, scheme, node, **data):
		active = self.facade.active
		self.select(scheme)
		result = self.facade.visit(node, **data)
		self.facade.active = active
		return result

	def fresh(self, stub):
		"generate a new fresh name"
		self.names[stub] += 1
		return "$%s%s" % (stub, self.names[stub])

	def token(self, spelling, kind = ID):
		token = CommonToken(
				type = kind,
				text = spelling
		)
		return token
	
	def id(self, name):
		return IdentifierNode(self.token(str(name), ID))

class CaseLifterS(TransformationScheme):
	def visit_ProgramNode(self, node, **data):
		for node in node.combinators():
			self.visit('E', node.body(), **data)

class CaseLifterE(TransformationScheme):
	def visit_LetNode(self, node, **data):
		for definition in node.definitions():
			self.visit('E', definition.body(), **data)
		self.visit('E', node.body(), **data)

	def visit_LetRecNode(self, node, **data):
		for definition in node.definitions():
			self.visit('E', definition.body(), **data)
		self.visit('E', node.body(), **data)
	
	def visit_CaseNode(self, node, **data):
		self.visit('E', node.condition(), **data)
		for alt in node.alternatives():
			self.visit('A', alt, **data)

	def visit_ConstructorNode(self, node, **data):
		for n in node.expressions():
			self.visit('C', n, **data)

	def visit_AddNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

	def visit_MinNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

	def visit_MulNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

	def visit_DivNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

	def visit_EqualNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

	def visit_NotEqualNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

	def visit_NegateNode(self, node, **data):
		self.visit('E', node.left(), **data)

	def visit_NumberNode(self, number, **kwargs):
		pass

	def fallback(self, node, **data):
		self.visit('C', node, **data)

class CaseLifterC(TransformationScheme):
	def visit_LetNode(self, node, **data):
		for definition in node.definitions():
			self.visit('C', definition.body(), **data)
		self.visit('C', node.body(), **data)

	def visit_LetRecNode(self, node, **data):
		for definition in node.definitions():
			self.visit('C', definition.body(), **data)
		self.visit('C', node.body(), **data)

	def visit_ConstructorNode(self, node, **data):
		print node.toStringTree()
		exit('C')

	def visit_CaseNode(self, node, **data):
		"lift case node in non-strict context to the top level as a new combinator"
		parent = node.getParent()
		program = node.getAncestor(PROGRAM)
		index = parent.children.index(node)
		parent.children.remove(node)
		
		name = self.fresh('combinator')
		sc = CombinatorNode(self.token("COMBINATOR", COMBINATOR))
		sc.addChild(self.id(name))

		fv = FreeVariables(self.facade.symtab)
		fv.visit(node)
		for v in fv.variables():
			sc.addChild(v)
		sc.addChild(node)		
		program.addChild(sc)
			
		vs = fv.variables()
		vs.reverse()
		ap = ApplicationNode(APPLICATION)
		ap.addChild(self.id(name))
		ap.addChild(vs.pop())
		while len(vs) > 0:
			a = ApplicationNode(APPLICATION)
			a.addChild(ap)
			a.addChild(self.id(vs.pop()))		
			ap = a
		parent.children.insert(index, ap)

		
	def visit_ConstructorNode(self, node, **data):
		if not node.saturated():
			parent = node.getParent()
			index = parent.children.index(node)
			parent.children.remove(node)
			program = node.getAncestor(PROGRAM)

			name = self.fresh('combinator')
			sc = CombinatorNode(self.token("COMBINATOR", COMBINATOR))
			sc.addChild(self.id(name))

			fv = FreeVariables(self.facade.symtab)
			fv.visit(node)
			for v in fv.variables():
				sc.addChild(v)
			for i in range(node.arity() - len(node.expressions())):
				id = self.id(self.fresh('id'))
				sc.addChild(id)
				node.children.append(id)
			sc.addChild(node)		
			program.addChild(sc)

			if node.arity() > 1:
				vs = fv.variables()
				vs.reverse()
				ap = ApplicationNode(APPLICATION)
				ap.addChild(self.id(name))
				ap.addChild(vs.pop())
				while len(vs) > 0:
					a = ApplicationNode(APPLICATION)
					a.addChild(ap)
					a.addChild(self.id(vs.pop()))		
					ap = a
				parent.children.insert(index, ap)
			else:
				parent.children.insert(index, self.id(name))

		else:
			for n in node.expressions():
				self.visit('C', n, **data)

	def visit_ApplicationNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_AddNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_MinNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_MulNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_DivNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_EqualNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_NotEqualNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_LessThanNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_LessThanEqualNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_GreaterThanNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_GreaterThanEqualNode(self, node, **data):
		self.visit('C', node.right(), **data)
		self.visit('C', node.left(), **data)

	def visit_IdentifierNode(self, identifier, **kwargs):
		pass

	def visit_NegateNode(self, node, **data):
		self.visit('C', node.left(), **data)

	def visit_NumberNode(self, number, **kwargs):
		pass

class CaseLifterA(TransformationScheme):
	def visit_AlternativeNode(self, node, **data):
		self.visit('E', node.body(), **data)