from antlr3.tree import CommonTree, CommonToken, INVALID_TOKEN_TYPE;
from CoreLexer import ID, APPLICATION

def mk_ap_chain(list_lst):
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

# class Environment is only used during code generation to maintain stack indices
class	Environment:
	def	__init__(self):
		self.mapping	=	{}
		self.index	=	0
		self.names = 0

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

class LambdaNode(ASTNode):
	spelling = 'LAMDA'

# local definitions
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

# algebraic data types

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

# binary operators 

class BinaryNode(ASTNode):
	def left(self):
		return self.children[0]

	def right(self):
		return self.children[1]

# function application

class ApplicationNode(BinaryNode):
	spelling = 'APPLICATION'

# operators

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