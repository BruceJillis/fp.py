from antlr3.tree import CommonTree, CommonToken, INVALID_TOKEN_TYPE;

# Symbol Table

class SymbolTable:
	"the symbol table maintains a tree of scope's such that we can re-enter scopes in different phases of the compiler and enrich the information present."
	# name of the field containing the back pointer to the parent, None for the root node
	PARENT = '__parent__'

	def __init__(self):
		self.tree = {}
		self.root = self.tree
		self.tree[SymbolTable.PARENT] = None

	def enter(self, context):
		'enter a new scope'
		key = str(context)
		if not key in self.tree:
			self.tree[key] = {}
		parent = self.tree
		self.tree = self.tree[key]
		self.tree[SymbolTable.PARENT] = parent

	def leave(self):
		'leave current scope'
		if self.tree[SymbolTable.PARENT] == None:
			raise Error('cannot pop root scope!')
		self.tree = self.tree[SymbolTable.PARENT]

	def __setitem__(self, key, value):
		self.tree[key] = value

	def __getitem__(self, key):
		return self.tree[key]

	def __contains__(self, key):
		"return True if this or a parent scope contains key"
		if key in self.tree:
			return True
		tree = self.tree[SymbolTable.PARENT]
		while tree != None:
			if key in tree:
				return True
			tree = tree[SymbolTable.PARENT]
		return False

	def __len__(self, key):
		return len(self.tree.keys())
	
	def prettyprint(self, tree, indent = 0):
		"prettyprint the tree"
		try:
			result = '\n'
			for k in tree:
				if k != SymbolTable.PARENT:
					result += (indent * '   ') + '%s = %s\n' % (k, self.prettyprint(tree[k], indent+1))
			return result
		except:
			return str(tree)

	def __str__(self):
		return self.prettyprint(self.root)

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
	EVAL = 10

	ADD = 11
	SUB = 12
	MUL = 13
	DIV = 14
	NEG = 15

	EQ = 16
	NEQ = 17
	LT = 18
	LTE = 19
	GT = 20
	GTE = 21
	
	COND = 22

	def __init__(self):
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
		if instr[0] == self.EVAL:
			str = "EVAL"
		if instr[0] == self.ADD:
			str = "ADD"
		if instr[0] == self.SUB:
			str = "SUB"
		if instr[0] == self.MUL:
			str = "MUL"
		if instr[0] == self.DIV:
			str = "DIV"
		if instr[0] == self.NEG:
			str = "NEG"
		if instr[0] == self.EQ:
			str = "EQ"
		if instr[0] == self.NEQ:
			str = "NEQ"
		if instr[0] == self.LT:
			str = "LT"
		if instr[0] == self.LTE:
			str = "LTE"
		if instr[0] == self.GT:
			str = "GT"
		if instr[0] == self.GTE:
			str = "GTE"
		if instr[0] == self.COND:
			str = "COND %s %s" % (instr[1], instr[2])
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

	def Eval(self):
		self.instructions.append((Code.EVAL,))

	def Add(self):
		self.instructions.append((Code.UNWIND,))

	def Push(self, index, name = ''):
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

# AST Nodes

class ASTNode(CommonTree):
	def __init__(self, payload):
		if type(payload) == int:
			CommonTree.__init__(self, CommonToken(type=payload, text=self.spelling))
		else:
			CommonTree.__init__(self, payload)
	
	def analyze(self, info):
		raise NotImplementedError
	
	def __repr__(self):
		return self.toString()

class ProgramNode(ASTNode):
	spelling = 'PROGRAM'

	def analyze(self, info):
		raise NotImplementedError

class CombinatorNode(ASTNode):
	spelling = 'COMBINATOR'

	def name(self):
		return str(self.children[0])

	def parameters(self):
		if len(self.children) == 2:
			return []
		return self.children[1:-1]

class LambdaNode(ASTNode):
	spelling = 'LAMDA'

# local definitions
class LetNode(ASTNode):
	spelling = 'LET'

class LetRecNode(ASTNode):
	spelling = 'LETREC'

class DefinitionNode(ASTNode):
	spelling = 'DEFINITION'

	def name(self):
		return str(self.children[0])

# function application
class ApplicationNode(ASTNode):
	spelling = 'APPLICATION'

# algebraic data types

class CaseNode(ASTNode):
	spelling = 'CASE'

class AlternativeNode(ASTNode):
	spelling = 'ALTERNATIVE'

class ConstructorNode(ASTNode):
	spelling = 'PACK'

# basic values (id's and numeric constants)

class BasicNode(ASTNode):
	def toStringTree(self):
		return self.toString()

class IdentifierNode(BasicNode):
	spelling = 'ID'

class NumberNode(BasicNode):
	spelling = 'NUMBER'

# operators

class OrNode(ASTNode):
	spelling = 'OR'

class AndNode(ASTNode):
	spelling = 'AND'

class LessThanNode(ASTNode):
	spelling = 'LT'

class LessThanEqualNode(ASTNode):
	spelling = 'LTE'

class GreaterThanNode(ASTNode):
	spelling = 'LT'

class GreaterThanEqualNode(ASTNode):
	spelling = 'GTE'

class EqualNode(ASTNode):
	spelling = 'EQ'

class NotEqualNode(ASTNode):
	spelling = 'NEQ'

class AddNode(ASTNode):
	spelling = 'ADD'

class MinNode(ASTNode):
	spelling = 'MIN'

class DivNode(ASTNode):
	spelling = 'DIV'

class MulNode(ASTNode):
	spelling = 'MUL'