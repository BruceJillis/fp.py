import antlr3
import sys
from MirandaLexer import *
from MirandaParser import *

class Offside:
  def __init__(self):
    self.stack = [(0,0)]

  def push(self, line, start):
    print 'INDENT', line, start
    self.stack.append((line, start))

  def compare(self, line, start):
    _line, _start = self.stack[-1]
    if line >= _line and start < _start:
      del self.stack[-1]
      print 'DEDENT', line, start
      return True
    return False

with open(sys.argv[1]) as f:
  stream = antlr3.ANTLRInputStream(f)
  lexer = MirandaLexer(stream)
  lexer.offside = Offside()
  tokens = antlr3.CommonTokenStream(lexer)
  # print [(t.type, t.text) for t in tokens.getTokens()]
  parser = MirandaParser(tokens)
  ast = parser.program()
  print ast.tree.toStringTree()