from antlr3.tree import CommonTree, CommonToken, INVALID_TOKEN_TYPE;

# Symbol Table

class SymbolTable:
	"the symbol table maintains a tree of scope's such that we can re-enter scopes in different phases of the compiler and enrich the information present."
	# reserved field names

	# name of the field containing the back pointer to the parent, None for the root node
	PARENT = '__parent__'
	# name of the field containing code for combinators
	CODE = '__code__'
	# contains a count
	COUNT = '__count__'

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
		if key in self.tree:
			return self.tree[key]
		tree = self.tree[SymbolTable.PARENT]
		while tree != None:
			if key in tree:
				return tree[key]
			tree = tree[SymbolTable.PARENT]
		raise KeyError(key)

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

	def value(self):
		return int(self.toString())

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