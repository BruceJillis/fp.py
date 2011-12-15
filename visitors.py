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
			# the fallback is defined on Visitor and thus will always be present
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

	def visit_ApplicationNode(self, node, *args, **kwargs):
		self.visit(node.children[1])
		self.visit(node.children[0])

	def visit_LetNode(self, node):
		self.symtab.enter(node)
		for definition in node.children[0:-1]:
			self.symtab[definition.name()] = definition
			self.visit(definition.children[-1])
		self.symtab[SymbolTable.COUNT] = len(node.children[0:-1])
		self.visit(node.children[-1])
		self.symtab.leave()

	def visit_LetRecNode(self, node):
		self.symtab.enter(node)
		for definition in node.children[0:-1]:
			self.symtab[definition.name()] = definition
		for definition in node.children[0:-1]:
			self.visit(definition.children[-1])
		self.symtab[SymbolTable.COUNT] = len(node.children[0:-1])
		self.visit(node.children[-1])
		self.symtab.leave()

	def visit_AlternativeNode(self, node):
		self.symtab.enter(node)
		for p in node.children[1:-1]:
			self.symtab[str(p)] = p
		self.visit(node.children[-1])
		self.symtab.leave()

# class Environment is only used during code generation to maintain stack indices
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
		return self.mapping[param]

	def	count(self):
		return len(self.mapping.keys())
	
	def merge_from(self, env, frm):
		for m in env.mapping:
			self.add_at(m, frm)
			frm -= 1

	def increment(self, amount = 1):
		"clone and increment this environment"
		result = Environment()
		result.index = self.index
		for k in self.mapping:
			result.mapping[k] = self.mapping[k] + amount
		return result

	def clone(self):
		"clone this environment so changes wont affect the master environment"
		result = Environment()
		result.index = self.index
		for k in self.mapping:
			result.mapping[k] = self.mapping[k]
		return result

class CodeGeneration(Visitor):
	"generate GMachine code for the supplied program."
	active = None

	def __init__(self, symtab):
		self.symtab = symtab
		self.SC = CompileSC(self, symtab)
		self.R = CompileR(self, symtab)
		self.C = CompileC(self, symtab)
		self.E = CompileE(self, symtab)
		self.A = CompileA(self, symtab)
		self.code = Code()
		self.switch_code(self.code)
		self.select('SC')

	def switch_code(self, code = None):
		"awkward code switching routine to isolate code generation for alternatives. should rethink the visitor to return values"
		if code != None:
			self.SC.code = code
			self.R.code = code
			self.C.code = code
			self.E.code = code
			self.A.code = code
		else:
			self.SC.code = self.code
			self.R.code = self.code
			self.C.code = self.code
			self.E.code = self.code
			self.A.code = self.code

	def select(self, scheme):
		self.active = getattr(self, scheme)

	def visit(self, node, *args, **kwargs):
		method = None
		for cls in node.__class__.__mro__:
			method_name = 'visit_' + cls.__name__
			method = getattr(self.active, method_name, None)
			if method:
				break
		if not method:
			# the fallback is defined on Visitor and thus will always be present
			method = self.active.fallback
		return method(node, *args, **kwargs)

class CompilationScheme(Visitor):
	def __init__(self, facade, symtab):
		self.symtab = symtab
		self.facade = facade
		self.code = None
	
	def select(self, scheme):
		self.facade.select(scheme)

	def visit(self, scheme, node, *args, **kwargs):
		active = self.facade.active
		self.select(scheme)
		result = self.facade.visit(node, *args, **kwargs)
		self.facade.active = active
		return result

	def fallback(self, node, *args, **kwargs):
		raise Exception('undefined node type %s for %s: ' % (node.__class__.__name__, self.__class__.__name__))

class CompileSC(CompilationScheme):
	def visit_ProgramNode(self, program):
		for combinator in program.children:
			self.visit('R', combinator)

class CompileR(CompilationScheme):
	"generates code which instantiates the expression combinator.children[-1] in environment env, for a supercombinator of arity d, and then proceeds to unwind the resulting stack."
	def visit_CombinatorNode(self, combinator):
		env = Environment()
		self.symtab.enter(combinator.name())
		for parameter in combinator.children[1:-1]:
			env.add(str(parameter))
		d = env.index
		self.visit('E', combinator.children[-1], env = env)
		self.code.Update(d)
		self.code.Pop(d)
		self.code.Unwind()
		self.symtab[SymbolTable.CODE] = self.code.clone()
		self.code.clear()
		self.symtab.leave()

class CompileE(CompilationScheme):
	"compiles code that evaluates an expression e to WHNF in environment env, leaving a pointer to the expression on top of the stack"
	def visit_LetNode(self, node, **kwargs):
		self.symtab.enter(node)
		env, n = kwargs['env'].increment(self.symtab[SymbolTable.COUNT]), 0
		for definition in node.children[0:-1]:
			env.add_at(definition.name(), self.symtab[SymbolTable.COUNT] - (n + 1))
			_env, n = kwargs['env'].increment(n), n + 1
			self.visit('E', definition.children[1], env = _env)
		self.visit('E', node.children[-1], env = env)
		self.code.Slide(self.symtab[SymbolTable.COUNT])
		self.symtab.leave()

	def visit_LetRecNode(self, node, **kwargs):
		self.symtab.enter(node)
		self.code.Alloc(self.symtab[SymbolTable.COUNT])
		env, n = kwargs['env'].increment(self.symtab[SymbolTable.COUNT]), 0
		for definition in node.children[0:-1]:
			env.add_at(definition.name(), self.symtab[SymbolTable.COUNT] - (n + 1))
			n += 1
		u = self.symtab[SymbolTable.COUNT] - 1
		for definition in node.children[0:-1]:
			self.visit('E', definition.children[-1], env = env)
			self.code.Update(u)
			u -= 1
		self.visit('E', node.children[-1], env = env)
		self.code.Slide(self.symtab[SymbolTable.COUNT])
		self.symtab.leave()
	
	def visit_CaseNode(self, node, *args, **kwargs):
		self.visit('E', node.children[0], *args, **kwargs)
		cases = {}
		for alt in node.children[1:]:
			self.visit('A', alt, *args, **kwargs)
			cases[self.facade.A.item[0]] = self.facade.A.item[1]
		self.code.Case(cases)

	def visit_ConstructorNode(self, node, *args, **kwargs):
		# massage the tree to get back the arguments for Pack, since they have been parsed as an application spine
		n = int(str(node.children[1]))
		for i, n in enumerate(node.children[2:]):
			_env = kwargs['env'].increment(i)
			self.visit('C', node.children[(i+2)], env = _env)
		self.code.Pack(str(node.children[0]), str(node.children[1]))

	def visit_AddNode(self, node, *args, **kwargs):
		self.visit('E', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.children[0], env = env)
		self.code.Add()

	def visit_MinNode(self, node, *args, **kwargs):
		self.visit('E', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.children[0], env = env)
		self.code.Sub()

	def visit_MulNode(self, node, *args, **kwargs):
		self.visit('E', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.children[0], env = env)
		self.code.Mul()

	def visit_DivNode(self, node, *args, **kwargs):
		self.visit('E', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.children[0], env = env)
		self.code.Div()

	def visit_EqualNode(self, node, *args, **kwargs):
		self.visit('E', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.children[0], env = env)
		self.code.Eq();

	def visit_NotEqualNode(self, node, *args, **kwargs):
		self.visit('E', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.children[0], env = env)
		self.code.Neq();

	def visit_NegateNode(self, node, *args, **kwargs):
		self.visit('E', node.children[0], *args, **kwargs)
		self.code.Neg()

	def visit_NumberNode(self, number, **kwargs):
		self.code.PushI(number.value())

	def fallback(self, node, *args, **kwargs):
		self.visit('C', node, *args, **kwargs)
		self.code.Eval()

class CompileC(CompilationScheme):
	"generates code which constructs the graph of e in environment env, leaving a pointer to it on top of the stack."
	def visit_LetNode(self, node, **kwargs):
		self.symtab.enter(node)
		env, n = kwargs['env'].increment(self.symtab[SymbolTable.COUNT]), 0
		for definition in node.children[0:-1]:
			env.add_at(definition.name(), self.symtab[SymbolTable.COUNT] - (n + 1))
			_env, n = kwargs['env'].increment(n), n + 1
			self.visit('C', definition.children[1], env = _env)
		self.visit('C', node.children[-1], env = env)
		self.code.Slide(self.symtab[SymbolTable.COUNT])
		self.symtab.leave()

	def visit_LetRecNode(self, node, **kwargs):
		self.symtab.enter(node)
		self.code.Alloc(self.symtab[SymbolTable.COUNT])
		env, n = kwargs['env'].increment(self.symtab[SymbolTable.COUNT]), 0
		for definition in node.children[0:-1]:
			env.add_at(definition.name(), self.symtab[SymbolTable.COUNT] - (n + 1))
			n += 1
		u = self.symtab[SymbolTable.COUNT] - 1
		for definition in node.children[0:-1]:
			self.visit('C', definition.children[-1], env = env)
			self.code.Update(u)
			u -= 1
		self.visit('C', node.children[-1], env = env)
		self.code.Slide(self.symtab[SymbolTable.COUNT])
		self.symtab.leave()

	def visit_CaseNode(self, node, *args, **kwargs):
		print 'transform here'
		print node.toStringTree()
		exit()

	def visit_ConstructorNode(self, node, *args, **kwargs):
		# massage the tree to get back the arguments for Pack, since they have been parsed as an application spine
		n = int(str(node.children[1]))
		for i, n in enumerate(node.children[2:]):
			_env = kwargs['env'].increment(i)
			self.visit('C', node.children[(i+2)], env = _env)
		self.code.Pack(str(node.children[0]), str(node.children[1]))

	def visit_ApplicationNode(self, node, **kwargs):
		self.visit('C', node.children[1], env = kwargs['env'])
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.Apply()

	def visit_AddNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('+')
		self.code.Apply()
		self.code.Apply()

	def visit_MinNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('-')
		self.code.Apply()
		self.code.Apply()

	def visit_MulNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('*')
		self.code.Apply()
		self.code.Apply()

	def visit_DivNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('/')
		self.code.Apply()
		self.code.Apply()

	def visit_EqualNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('==')
		self.code.Apply()
		self.code.Apply()

	def visit_NotEqualNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('!=')
		self.code.Apply()
		self.code.Apply()

	def visit_LessThanNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('<')
		self.code.Apply()
		self.code.Apply()

	def visit_LessThanEqualNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('<=')
		self.code.Apply()
		self.code.Apply()

	def visit_GreaterThanNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('>')
		self.code.Apply()
		self.code.Apply()

	def visit_GreaterThanEqualNode(self, node, *args, **kwargs):
		self.visit('C', node.children[1], *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.children[0], env = env)
		self.code.PushG('>=')
		self.code.Apply()
		self.code.Apply()

	def visit_IdentifierNode(self, identifier, **kwargs):
		name = str(identifier)
		try:
			node = self.symtab[name]
		except:
			for a in self.symtab.tree:
				print a
		if isinstance(node, ASTNode):
			self.code.Push(kwargs['env'].get(name))
		else:
			self.code.PushG(name)

	def visit_NegateNode(self, node, *args, **kwargs):
		self.visit('C', node.children[0], *args, **kwargs)
		self.code.PushG('negate')
		self.code.Apply()

	def visit_NumberNode(self, number, **kwargs):
		self.code.PushI(number.value())

class CompileA(CompilationScheme):
	"compiles the code for an alternative in a case expression."

	def visit_AlternativeNode(self, node, *args, **kwargs):
		self.symtab.enter(node)	
		code = Code()
		self.facade.switch_code(code)
		n = len(node.children[1:-1])
		env = kwargs['env'].increment(n)
		code.Split(n)
		np = 0
		for p in node.children[1:-1]:
			env.add_at(str(p), np)
			np += 1
		self.visit('E', node.children[-1], env = env)
		code.Slide(n)
		self.item = (int(str(node.children[0])), code)
		self.facade.switch_code()
		self.symtab.leave()