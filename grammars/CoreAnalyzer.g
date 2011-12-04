tree grammar CoreAnalyzer;

options {
   language     = Python;
   ASTLabelType = CommonTree;
   tokenVocab   = Core;
   rewrite      = true;
}

start[info]
   : combinator[info]+
;

combinator[info]
   : ^(COMBINATOR n=ID {info.current = $n.text} (p+=ID)* expression[info]) {
      info.combinator($n.text, $p)
   }
;

expression[info]
   : ^(LET definition[info, None]+ expression[info])
   | {
      index = self.input.index()
      print index
   }
     ^(LETREC (definition[info, index])+ expression[info])
   | ^(CASE expression[info] alternative[info]+)
   | ^(LAMBDA ID+ expression[info])
   | ^(MUL expression[info] expression[info])
   | ^(DIV expression[info] expression[info])
   | ^(ADD expression[info] expression[info])
   | ^(MIN expression[info] expression[info])
   | ^(AND expression[info] expression[info])
   | ^(OR expression[info] expression[info])
   | ^(EQ expression[info] expression[info])
   | ^(NEQ expression[info] expression[info])
   | ^(LT expression[info] expression[info])
   | ^(LTE expression[info] expression[info])
   | ^(GT expression[info] expression[info])
   | ^(GTE expression[info] expression[info])
   | ^(APPLICATION expression[info] expression[info])
   | basic[info]
;

basic[info]
   : ID
   | NUMBER
   | ^(PACK NUMBER NUMBER)
;

alternative[info]
   : ^(ARROW NUMBER expression[info])
;

definition[info, index]
   : ^(IS ID expression[info]) {
      if index != None:
         info.letrec(index, $ID.text)
   }
;