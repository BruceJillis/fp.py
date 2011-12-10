grammar Core;

options {
   language     = Python;
   output       = AST;
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
   
   PROGRAM = '<program>';
   COMBINATOR = '<combinator>';
   APPLICATION = '<application>';
   ALTERNATIVE = '<alternative>';
   DEFINITION = '<definition>';
}

@header {
   from common import *
}

program!
   : (COMMENT | combinator) (SCOLON combinator | COMMENT)* SCOLON? EOF
     -> ^(PROGRAM<ProgramNode> combinator+)
;

combinator!
   : ID ID* IS expression 
     -> ^(COMBINATOR<CombinatorNode> ID ID* expression)
;

expression!
   : LET definitions IN expression
     -> ^(LET<LetNode> definitions expression)
   | LETREC definitions IN expression
     -> ^(LETREC<LetRecNode> definitions expression)
   | CASE expression OF alternatives
     -> ^(CASE<CaseNode> expression alternatives)
   | LAMBDA ID+ DOT expression
     -> ^(LAMBDA<LambdaNode> ID+ expression)
   | expr1
;

alternatives: alternative (SCOLON! alternative)*;
alternative!
   : LT NUMBER GT ARROW expression
     -> ^(ALTERNATIVE<AlternativeNode> NUMBER expression)
;

definitions: definition (SCOLON! definition)*;
definition!
   : ID IS expression
     -> ^(DEFINITION<DefinitionNode> ID expression)
;

expr1: expr2 (OR<OrNode>^ expr1)*;

expr2: expr3 (AND<AndNode>^ expr2)*;

expr3: expr4 (relop^ expr4)*;

expr4: expr5 ((ADD<AddNode>^|MIN<MinNode>^) expr4)*;

expr5: expr6 ((DIV<DivNode>^|MUL<MulNode>^) expr6)*;

expr6: (lst+=aexpr!)+ {
      # format linear list as application spine
      if len(list_lst) >= 2:
         chain = self._adaptor.nil()
         # b = self._adaptor.createFromType(APPLICATION, "APPLICATION")
         b = ApplicationNode(APPLICATION)
         list_lst.reverse()
         item = list_lst.pop()
         b.addChild(item)
         b.addChild(list_lst.pop())         
         chain = self._adaptor.becomeRoot(b, chain)
         while len(list_lst) > 0:
            # a = self._adaptor.createFromType(APPLICATION, "APPLICATION")
            a = ApplicationNode(APPLICATION)
            a.addChild(list_lst.pop())
            a.addChild(chain)
            chain = a
         self._adaptor.addChild(root_0, chain)
      else:
         self._adaptor.addChild(root_0, list_lst[0])
   }
;

aexpr!
   : ID
     -> ^(ID<IdentifierNode> ID)
   | NUMBER
     -> ^(NUMBER<NumberNode> NUMBER)
   | PACK LCURLY NUMBER COMMA NUMBER RCURLY
     -> ^(PACK<ConstructorNode> NUMBER NUMBER)
   | LPAREN expr1 RPAREN
     -> expr1
;

relop: LT<LessThanNode> | LTE<LessThanEqualNode> | EQ<EqualNode> | NEQ<NotEqualNode> | GTE<GreaterThanEqualNode> | GT<GreaterThanNode>;

NUMBER: ('0'..'9')+;

ID: ('a'..'z' | 'A' .. 'Z') ('a'..'z' | 'A'..'Z' | '0'..'9')* ('?' | '!')?;

WHITESPACE: (' ' | '\t' | '\r' | '\n')+ 
   {$channel=HIDDEN;}
;

COMMENT: '#' (~('\n' | '\r'))* ('\r'? '\n' | EOF)
   {$channel=HIDDEN;}
;