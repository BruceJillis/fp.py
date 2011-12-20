from CoreParser import PROGRAM, COMBINATOR, APPLICATION, ID, LET, DEFINITION
from common import Visitor, CompositeVisitor
from collections import defaultdict
from ast import *

class FreeVariables(Visitor):
	'''	An occurrence of a variable v in an expression e is said to be free in e if the occurrence is not bound by an enclosing lambda or let(rec) expression in e but there is no need to treat 
	other top-level (combinators) functions as extra parameters.	'''

	def __init__(self, symtab):
		self.symtab = symtab
		self.bound = {}
		for c in symtab.combinators:
			self.bound[c] = True
		self.vars = []

	def variables(self):
		return list(set(self.vars))

	def visit_CombinatorNode(self, node, **data):
		for p in node.parameters():
			self.bound[str(p)] = True
		self.visit(node.body(), **data)

	def visit_LambdaNode(self, node, **data):
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
			self.vars.append(str(node))

class Transformer(Visitor):
	def __init__(self):
		super(Transformer, self).__init__()
		self.names = defaultdict(int)

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

class TransformationScheme(Transformer):
	def __init__(self, facade):
		super(TransformationScheme, self).__init__()
		self.facade = facade

	def select(self, scheme):
		self.facade.select(scheme)

	def visit(self, scheme, node, **data):
		if scheme != None:
			active = self.facade.active
			self.select(scheme)
		result = self.facade.visit(node, **data)
		if scheme != None:
			self.facade.active = active
		return result

	def fallback(self, node, **data):
		"define a fallback that is aware of the scheme parameter."
		if self.debug:
			# if we are in debug mode print that we end up here (handy during development)
			print 'fallback ' + node.__class__.__name__
			print node.toStringTree()
		if hasattr(node, 'children'):
			# call and collect results for all children
			result = []
			for child in node.children:
				ans = self.visit(None, child, **data)
				result.append(ans)
			return result

class CaseLifter(CompositeVisitor):
	def __init__(self, symtab):
		super(CaseLifter, self).__init__()
		self.symtab = symtab
		self['S'] = CaseLifterS(self)
		self['E'] = CaseLifterE(self)
		self['C'] = CaseLifterC(self)
		self['A'] = CaseLifterA(self)
		self.select('S')

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

	def visit_AndNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

	def visit_OrNode(self, node, **data):
		self.visit('E', node.right(), **data)
		self.visit('E', node.left(), **data)

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
			sc.addChild(self.id(v))
		sc.addChild(node)		
		program.addChild(sc)
			
		vs = fv.variables()
		vs.reverse()
		ap = ApplicationNode(APPLICATION)
		ap.addChild(self.id(name))
		ap.addChild(self.id(vs.pop()))
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
				sc.addChild(self.id(v))
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
				ap.addChild(self.id(vs.pop()))
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

class Renamer(Transformer):
	def __init__(self, source, target):
		super(Renamer, self).__init__()
		self.source = str(source)
		self.target = target

	def visit_IdentifierNode(self, identifier, **kwargs):
		if str(identifier) == self.source:
			parent = identifier.getParent()
			index = parent.children.index(identifier)
			parent.children.remove(identifier)
			parent.children.insert(index, self.target)

class LambdaLifter(Transformer):
	def __init__(self, symtab):
		super(LambdaLifter, self).__init__()
		self.symtab = symtab

	def visit_ProgramNode(self, node, **data):
		self.program = node
		for node in node.combinators():
			self.visit(node, **data)

	def visit_CombinatorNode(self, node, **data):
		if node.body().__class__ == LambdaNode:
			# special case: do not introduce redundant supercombinator definitions by reusing the current combinator
			lambda_node = node.body()
			index = node.children.index(lambda_node)
			node.children.remove(lambda_node)
			# move lambda to the top level as combinator
			fv = FreeVariables(self.symtab)
			fv.visit(lambda_node)
			for v in fv.variables():
				node.children.insert(0, self.id(v))
			for n in lambda_node.parameters():
				node.children.insert(1, n)
			node.addChild(lambda_node.body())
		self.visit(node.body(), **data)

	def visit_LetNode(self, node, **data):
		for definition in node.definitions():
			if definition.body().__class__ == LambdaNode:
				# special case to avoid introducing too many useless let definitions
				self.visit(definition.body(), **data)
				fv = FreeVariables(self.symtab)
				fv.visit(node.getAncestor(COMBINATOR))
				if len(fv.variables()) == 1 and fv.variables()[0] == definition.name():
					# if the name of the definition is the only free variable and we 
					rn = Renamer(definition.name(), definition.body())
					rn.visit(node.body())
					parent = node.getParent()
					index = parent.children.index(node)
					parent.children.remove(node)
					parent.children.insert(index, node.body())
			else:
				self.visit(definition.body(), **data)
		self.visit(node.body(), **data)

	def visit_LambdaNode(self, node, **data):
		parent = node.getParent()
		index = parent.children.index(node)
		parent.children.remove(node)
		# move lambda to the top level as combinator
		fv = FreeVariables(self.symtab)
		fv.visit(node)
		for v in fv.variables():
			node.children.insert(0, self.id(v))
		# now make the combinator
		name = self.fresh('sc')
		sc = CombinatorNode(self.token("COMBINATOR", COMBINATOR))
		sc.addChild(self.id(name))
		self.symtab.combinators[name] = sc
		for n in node.parameters():
			sc.addChild(n)
		sc.addChild(node.body())	
		self.program.addChild(sc)
		# replace the original expression
		vs = fv.variables()
		if len(vs) > 0:
			# build application spine
			vs.reverse()
			ap = ApplicationNode(APPLICATION)
			ap.addChild(self.id(name))
			ap.addChild(self.id(vs.pop()))
			while len(vs) > 0:
				a = ApplicationNode(APPLICATION)
				a.addChild(ap)
				a.addChild(self.id(vs.pop()))		
				ap = a
			parent.children.insert(index, ap)
		else:
			# if there is only 1 argument, add it as simple identifier
			parent.children.insert(index, self.id(name))