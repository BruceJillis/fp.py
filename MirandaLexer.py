# $ANTLR 3.4 grammars/Miranda.g 2011-12-25 17:16:35

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ADD=4
ALPHANUMERIC=5
AND=6
CHAR=7
COMMA=8
COMMENT=9
CONCAT=10
DEDENT=11
DEFINITION=12
DIV=13
DOT=14
DOUBLE_QUOTE=15
EQ=16
EXP=17
FALSE=18
FLOAT=19
GT=20
GTE=21
ID=22
IDIV=23
INT=24
IS=25
LBRACKET=26
LIST=27
LPAREN=28
LT=29
LTE=30
MIN=31
MOD=32
MUL=33
NEQ=34
NOT=35
NUMERIC=36
OR=37
RBRACKET=38
RPAREN=39
SECTION=40
SINGLE_QUOTE=41
STRING=42
SUBTRACT=43
TRUE=44
TUPLE=45
WHITESPACE=46


class MirandaLexer(Lexer):

    grammarFileName = "grammars/Miranda.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(MirandaLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )




                             
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



    # $ANTLR start "ADD"
    def mADD(self, ):
        try:
            _type = ADD
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:46:5: ( '+' )
            # grammars/Miranda.g:46:7: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ADD"



    # $ANTLR start "AND"
    def mAND(self, ):
        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:47:5: ( '&' )
            # grammars/Miranda.g:47:7: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:48:7: ( ',' )
            # grammars/Miranda.g:48:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "CONCAT"
    def mCONCAT(self, ):
        try:
            _type = CONCAT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:49:8: ( '++' )
            # grammars/Miranda.g:49:10: '++'
            pass 
            self.match("++")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONCAT"



    # $ANTLR start "DEDENT"
    def mDEDENT(self, ):
        try:
            _type = DEDENT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:50:8: ( '<dedent>' )
            # grammars/Miranda.g:50:10: '<dedent>'
            pass 
            self.match("<dedent>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEDENT"



    # $ANTLR start "DEFINITION"
    def mDEFINITION(self, ):
        try:
            _type = DEFINITION
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:51:12: ( '<definition>' )
            # grammars/Miranda.g:51:14: '<definition>'
            pass 
            self.match("<definition>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEFINITION"



    # $ANTLR start "DIV"
    def mDIV(self, ):
        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:52:5: ( '/' )
            # grammars/Miranda.g:52:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIV"



    # $ANTLR start "DOT"
    def mDOT(self, ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:53:5: ( '.' )
            # grammars/Miranda.g:53:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "DOUBLE_QUOTE"
    def mDOUBLE_QUOTE(self, ):
        try:
            _type = DOUBLE_QUOTE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:54:14: ( '\"' )
            # grammars/Miranda.g:54:16: '\"'
            pass 
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOUBLE_QUOTE"



    # $ANTLR start "EQ"
    def mEQ(self, ):
        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:55:4: ( '==' )
            # grammars/Miranda.g:55:6: '=='
            pass 
            self.match("==")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQ"



    # $ANTLR start "EXP"
    def mEXP(self, ):
        try:
            _type = EXP
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:56:5: ( '^' )
            # grammars/Miranda.g:56:7: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EXP"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):
        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:57:7: ( 'false' )
            # grammars/Miranda.g:57:9: 'false'
            pass 
            self.match("false")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "GT"
    def mGT(self, ):
        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:58:4: ( '>' )
            # grammars/Miranda.g:58:6: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GT"



    # $ANTLR start "GTE"
    def mGTE(self, ):
        try:
            _type = GTE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:59:5: ( '>=' )
            # grammars/Miranda.g:59:7: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GTE"



    # $ANTLR start "IDIV"
    def mIDIV(self, ):
        try:
            _type = IDIV
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:60:6: ( 'div' )
            # grammars/Miranda.g:60:8: 'div'
            pass 
            self.match("div")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDIV"



    # $ANTLR start "IS"
    def mIS(self, ):
        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:61:4: ( '=' )
            # grammars/Miranda.g:61:6: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IS"



    # $ANTLR start "LBRACKET"
    def mLBRACKET(self, ):
        try:
            _type = LBRACKET
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:62:10: ( '[' )
            # grammars/Miranda.g:62:12: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LBRACKET"



    # $ANTLR start "LIST"
    def mLIST(self, ):
        try:
            _type = LIST
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:63:6: ( '<list>' )
            # grammars/Miranda.g:63:8: '<list>'
            pass 
            self.match("<list>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LIST"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:64:8: ( '(' )
            # grammars/Miranda.g:64:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "LT"
    def mLT(self, ):
        try:
            _type = LT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:65:4: ( '<' )
            # grammars/Miranda.g:65:6: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LT"



    # $ANTLR start "LTE"
    def mLTE(self, ):
        try:
            _type = LTE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:66:5: ( '<=' )
            # grammars/Miranda.g:66:7: '<='
            pass 
            self.match("<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LTE"



    # $ANTLR start "MIN"
    def mMIN(self, ):
        try:
            _type = MIN
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:67:5: ( '-' )
            # grammars/Miranda.g:67:7: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MIN"



    # $ANTLR start "MOD"
    def mMOD(self, ):
        try:
            _type = MOD
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:68:5: ( 'mod' )
            # grammars/Miranda.g:68:7: 'mod'
            pass 
            self.match("mod")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOD"



    # $ANTLR start "MUL"
    def mMUL(self, ):
        try:
            _type = MUL
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:69:5: ( '*' )
            # grammars/Miranda.g:69:7: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MUL"



    # $ANTLR start "NEQ"
    def mNEQ(self, ):
        try:
            _type = NEQ
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:70:5: ( '!=' )
            # grammars/Miranda.g:70:7: '!='
            pass 
            self.match("!=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEQ"



    # $ANTLR start "NOT"
    def mNOT(self, ):
        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:71:5: ( '!' )
            # grammars/Miranda.g:71:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:72:4: ( '|' )
            # grammars/Miranda.g:72:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "RBRACKET"
    def mRBRACKET(self, ):
        try:
            _type = RBRACKET
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:73:10: ( ']' )
            # grammars/Miranda.g:73:12: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RBRACKET"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:74:8: ( ')' )
            # grammars/Miranda.g:74:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "SECTION"
    def mSECTION(self, ):
        try:
            _type = SECTION
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:75:9: ( '<section>' )
            # grammars/Miranda.g:75:11: '<section>'
            pass 
            self.match("<section>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SECTION"



    # $ANTLR start "SINGLE_QUOTE"
    def mSINGLE_QUOTE(self, ):
        try:
            _type = SINGLE_QUOTE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:76:14: ( '\\'' )
            # grammars/Miranda.g:76:16: '\\''
            pass 
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SINGLE_QUOTE"



    # $ANTLR start "SUBTRACT"
    def mSUBTRACT(self, ):
        try:
            _type = SUBTRACT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:77:10: ( '--' )
            # grammars/Miranda.g:77:12: '--'
            pass 
            self.match("--")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SUBTRACT"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):
        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:78:6: ( 'true' )
            # grammars/Miranda.g:78:8: 'true'
            pass 
            self.match("true")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "TUPLE"
    def mTUPLE(self, ):
        try:
            _type = TUPLE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:79:7: ( '<tuple>' )
            # grammars/Miranda.g:79:9: '<tuple>'
            pass 
            self.match("<tuple>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TUPLE"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:149:4: ( ( MIN | ADD )? ( NUMERIC )+ )
            # grammars/Miranda.g:149:6: ( MIN | ADD )? ( NUMERIC )+
            pass 
            # grammars/Miranda.g:149:6: ( MIN | ADD )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 43 or LA1_0 == 45) :
                alt1 = 1
            if alt1 == 1:
                # grammars/Miranda.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # grammars/Miranda.g:149:19: ( NUMERIC )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:150:6: ( ( MIN | ADD )? ( NUMERIC )+ DOT ( NUMERIC )+ )
            # grammars/Miranda.g:150:8: ( MIN | ADD )? ( NUMERIC )+ DOT ( NUMERIC )+
            pass 
            # grammars/Miranda.g:150:8: ( MIN | ADD )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 43 or LA3_0 == 45) :
                alt3 = 1
            if alt3 == 1:
                # grammars/Miranda.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # grammars/Miranda.g:150:21: ( NUMERIC )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1


            self.mDOT()


            # grammars/Miranda.g:150:34: ( NUMERIC )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57)) :
                    alt5 = 1


                if alt5 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "NUMERIC"
    def mNUMERIC(self, ):
        try:
            # grammars/Miranda.g:151:17: ( ( '0' .. '9' ) )
            # grammars/Miranda.g:
            pass 
            if (48 <= self.input.LA(1) <= 57):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "NUMERIC"



    # $ANTLR start "CHAR"
    def mCHAR(self, ):
        try:
            _type = CHAR
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:153:5: ( ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE ) )
            # grammars/Miranda.g:153:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:153:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 39) :
                alt6 = 1
            elif (LA6_0 == 34) :
                alt6 = 2
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae


            if alt6 == 1:
                # grammars/Miranda.g:153:8: SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                self.mALPHANUMERIC()


                self.mSINGLE_QUOTE()



            elif alt6 == 2:
                # grammars/Miranda.g:153:49: DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE
                pass 
                self.mDOUBLE_QUOTE()


                self.mALPHANUMERIC()


                self.mDOUBLE_QUOTE()







            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHAR"



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:154:7: ( ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE ) )
            # grammars/Miranda.g:154:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:154:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 39) :
                alt9 = 1
            elif (LA9_0 == 34) :
                alt9 = 2
            else:
                nvae = NoViableAltException("", 9, 0, self.input)

                raise nvae


            if alt9 == 1:
                # grammars/Miranda.g:154:10: SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                # grammars/Miranda.g:154:23: ( ALPHANUMERIC )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 32 or (48 <= LA7_0 <= 57) or (65 <= LA7_0 <= 90) or (97 <= LA7_0 <= 122)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammars/Miranda.g:
                        pass 
                        if self.input.LA(1) == 32 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop7


                self.mSINGLE_QUOTE()



            elif alt9 == 2:
                # grammars/Miranda.g:154:52: DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE
                pass 
                self.mDOUBLE_QUOTE()


                # grammars/Miranda.g:154:65: ( ALPHANUMERIC )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 32 or (48 <= LA8_0 <= 57) or (65 <= LA8_0 <= 90) or (97 <= LA8_0 <= 122)) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammars/Miranda.g:
                        pass 
                        if self.input.LA(1) == 32 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop8


                self.mDOUBLE_QUOTE()







            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "ALPHANUMERIC"
    def mALPHANUMERIC(self, ):
        try:
            # grammars/Miranda.g:155:22: ( ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | ' ' ) )
            # grammars/Miranda.g:
            pass 
            if self.input.LA(1) == 32 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "ALPHANUMERIC"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:157:3: ( ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '-' )* ( '?' | '!' )? )
            # grammars/Miranda.g:157:5: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '-' )* ( '?' | '!' )?
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # grammars/Miranda.g:157:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '-' )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((45 <= LA10_0 <= 46) or (48 <= LA10_0 <= 57) or (65 <= LA10_0 <= 90) or LA10_0 == 95 or (97 <= LA10_0 <= 122)) :
                    alt10 = 1


                if alt10 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (45 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop10


            # grammars/Miranda.g:157:81: ( '?' | '!' )?
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 33 or LA11_0 == 63) :
                alt11 = 1
            if alt11 == 1:
                # grammars/Miranda.g:
                pass 
                if self.input.LA(1) == 33 or self.input.LA(1) == 63:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse








            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):
        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:159:11: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # grammars/Miranda.g:159:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # grammars/Miranda.g:159:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((9 <= LA12_0 <= 10) or LA12_0 == 13 or LA12_0 == 32) :
                    alt12 = 1


                if alt12 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1


            #action start
                                                    
            _channel=HIDDEN;

            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:163:8: ( '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF ) )
            # grammars/Miranda.g:163:10: '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF )
            pass 
            self.match(35)

            # grammars/Miranda.g:163:14: (~ ( '\\n' | '\\r' ) )*
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if ((0 <= LA13_0 <= 9) or (11 <= LA13_0 <= 12) or (14 <= LA13_0 <= 65535)) :
                    alt13 = 1


                if alt13 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop13


            # grammars/Miranda.g:163:32: ( ( '\\r' )? '\\n' | EOF )
            alt15 = 2
            LA15_0 = self.input.LA(1)

            if (LA15_0 == 10 or LA15_0 == 13) :
                alt15 = 1
            else:
                alt15 = 2

            if alt15 == 1:
                # grammars/Miranda.g:163:33: ( '\\r' )? '\\n'
                pass 
                # grammars/Miranda.g:163:33: ( '\\r' )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 13) :
                    alt14 = 1
                if alt14 == 1:
                    # grammars/Miranda.g:163:33: '\\r'
                    pass 
                    self.match(13)




                self.match(10)


            elif alt15 == 2:
                # grammars/Miranda.g:163:46: EOF
                pass 
                self.match(EOF)





            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    def mTokens(self):
        # grammars/Miranda.g:1:8: ( ADD | AND | COMMA | CONCAT | DEDENT | DEFINITION | DIV | DOT | DOUBLE_QUOTE | EQ | EXP | FALSE | GT | GTE | IDIV | IS | LBRACKET | LIST | LPAREN | LT | LTE | MIN | MOD | MUL | NEQ | NOT | OR | RBRACKET | RPAREN | SECTION | SINGLE_QUOTE | SUBTRACT | TRUE | TUPLE | INT | FLOAT | CHAR | STRING | ID | WHITESPACE | COMMENT )
        alt16 = 41
        alt16 = self.dfa16.predict(self.input)
        if alt16 == 1:
            # grammars/Miranda.g:1:10: ADD
            pass 
            self.mADD()



        elif alt16 == 2:
            # grammars/Miranda.g:1:14: AND
            pass 
            self.mAND()



        elif alt16 == 3:
            # grammars/Miranda.g:1:18: COMMA
            pass 
            self.mCOMMA()



        elif alt16 == 4:
            # grammars/Miranda.g:1:24: CONCAT
            pass 
            self.mCONCAT()



        elif alt16 == 5:
            # grammars/Miranda.g:1:31: DEDENT
            pass 
            self.mDEDENT()



        elif alt16 == 6:
            # grammars/Miranda.g:1:38: DEFINITION
            pass 
            self.mDEFINITION()



        elif alt16 == 7:
            # grammars/Miranda.g:1:49: DIV
            pass 
            self.mDIV()



        elif alt16 == 8:
            # grammars/Miranda.g:1:53: DOT
            pass 
            self.mDOT()



        elif alt16 == 9:
            # grammars/Miranda.g:1:57: DOUBLE_QUOTE
            pass 
            self.mDOUBLE_QUOTE()



        elif alt16 == 10:
            # grammars/Miranda.g:1:70: EQ
            pass 
            self.mEQ()



        elif alt16 == 11:
            # grammars/Miranda.g:1:73: EXP
            pass 
            self.mEXP()



        elif alt16 == 12:
            # grammars/Miranda.g:1:77: FALSE
            pass 
            self.mFALSE()



        elif alt16 == 13:
            # grammars/Miranda.g:1:83: GT
            pass 
            self.mGT()



        elif alt16 == 14:
            # grammars/Miranda.g:1:86: GTE
            pass 
            self.mGTE()



        elif alt16 == 15:
            # grammars/Miranda.g:1:90: IDIV
            pass 
            self.mIDIV()



        elif alt16 == 16:
            # grammars/Miranda.g:1:95: IS
            pass 
            self.mIS()



        elif alt16 == 17:
            # grammars/Miranda.g:1:98: LBRACKET
            pass 
            self.mLBRACKET()



        elif alt16 == 18:
            # grammars/Miranda.g:1:107: LIST
            pass 
            self.mLIST()



        elif alt16 == 19:
            # grammars/Miranda.g:1:112: LPAREN
            pass 
            self.mLPAREN()



        elif alt16 == 20:
            # grammars/Miranda.g:1:119: LT
            pass 
            self.mLT()



        elif alt16 == 21:
            # grammars/Miranda.g:1:122: LTE
            pass 
            self.mLTE()



        elif alt16 == 22:
            # grammars/Miranda.g:1:126: MIN
            pass 
            self.mMIN()



        elif alt16 == 23:
            # grammars/Miranda.g:1:130: MOD
            pass 
            self.mMOD()



        elif alt16 == 24:
            # grammars/Miranda.g:1:134: MUL
            pass 
            self.mMUL()



        elif alt16 == 25:
            # grammars/Miranda.g:1:138: NEQ
            pass 
            self.mNEQ()



        elif alt16 == 26:
            # grammars/Miranda.g:1:142: NOT
            pass 
            self.mNOT()



        elif alt16 == 27:
            # grammars/Miranda.g:1:146: OR
            pass 
            self.mOR()



        elif alt16 == 28:
            # grammars/Miranda.g:1:149: RBRACKET
            pass 
            self.mRBRACKET()



        elif alt16 == 29:
            # grammars/Miranda.g:1:158: RPAREN
            pass 
            self.mRPAREN()



        elif alt16 == 30:
            # grammars/Miranda.g:1:165: SECTION
            pass 
            self.mSECTION()



        elif alt16 == 31:
            # grammars/Miranda.g:1:173: SINGLE_QUOTE
            pass 
            self.mSINGLE_QUOTE()



        elif alt16 == 32:
            # grammars/Miranda.g:1:186: SUBTRACT
            pass 
            self.mSUBTRACT()



        elif alt16 == 33:
            # grammars/Miranda.g:1:195: TRUE
            pass 
            self.mTRUE()



        elif alt16 == 34:
            # grammars/Miranda.g:1:200: TUPLE
            pass 
            self.mTUPLE()



        elif alt16 == 35:
            # grammars/Miranda.g:1:206: INT
            pass 
            self.mINT()



        elif alt16 == 36:
            # grammars/Miranda.g:1:210: FLOAT
            pass 
            self.mFLOAT()



        elif alt16 == 37:
            # grammars/Miranda.g:1:216: CHAR
            pass 
            self.mCHAR()



        elif alt16 == 38:
            # grammars/Miranda.g:1:221: STRING
            pass 
            self.mSTRING()



        elif alt16 == 39:
            # grammars/Miranda.g:1:228: ID
            pass 
            self.mID()



        elif alt16 == 40:
            # grammars/Miranda.g:1:231: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt16 == 41:
            # grammars/Miranda.g:1:242: COMMENT
            pass 
            self.mCOMMENT()








    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\1\uffff\1\35\2\uffff\1\43\2\uffff\1\44\1\50\1\uffff\1\31\1\53"
        u"\1\31\2\uffff\1\56\1\31\1\uffff\1\61\3\uffff\1\62\1\31\1\65\20"
        u"\uffff\1\31\2\uffff\1\31\2\uffff\1\31\4\uffff\1\31\4\uffff\1\31"
        u"\1\102\1\103\1\uffff\1\31\3\uffff\1\31\2\uffff\1\106\1\107\2\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\110\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\1\11\1\53\2\uffff\1\75\2\uffff\1\40\1\75\1\uffff\1\141\1\75\1"
        u"\151\2\uffff\1\55\1\157\1\uffff\1\75\3\uffff\1\40\1\162\1\56\5"
        u"\uffff\1\145\6\uffff\1\40\3\uffff\1\154\2\uffff\1\166\2\uffff\1"
        u"\144\3\uffff\1\40\1\165\2\uffff\1\144\1\uffff\1\163\2\41\1\uffff"
        u"\1\145\3\uffff\1\145\2\uffff\2\41\2\uffff"
        )

    DFA16_max = DFA.unpack(
        u"\1\174\1\71\2\uffff\1\164\2\uffff\1\172\1\75\1\uffff\1\141\1\75"
        u"\1\151\2\uffff\1\71\1\157\1\uffff\1\75\3\uffff\1\172\1\162\1\71"
        u"\5\uffff\1\145\6\uffff\1\172\3\uffff\1\154\2\uffff\1\166\2\uffff"
        u"\1\144\3\uffff\1\172\1\165\2\uffff\1\146\1\uffff\1\163\2\172\1"
        u"\uffff\1\145\3\uffff\1\145\2\uffff\2\172\2\uffff"
        )

    DFA16_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\uffff\1\7\1\10\2\uffff\1\13\3\uffff\1\21\1\23"
        u"\2\uffff\1\30\1\uffff\1\33\1\34\1\35\3\uffff\1\47\1\50\1\51\1\4"
        u"\1\1\1\uffff\1\22\1\25\1\36\1\42\1\24\1\11\1\uffff\1\46\1\12\1"
        u"\20\1\uffff\1\16\1\15\1\uffff\1\40\1\26\1\uffff\1\31\1\32\1\37"
        u"\2\uffff\1\43\1\44\1\uffff\1\45\3\uffff\1\45\1\uffff\1\5\1\6\1"
        u"\45\1\uffff\1\17\1\27\2\uffff\1\41\1\14"
        )

    DFA16_special = DFA.unpack(
        u"\110\uffff"
        )


    DFA16_transition = [
        DFA.unpack(u"\2\32\2\uffff\1\32\22\uffff\1\32\1\22\1\7\1\33\2\uffff"
        u"\1\2\1\26\1\16\1\25\1\21\1\1\1\3\1\17\1\6\1\5\12\30\2\uffff\1\4"
        u"\1\10\1\13\2\uffff\32\31\1\15\1\uffff\1\24\1\11\2\uffff\3\31\1"
        u"\14\1\31\1\12\6\31\1\20\6\31\1\27\6\31\1\uffff\1\23"),
        DFA.unpack(u"\1\34\4\uffff\12\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\40\46\uffff\1\36\7\uffff\1\37\6\uffff\1\41\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\45\1\uffff\1\46\15\uffff\12\45\7\uffff\32\45\6\uffff"
        u"\32\45"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55\2\uffff\12\30"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\63\6\uffff\1\46\10\uffff\12\63\7\uffff\32\63\6\uffff"
        u"\32\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\66\1\uffff\12\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\46\1\uffff\1\70\15\uffff\12\46\7\uffff\32\46\6\uffff"
        u"\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\46\6\uffff\1\74\10\uffff\12\46\7\uffff\32\46\6\uffff"
        u"\32\46"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\76\1\uffff\1\77"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\31\13\uffff\2\31\1\uffff\12\31\5\uffff\1\31\1\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\31\13\uffff\2\31\1\uffff\12\31\5\uffff\1\31\1\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\13\uffff\2\31\1\uffff\12\31\5\uffff\1\31\1\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\31\13\uffff\2\31\1\uffff\12\31\5\uffff\1\31\1\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #16

    class DFA16(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(MirandaLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
