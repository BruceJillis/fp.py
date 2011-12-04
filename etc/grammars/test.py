import sys
import antlr3
import antlr3.tree
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from Eval import Eval

char_stream = antlr3.ANTLRInputStream(sys.stdin)
lexer = ExprLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = ExprParser(tokens)
r = parser.prog()

# this is the root of the AST
root = r.tree

nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)
eval = Eval(nodes)
eval.prog()