from antlr3.tree import CommonTree, CommonToken, INVALID_TOKEN_TYPE;

class Node(CommonTree):
	def __init__(self, payload):
		if type(payload) == int:
			CommonTree.__init__(self, CommonToken(type=payload, text=self.spelling))
		else:
			CommonTree.__init__(self, payload)

class ProgramNode(Node):
	spelling = 'PROGRAM'

class CombinatorNode(Node):
	spelling = 'COMBINATOR'

class LambdaNode(Node):
	spelling = 'LAMDA'

# local definitions
class LetNode(Node):
	spelling = 'LET'

class LetRecNode(Node):
	spelling = 'LETREC'

class DefinitionNode(Node):
	spelling = 'DEFINITION'

# function application
class ApplicationNode(Node):
	spelling = 'APPLICATION'

# algebraic data types
class CaseNode(Node):
	spelling = 'CASE'

class AlternativeNode(Node):
	spelling = 'ALTERNATIVE'

class ConstructorNode(Node):
	spelling = 'PACK'

# basic values (id's and numeric constants)
class BasicNode(Node):
	def toStringTree(self):
		return self.toString()

class IdentifierNode(BasicNode):
	spelling = 'ID'

class NumberNode(BasicNode):
	spelling = 'NUMBER'

# operators
class OrNode(Node):
	spelling = 'OR'

class AndNode(Node):
	spelling = 'AND'

class LessThanNode(Node):
	spelling = 'LT'

class LessThanEqualNode(Node):
	spelling = 'LTE'

class GreaterThanNode(Node):
	spelling = 'LT'

class GreaterThanEqualNode(Node):
	spelling = 'GTE'

class EqualNode(Node):
	spelling = 'EQ'

class NotEqualNode(Node):
	spelling = 'NEQ'

class AddNode(Node):
	spelling = 'ADD'

class MinNode(Node):
	spelling = 'MIN'

class DivNode(Node):
	spelling = 'DIV'

class MulNode(Node):
	spelling = 'MUL'