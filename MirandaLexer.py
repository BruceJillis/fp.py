# $ANTLR 3.4 grammars/Miranda.g 2011-12-25 16:11:37

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
DEDENT=10
DEFINITION=11
DIV=12
DOT=13
DOUBLE_QUOTE=14
EQ=15
FLOAT=16
GT=17
GTE=18
ID=19
INT=20
IS=21
LPAREN=22
LT=23
LTE=24
MIN=25
MUL=26
NEQ=27
OR=28
RPAREN=29
SINGLE_QUOTE=30
STRING=31
TUPLE=32
WHITESPACE=33


class MirandaLexer(Lexer):

    grammarFileName = "grammars/Miranda.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(MirandaLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa12 = self.DFA12(
            self, 12,
            eot = self.DFA12_eot,
            eof = self.DFA12_eof,
            min = self.DFA12_min,
            max = self.DFA12_max,
            accept = self.DFA12_accept,
            special = self.DFA12_special,
            transition = self.DFA12_transition
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



    # $ANTLR start "DEDENT"
    def mDEDENT(self, ):
        try:
            _type = DEDENT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:49:8: ( '<dedent>' )
            # grammars/Miranda.g:49:10: '<dedent>'
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

            # grammars/Miranda.g:50:12: ( '<definition>' )
            # grammars/Miranda.g:50:14: '<definition>'
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

            # grammars/Miranda.g:51:5: ( '/' )
            # grammars/Miranda.g:51:7: '/'
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

            # grammars/Miranda.g:52:5: ( '.' )
            # grammars/Miranda.g:52:7: '.'
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

            # grammars/Miranda.g:53:14: ( '\"' )
            # grammars/Miranda.g:53:16: '\"'
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

            # grammars/Miranda.g:54:4: ( '==' )
            # grammars/Miranda.g:54:6: '=='
            pass 
            self.match("==")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQ"



    # $ANTLR start "GT"
    def mGT(self, ):
        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:55:4: ( '>' )
            # grammars/Miranda.g:55:6: '>'
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

            # grammars/Miranda.g:56:5: ( '>=' )
            # grammars/Miranda.g:56:7: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GTE"



    # $ANTLR start "IS"
    def mIS(self, ):
        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:57:4: ( '=' )
            # grammars/Miranda.g:57:6: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IS"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:58:8: ( '(' )
            # grammars/Miranda.g:58:10: '('
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

            # grammars/Miranda.g:59:4: ( '<' )
            # grammars/Miranda.g:59:6: '<'
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

            # grammars/Miranda.g:60:5: ( '<=' )
            # grammars/Miranda.g:60:7: '<='
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

            # grammars/Miranda.g:61:5: ( '-' )
            # grammars/Miranda.g:61:7: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MIN"



    # $ANTLR start "MUL"
    def mMUL(self, ):
        try:
            _type = MUL
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:62:5: ( '*' )
            # grammars/Miranda.g:62:7: '*'
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

            # grammars/Miranda.g:63:5: ( '!=' )
            # grammars/Miranda.g:63:7: '!='
            pass 
            self.match("!=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEQ"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:64:4: ( '|' )
            # grammars/Miranda.g:64:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:65:8: ( ')' )
            # grammars/Miranda.g:65:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "SINGLE_QUOTE"
    def mSINGLE_QUOTE(self, ):
        try:
            _type = SINGLE_QUOTE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:66:14: ( '\\'' )
            # grammars/Miranda.g:66:16: '\\''
            pass 
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SINGLE_QUOTE"



    # $ANTLR start "TUPLE"
    def mTUPLE(self, ):
        try:
            _type = TUPLE
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:67:7: ( '<tuple>' )
            # grammars/Miranda.g:67:9: '<tuple>'
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

            # grammars/Miranda.g:114:4: ( ( '0' .. '9' )+ )
            # grammars/Miranda.g:114:6: ( '0' .. '9' )+
            pass 
            # grammars/Miranda.g:114:6: ( '0' .. '9' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




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

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:115:6: ( INT DOT INT )
            # grammars/Miranda.g:115:8: INT DOT INT
            pass 
            self.mINT()


            self.mDOT()


            self.mINT()




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "CHAR"
    def mCHAR(self, ):
        try:
            _type = CHAR
            _channel = DEFAULT_CHANNEL

            # grammars/Miranda.g:117:5: ( ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE ) )
            # grammars/Miranda.g:117:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:117:7: ( SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE | DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 39) :
                alt2 = 1
            elif (LA2_0 == 34) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae


            if alt2 == 1:
                # grammars/Miranda.g:117:8: SINGLE_QUOTE ALPHANUMERIC SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                self.mALPHANUMERIC()


                self.mSINGLE_QUOTE()



            elif alt2 == 2:
                # grammars/Miranda.g:117:49: DOUBLE_QUOTE ALPHANUMERIC DOUBLE_QUOTE
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

            # grammars/Miranda.g:118:7: ( ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE ) )
            # grammars/Miranda.g:118:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
            pass 
            # grammars/Miranda.g:118:9: ( SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE | DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE )
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 39) :
                alt5 = 1
            elif (LA5_0 == 34) :
                alt5 = 2
            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae


            if alt5 == 1:
                # grammars/Miranda.g:118:10: SINGLE_QUOTE ( ALPHANUMERIC )* SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()


                # grammars/Miranda.g:118:23: ( ALPHANUMERIC )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 32 or (48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or (97 <= LA3_0 <= 122)) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammars/Miranda.g:
                        pass 
                        if self.input.LA(1) == 32 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop3


                self.mSINGLE_QUOTE()



            elif alt5 == 2:
                # grammars/Miranda.g:118:52: DOUBLE_QUOTE ( ALPHANUMERIC )* DOUBLE_QUOTE
                pass 
                self.mDOUBLE_QUOTE()


                # grammars/Miranda.g:118:65: ( ALPHANUMERIC )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 32 or (48 <= LA4_0 <= 57) or (65 <= LA4_0 <= 90) or (97 <= LA4_0 <= 122)) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammars/Miranda.g:
                        pass 
                        if self.input.LA(1) == 32 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop4


                self.mDOUBLE_QUOTE()







            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "ALPHANUMERIC"
    def mALPHANUMERIC(self, ):
        try:
            # grammars/Miranda.g:119:22: ( ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | ' ' ) )
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

            # grammars/Miranda.g:121:3: ( ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '?' | '!' )? )
            # grammars/Miranda.g:121:5: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '?' | '!' )?
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # grammars/Miranda.g:121:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((48 <= LA6_0 <= 57) or (65 <= LA6_0 <= 90) or (97 <= LA6_0 <= 122)) :
                    alt6 = 1


                if alt6 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop6


            # grammars/Miranda.g:121:63: ( '?' | '!' )?
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 33 or LA7_0 == 63) :
                alt7 = 1
            if alt7 == 1:
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

            # grammars/Miranda.g:123:11: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # grammars/Miranda.g:123:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # grammars/Miranda.g:123:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt8 = 0
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((9 <= LA8_0 <= 10) or LA8_0 == 13 or LA8_0 == 32) :
                    alt8 = 1


                if alt8 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt8 >= 1:
                        break #loop8

                    eee = EarlyExitException(8, self.input)
                    raise eee

                cnt8 += 1


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

            # grammars/Miranda.g:127:8: ( '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF ) )
            # grammars/Miranda.g:127:10: '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF )
            pass 
            self.match(35)

            # grammars/Miranda.g:127:14: (~ ( '\\n' | '\\r' ) )*
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((0 <= LA9_0 <= 9) or (11 <= LA9_0 <= 12) or (14 <= LA9_0 <= 65535)) :
                    alt9 = 1


                if alt9 == 1:
                    # grammars/Miranda.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop9


            # grammars/Miranda.g:127:32: ( ( '\\r' )? '\\n' | EOF )
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 10 or LA11_0 == 13) :
                alt11 = 1
            else:
                alt11 = 2

            if alt11 == 1:
                # grammars/Miranda.g:127:33: ( '\\r' )? '\\n'
                pass 
                # grammars/Miranda.g:127:33: ( '\\r' )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 13) :
                    alt10 = 1
                if alt10 == 1:
                    # grammars/Miranda.g:127:33: '\\r'
                    pass 
                    self.match(13)




                self.match(10)


            elif alt11 == 2:
                # grammars/Miranda.g:127:46: EOF
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
        # grammars/Miranda.g:1:8: ( ADD | AND | COMMA | DEDENT | DEFINITION | DIV | DOT | DOUBLE_QUOTE | EQ | GT | GTE | IS | LPAREN | LT | LTE | MIN | MUL | NEQ | OR | RPAREN | SINGLE_QUOTE | TUPLE | INT | FLOAT | CHAR | STRING | ID | WHITESPACE | COMMENT )
        alt12 = 29
        alt12 = self.dfa12.predict(self.input)
        if alt12 == 1:
            # grammars/Miranda.g:1:10: ADD
            pass 
            self.mADD()



        elif alt12 == 2:
            # grammars/Miranda.g:1:14: AND
            pass 
            self.mAND()



        elif alt12 == 3:
            # grammars/Miranda.g:1:18: COMMA
            pass 
            self.mCOMMA()



        elif alt12 == 4:
            # grammars/Miranda.g:1:24: DEDENT
            pass 
            self.mDEDENT()



        elif alt12 == 5:
            # grammars/Miranda.g:1:31: DEFINITION
            pass 
            self.mDEFINITION()



        elif alt12 == 6:
            # grammars/Miranda.g:1:42: DIV
            pass 
            self.mDIV()



        elif alt12 == 7:
            # grammars/Miranda.g:1:46: DOT
            pass 
            self.mDOT()



        elif alt12 == 8:
            # grammars/Miranda.g:1:50: DOUBLE_QUOTE
            pass 
            self.mDOUBLE_QUOTE()



        elif alt12 == 9:
            # grammars/Miranda.g:1:63: EQ
            pass 
            self.mEQ()



        elif alt12 == 10:
            # grammars/Miranda.g:1:66: GT
            pass 
            self.mGT()



        elif alt12 == 11:
            # grammars/Miranda.g:1:69: GTE
            pass 
            self.mGTE()



        elif alt12 == 12:
            # grammars/Miranda.g:1:73: IS
            pass 
            self.mIS()



        elif alt12 == 13:
            # grammars/Miranda.g:1:76: LPAREN
            pass 
            self.mLPAREN()



        elif alt12 == 14:
            # grammars/Miranda.g:1:83: LT
            pass 
            self.mLT()



        elif alt12 == 15:
            # grammars/Miranda.g:1:86: LTE
            pass 
            self.mLTE()



        elif alt12 == 16:
            # grammars/Miranda.g:1:90: MIN
            pass 
            self.mMIN()



        elif alt12 == 17:
            # grammars/Miranda.g:1:94: MUL
            pass 
            self.mMUL()



        elif alt12 == 18:
            # grammars/Miranda.g:1:98: NEQ
            pass 
            self.mNEQ()



        elif alt12 == 19:
            # grammars/Miranda.g:1:102: OR
            pass 
            self.mOR()



        elif alt12 == 20:
            # grammars/Miranda.g:1:105: RPAREN
            pass 
            self.mRPAREN()



        elif alt12 == 21:
            # grammars/Miranda.g:1:112: SINGLE_QUOTE
            pass 
            self.mSINGLE_QUOTE()



        elif alt12 == 22:
            # grammars/Miranda.g:1:125: TUPLE
            pass 
            self.mTUPLE()



        elif alt12 == 23:
            # grammars/Miranda.g:1:131: INT
            pass 
            self.mINT()



        elif alt12 == 24:
            # grammars/Miranda.g:1:135: FLOAT
            pass 
            self.mFLOAT()



        elif alt12 == 25:
            # grammars/Miranda.g:1:141: CHAR
            pass 
            self.mCHAR()



        elif alt12 == 26:
            # grammars/Miranda.g:1:146: STRING
            pass 
            self.mSTRING()



        elif alt12 == 27:
            # grammars/Miranda.g:1:153: ID
            pass 
            self.mID()



        elif alt12 == 28:
            # grammars/Miranda.g:1:156: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt12 == 29:
            # grammars/Miranda.g:1:167: COMMENT
            pass 
            self.mCOMMENT()








    # lookup tables for DFA #12

    DFA12_eot = DFA.unpack(
        u"\4\uffff\1\30\2\uffff\1\31\1\35\1\37\6\uffff\1\40\1\42\30\uffff"
        )

    DFA12_eof = DFA.unpack(
        u"\52\uffff"
        )

    DFA12_min = DFA.unpack(
        u"\1\11\3\uffff\1\75\2\uffff\1\40\2\75\6\uffff\1\40\1\56\3\uffff"
        u"\1\145\4\uffff\1\40\6\uffff\1\40\2\uffff\1\144\5\uffff"
        )

    DFA12_max = DFA.unpack(
        u"\1\174\3\uffff\1\164\2\uffff\1\172\2\75\6\uffff\1\172\1\71\3\uffff"
        u"\1\145\4\uffff\1\172\6\uffff\1\172\2\uffff\1\146\5\uffff"
        )

    DFA12_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\6\1\7\3\uffff\1\15\1\20\1\21\1\22"
        u"\1\23\1\24\2\uffff\1\33\1\34\1\35\1\uffff\1\17\1\26\1\16\1\10\1"
        u"\uffff\1\32\1\11\1\14\1\13\1\12\1\25\1\uffff\1\27\1\30\1\uffff"
        u"\2\31\1\4\1\5\1\31"
        )

    DFA12_special = DFA.unpack(
        u"\52\uffff"
        )


    DFA12_transition = [
        DFA.unpack(u"\2\23\2\uffff\1\23\22\uffff\1\23\1\15\1\7\1\24\2\uffff"
        u"\1\2\1\20\1\12\1\17\1\14\1\1\1\3\1\13\1\6\1\5\12\21\2\uffff\1\4"
        u"\1\10\1\11\2\uffff\32\22\6\uffff\32\22\1\uffff\1\16"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26\46\uffff\1\25\17\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\1\uffff\1\33\15\uffff\12\32\7\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41\6\uffff\1\33\10\uffff\12\41\7\uffff\32\41\6\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\33\1\uffff\1\45\15\uffff\12\33\7\uffff\32\33\6\uffff"
        u"\32\33"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\33\6\uffff\1\46\10\uffff\12\33\7\uffff\32\33\6\uffff"
        u"\32\33"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\47\1\uffff\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #12

    class DFA12(DFA):
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
