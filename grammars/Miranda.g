grammar Miranda;

options {
  language     = Python;
  output       = AST;
  ASTLabelType = Node;
  backtrack    = true;
  memoize      = true;
}

tokens {
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
   LPAREN = '(';
   RPAREN = ')';
   COMMA  = ',';
   DOT    = '.';
   IS     = '=';
   NOT    = '!';
   COMMA  = ',';
   COLON  = ':';
   LBRACKET = '[';
   RBRACKET = ']';
   SINGLE_QUOTE = '\'';
   DOUBLE_QUOTE = '"';
   SUBTRACT = '--';
   CONCAT = '++';

   TRUE = 'true';
   FALSE = 'false';

   MOD = 'mod';
   IDIV = 'div';
   EXP = '^';

   WHERE = 'where';
   OTHERWISE = 'otherwise';
   PROGRAM = 'program';
    
   // imaginary
   DEDENT     = '<dedent>';
   DEFINITION = '<definition>';
   TUPLE      = '<tuple>';
   LIST       = '<list>';
   SECTION    = '<section>';
   GUARD      = '<guard>';
}

@header {
  from ast import mk_ap_chain, IntNode, FloatNode, IdentifierNode, CharNode, AddNode, MinNode, MulNode, DivNode
  from miranda_ast import *
}

@lexer::members {
  offside = None

  next = None
  def nextToken(self):
    if self.next != None:
      result = self.next
      self.next = None
      return result
    while 1:
      self._state.token = None
      self._state.channel = DEFAULT_CHANNEL
      self._state.tokenStartCharIndex = self.input.index()
      self._state.tokenStartCharPositionInLine = self.input.charPositionInLine
      self._state.tokenStartLine = self.input.line
      self._state.text = None
      if self.input.LA(1) == EOF:
        return self.makeEOFToken()
      try:
        self.mTokens()
        if self._state.token is None:
          self.emit()
        elif self._state.token == SKIP_TOKEN:
          continue
        
        if self._state.token.type == IS:
          self.offside.push(self._state.token.getLine(), self._state.token.getCharPositionInLine())
        else:
          if self.offside.compare(self._state.token.getLine(), self._state.token.getCharPositionInLine()):
            # emit a dedent token
            self.next = self._state.token
            return CommonToken(type=DEDENT, text='DEDENT')

        return self._state.token
      except NoViableAltException, re:
        self.reportError(re)
        self.recover(re) # throw out current char and try again
      except RecognitionException, re:
        self.reportError(re)      
}

program: 
  (definition DEDENT)* expression EOF
  -> ^(PROGRAM<ProgramNode> definition* expression)
;

definition: 
  ID parameter* IS expression guard? 
  -> ^(DEFINITION<MirandaDefinitionNode> ID parameter* expression guard?)
;

guard: COMMA (expression|OTHERWISE);

parameter
  : basic ((COLON|ADD)^ parameter)?
;
  
basic
  : ID
  | INT
  | FLOAT
  | boolean
  | list
  | tuple
  | LPAREN! parameter RPAREN!
;

expression: expr0;

expr0: expr1 ((CONCAT^|SUBTRACT^|COLON^) expr0)?;

expr1: expr2 (OR^ expression)*;

expr2: expr3 (AND^ expression)*;

expr3: expr4 ((LT|LTE|EQ|NEQ|GTE|GT)^ expression)*;

expr4: expr5 ((ADD<AddNode>^|MIN<MinNode>^) expr5)*;

expr5: expr6 ((DIV<DivNode>^|MUL<MulNode>^) expr6)*;

expr6: expr7 ((IDIV^|MOD^) expr7)*;

expr7: expr8 ((EXP^) expr8)*;

expr8: aexpr+ {
  chain = mk_ap_chain(root_0.children)
  root_0.children = []
  self._adaptor.addChild(root_0, chain)
};

aexpr
  : ID
    -> ^(ID<IdentifierNode>)
  | INT
    -> ^(INT<IntNode>)
  | FLOAT
    -> ^(FLOAT<FloatNode>)
  | CHAR
    -> ^(CHAR<CharNode>)
  | STRING
  | NOT expression
  | boolean
  | section
  | tuple
  | list
  | LPAREN! expression RPAREN!
;

tuple: LPAREN expression (COMMA expression)+ RPAREN
       -> ^(TUPLE expression*)
;

list: LBRACKET expression? (COMMA expression)* RBRACKET
      -> ^(LIST expression*)
;

section
  : LPAREN operator RPAREN
   -> ^(SECTION operator)
  | LPAREN operator expression RPAREN
   -> ^(SECTION operator expression)
  | LPAREN expression operator RPAREN
   -> ^(SECTION expression operator)
;
fragment operator: OR|AND|LT|LTE|EQ|NEQ|GTE|GT|ADD|MIN|CONCAT|SUBTRACT|DIV|MUL|IDIV|MOD|EXP;

boolean: TRUE | FALSE;

INT: MIN? NUMERIC+;
FLOAT: MIN? NUMERIC+ DOT NUMERIC+;
fragment NUMERIC: ('0'..'9');

CHAR: (SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE);
STRING: (SINGLE_QUOTE ALPHANUMERIC* SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC* DOUBLE_QUOTE);
fragment ALPHANUMERIC: ('a'..'z' | 'A'..'Z' | '0'..'9' | ' ');

ID: ('a'..'z' | 'A' .. 'Z') ('a'..'z' | 'A'..'Z' | '0'..'9' | '_' | '.')* ('?' | '!')?;

WHITESPACE: (' ' | '\t' | '\r' | '\n')+ {
  $channel=HIDDEN;
};

COMMENT: '#' (~('\n' | '\r'))* ('\r'? '\n')
   {$channel=HIDDEN;}
;