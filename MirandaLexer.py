# $ANTLR 3.4 grammars/Miranda.g 2011-12-28 15:47:07

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
CHAR_TYPE=9
COLON=10
COMMA=11
COMMENT=12
CONCAT=13
DEDENT=14
DEFINITION=15
DIV=16
DOT=17
DOUBLE_QUOTE=18
EQ=19
EXP=20
FALSE=21
FLOAT=22
GENERIC=23
GT=24
GTE=25
ID=26
IDIV=27
INT=28
IS=29
LBRACKET=30
LIST=31
LPAREN=32
LT=33
LTE=34
MIN=35
MOD=36
NEQ=37
NOT=38
NUMERIC=39
NUM_TYPE=40
OR=41
OTHERWISE=42
PART=43
PROGRAM=44
RBRACKET=45
RPAREN=46
SECTION=47
SINGLE_QUOTE=48
STARS=49
STRING=50
SUBTRACT=51
TRUE=52
TUPLE=53
TYPE=54
TYPE_IS=55
WHERE=56
WHITESPACE=57


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
          
          # if we are defining a function or type constructor
          if self._state.token.type in [IS, TYPE_IS]:
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

            # grammars/Miranda.g:47:5: ( '+' )
            # grammars/Miranda.g:47:7: '+'
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

            # grammars/Miranda.g:48:5: ( '&' )
            # grammars/Miranda.g:48:7: '&'
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

            # grammars/Miranda.g:49:6: ( '<body>' )
            # grammars/Miranda.g:49:8: '<body>'
            pass 
            self.match("<body>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BODY"



    # $ANTLR start "CHAR_TYPE"
    def mCHAR_TYPE(self, ):
        try:
            _type = CHAR_TYPE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:50:11: ( 'char' )
            # grammars/Miranda.g:50:13: 'char'
            pass 
            self.match("char")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHAR_TYPE"



    # $ANTLR start "COLON"
    def mCOLON(self, ):
        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:51:7: ( ':' )
            # grammars/Miranda.g:51:9: ':'
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

            # grammars/Miranda.g:52:7: ( ',' )
            # grammars/Miranda.g:52:9: ','
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

            # grammars/Miranda.g:53:8: ( '++' )
            # grammars/Miranda.g:53:10: '++'
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

            # grammars/Miranda.g:54:8: ( '<dedent>' )
            # grammars/Miranda.g:54:10: '<dedent>'
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

            # grammars/Miranda.g:55:12: ( '<definition>' )
            # grammars/Miranda.g:55:14: '<definition>'
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

            # grammars/Miranda.g:56:5: ( '/' )
            # grammars/Miranda.g:56:7: '/'
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

            # grammars/Miranda.g:57:5: ( '.' )
            # grammars/Miranda.g:57:7: '.'
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

            # grammars/Miranda.g:58:14: ( '\"' )
            # grammars/Miranda.g:58:16: '\"'
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

            # grammars/Miranda.g:59:4: ( '==' )
            # grammars/Miranda.g:59:6: '=='
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

            # grammars/Miranda.g:60:5: ( '^' )
            # grammars/Miranda.g:60:7: '^'
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

            # grammars/Miranda.g:61:7: ( 'false' )
            # grammars/Miranda.g:61:9: 'false'
            pass 
            self.match("false")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "GENERIC"
    def mGENERIC(self, ):
        try:
            _type = GENERIC
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:62:9: ( '<generic>' )
            # grammars/Miranda.g:62:11: '<generic>'
            pass 
            self.match("<generic>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GENERIC"



    # $ANTLR start "GT"
    def mGT(self, ):
        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:63:4: ( '>' )
            # grammars/Miranda.g:63:6: '>'
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

            # grammars/Miranda.g:64:5: ( '>=' )
            # grammars/Miranda.g:64:7: '>='
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

            # grammars/Miranda.g:65:6: ( 'div' )
            # grammars/Miranda.g:65:8: 'div'
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

            # grammars/Miranda.g:66:4: ( '=' )
            # grammars/Miranda.g:66:6: '='
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

            # grammars/Miranda.g:67:10: ( '[' )
            # grammars/Miranda.g:67:12: '['
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

            # grammars/Miranda.g:68:6: ( '<list>' )
            # grammars/Miranda.g:68:8: '<list>'
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

            # grammars/Miranda.g:69:8: ( '(' )
            # grammars/Miranda.g:69:10: '('
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

            # grammars/Miranda.g:70:4: ( '<' )
            # grammars/Miranda.g:70:6: '<'
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

            # grammars/Miranda.g:71:5: ( '<=' )
            # grammars/Miranda.g:71:7: '<='
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

            # grammars/Miranda.g:72:5: ( '-' )
            # grammars/Miranda.g:72:7: '-'
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

            # grammars/Miranda.g:73:5: ( 'mod' )
            # grammars/Miranda.g:73:7: 'mod'
            pass 
            self.match("mod")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOD"



    # $ANTLR start "NEQ"
    def mNEQ(self, ):
        try:
            _type = NEQ
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:74:5: ( '!=' )
            # grammars/Miranda.g:74:7: '!='
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

            # grammars/Miranda.g:75:5: ( '!' )
            # grammars/Miranda.g:75:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"



    # $ANTLR start "NUM_TYPE"
    def mNUM_TYPE(self, ):
        try:
            _type = NUM_TYPE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:76:10: ( 'num' )
            # grammars/Miranda.g:76:12: 'num'
            pass 
            self.match("num")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NUM_TYPE"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:77:4: ( '|' )
            # grammars/Miranda.g:77:6: '|'
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

            # grammars/Miranda.g:78:11: ( 'otherwise' )
            # grammars/Miranda.g:78:13: 'otherwise'
            pass 
            self.match("otherwise")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OTHERWISE"



    # $ANTLR start "PART"
    def mPART(self, ):
        try:
            _type = PART
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:79:6: ( '<part>' )
            # grammars/Miranda.g:79:8: '<part>'
            pass 
            self.match("<part>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PART"



    # $ANTLR start "PROGRAM"
    def mPROGRAM(self, ):
        try:
            _type = PROGRAM
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:80:9: ( 'program' )
            # grammars/Miranda.g:80:11: 'program'
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

            # grammars/Miranda.g:81:10: ( ']' )
            # grammars/Miranda.g:81:12: ']'
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

            # grammars/Miranda.g:82:8: ( ')' )
            # grammars/Miranda.g:82:10: ')'
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

            # grammars/Miranda.g:83:9: ( '<section>' )
            # grammars/Miranda.g:83:11: '<section>'
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

            # grammars/Miranda.g:84:14: ( '\\'' )
            # grammars/Miranda.g:84:16: '\\''
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

            # grammars/Miranda.g:85:10: ( '--' )
            # grammars/Miranda.g:85:12: '--'
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

            # grammars/Miranda.g:86:6: ( 'true' )
            # grammars/Miranda.g:86:8: 'true'
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

            # grammars/Miranda.g:87:7: ( '<tuple>' )
            # grammars/Miranda.g:87:9: '<tuple>'
            pass 
            self.match("<tuple>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TUPLE"



    # $ANTLR start "TYPE"
    def mTYPE(self, ):
        try:
            _type = TYPE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:88:6: ( '<type>' )
            # grammars/Miranda.g:88:8: '<type>'
            pass 
            self.match("<type>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPE"



    # $ANTLR start "TYPE_IS"
    def mTYPE_IS(self, ):
        try:
            _type = TYPE_IS
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:89:9: ( '::=' )
            # grammars/Miranda.g:89:11: '::='
            pass 
            self.match("::=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPE_IS"



    # $ANTLR start "WHERE"
    def mWHERE(self, ):
        try:
            _type = WHERE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:90:7: ( 'where' )
            # grammars/Miranda.g:90:9: 'where'
            pass 
            self.match("where")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHERE"



    # $ANTLR start "STARS"
    def mSTARS(self, ):
        try:
            _type = STARS
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:132:6: ( ( '*' )+ )
            # grammars/Miranda.g:132:8: ( '*' )+
            pass 
            # grammars/Miranda.g:132:8: ( '*' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 42) :
                    alt1 = 1


                if alt1 == 1:
                    # grammars/Miranda.g:132:8: '*'
                    pass 
                    self.match(42)


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STARS"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:218:4: ( ( MIN )? ( NUMERIC )+ )
            # grammars/Miranda.g:218:6: ( MIN )? ( NUMERIC )+
            pass 
            # grammars/Miranda.g:218:6: ( MIN )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 45) :
                alt2 = 1
            if alt2 == 1:
                # grammars/Miranda.g:
                pass 
                if self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # grammars/Miranda.g:218:11: ( NUMERIC )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1




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

            # grammars/Miranda.g:219:6: ( ( MIN )? ( NUMERIC )+ DOT ( NUMERIC )+ )
            # grammars/Miranda.g:219:8: ( MIN )? ( NUMERIC )+ DOT ( NUMERIC )+
            pass 
            # grammars/Miranda.g:219:8: ( MIN )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 45) :
                alt4 = 1
            if alt4 == 1:
                # grammars/Miranda.g:
                pass 
                if self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # grammars/Miranda.g:219:13: ( NUMERIC )+
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


            self.mDOT()


            # grammars/Miranda.g:219:26: ( NUMERIC )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((48 <= LA6_0 <= 57)) :
                    alt6 = 1


                if alt6 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "NUMERIC"
    def mNUMERIC(self, ):
        try:
            # grammars/Miranda.g:220:17: ( ( '0' .. '9' ) )
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

            # grammars/Miranda.g:222:5: ( ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE ) )
            # grammars/Miranda.g:222:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:222:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 39) :
                alt7 = 1
            elif (LA7_0 == 34) :
                alt7 = 2
            else:
                nvae = NoViableAltException("", 7, 0, self.input)

                raise nvae


            if alt7 == 1:
                # grammars/Miranda.g:222:8: SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                self.mALPHANUMERIC()


                self.mSINGLE_QUOTE()



            elif alt7 == 2:
                # grammars/Miranda.g:222:49: DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE
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

            # grammars/Miranda.g:223:7: ( ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE ) )
            # grammars/Miranda.g:223:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:223:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 39) :
                alt10 = 1
            elif (LA10_0 == 34) :
                alt10 = 2
            else:
                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae


            if alt10 == 1:
                # grammars/Miranda.g:223:10: SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                # grammars/Miranda.g:223:23: ( ALPHANUMERIC )*
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


                self.mSINGLE_QUOTE()



            elif alt10 == 2:
                # grammars/Miranda.g:223:52: DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE
                pass 
                self.mDOUBLE_QUOTE()


                # grammars/Miranda.g:223:65: ( ALPHANUMERIC )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 32 or (48 <= LA9_0 <= 57) or (65 <= LA9_0 <= 90) or (97 <= LA9_0 <= 122)) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammars/Miranda.g:
                        pass 
                        if self.input.LA(1) == 32 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop9


                self.mDOUBLE_QUOTE()







            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "ALPHANUMERIC"
    def mALPHANUMERIC(self, ):
        try:
            # grammars/Miranda.g:224:22: ( ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | ' ' ) )
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

            # grammars/Miranda.g:226:3: ( ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )* ( '?' | '!' )? )
            # grammars/Miranda.g:226:5: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )* ( '?' | '!' )?
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # grammars/Miranda.g:226:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )*
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 46 or (48 <= LA11_0 <= 57) or (65 <= LA11_0 <= 90) or LA11_0 == 95 or (97 <= LA11_0 <= 122)) :
                    alt11 = 1


                if alt11 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if self.input.LA(1) == 46 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop11


            # grammars/Miranda.g:226:75: ( '?' | '!' )?
            alt12 = 2
            LA12_0 = self.input.LA(1)

            if (LA12_0 == 33 or LA12_0 == 63) :
                alt12 = 1
            if alt12 == 1:
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

            # grammars/Miranda.g:228:11: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # grammars/Miranda.g:228:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # grammars/Miranda.g:228:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt13 = 0
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if ((9 <= LA13_0 <= 10) or LA13_0 == 13 or LA13_0 == 32) :
                    alt13 = 1


                if alt13 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt13 >= 1:
                        break #loop13

                    eee = EarlyExitException(13, self.input)
                    raise eee

                cnt13 += 1


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

            # grammars/Miranda.g:232:8: ( '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' ) )
            # grammars/Miranda.g:232:10: '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' )
            pass 
            self.match(35)

            # grammars/Miranda.g:232:14: (~ ( '\\n' | '\\r' ) )*
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((0 <= LA14_0 <= 9) or (11 <= LA14_0 <= 12) or (14 <= LA14_0 <= 65535)) :
                    alt14 = 1


                if alt14 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop14


            # grammars/Miranda.g:232:32: ( ( '\\r' )? '\\n' )
            # grammars/Miranda.g:232:33: ( '\\r' )? '\\n'
            pass 
            # grammars/Miranda.g:232:33: ( '\\r' )?
            alt15 = 2
            LA15_0 = self.input.LA(1)

            if (LA15_0 == 13) :
                alt15 = 1
            if alt15 == 1:
                # grammars/Miranda.g:232:33: '\\r'
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
        # grammars/Miranda.g:1:8: ( ADD | AND | BODY | CHAR_TYPE | COLON | COMMA | CONCAT | DEDENT | DEFINITION | DIV | DOT | DOUBLE_QUOTE | EQ | EXP | FALSE | GENERIC | GT | GTE | IDIV | IS | LBRACKET | LIST | LPAREN | LT | LTE | MIN | MOD | NEQ | NOT | NUM_TYPE | OR | OTHERWISE | PART | PROGRAM | RBRACKET | RPAREN | SECTION | SINGLE_QUOTE | SUBTRACT | TRUE | TUPLE | TYPE | TYPE_IS | WHERE | STARS | INT | FLOAT | CHAR | STRING | ID | WHITESPACE | COMMENT )
        alt16 = 52
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
            # grammars/Miranda.g:1:18: BODY
            pass 
            self.mBODY()



        elif alt16 == 4:
            # grammars/Miranda.g:1:23: CHAR_TYPE
            pass 
            self.mCHAR_TYPE()



        elif alt16 == 5:
            # grammars/Miranda.g:1:33: COLON
            pass 
            self.mCOLON()



        elif alt16 == 6:
            # grammars/Miranda.g:1:39: COMMA
            pass 
            self.mCOMMA()



        elif alt16 == 7:
            # grammars/Miranda.g:1:45: CONCAT
            pass 
            self.mCONCAT()



        elif alt16 == 8:
            # grammars/Miranda.g:1:52: DEDENT
            pass 
            self.mDEDENT()



        elif alt16 == 9:
            # grammars/Miranda.g:1:59: DEFINITION
            pass 
            self.mDEFINITION()



        elif alt16 == 10:
            # grammars/Miranda.g:1:70: DIV
            pass 
            self.mDIV()



        elif alt16 == 11:
            # grammars/Miranda.g:1:74: DOT
            pass 
            self.mDOT()



        elif alt16 == 12:
            # grammars/Miranda.g:1:78: DOUBLE_QUOTE
            pass 
            self.mDOUBLE_QUOTE()



        elif alt16 == 13:
            # grammars/Miranda.g:1:91: EQ
            pass 
            self.mEQ()



        elif alt16 == 14:
            # grammars/Miranda.g:1:94: EXP
            pass 
            self.mEXP()



        elif alt16 == 15:
            # grammars/Miranda.g:1:98: FALSE
            pass 
            self.mFALSE()



        elif alt16 == 16:
            # grammars/Miranda.g:1:104: GENERIC
            pass 
            self.mGENERIC()



        elif alt16 == 17:
            # grammars/Miranda.g:1:112: GT
            pass 
            self.mGT()



        elif alt16 == 18:
            # grammars/Miranda.g:1:115: GTE
            pass 
            self.mGTE()



        elif alt16 == 19:
            # grammars/Miranda.g:1:119: IDIV
            pass 
            self.mIDIV()



        elif alt16 == 20:
            # grammars/Miranda.g:1:124: IS
            pass 
            self.mIS()



        elif alt16 == 21:
            # grammars/Miranda.g:1:127: LBRACKET
            pass 
            self.mLBRACKET()



        elif alt16 == 22:
            # grammars/Miranda.g:1:136: LIST
            pass 
            self.mLIST()



        elif alt16 == 23:
            # grammars/Miranda.g:1:141: LPAREN
            pass 
            self.mLPAREN()



        elif alt16 == 24:
            # grammars/Miranda.g:1:148: LT
            pass 
            self.mLT()



        elif alt16 == 25:
            # grammars/Miranda.g:1:151: LTE
            pass 
            self.mLTE()



        elif alt16 == 26:
            # grammars/Miranda.g:1:155: MIN
            pass 
            self.mMIN()



        elif alt16 == 27:
            # grammars/Miranda.g:1:159: MOD
            pass 
            self.mMOD()



        elif alt16 == 28:
            # grammars/Miranda.g:1:163: NEQ
            pass 
            self.mNEQ()



        elif alt16 == 29:
            # grammars/Miranda.g:1:167: NOT
            pass 
            self.mNOT()



        elif alt16 == 30:
            # grammars/Miranda.g:1:171: NUM_TYPE
            pass 
            self.mNUM_TYPE()



        elif alt16 == 31:
            # grammars/Miranda.g:1:180: OR
            pass 
            self.mOR()



        elif alt16 == 32:
            # grammars/Miranda.g:1:183: OTHERWISE
            pass 
            self.mOTHERWISE()



        elif alt16 == 33:
            # grammars/Miranda.g:1:193: PART
            pass 
            self.mPART()



        elif alt16 == 34:
            # grammars/Miranda.g:1:198: PROGRAM
            pass 
            self.mPROGRAM()



        elif alt16 == 35:
            # grammars/Miranda.g:1:206: RBRACKET
            pass 
            self.mRBRACKET()



        elif alt16 == 36:
            # grammars/Miranda.g:1:215: RPAREN
            pass 
            self.mRPAREN()



        elif alt16 == 37:
            # grammars/Miranda.g:1:222: SECTION
            pass 
            self.mSECTION()



        elif alt16 == 38:
            # grammars/Miranda.g:1:230: SINGLE_QUOTE
            pass 
            self.mSINGLE_QUOTE()



        elif alt16 == 39:
            # grammars/Miranda.g:1:243: SUBTRACT
            pass 
            self.mSUBTRACT()



        elif alt16 == 40:
            # grammars/Miranda.g:1:252: TRUE
            pass 
            self.mTRUE()



        elif alt16 == 41:
            # grammars/Miranda.g:1:257: TUPLE
            pass 
            self.mTUPLE()



        elif alt16 == 42:
            # grammars/Miranda.g:1:263: TYPE
            pass 
            self.mTYPE()



        elif alt16 == 43:
            # grammars/Miranda.g:1:268: TYPE_IS
            pass 
            self.mTYPE_IS()



        elif alt16 == 44:
            # grammars/Miranda.g:1:276: WHERE
            pass 
            self.mWHERE()



        elif alt16 == 45:
            # grammars/Miranda.g:1:282: STARS
            pass 
            self.mSTARS()



        elif alt16 == 46:
            # grammars/Miranda.g:1:288: INT
            pass 
            self.mINT()



        elif alt16 == 47:
            # grammars/Miranda.g:1:292: FLOAT
            pass 
            self.mFLOAT()



        elif alt16 == 48:
            # grammars/Miranda.g:1:298: CHAR
            pass 
            self.mCHAR()



        elif alt16 == 49:
            # grammars/Miranda.g:1:303: STRING
            pass 
            self.mSTRING()



        elif alt16 == 50:
            # grammars/Miranda.g:1:310: ID
            pass 
            self.mID()



        elif alt16 == 51:
            # grammars/Miranda.g:1:313: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt16 == 52:
            # grammars/Miranda.g:1:324: COMMENT
            pass 
            self.mCOMMENT()








    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\1\uffff\1\43\1\uffff\1\54\1\37\1\57\3\uffff\1\60\1\64\1\uffff"
        u"\1\37\1\67\1\37\2\uffff\1\72\1\37\1\75\1\37\1\uffff\2\37\2\uffff"
        u"\1\101\2\37\1\uffff\1\105\16\uffff\1\37\7\uffff\1\37\2\uffff\1"
        u"\37\2\uffff\1\37\2\uffff\3\37\2\uffff\2\37\5\uffff\1\37\1\uffff"
        u"\1\37\1\132\1\133\1\134\2\37\1\uffff\2\37\2\uffff\1\141\1\uffff"
        u"\1\37\3\uffff\2\37\1\145\1\37\1\uffff\1\147\2\37\1\uffff\1\152"
        u"\1\uffff\2\37\1\uffff\1\37\1\156\1\37\1\uffff\1\160\1\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\161\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\1\11\1\53\1\uffff\1\75\1\150\1\72\3\uffff\1\40\1\75\1\uffff\1"
        u"\141\1\75\1\151\2\uffff\1\55\1\157\1\75\1\165\1\uffff\1\164\1\162"
        u"\2\uffff\1\40\1\162\1\150\1\uffff\1\56\6\uffff\1\145\5\uffff\1"
        u"\165\1\uffff\1\141\3\uffff\1\40\3\uffff\1\154\2\uffff\1\166\2\uffff"
        u"\1\144\2\uffff\1\155\1\150\1\157\1\uffff\1\40\1\165\1\145\2\uffff"
        u"\1\144\2\uffff\1\162\1\uffff\1\163\3\41\1\145\1\147\1\uffff\1\145"
        u"\1\162\2\uffff\1\41\1\uffff\1\145\3\uffff\2\162\1\41\1\145\1\uffff"
        u"\1\41\1\167\1\141\1\uffff\1\41\1\uffff\1\151\1\155\1\uffff\1\163"
        u"\1\41\1\145\1\uffff\1\41\1\uffff"
        )

    DFA16_max = DFA.unpack(
        u"\1\174\1\53\1\uffff\1\164\1\150\1\72\3\uffff\1\172\1\75\1\uffff"
        u"\1\141\1\75\1\151\2\uffff\1\71\1\157\1\75\1\165\1\uffff\1\164\1"
        u"\162\2\uffff\1\172\1\162\1\150\1\uffff\1\71\6\uffff\1\145\5\uffff"
        u"\1\171\1\uffff\1\141\3\uffff\1\172\3\uffff\1\154\2\uffff\1\166"
        u"\2\uffff\1\144\2\uffff\1\155\1\150\1\157\1\uffff\1\172\1\165\1"
        u"\145\2\uffff\1\146\2\uffff\1\162\1\uffff\1\163\3\172\1\145\1\147"
        u"\1\uffff\1\145\1\162\2\uffff\1\172\1\uffff\1\145\3\uffff\2\162"
        u"\1\172\1\145\1\uffff\1\172\1\167\1\141\1\uffff\1\172\1\uffff\1"
        u"\151\1\155\1\uffff\1\163\1\172\1\145\1\uffff\1\172\1\uffff"
        )

    DFA16_accept = DFA.unpack(
        u"\2\uffff\1\2\3\uffff\1\6\1\12\1\13\2\uffff\1\16\3\uffff\1\25\1"
        u"\27\4\uffff\1\37\2\uffff\1\43\1\44\3\uffff\1\55\1\uffff\1\62\1"
        u"\63\1\64\1\7\1\1\1\3\1\uffff\1\20\1\26\1\31\1\41\1\45\1\uffff\1"
        u"\30\1\uffff\1\53\1\5\1\14\1\uffff\1\61\1\15\1\24\1\uffff\1\22\1"
        u"\21\1\uffff\1\47\1\32\1\uffff\1\34\1\35\3\uffff\1\46\3\uffff\1"
        u"\56\1\57\1\uffff\1\51\1\52\1\uffff\1\60\6\uffff\1\60\2\uffff\1"
        u"\10\1\11\1\uffff\1\60\1\uffff\1\23\1\33\1\36\4\uffff\1\4\3\uffff"
        u"\1\50\1\uffff\1\17\2\uffff\1\54\3\uffff\1\42\1\uffff\1\40"
        )

    DFA16_special = DFA.unpack(
        u"\161\uffff"
        )


    DFA16_transition = [
        DFA.unpack(u"\2\40\2\uffff\1\40\22\uffff\1\40\1\23\1\11\1\41\2\uffff"
        u"\1\2\1\32\1\20\1\31\1\35\1\1\1\6\1\21\1\10\1\7\12\36\1\5\1\uffff"
        u"\1\3\1\12\1\15\2\uffff\32\37\1\17\1\uffff\1\30\1\13\2\uffff\2\37"
        u"\1\4\1\16\1\37\1\14\6\37\1\22\1\24\1\26\1\27\3\37\1\33\2\37\1\34"
        u"\3\37\1\uffff\1\25"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\50\44\uffff\1\44\1\uffff\1\45\2\uffff\1\46\4\uffff"
        u"\1\47\3\uffff\1\51\2\uffff\1\52\1\53"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61\1\uffff\1\62\15\uffff\12\61\7\uffff\32\61\6\uffff"
        u"\32\61"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\71\2\uffff\12\36"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\102\6\uffff\1\62\10\uffff\12\102\7\uffff\32\102"
        u"\6\uffff\32\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\106\1\uffff\12\36"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\110\3\uffff\1\111"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\62\1\uffff\1\113\15\uffff\12\62\7\uffff\32\62\6"
        u"\uffff\32\62"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\62\6\uffff\1\122\10\uffff\12\62\7\uffff\32\62\6"
        u"\uffff\32\62"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\125\1\uffff\1\126"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\14\uffff\1\37\1\uffff\12\37\5\uffff\1\37\1\uffff"
        u"\32\37\4\uffff\1\37\1\uffff\32\37"),
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
