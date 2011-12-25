from antlr3.tree import CommonTree, CommonToken
from ast import ASTNode

class ProgramNode(ASTNode):
  spelling = 'PROGRAM'

  def definitions(self):
    return self.children[0:-1]

  def expression(self):
    return self.children[-1]

class MirandaDefinitionNode(ASTNode):
	spelling = 'DEFINITION'

	def name(self):
		return str(self.children[0])

	def parameters(self):
		return self.children[1:-1]

	def body(self):
		return self.children[-1]