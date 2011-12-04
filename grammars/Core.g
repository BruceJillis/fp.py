grammar Core;

options {
   language     = Python;
   output       = AST;
   ASTLabelType = CommonTree;
   backtrack    = true;
   memoize      = true;
}

tokens {
   IS     = '=';
   EQ     = '==';
   NEQ    = '!=';
   LT     = '<';
   LTE    = '<=';
   GT     = '>';
   GTE    = '>=';
   ADD    = '+';
   MIN    = '-';
   MUL    = '*';
   DIV    = '/';
   AND    = '&';
   OR     = '|';
   NOT    = '!';
   LPAREN = '(';
   RPAREN = ')';
   SCOLON = ';';
   COLON  = ':';
   COMMA  = ',';
   DOT    = '.';
   LAMBDA = '\\';
   ARROW  = '->';

   // keywords
   LET    = 'let';
   LETREC = 'letrec';
   CASE   = 'case';
   IN     = 'in';
   OF     = 'of';
   PACK   = 'pack';
   LCURLY = '{';
   RCURLY = '}';
   CASE   = 'case';
   OF     = 'of';

   COMBINATOR = '<combinator>';
   APPLICATION = '<application>';
}

start: (COMMENT | combinator) (SCOLON! combinator | COMMENT)* SCOLON!? EOF!;

combinator: i=ID ID* IS expression -> ^(COMBINATOR[i] ID ID* expression);

expression: LET^ definitions IN! expression
          | LETREC^ definitions IN! expression
          | CASE^ expression OF! alternatives
          | LAMBDA^ ID+ DOT! expression
          | expr1
          ;

alternatives: alternative (SCOLON! alternative)*;
alternative: LT! NUMBER GT! ARROW^ expression;

definitions: definition (SCOLON! definition)*;
definition: ID IS^ expression;

expr1: expr2 (OR^ expr1)*
     ;

expr2: expr3 (AND^ expr2)*
     ;

expr3: expr4 (relop^ expr4)*
     ;

expr4: expr5 ((ADD^|MIN^) expr4)*
     ;

expr5: expr6 ((DIV^|MUL^) expr6)*
     ;

expr6: (lst+=aexpr!)+ {
      if len(list_lst) >= 2:
         chain = self._adaptor.nil()
         b = self._adaptor.createFromType(APPLICATION, "APPLICATION")
         list_lst.reverse()
         item = list_lst.pop()
         b.addChild(list_lst.pop())
         b.addChild(item)
         chain = self._adaptor.becomeRoot(b, chain)
         while len(list_lst) > 0:
            a = self._adaptor.createFromType(APPLICATION, "APPLICATION")
            a.addChild(list_lst.pop())
            a.addChild(chain)
            chain = a
         self._adaptor.addChild(root_0, chain)
      else:
         self._adaptor.addChild(root_0, list_lst[0])
   }
;

aexpr: ID
     | NUMBER
     | PACK^ LCURLY! NUMBER COMMA! NUMBER RCURLY!
     | LPAREN! expr1 RPAREN!
     ;

relop: LT | LTE | EQ | NEQ | GTE | GT;

NUMBER: ('0'..'9')+;

ID: ('a'..'z' | 'A' .. 'Z') ('a'..'z' | 'A'..'Z' | '0'..'9')* ('?' | '!')?;

WHITESPACE: (' ' | '\t' | '\r' | '\n')+ 
   {$channel=HIDDEN;}
;

COMMENT: '#' (~('\n' | '\r'))* ('\r'? '\n' | EOF)
   {$channel=HIDDEN;}
;