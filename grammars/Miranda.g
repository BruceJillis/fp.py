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
   COMMA  = ',';
   SINGLE_QUOTE = '\'';
   DOUBLE_QUOTE = '"';
    
   // imaginary
   DEDENT     = '<dedent>';
   DEFINITION = '<definition>';
   TUPLE      = '<tuple>';
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

program: (definition DEDENT!)* expression EOF!;

definition: 
  ID IS expression
  -> ^(DEFINITION ID expression)
;

expression: expr1;

expr1: expr2 (OR^ expression)*;

expr2: expr3 (AND^ expression)*;

expr3: expr4 (relop^ expression)*;

expr4: expr5 ((ADD^|MIN^) expr5)*;

expr5: expr6 ((DIV^|MUL^) expr6)*;

expr6: aexpr+;

aexpr
   : ID
   | INT
	 | FLOAT
   | CHAR
   | STRING
   | LPAREN! expression RPAREN!
   | LPAREN expression (COMMA expression)* RPAREN
     -> ^(TUPLE expression*)
;

relop: LT | LTE | EQ | NEQ | GTE | GT;

INT: ('0'..'9')+;
FLOAT: INT DOT INT;

CHAR: (SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE);
STRING: (SINGLE_QUOTE ALPHANUMERIC* SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC* DOUBLE_QUOTE);
fragment ALPHANUMERIC: ('a'..'z' | 'A'..'Z' | '0'..'9' | ' ');

ID: ('a'..'z' | 'A' .. 'Z') ('a'..'z' | 'A'..'Z' | '0'..'9')* ('?' | '!')?;

WHITESPACE: (' ' | '\t' | '\r' | '\n')+ {
  $channel=HIDDEN;
};

COMMENT: '#' (~('\n' | '\r'))* ('\r'? '\n' | EOF)
   {$channel=HIDDEN;}
;