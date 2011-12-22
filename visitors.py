from common import Visitor, CompositeVisitor
from gmachine import Code, SymbolTable
from common import Environment
from ast import *

class PrettyPrinter(Visitor):
	'pretty print a Core program'
	def visit_ProgramNode(self, node):
		for c in node.combinators():
			self.visit(c)
		
	def visit_CombinatorNode(self, node):
		print node.name(),
		for p in node.parameters():
			print str(p),
		print '=',
		self.visit(node.body())
		print ';'

	def visit_LetNode(self, node):
		print 'let',
		for definition in node.children[0:-1]:
			self.visit(definition)
		print 'in',
		self.visit(node.children[-1])

	def visit_LetRecNode(self, node):
		print 'letrec',
		for definition in node.children[0:-1]:
			self.visit(definition)
		print 'in',
		self.visit(node.children[-1])

	def visit_DefinitionNode(self, node):
		self.visit(node.children[0])
		print '=',
		self.visit(node.children[1])

	def visit_CaseNode(self, node, *args, **kwargs):
		print 'case',
		self.visit(node.condition())
		print 'of',
		for alt in node.alternatives():
			print '<',
			self.visit(alt.children[0])
			print '> =',
			self.visit(alt.body())

	def visit_LambdaNode(self, node):
		print '\\',
		for p in node.parameters():
			self.visit(p)
		print '.',
		self.visit(node.body())

	def visit_ApplicationNode(self, node):
		print '(',
		self.visit(node.left())
		self.visit(node.right())
		print ')',

	def visit_EqualNode(self, node):
		self.visit(node.left())
		print '==',
		self.visit(node.right())

	def visit_NotEqualNode(self, node):
		self.visit(node.left())
		print '!=',
		self.visit(node.right())

	def visit_NegateNode(self, node):
		print '-',
		self.visit(node.left())

	def visit_AddNode(self, node):
		self.visit(node.left())
		print '+',
		self.visit(node.right())

	def visit_MinNode(self, node):
		self.visit(node.left())
		print '-',
		self.visit(node.right())

	def visit_DivNode(self, node):
		self.visit(node.left())
		print '/',
		self.visit(node.right())

	def visit_MulNode(self, node):
		self.visit(node.left())
		print '*',
		self.visit(node.right())

	def visit_AndNode(self, node):
		self.visit(node.left())
		print '&',
		self.visit(node.right())

	def visit_OrNode(self, node):
		self.visit(node.left())
		print '|',
		self.visit(node.right())

	def visit_IdentifierNode(self, node):
		print node,

	def visit_NumberNode(self, node):
		print node,

class Identification(Visitor):
	"identify variables, combinators."
	def __init__(self, symtab):
		self.symtab = symtab

	def visit_CombinatorNode(self, combinator):
		if combinator.name() in self.symtab:
			raise SyntaxError('%s already defined' % combinator.name())
		self.symtab[combinator.name()] = {}
		self.symtab[combinator.name()]['__count__'] = len(combinator.parameters())
		binders = {
			combinator.name(): combinator
		}
		for parameter in combinator.parameters():
			binders[str(parameter)] = parameter
		self.visit(combinator.body(), env=binders)

	def visit_ApplicationNode(self, node, **kwargs):
		self.visit(node.right(), **kwargs)
		self.visit(node.left(), **kwargs)

	def visit_LetNode(self, node, **kwargs):
		for definition in node.definitions():
			kwargs['env'][definition.name()] = definition.children[0]
			self.visit(definition.children[-1], **kwargs)
		self.visit(node.body(), **kwargs)

	def visit_LetRecNode(self, node, **kwargs):
		for definition in node.definitions():
			kwargs['env'][definition.name()] = definition.children[0]
		for definition in node.definitions():
			self.visit(definition.children[-1], **kwargs)
		self.visit(node.body(), **kwargs)

	def visit_CaseNode(self, node, **kwargs):
		self.visit(node.condition(), **kwargs)
		for alt in node.alternatives():
			self.visit(alt, **kwargs)

	def visit_AlternativeNode(self, node, **kwargs):
		for p in node.parameters():
			kwargs['env'][str(p)] = p
		self.visit(node.body(), **kwargs)

	def visit_IdentifierNode(self, node, **kwargs):
		if str(node) in kwargs['env']:
			node.binder(kwargs['env'][str(node)])

class CodeGeneration(CompositeVisitor):
	"generate GMachine code for the supplied program."
	def __init__(self, symtab):
		super(CodeGeneration, self).__init__()
		self.symtab = symtab
		self['SC'] = CompileSC(self, symtab)
		self['R'] = CompileR(self, symtab)
		self['C'] = CompileC(self, symtab)
		self['E'] = CompileE(self, symtab)
		self['A'] = CompileA(self, symtab)
		self.select('SC')
		self.code = Code()
		self.switch_code(self.code)


	def switch_code(self, code = None):
		"switch the code object to a new instance"
		for k in self.schemes:
			if code != None:
				self.schemes[k].code = code
			else:
				self.schemes[k].code = self.code

class CompilationScheme(Visitor):
	def __init__(self, facade, symtab):
		self.symtab = symtab
		self.facade = facade
		self.code = None
	
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

class CompileSC(CompilationScheme):
	'generates the G-machine code for the supercombinator definition d.'
	def visit_ProgramNode(self, node):
		for combinator in node.combinators():
			self.visit('R', combinator)

class CompileR(CompilationScheme):
	"generates code which instantiates the expression combinator.children[-1] in environment env, for a supercombinator of arity d, and then proceeds to unwind the resulting stack."

	def visit_CombinatorNode(self, node):
		env = Environment()
		for parameter in node.parameters():
			env.add(str(parameter))
		d = env.index
		self.visit('E', node.body(), env = env)
		self.code.Update(d)
		self.code.Pop(d)
		self.code.Unwind()
		self.symtab[node.name()][SymbolTable.CODE] = self.code.clone()
		self.code.clear()

class CompileE(CompilationScheme):
	"compiles code that evaluates an expression e to WHNF in environment env, leaving a pointer to the expression on top of the stack"

	def visit_LetNode(self, node, **kwargs):
		count = len(node.definitions())
		env, n = kwargs['env'].increment(count), 0
		for definition in node.definitions():
			env.add_at(definition.name(), count - (n + 1))
			_env, n = kwargs['env'].increment(n), n + 1
			self.visit('E', definition.body(), env = _env)
		self.visit('E', node.body(), env = env)
		self.code.Slide(count)

	def visit_LetRecNode(self, node, **kwargs):
		count = len(node.definitions())
		self.code.Alloc(count)
		env, n = kwargs['env'].increment(count), 0
		for definition in node.definitions():
			env.add_at(definition.name(), count - (n + 1))
			n += 1
		u = count - 1
		for definition in node.definitions():
			self.visit('E', definition.body(), env = env)
			self.code.Update(u)
			u -= 1
		self.visit('E', node.body(), env = env)
		self.code.Slide(count)
	
	def visit_CaseNode(self, node, *args, **kwargs):
		self.visit('E', node.condition(), *args, **kwargs)
		cases = {}
		for alt in node.alternatives():
			self.visit('A', alt, *args, **kwargs)
			cases[self.facade['A'].item[0]] = self.facade['A'].item[1]
		self.code.Case(cases)

	def visit_ConstructorNode(self, node, *args, **kwargs):
		for i, n in enumerate(node.expressions()):
			_env = kwargs['env'].increment(i)
			self.visit('C', node.children[(i+2)], env = _env)
		self.code.Pack(node.tag(), node.arity())

	def visit_AndNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.And()

	def visit_OrNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.Or()

	def visit_AddNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.Add()

	def visit_MinNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.Sub()

	def visit_MulNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.Mul()

	def visit_DivNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.Div()

	def visit_EqualNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.Eq();

	def visit_NotEqualNode(self, node, *args, **kwargs):
		self.visit('E', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('E', node.left(), env = env)
		self.code.Neq();

	def visit_NegateNode(self, node, *args, **kwargs):
		self.visit('E', node.left(), *args, **kwargs)
		self.code.Neg()

	def visit_NumberNode(self, number, **kwargs):
		self.code.PushI(number.value())

	def fallback(self, node, *args, **kwargs):
		self.visit('C', node, *args, **kwargs)
		self.code.Eval()

class CompileC(CompilationScheme):
	"generates code which constructs the graph of e in environment env, leaving a pointer to it on top of the stack."

	def visit_LetNode(self, node, **kwargs):
		count = len(node.definitions())
		env, n = kwargs['env'].increment(count), 0
		for definition in node.definitions():
			env.add_at(definition.name(), count - (n + 1))
			_env, n = kwargs['env'].increment(n), n + 1
			self.visit('C', definition.body(), env = _env)
		self.visit('C', node.body(), env = env)
		self.code.Slide(count)

	def visit_LetRecNode(self, node, **kwargs):
		count = len(node.definitions())
		self.code.Alloc(count)
		env, n = kwargs['env'].increment(count), 0
		for definition in node.definitions():
			env.add_at(definition.name(), count - (n + 1))
			n += 1
		u = count - 1
		for definition in node.definitions():
			self.visit('C', definition.body(), env = env)
			self.code.Update(u)
			u -= 1
		self.visit('C', node.body(), env = env)
		self.code.Slide(count)

	def visit_CaseNode(self, node, **data):
		self.visit('E', node.condition(), **data)
		for alt in node.alternatives():
			self.visit('A', alt, **data)

	def visit_ConstructorNode(self, node, *args, **kwargs):
		for i, n in enumerate(node.expressions()):
			_env = kwargs['env'].increment(i)
			self.visit('C', node.children[(i+2)], env = _env)
		self.code.Pack(node.tag(), node.arity())

	def visit_ApplicationNode(self, node, **kwargs):
		self.visit('C', node.right(), env = kwargs['env'])
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.Apply()

	def visit_AndNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('&')
		self.code.Apply()
		self.code.Apply()

	def visit_OrNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('|')
		self.code.Apply()
		self.code.Apply()

	def visit_AddNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('+')
		self.code.Apply()
		self.code.Apply()

	def visit_MinNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('-')
		self.code.Apply()
		self.code.Apply()

	def visit_MulNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('*')
		self.code.Apply()
		self.code.Apply()

	def visit_DivNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('/')
		self.code.Apply()
		self.code.Apply()

	def visit_EqualNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('==')
		self.code.Apply()
		self.code.Apply()

	def visit_NotEqualNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('!=')
		self.code.Apply()
		self.code.Apply()

	def visit_LessThanNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('<')
		self.code.Apply()
		self.code.Apply()

	def visit_LessThanEqualNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('<=')
		self.code.Apply()
		self.code.Apply()

	def visit_GreaterThanNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('>')
		self.code.Apply()
		self.code.Apply()

	def visit_GreaterThanEqualNode(self, node, *args, **kwargs):
		self.visit('C', node.right(), *args, **kwargs)
		env = kwargs['env'].increment(1)
		self.visit('C', node.left(), env = env)
		self.code.PushG('>=')
		self.code.Apply()
		self.code.Apply()

	def visit_IdentifierNode(self, identifier, **kwargs):
		name = str(identifier)
		if identifier.binder().__class__ == IdentifierNode:
			self.code.Push(kwargs['env'].get(name))
		else:
			self.code.PushG(name)

	def visit_NegateNode(self, node, *args, **kwargs):
		self.visit('C', node.left(), *args, **kwargs)
		self.code.PushG('negate')
		self.code.Apply()

	def visit_NumberNode(self, number, **kwargs):
		self.code.PushI(number.value())

class CompileA(CompilationScheme):
	"compiles the code for an alternative in a case expression."

	def visit_AlternativeNode(self, node, *args, **kwargs):
		# temporarily switch to a new code object to store the generated code
		code = Code()
		self.facade.switch_code(code)
		# now generate code as normal
		count = len(node.parameters())
		env = kwargs['env'].increment(count)
		code.Split(count)
		np = 0
		for p in node.parameters():
			env.add_at(str(p), np)
			np += 1
		self.visit('E', node.body(), env = env)
		code.Slide(count)
		# switch back to the previous code object, store the new generated code object in self.item for later retrieval
		self.item = (node.tag(), code)
		self.facade.switch_code()
