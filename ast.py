"this module bundles all classes and functions pertaining to the AST and it's structure."
from antlr3.tree import CommonTree, CommonToken;
from CoreLexer import ID, APPLICATION
from decimal import *

def mk_ap_chain(list_lst):
	"helper function to: parse a linear list of ASTNodes into an application spine and construct (un)saturated constructors"
	# collapse all constructor nodes, assume there are enough arguments to saturate it
	if len(list_lst) >= 2:
		i = 0
		while i < len(list_lst):
			if list_lst[i].__class__ == ConstructorNode and not list_lst[i].saturated() and len(list_lst[i].expressions()) == 0:
				for j in range(1, list_lst[i].arity()+1):
					if j > len(list_lst):
						break;
					list_lst[i].addChild(list_lst[i+1])
					del list_lst[i+1]
			i += 1
	# check again if the list has more then 1 element, constructor reduction could have dropped it to 1
	# format linear list as application spine
	if len(list_lst) >= 2:
		# now collapse the remaining nodes into an application spine
		chain = ApplicationNode(APPLICATION)
		list_lst.reverse()
		chain.addChild(list_lst.pop())         
		chain.addChild(list_lst.pop())
		while len(list_lst) > 0:
			ap = ApplicationNode(APPLICATION)
			ap.addChild(chain)
			ap.addChild(list_lst.pop())
			chain = ap
		return chain
	else:
		return list_lst[0]

class ASTNode(CommonTree):
	def __init__(self, payload):
		if type(payload) == int:
			CommonTree.__init__(self, CommonToken(type=payload, text=self.spelling))
		else:
			CommonTree.__init__(self, payload)
	
	def __repr__(self):
		return self.toString()

# Top Level Constructs (Program / Combinator)

class ProgramNode(ASTNode):
	spelling = 'PROGRAM'

	def combinators(self):
		return self.children

class CombinatorNode(ASTNode):
	spelling = 'COMBINATOR'

	def name(self):
		return str(self.children[0])

	def parameters(self):
		if len(self.children) == 2:
			return []
		return self.children[1:-1]
	
	def body(self):
		return self.children[-1]

# Lambda Nodes

class LambdaNode(ASTNode):
	spelling = 'LAMDA'

	def parameters(self):
		return self.children[0:-1]
	
	def body(self):
		return self.children[-1]

# Local (Recursive) Definitions

class LetNode(ASTNode):
	spelling = 'LET'

	def definitions(self):
		return self.children[0:-1]

	def body(self):
		return self.children[-1]

class LetRecNode(ASTNode):
	spelling = 'LETREC'

	def definitions(self):
		return self.children[0:-1]

	def body(self):
		return self.children[-1]

class DefinitionNode(ASTNode):
	spelling = 'DEFINITION'

	def name(self):
		return str(self.children[0])

	def body(self):
		return self.children[1]

# Algebraic Data Types

class CaseNode(ASTNode):
	spelling = 'CASE'

	def condition(self):
		return self.children[0]
	
	def alternatives(self):
		return self.children[1:]

class AlternativeNode(ASTNode):
	spelling = 'ALTERNATIVE'
	
	def tag(self):
		return self.children[0].value()

	def parameters(self):
		return self.children[1:-1]

	def body(self):
		return self.children[-1]

class ConstructorNode(ASTNode):
	spelling = 'PACK'

	def tag(self):
		return self.children[0].value()

	def arity(self):
		return self.children[1].value()

	def expressions(self):
		return self.children[2:]

	def saturated(self):		
		return self.arity() != 0 and len(self.expressions()) != 0 and self.arity() == len(self.expressions())

# Binary Operators 

class BinaryNode(ASTNode):
	def left(self):
		return self.children[0]

	def right(self):
		return self.children[1]

# Function Application

class ApplicationNode(BinaryNode):
	spelling = 'APPLICATION'

# Operators

class OrNode(BinaryNode):
	spelling = 'OR'

class AndNode(BinaryNode):
	spelling = 'AND'

class LessThanNode(BinaryNode):
	spelling = 'LT'

class LessThanEqualNode(BinaryNode):
	spelling = 'LTE'

class GreaterThanNode(BinaryNode):
	spelling = 'LT'

class GreaterThanEqualNode(BinaryNode):
	spelling = 'GTE'

class EqualNode(BinaryNode):
	spelling = 'EQ'

class NotEqualNode(BinaryNode):
	spelling = 'NEQ'

class AddNode(BinaryNode):
	spelling = 'ADD'

class MinNode(BinaryNode):
	spelling = 'MIN'

class DivNode(BinaryNode):
	spelling = 'DIV'

class MulNode(BinaryNode):
	spelling = 'MUL'

# Basic Primitive Values (id's and numeric constants)

class BasicNode(ASTNode):
	def toStringTree(self):
		return self.toString()

class IdentifierNode(BasicNode):
	spelling = 'ID'

	def binder(self, node = None):
		if node == None:
			if hasattr(self, '_binder'):
				return self._binder
			return None
		self._binder = node

class IntNode(BasicNode):
	spelling = 'INT'

	def value(self):
		return int(self.toString())

class FloatNode(BasicNode):
	spelling = 'FLOAT'

	def value(self):
		return Decimal(self.toString())

class CharNode(BasicNode):
	spelling = 'CHAR'

	def value(self):
		return self.toString().replace('\'', '')
