from antlr3.tree import CommonTree, CommonToken, INVALID_TOKEN_TYPE;

def mk_ap_chain(list_lst, APPLICATION):
	# collapse all constructor nodes, assume there are enough arguments to saturate it
	if len(list_lst) >= 2:
		i = 0
		while i < len(list_lst):
			if list_lst[i].__class__ == ConstructorNode and not list_lst[i].saturated():
				for j in range(1, list_lst[i].arity()+1):
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
		exit()
	else:
		return list_lst[0]

# AST Nodes

class ASTNode(CommonTree):
	def __init__(self, payload):
		if type(payload) == int:
			CommonTree.__init__(self, CommonToken(type=payload, text=self.spelling))
		else:
			CommonTree.__init__(self, payload)
	
	def __repr__(self):
		return self.toString()

class ProgramNode(ASTNode):
	spelling = 'PROGRAM'

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

class IfNode(ASTNode):
	spelling = 'IF'

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

	def tag(self):
		return self.children[0].value()

	def arity(self):
		return self.children[1].value()

	def expressions(self):
		return self.children[2:]

	def saturated(self):		
		return self.arity() != 0 and len(self.expressions()) != 0 and self.arity() == len(self.expressions())

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

class NegateNode(ASTNode):
	spelling = 'NEG'

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