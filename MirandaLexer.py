# $ANTLR 3.4 grammars/Miranda.g 2011-12-27 08:51:47

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
BODY=7
CHAR=8
COLON=9
COMMA=10
COMMENT=11
CONCAT=12
DEDENT=13
DEFINITION=14
DIV=15
DOT=16
DOUBLE_QUOTE=17
EQ=18
EXP=19
FALSE=20
FLOAT=21
GT=22
GTE=23
ID=24
IDIV=25
INT=26
IS=27
LBRACKET=28
LIST=29
LPAREN=30
LT=31
LTE=32
MIN=33
MOD=34
MUL=35
NEQ=36
NOT=37
NUMERIC=38
OR=39
OTHERWISE=40
PROGRAM=41
RBRACKET=42
RPAREN=43
SECTION=44
SINGLE_QUOTE=45
STRING=46
SUBTRACT=47
TRUE=48
TUPLE=49
TYPEDEF=50
WHERE=51
WHITESPACE=52


class MirandaLexer(Lexer):

    grammarFileName = "grammars/Miranda.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(MirandaLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa15 = self.DFA15(
            self, 15,
            eot = self.DFA15_eot,
            eof = self.DFA15_eof,
            min = self.DFA15_min,
            max = self.DFA15_max,
            accept = self.DFA15_accept,
            special = self.DFA15_special,
            transition = self.DFA15_transition
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
            self.offside.push(self._state.token)
          else:
            if self.offside.compare(self._state.token):
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



    # $ANTLR start "BODY"
    def mBODY(self, ):
        try:
            _type = BODY
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:48:6: ( '<body>' )
            # grammars/Miranda.g:48:8: '<body>'
            pass 
            self.match("<body>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BODY"



    # $ANTLR start "COLON"
    def mCOLON(self, ):
        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:49:7: ( ':' )
            # grammars/Miranda.g:49:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLON"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:50:7: ( ',' )
            # grammars/Miranda.g:50:9: ','
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

            # grammars/Miranda.g:51:8: ( '++' )
            # grammars/Miranda.g:51:10: '++'
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

            # grammars/Miranda.g:52:8: ( '<dedent>' )
            # grammars/Miranda.g:52:10: '<dedent>'
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

            # grammars/Miranda.g:53:12: ( '<definition>' )
            # grammars/Miranda.g:53:14: '<definition>'
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

            # grammars/Miranda.g:54:5: ( '/' )
            # grammars/Miranda.g:54:7: '/'
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

            # grammars/Miranda.g:55:5: ( '.' )
            # grammars/Miranda.g:55:7: '.'
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

            # grammars/Miranda.g:56:14: ( '\"' )
            # grammars/Miranda.g:56:16: '\"'
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

            # grammars/Miranda.g:57:4: ( '==' )
            # grammars/Miranda.g:57:6: '=='
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

            # grammars/Miranda.g:58:5: ( '^' )
            # grammars/Miranda.g:58:7: '^'
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

            # grammars/Miranda.g:59:7: ( 'false' )
            # grammars/Miranda.g:59:9: 'false'
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

            # grammars/Miranda.g:60:4: ( '>' )
            # grammars/Miranda.g:60:6: '>'
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

            # grammars/Miranda.g:61:5: ( '>=' )
            # grammars/Miranda.g:61:7: '>='
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

            # grammars/Miranda.g:62:6: ( 'div' )
            # grammars/Miranda.g:62:8: 'div'
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

            # grammars/Miranda.g:63:4: ( '=' )
            # grammars/Miranda.g:63:6: '='
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

            # grammars/Miranda.g:64:10: ( '[' )
            # grammars/Miranda.g:64:12: '['
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

            # grammars/Miranda.g:65:6: ( '<list>' )
            # grammars/Miranda.g:65:8: '<list>'
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

            # grammars/Miranda.g:66:8: ( '(' )
            # grammars/Miranda.g:66:10: '('
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

            # grammars/Miranda.g:67:4: ( '<' )
            # grammars/Miranda.g:67:6: '<'
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

            # grammars/Miranda.g:68:5: ( '<=' )
            # grammars/Miranda.g:68:7: '<='
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

            # grammars/Miranda.g:69:5: ( '-' )
            # grammars/Miranda.g:69:7: '-'
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

            # grammars/Miranda.g:70:5: ( 'mod' )
            # grammars/Miranda.g:70:7: 'mod'
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

            # grammars/Miranda.g:71:5: ( '*' )
            # grammars/Miranda.g:71:7: '*'
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

            # grammars/Miranda.g:72:5: ( '!=' )
            # grammars/Miranda.g:72:7: '!='
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

            # grammars/Miranda.g:73:5: ( '!' )
            # grammars/Miranda.g:73:7: '!'
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

            # grammars/Miranda.g:74:4: ( '|' )
            # grammars/Miranda.g:74:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "OTHERWISE"
    def mOTHERWISE(self, ):
        try:
            _type = OTHERWISE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:75:11: ( 'otherwise' )
            # grammars/Miranda.g:75:13: 'otherwise'
            pass 
            self.match("otherwise")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OTHERWISE"



    # $ANTLR start "PROGRAM"
    def mPROGRAM(self, ):
        try:
            _type = PROGRAM
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:76:9: ( 'program' )
            # grammars/Miranda.g:76:11: 'program'
            pass 
            self.match("program")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROGRAM"



    # $ANTLR start "RBRACKET"
    def mRBRACKET(self, ):
        try:
            _type = RBRACKET
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:77:10: ( ']' )
            # grammars/Miranda.g:77:12: ']'
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

            # grammars/Miranda.g:78:8: ( ')' )
            # grammars/Miranda.g:78:10: ')'
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

            # grammars/Miranda.g:79:9: ( '<section>' )
            # grammars/Miranda.g:79:11: '<section>'
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

            # grammars/Miranda.g:80:14: ( '\\'' )
            # grammars/Miranda.g:80:16: '\\''
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

            # grammars/Miranda.g:81:10: ( '--' )
            # grammars/Miranda.g:81:12: '--'
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

            # grammars/Miranda.g:82:6: ( 'true' )
            # grammars/Miranda.g:82:8: 'true'
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

            # grammars/Miranda.g:83:7: ( '<tuple>' )
            # grammars/Miranda.g:83:9: '<tuple>'
            pass 
            self.match("<tuple>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TUPLE"



    # $ANTLR start "TYPEDEF"
    def mTYPEDEF(self, ):
        try:
            _type = TYPEDEF
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:84:9: ( '::=' )
            # grammars/Miranda.g:84:11: '::='
            pass 
            self.match("::=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPEDEF"



    # $ANTLR start "WHERE"
    def mWHERE(self, ):
        try:
            _type = WHERE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:85:7: ( 'where' )
            # grammars/Miranda.g:85:9: 'where'
            pass 
            self.match("where")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHERE"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:202:4: ( ( MIN )? ( NUMERIC )+ )
            # grammars/Miranda.g:202:6: ( MIN )? ( NUMERIC )+
            pass 
            # grammars/Miranda.g:202:6: ( MIN )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 45) :
                alt1 = 1
            if alt1 == 1:
                # grammars/Miranda.g:
                pass 
                if self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # grammars/Miranda.g:202:11: ( NUMERIC )+
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

            # grammars/Miranda.g:203:6: ( ( MIN )? ( NUMERIC )+ DOT ( NUMERIC )+ )
            # grammars/Miranda.g:203:8: ( MIN )? ( NUMERIC )+ DOT ( NUMERIC )+
            pass 
            # grammars/Miranda.g:203:8: ( MIN )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 45) :
                alt3 = 1
            if alt3 == 1:
                # grammars/Miranda.g:
                pass 
                if self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # grammars/Miranda.g:203:13: ( NUMERIC )+
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


            # grammars/Miranda.g:203:26: ( NUMERIC )+
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
            # grammars/Miranda.g:204:17: ( ( '0' .. '9' ) )
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

            # grammars/Miranda.g:206:5: ( ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE ) )
            # grammars/Miranda.g:206:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:206:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
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
                # grammars/Miranda.g:206:8: SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                self.mALPHANUMERIC()


                self.mSINGLE_QUOTE()



            elif alt6 == 2:
                # grammars/Miranda.g:206:49: DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE
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

            # grammars/Miranda.g:207:7: ( ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE ) )
            # grammars/Miranda.g:207:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:207:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
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
                # grammars/Miranda.g:207:10: SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                # grammars/Miranda.g:207:23: ( ALPHANUMERIC )*
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
                # grammars/Miranda.g:207:52: DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE
                pass 
                self.mDOUBLE_QUOTE()


                # grammars/Miranda.g:207:65: ( ALPHANUMERIC )*
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
            # grammars/Miranda.g:208:22: ( ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | ' ' ) )
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

            # grammars/Miranda.g:210:3: ( ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )* ( '?' | '!' )? )
            # grammars/Miranda.g:210:5: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )* ( '?' | '!' )?
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # grammars/Miranda.g:210:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 46 or (48 <= LA10_0 <= 57) or (65 <= LA10_0 <= 90) or LA10_0 == 95 or (97 <= LA10_0 <= 122)) :
                    alt10 = 1


                if alt10 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if self.input.LA(1) == 46 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop10


            # grammars/Miranda.g:210:75: ( '?' | '!' )?
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

            # grammars/Miranda.g:212:11: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # grammars/Miranda.g:212:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # grammars/Miranda.g:212:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
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

            # grammars/Miranda.g:216:8: ( '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' ) )
            # grammars/Miranda.g:216:10: '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' )
            pass 
            self.match(35)

            # grammars/Miranda.g:216:14: (~ ( '\\n' | '\\r' ) )*
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


            # grammars/Miranda.g:216:32: ( ( '\\r' )? '\\n' )
            # grammars/Miranda.g:216:33: ( '\\r' )? '\\n'
            pass 
            # grammars/Miranda.g:216:33: ( '\\r' )?
            alt14 = 2
            LA14_0 = self.input.LA(1)

            if (LA14_0 == 13) :
                alt14 = 1
            if alt14 == 1:
                # grammars/Miranda.g:216:33: '\\r'
                pass 
                self.match(13)




            self.match(10)




            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    def mTokens(self):
        # grammars/Miranda.g:1:8: ( ADD | AND | BODY | COLON | COMMA | CONCAT | DEDENT | DEFINITION | DIV | DOT | DOUBLE_QUOTE | EQ | EXP | FALSE | GT | GTE | IDIV | IS | LBRACKET | LIST | LPAREN | LT | LTE | MIN | MOD | MUL | NEQ | NOT | OR | OTHERWISE | PROGRAM | RBRACKET | RPAREN | SECTION | SINGLE_QUOTE | SUBTRACT | TRUE | TUPLE | TYPEDEF | WHERE | INT | FLOAT | CHAR | STRING | ID | WHITESPACE | COMMENT )
        alt15 = 47
        alt15 = self.dfa15.predict(self.input)
        if alt15 == 1:
            # grammars/Miranda.g:1:10: ADD
            pass 
            self.mADD()



        elif alt15 == 2:
            # grammars/Miranda.g:1:14: AND
            pass 
            self.mAND()



        elif alt15 == 3:
            # grammars/Miranda.g:1:18: BODY
            pass 
            self.mBODY()



        elif alt15 == 4:
            # grammars/Miranda.g:1:23: COLON
            pass 
            self.mCOLON()



        elif alt15 == 5:
            # grammars/Miranda.g:1:29: COMMA
            pass 
            self.mCOMMA()



        elif alt15 == 6:
            # grammars/Miranda.g:1:35: CONCAT
            pass 
            self.mCONCAT()



        elif alt15 == 7:
            # grammars/Miranda.g:1:42: DEDENT
            pass 
            self.mDEDENT()



        elif alt15 == 8:
            # grammars/Miranda.g:1:49: DEFINITION
            pass 
            self.mDEFINITION()



        elif alt15 == 9:
            # grammars/Miranda.g:1:60: DIV
            pass 
            self.mDIV()



        elif alt15 == 10:
            # grammars/Miranda.g:1:64: DOT
            pass 
            self.mDOT()



        elif alt15 == 11:
            # grammars/Miranda.g:1:68: DOUBLE_QUOTE
            pass 
            self.mDOUBLE_QUOTE()



        elif alt15 == 12:
            # grammars/Miranda.g:1:81: EQ
            pass 
            self.mEQ()



        elif alt15 == 13:
            # grammars/Miranda.g:1:84: EXP
            pass 
            self.mEXP()



        elif alt15 == 14:
            # grammars/Miranda.g:1:88: FALSE
            pass 
            self.mFALSE()



        elif alt15 == 15:
            # grammars/Miranda.g:1:94: GT
            pass 
            self.mGT()



        elif alt15 == 16:
            # grammars/Miranda.g:1:97: GTE
            pass 
            self.mGTE()



        elif alt15 == 17:
            # grammars/Miranda.g:1:101: IDIV
            pass 
            self.mIDIV()



        elif alt15 == 18:
            # grammars/Miranda.g:1:106: IS
            pass 
            self.mIS()



        elif alt15 == 19:
            # grammars/Miranda.g:1:109: LBRACKET
            pass 
            self.mLBRACKET()



        elif alt15 == 20:
            # grammars/Miranda.g:1:118: LIST
            pass 
            self.mLIST()



        elif alt15 == 21:
            # grammars/Miranda.g:1:123: LPAREN
            pass 
            self.mLPAREN()



        elif alt15 == 22:
            # grammars/Miranda.g:1:130: LT
            pass 
            self.mLT()



        elif alt15 == 23:
            # grammars/Miranda.g:1:133: LTE
            pass 
            self.mLTE()



        elif alt15 == 24:
            # grammars/Miranda.g:1:137: MIN
            pass 
            self.mMIN()



        elif alt15 == 25:
            # grammars/Miranda.g:1:141: MOD
            pass 
            self.mMOD()



        elif alt15 == 26:
            # grammars/Miranda.g:1:145: MUL
            pass 
            self.mMUL()



        elif alt15 == 27:
            # grammars/Miranda.g:1:149: NEQ
            pass 
            self.mNEQ()



        elif alt15 == 28:
            # grammars/Miranda.g:1:153: NOT
            pass 
            self.mNOT()



        elif alt15 == 29:
            # grammars/Miranda.g:1:157: OR
            pass 
            self.mOR()



        elif alt15 == 30:
            # grammars/Miranda.g:1:160: OTHERWISE
            pass 
            self.mOTHERWISE()



        elif alt15 == 31:
            # grammars/Miranda.g:1:170: PROGRAM
            pass 
            self.mPROGRAM()



        elif alt15 == 32:
            # grammars/Miranda.g:1:178: RBRACKET
            pass 
            self.mRBRACKET()



        elif alt15 == 33:
            # grammars/Miranda.g:1:187: RPAREN
            pass 
            self.mRPAREN()



        elif alt15 == 34:
            # grammars/Miranda.g:1:194: SECTION
            pass 
            self.mSECTION()



        elif alt15 == 35:
            # grammars/Miranda.g:1:202: SINGLE_QUOTE
            pass 
            self.mSINGLE_QUOTE()



        elif alt15 == 36:
            # grammars/Miranda.g:1:215: SUBTRACT
            pass 
            self.mSUBTRACT()



        elif alt15 == 37:
            # grammars/Miranda.g:1:224: TRUE
            pass 
            self.mTRUE()



        elif alt15 == 38:
            # grammars/Miranda.g:1:229: TUPLE
            pass 
            self.mTUPLE()



        elif alt15 == 39:
            # grammars/Miranda.g:1:235: TYPEDEF
            pass 
            self.mTYPEDEF()



        elif alt15 == 40:
            # grammars/Miranda.g:1:243: WHERE
            pass 
            self.mWHERE()



        elif alt15 == 41:
            # grammars/Miranda.g:1:249: INT
            pass 
            self.mINT()



        elif alt15 == 42:
            # grammars/Miranda.g:1:253: FLOAT
            pass 
            self.mFLOAT()



        elif alt15 == 43:
            # grammars/Miranda.g:1:259: CHAR
            pass 
            self.mCHAR()



        elif alt15 == 44:
            # grammars/Miranda.g:1:264: STRING
            pass 
            self.mSTRING()



        elif alt15 == 45:
            # grammars/Miranda.g:1:271: ID
            pass 
            self.mID()



        elif alt15 == 46:
            # grammars/Miranda.g:1:274: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt15 == 47:
            # grammars/Miranda.g:1:285: COMMENT
            pass 
            self.mCOMMENT()








    # lookup tables for DFA #15

    DFA15_eot = DFA.unpack(
        u"\1\uffff\1\41\1\uffff\1\50\1\52\3\uffff\1\53\1\57\1\uffff\1\35"
        u"\1\62\1\35\2\uffff\1\65\1\35\1\uffff\1\70\1\uffff\2\35\2\uffff"
        u"\1\73\2\35\1\77\23\uffff\1\35\2\uffff\1\35\2\uffff\1\35\2\uffff"
        u"\2\35\2\uffff\2\35\4\uffff\1\35\1\117\1\120\2\35\1\uffff\2\35\3"
        u"\uffff\1\35\2\uffff\2\35\1\130\1\35\1\132\2\35\1\uffff\1\135\1"
        u"\uffff\2\35\1\uffff\1\35\1\141\1\35\1\uffff\1\143\1\uffff"
        )

    DFA15_eof = DFA.unpack(
        u"\144\uffff"
        )

    DFA15_min = DFA.unpack(
        u"\1\11\1\53\1\uffff\1\75\1\72\3\uffff\1\40\1\75\1\uffff\1\141\1"
        u"\75\1\151\2\uffff\1\55\1\157\1\uffff\1\75\1\uffff\1\164\1\162\2"
        u"\uffff\1\40\1\162\1\150\1\56\6\uffff\1\145\10\uffff\1\40\3\uffff"
        u"\1\154\2\uffff\1\166\2\uffff\1\144\2\uffff\1\150\1\157\1\uffff"
        u"\1\40\1\165\1\145\2\uffff\1\144\1\uffff\1\163\2\41\1\145\1\147"
        u"\1\uffff\1\145\1\162\3\uffff\1\145\2\uffff\2\162\1\41\1\145\1\41"
        u"\1\167\1\141\1\uffff\1\41\1\uffff\1\151\1\155\1\uffff\1\163\1\41"
        u"\1\145\1\uffff\1\41\1\uffff"
        )

    DFA15_max = DFA.unpack(
        u"\1\174\1\53\1\uffff\1\164\1\72\3\uffff\1\172\1\75\1\uffff\1\141"
        u"\1\75\1\151\2\uffff\1\71\1\157\1\uffff\1\75\1\uffff\1\164\1\162"
        u"\2\uffff\1\172\1\162\1\150\1\71\6\uffff\1\145\10\uffff\1\172\3"
        u"\uffff\1\154\2\uffff\1\166\2\uffff\1\144\2\uffff\1\150\1\157\1"
        u"\uffff\1\172\1\165\1\145\2\uffff\1\146\1\uffff\1\163\2\172\1\145"
        u"\1\147\1\uffff\1\145\1\162\3\uffff\1\145\2\uffff\2\162\1\172\1"
        u"\145\1\172\1\167\1\141\1\uffff\1\172\1\uffff\1\151\1\155\1\uffff"
        u"\1\163\1\172\1\145\1\uffff\1\172\1\uffff"
        )

    DFA15_accept = DFA.unpack(
        u"\2\uffff\1\2\2\uffff\1\5\1\11\1\12\2\uffff\1\15\3\uffff\1\23\1"
        u"\25\2\uffff\1\32\1\uffff\1\35\2\uffff\1\40\1\41\4\uffff\1\55\1"
        u"\56\1\57\1\6\1\1\1\3\1\uffff\1\24\1\27\1\42\1\46\1\26\1\47\1\4"
        u"\1\13\1\uffff\1\54\1\14\1\22\1\uffff\1\20\1\17\1\uffff\1\44\1\30"
        u"\1\uffff\1\33\1\34\2\uffff\1\43\3\uffff\1\51\1\52\1\uffff\1\53"
        u"\5\uffff\1\53\2\uffff\1\7\1\10\1\53\1\uffff\1\21\1\31\7\uffff\1"
        u"\45\1\uffff\1\16\2\uffff\1\50\3\uffff\1\37\1\uffff\1\36"
        )

    DFA15_special = DFA.unpack(
        u"\144\uffff"
        )


    DFA15_transition = [
        DFA.unpack(u"\2\36\2\uffff\1\36\22\uffff\1\36\1\23\1\10\1\37\2\uffff"
        u"\1\2\1\31\1\17\1\30\1\22\1\1\1\5\1\20\1\7\1\6\12\34\1\4\1\uffff"
        u"\1\3\1\11\1\14\2\uffff\32\35\1\16\1\uffff\1\27\1\12\2\uffff\3\35"
        u"\1\15\1\35\1\13\6\35\1\21\1\35\1\25\1\26\3\35\1\32\2\35\1\33\3"
        u"\35\1\uffff\1\24"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\45\44\uffff\1\42\1\uffff\1\43\7\uffff\1\44\6\uffff"
        u"\1\46\1\47"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54\1\uffff\1\55\15\uffff\12\54\7\uffff\32\54\6\uffff"
        u"\32\54"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\64\2\uffff\12\34"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\74\6\uffff\1\55\10\uffff\12\74\7\uffff\32\74\6\uffff"
        u"\32\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\100\1\uffff\12\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55\1\uffff\1\102\15\uffff\12\55\7\uffff\32\55\6"
        u"\uffff\32\55"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55\6\uffff\1\110\10\uffff\12\55\7\uffff\32\55\6"
        u"\uffff\32\55"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\113\1\uffff\1\114"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\35\14\uffff\1\35\1\uffff\12\35\5\uffff\1\35\1\uffff"
        u"\32\35\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u"\1\35\14\uffff\1\35\1\uffff\12\35\5\uffff\1\35\1\uffff"
        u"\32\35\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\35\14\uffff\1\35\1\uffff\12\35\5\uffff\1\35\1\uffff"
        u"\32\35\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\35\14\uffff\1\35\1\uffff\12\35\5\uffff\1\35\1\uffff"
        u"\32\35\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\35\14\uffff\1\35\1\uffff\12\35\5\uffff\1\35\1\uffff"
        u"\32\35\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\35\14\uffff\1\35\1\uffff\12\35\5\uffff\1\35\1\uffff"
        u"\32\35\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\35\14\uffff\1\35\1\uffff\12\35\5\uffff\1\35\1\uffff"
        u"\32\35\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #15

    class DFA15(DFA):
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
