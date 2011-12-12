from antlr3.tree import CommonTree, CommonToken, INVALID_TOKEN_TYPE;

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

class IfNode(ASTNode):
	spelling = 'IF'

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