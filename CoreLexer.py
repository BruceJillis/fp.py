# $ANTLR 3.4 grammars/Core.g 2011-12-04 17:45:53

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ADD=4
AND=5
APPLICATION=6
ARROW=7
CASE=8
COLON=9
COMBINATOR=10
COMMA=11
COMMENT=12
DIV=13
DOT=14
EQ=15
GT=16
GTE=17
ID=18
IN=19
IS=20
LAMBDA=21
LCURLY=22
LET=23
LETREC=24
LPAREN=25
LT=26
LTE=27
MIN=28
MUL=29
NEQ=30
NOT=31
NUMBER=32
OF=33
OR=34
PACK=35
RCURLY=36
RPAREN=37
SCOLON=38
WHITESPACE=39


class CoreLexer(Lexer):

    grammarFileName = "grammars/Core.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(CoreLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "ADD"
    def mADD(self, ):
        try:
            _type = ADD
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:7:5: ( '+' )
            # grammars/Core.g:7:7: '+'
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

            # grammars/Core.g:8:5: ( '&' )
            # grammars/Core.g:8:7: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"



    # $ANTLR start "APPLICATION"
    def mAPPLICATION(self, ):
        try:
            _type = APPLICATION
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:9:13: ( '<application>' )
            # grammars/Core.g:9:15: '<application>'
            pass 
            self.match("<application>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "APPLICATION"



    # $ANTLR start "ARROW"
    def mARROW(self, ):
        try:
            _type = ARROW
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:10:7: ( '->' )
            # grammars/Core.g:10:9: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARROW"



    # $ANTLR start "CASE"
    def mCASE(self, ):
        try:
            _type = CASE
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:11:6: ( 'case' )
            # grammars/Core.g:11:8: 'case'
            pass 
            self.match("case")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CASE"



    # $ANTLR start "COLON"
    def mCOLON(self, ):
        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:12:7: ( ':' )
            # grammars/Core.g:12:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLON"



    # $ANTLR start "COMBINATOR"
    def mCOMBINATOR(self, ):
        try:
            _type = COMBINATOR
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:13:12: ( '<combinator>' )
            # grammars/Core.g:13:14: '<combinator>'
            pass 
            self.match("<combinator>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMBINATOR"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:14:7: ( ',' )
            # grammars/Core.g:14:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "DIV"
    def mDIV(self, ):
        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:15:5: ( '/' )
            # grammars/Core.g:15:7: '/'
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

            # grammars/Core.g:16:5: ( '.' )
            # grammars/Core.g:16:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "EQ"
    def mEQ(self, ):
        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:17:4: ( '==' )
            # grammars/Core.g:17:6: '=='
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

            # grammars/Core.g:18:4: ( '>' )
            # grammars/Core.g:18:6: '>'
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

            # grammars/Core.g:19:5: ( '>=' )
            # grammars/Core.g:19:7: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GTE"



    # $ANTLR start "IN"
    def mIN(self, ):
        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:20:4: ( 'in' )
            # grammars/Core.g:20:6: 'in'
            pass 
            self.match("in")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IN"



    # $ANTLR start "IS"
    def mIS(self, ):
        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:21:4: ( '=' )
            # grammars/Core.g:21:6: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IS"



    # $ANTLR start "LAMBDA"
    def mLAMBDA(self, ):
        try:
            _type = LAMBDA
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:22:8: ( '\\\\' )
            # grammars/Core.g:22:10: '\\\\'
            pass 
            self.match(92)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LAMBDA"



    # $ANTLR start "LCURLY"
    def mLCURLY(self, ):
        try:
            _type = LCURLY
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:23:8: ( '{' )
            # grammars/Core.g:23:10: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LCURLY"



    # $ANTLR start "LET"
    def mLET(self, ):
        try:
            _type = LET
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:24:5: ( 'let' )
            # grammars/Core.g:24:7: 'let'
            pass 
            self.match("let")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LET"



    # $ANTLR start "LETREC"
    def mLETREC(self, ):
        try:
            _type = LETREC
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:25:8: ( 'letrec' )
            # grammars/Core.g:25:10: 'letrec'
            pass 
            self.match("letrec")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LETREC"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:26:8: ( '(' )
            # grammars/Core.g:26:10: '('
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

            # grammars/Core.g:27:4: ( '<' )
            # grammars/Core.g:27:6: '<'
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

            # grammars/Core.g:28:5: ( '<=' )
            # grammars/Core.g:28:7: '<='
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

            # grammars/Core.g:29:5: ( '-' )
            # grammars/Core.g:29:7: '-'
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

            # grammars/Core.g:30:5: ( '*' )
            # grammars/Core.g:30:7: '*'
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

            # grammars/Core.g:31:5: ( '!=' )
            # grammars/Core.g:31:7: '!='
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

            # grammars/Core.g:32:5: ( '!' )
            # grammars/Core.g:32:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"



    # $ANTLR start "OF"
    def mOF(self, ):
        try:
            _type = OF
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:33:4: ( 'of' )
            # grammars/Core.g:33:6: 'of'
            pass 
            self.match("of")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OF"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:34:4: ( '|' )
            # grammars/Core.g:34:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "PACK"
    def mPACK(self, ):
        try:
            _type = PACK
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:35:6: ( 'pack' )
            # grammars/Core.g:35:8: 'pack'
            pass 
            self.match("pack")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PACK"



    # $ANTLR start "RCURLY"
    def mRCURLY(self, ):
        try:
            _type = RCURLY
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:36:8: ( '}' )
            # grammars/Core.g:36:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RCURLY"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:37:8: ( ')' )
            # grammars/Core.g:37:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "SCOLON"
    def mSCOLON(self, ):
        try:
            _type = SCOLON
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:38:8: ( ';' )
            # grammars/Core.g:38:10: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCOLON"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):
        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:111:7: ( ( '0' .. '9' )+ )
            # grammars/Core.g:111:9: ( '0' .. '9' )+
            pass 
            # grammars/Core.g:111:9: ( '0' .. '9' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # grammars/Core.g:
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

    # $ANTLR end "NUMBER"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:113:3: ( ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '?' | '!' )? )
            # grammars/Core.g:113:5: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '?' | '!' )?
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # grammars/Core.g:113:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57) or (65 <= LA2_0 <= 90) or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # grammars/Core.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2


            # grammars/Core.g:113:63: ( '?' | '!' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 33 or LA3_0 == 63) :
                alt3 = 1
            if alt3 == 1:
                # grammars/Core.g:
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

            # grammars/Core.g:115:11: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # grammars/Core.g:115:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # grammars/Core.g:115:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((9 <= LA4_0 <= 10) or LA4_0 == 13 or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # grammars/Core.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
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

            # grammars/Core.g:119:8: ( '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF ) )
            # grammars/Core.g:119:10: '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF )
            pass 
            self.match(35)

            # grammars/Core.g:119:14: (~ ( '\\n' | '\\r' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 12) or (14 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # grammars/Core.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5


            # grammars/Core.g:119:32: ( ( '\\r' )? '\\n' | EOF )
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 10 or LA7_0 == 13) :
                alt7 = 1
            else:
                alt7 = 2

            if alt7 == 1:
                # grammars/Core.g:119:33: ( '\\r' )? '\\n'
                pass 
                # grammars/Core.g:119:33: ( '\\r' )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 13) :
                    alt6 = 1
                if alt6 == 1:
                    # grammars/Core.g:119:33: '\\r'
                    pass 
                    self.match(13)




                self.match(10)


            elif alt7 == 2:
                # grammars/Core.g:119:46: EOF
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
        # grammars/Core.g:1:8: ( ADD | AND | APPLICATION | ARROW | CASE | COLON | COMBINATOR | COMMA | DIV | DOT | EQ | GT | GTE | IN | IS | LAMBDA | LCURLY | LET | LETREC | LPAREN | LT | LTE | MIN | MUL | NEQ | NOT | OF | OR | PACK | RCURLY | RPAREN | SCOLON | NUMBER | ID | WHITESPACE | COMMENT )
        alt8 = 36
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # grammars/Core.g:1:10: ADD
            pass 
            self.mADD()



        elif alt8 == 2:
            # grammars/Core.g:1:14: AND
            pass 
            self.mAND()



        elif alt8 == 3:
            # grammars/Core.g:1:18: APPLICATION
            pass 
            self.mAPPLICATION()



        elif alt8 == 4:
            # grammars/Core.g:1:30: ARROW
            pass 
            self.mARROW()



        elif alt8 == 5:
            # grammars/Core.g:1:36: CASE
            pass 
            self.mCASE()



        elif alt8 == 6:
            # grammars/Core.g:1:41: COLON
            pass 
            self.mCOLON()



        elif alt8 == 7:
            # grammars/Core.g:1:47: COMBINATOR
            pass 
            self.mCOMBINATOR()



        elif alt8 == 8:
            # grammars/Core.g:1:58: COMMA
            pass 
            self.mCOMMA()



        elif alt8 == 9:
            # grammars/Core.g:1:64: DIV
            pass 
            self.mDIV()



        elif alt8 == 10:
            # grammars/Core.g:1:68: DOT
            pass 
            self.mDOT()



        elif alt8 == 11:
            # grammars/Core.g:1:72: EQ
            pass 
            self.mEQ()



        elif alt8 == 12:
            # grammars/Core.g:1:75: GT
            pass 
            self.mGT()



        elif alt8 == 13:
            # grammars/Core.g:1:78: GTE
            pass 
            self.mGTE()



        elif alt8 == 14:
            # grammars/Core.g:1:82: IN
            pass 
            self.mIN()



        elif alt8 == 15:
            # grammars/Core.g:1:85: IS
            pass 
            self.mIS()



        elif alt8 == 16:
            # grammars/Core.g:1:88: LAMBDA
            pass 
            self.mLAMBDA()



        elif alt8 == 17:
            # grammars/Core.g:1:95: LCURLY
            pass 
            self.mLCURLY()



        elif alt8 == 18:
            # grammars/Core.g:1:102: LET
            pass 
            self.mLET()



        elif alt8 == 19:
            # grammars/Core.g:1:106: LETREC
            pass 
            self.mLETREC()



        elif alt8 == 20:
            # grammars/Core.g:1:113: LPAREN
            pass 
            self.mLPAREN()



        elif alt8 == 21:
            # grammars/Core.g:1:120: LT
            pass 
            self.mLT()



        elif alt8 == 22:
            # grammars/Core.g:1:123: LTE
            pass 
            self.mLTE()



        elif alt8 == 23:
            # grammars/Core.g:1:127: MIN
            pass 
            self.mMIN()



        elif alt8 == 24:
            # grammars/Core.g:1:131: MUL
            pass 
            self.mMUL()



        elif alt8 == 25:
            # grammars/Core.g:1:135: NEQ
            pass 
            self.mNEQ()



        elif alt8 == 26:
            # grammars/Core.g:1:139: NOT
            pass 
            self.mNOT()



        elif alt8 == 27:
            # grammars/Core.g:1:143: OF
            pass 
            self.mOF()



        elif alt8 == 28:
            # grammars/Core.g:1:146: OR
            pass 
            self.mOR()



        elif alt8 == 29:
            # grammars/Core.g:1:149: PACK
            pass 
            self.mPACK()



        elif alt8 == 30:
            # grammars/Core.g:1:154: RCURLY
            pass 
            self.mRCURLY()



        elif alt8 == 31:
            # grammars/Core.g:1:161: RPAREN
            pass 
            self.mRPAREN()



        elif alt8 == 32:
            # grammars/Core.g:1:168: SCOLON
            pass 
            self.mSCOLON()



        elif alt8 == 33:
            # grammars/Core.g:1:175: NUMBER
            pass 
            self.mNUMBER()



        elif alt8 == 34:
            # grammars/Core.g:1:182: ID
            pass 
            self.mID()



        elif alt8 == 35:
            # grammars/Core.g:1:185: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt8 == 36:
            # grammars/Core.g:1:196: COMMENT
            pass 
            self.mCOMMENT()








    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\3\uffff\1\40\1\42\1\32\4\uffff\1\45\1\47\1\32\2\uffff\1\32\2\uffff"
        u"\1\53\1\32\1\uffff\1\32\15\uffff\1\32\4\uffff\1\57\1\32\2\uffff"
        u"\1\61\2\32\1\uffff\1\65\1\uffff\1\32\1\67\1\32\1\uffff\1\71\1\uffff"
        u"\1\32\1\uffff\1\73\1\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\74\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\11\2\uffff\1\75\1\76\1\141\4\uffff\2\75\1\156\2\uffff\1\145"
        u"\2\uffff\1\75\1\146\1\uffff\1\141\15\uffff\1\163\4\uffff\1\41\1"
        u"\164\2\uffff\1\41\1\143\1\145\1\uffff\1\41\1\uffff\1\153\1\41\1"
        u"\145\1\uffff\1\41\1\uffff\1\143\1\uffff\1\41\1\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\1\175\2\uffff\1\143\1\76\1\141\4\uffff\2\75\1\156\2\uffff\1\145"
        u"\2\uffff\1\75\1\146\1\uffff\1\141\15\uffff\1\163\4\uffff\1\172"
        u"\1\164\2\uffff\1\172\1\143\1\145\1\uffff\1\172\1\uffff\1\153\1"
        u"\172\1\145\1\uffff\1\172\1\uffff\1\143\1\uffff\1\172\1\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\3\uffff\1\6\1\10\1\11\1\12\3\uffff\1\20\1\21\1"
        u"\uffff\1\24\1\30\2\uffff\1\34\1\uffff\1\36\1\37\1\40\1\41\1\42"
        u"\1\43\1\44\1\3\1\7\1\26\1\25\1\4\1\27\1\uffff\1\13\1\17\1\15\1"
        u"\14\2\uffff\1\31\1\32\3\uffff\1\16\1\uffff\1\33\3\uffff\1\22\1"
        u"\uffff\1\5\1\uffff\1\35\1\uffff\1\23"
        )

    DFA8_special = DFA.unpack(
        u"\74\uffff"
        )


    DFA8_transition = [
        DFA.unpack(u"\2\33\2\uffff\1\33\22\uffff\1\33\1\22\1\uffff\1\34\2"
        u"\uffff\1\2\1\uffff\1\20\1\27\1\21\1\1\1\7\1\4\1\11\1\10\12\31\1"
        u"\6\1\30\1\3\1\12\1\13\2\uffff\32\32\1\uffff\1\15\4\uffff\2\32\1"
        u"\5\5\32\1\14\2\32\1\17\2\32\1\23\1\25\12\32\1\16\1\24\1\26"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\43\uffff\1\35\1\uffff\1\36"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\21\32\1\64\10\32"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(CoreLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
