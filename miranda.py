import antlr3
import sys
from collections import defaultdict
from MirandaLexer import *
from MirandaParser import *
from common import Visitor, CompositeVisitor
from CoreParser import *
from ast import LetRecNode, DefinitionNode, LambdaNode

class Offside:
  "This class takes care of bookkeeping for parsing with the offside rule"
  def __init__(self):
    self.stack = [(0,0)]

  def push(self, token):
    line, start = token.getLine(), token.getCharPositionInLine()
    print token
    if len(self.stack) == 0:
      self.stack.append((line, start))
    else:
      _line, _start = self.stack[-1]
      if line >= _line and start > _start:
        print 'INDENT', line, start
        self.stack[-1] = (line, start)
        print self.stack

  def compare(self, token):
    line, start = token.getLine(), token.getCharPositionInLine()
    if len(self.stack) > 0:
      _line, _start = self.stack[-1]
      if line >= _line and start < _start:
        del self.stack[-1]
        print 'DEDENT', line, start
        return True
    return False

def parse(filename):
  with open(filename) as f:
    stream = antlr3.ANTLRInputStream(f)
    lexer = MirandaLexer(stream)
    lexer.offside = Offside()
    tokens = antlr3.CommonTokenStream(lexer)
    parser = MirandaParser(tokens)
    ast = parser.program()
    return ast.tree

class MirandaTransformer(Visitor):
  'base class for all transforming visitors'
  def __init__(self):
    super(MirandaTransformer, self).__init__()
    self.names = defaultdict(int)

  def fresh(self, stub):
    "generate a new fresh name"
    self.names[stub] += 1
    return "$%s%s" % (stub, self.names[stub])

  def token(self, spelling, kind = ID):
    token = CommonToken(
      type = kind,
      text = spelling
    )
    return token

  def id(self, name):
    return IdentifierNode(self.token(str(name), ID))

  def replace(self, source, target):
    i = source.getParent().children.index(source)
    del source.getParent().children[i]
    source.getParent().children.insert(i, target)
    target.setParent(source.getParent())

class MirandaTransformationScheme(MirandaTransformer):
	'base class for transformers that are composed of multiple mutually recursive sub-transformers'
	def __init__(self, facade):
		super(MirandaTransformationScheme, self).__init__()
		self.facade = facade

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
		if hasattr(node, 'children'):
			# call and collect results for all children
			result = []
			for child in node.children:
				ans = self.visit(None, child, **data)
				result.append(ans)
			return result

class Desugar(CompositeVisitor):
  def __init__(self):
    super(Desugar, self).__init__()
    self['P']  = DesugarP(self)
    self['TE'] = DesugarTE(self)
    self['TD'] = DesugarTD(self)
    self.select('P')

class DesugarP(MirandaTransformationScheme):
  def visit_ProgramNode(self, node, **data):
    program = ProgramNode(self.token("PROGRAM", PROGRAM))
    main = CombinatorNode(self.token("COMBINATOR", COMBINATOR))
    main.addChild(self.id('main'))
    program.addChild(main)
    letrec = LetRecNode(self.token("letrec", LETREC))
    for d in node.definitions():
      self.visit('TD', d)
    for d in node.definitions():
      letrec.addChild(d)
    self.visit('TE', node.expression())
    letrec.addChild(node.expression())
    main.addChild(letrec)
    return program

class DesugarTE(MirandaTransformationScheme):
  pass

class DesugarTD(MirandaTransformationScheme):
  def visit_MirandaDefinitionNode(self, node, **data):
    definition = DefinitionNode(self.token("DEFINITION", DEFINITION))
    definition.addChild(self.id(node.children[0]))
    if len(node.parameters()) > 0:
      l = LambdaNode(self.token("LAMBDA", LAMBDA))
      for p in node.parameters():
        l.addChild(self.id(p))
      l.addChild(node.body())
      definition.addChild(l)
    else:
      definition.addChild(node.body())
    self.replace(node, definition)

ast = parse(sys.argv[1])
print
print 'original:'
print ast.toStringTree()

if len(sys.argv) > 2 and sys.argv[2] == '--eval':
  te = Desugar()
  ast = te.visit(ast)
  print
  print 'desugared:'
  print ast.toStringTree()

  from CoreLexer import CoreLexer
  from CoreParser import CoreParser
  from visitors import Identification, CodeGeneration, PrettyPrinter
  from transforms import CaseLifter, LambdaLifter, LambdaSplitter
  from gmachine import State, SymbolTable, run

  # symbol table for global registration of info
  symtab = SymbolTable()

  # phases of the compiler
  identification = Identification(symtab)
  codegeneration = CodeGeneration(symtab)

  # transformations
  #lambdasplitter = LambdaSplitter()
  lambdalifter = LambdaLifter(symtab)
  caselifter = CaseLifter(symtab)

  #lambdasplitter.visit(ast)
  lambdalifter.visit(ast)
  caselifter.visit(ast)

  print
  print 'gmachine:'
  print ast.toStringTree()

  identification.visit(ast)
  codegeneration.visit(ast)

  state = State(symtab)
  print	'result:', run(state, False)