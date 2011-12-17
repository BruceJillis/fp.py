grammar Core;

options {
   language     = Python;
   output       = AST;
   ASTLabelType = Node;
   memoize      = true;
   backtrack    = true;
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
   PACK   = 'Pack';
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
   from ast import *
}

program!
   : (COMMENT | combinator) (SCOLON combinator | COMMENT)* SCOLON? EOF
     -> ^(PROGRAM<ProgramNode> combinator+)
;

combinator!
   : ID ID* IS expression 
     -> ^(COMBINATOR<CombinatorNode> ID<IdentifierNode> ID<IdentifierNode>* expression)
;

expression!
   : LET definitions IN expression
     -> ^(LET<LetNode> definitions expression)
   | LETREC definitions IN expression
     -> ^(LETREC<LetRecNode> definitions expression)
   | CASE expression OF alternatives
     -> ^(CASE<CaseNode> expression alternatives)
   | LAMBDA ID+ DOT expression
     -> ^(LAMBDA<LambdaNode> ID<IdentifierNode>+ expression)
   | expr1
;

alternatives: alternative (COMMA! alternative)*;
alternative!
   : LT NUMBER GT ID* ARROW expression
     -> ^(ALTERNATIVE<AlternativeNode> NUMBER<NumberNode> ID<IdentifierNode>* expression)
;

definitions: definition (COMMA! definition)*;
definition!
   : ID IS expression
     -> ^(DEFINITION<DefinitionNode> ID<IdentifierNode> expression)
;

expr1: expr2 (OR<OrNode>^ expression)*;

expr2: expr3 (AND<AndNode>^ expression)*;

expr3: expr4 (relop^ expression)*;

expr4: expr5 ((ADD<AddNode>^|MIN<MinNode>^) expression)*;

expr5: expr6 ((DIV<DivNode>^|MUL<MulNode>^) expression)*;

expr6: (lst+=aexpr!)+ {
   self._adaptor.addChild(root_0, mk_ap_chain(list_lst))
};

aexpr!
   : ID
     -> ^(ID<IdentifierNode>)
   | NUMBER
     -> ^(NUMBER<NumberNode>)
   | PACK LCURLY NUMBER COMMA NUMBER RCURLY
     -> ^(PACK<ConstructorNode> NUMBER<NumberNode> NUMBER<NumberNode>)
   | LPAREN expression RPAREN
     -> expression
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