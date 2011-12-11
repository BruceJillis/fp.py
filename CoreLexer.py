# $ANTLR 3.4 grammars/Core.g 2011-12-11 20:55:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ADD=4
ALTERNATIVE=5
AND=6
APPLICATION=7
ARROW=8
CASE=9
COLON=10
COMBINATOR=11
COMMA=12
COMMENT=13
DEFINITION=14
DIV=15
DOT=16
EQ=17
GT=18
GTE=19
ID=20
IN=21
IS=22
LAMBDA=23
LCURLY=24
LET=25
LETREC=26
LPAREN=27
LT=28
LTE=29
MIN=30
MUL=31
NEQ=32
NOT=33
NUMBER=34
OF=35
OR=36
PACK=37
PROGRAM=38
RCURLY=39
RPAREN=40
SCOLON=41
WHITESPACE=42


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



    # $ANTLR start "ALTERNATIVE"
    def mALTERNATIVE(self, ):
        try:
            _type = ALTERNATIVE
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:8:13: ( '<alternative>' )
            # grammars/Core.g:8:15: '<alternative>'
            pass 
            self.match("<alternative>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ALTERNATIVE"



    # $ANTLR start "AND"
    def mAND(self, ):
        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:9:5: ( '&' )
            # grammars/Core.g:9:7: '&'
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

            # grammars/Core.g:10:13: ( '<application>' )
            # grammars/Core.g:10:15: '<application>'
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

            # grammars/Core.g:11:7: ( '->' )
            # grammars/Core.g:11:9: '->'
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

            # grammars/Core.g:12:6: ( 'case' )
            # grammars/Core.g:12:8: 'case'
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

            # grammars/Core.g:13:7: ( ':' )
            # grammars/Core.g:13:9: ':'
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

            # grammars/Core.g:14:12: ( '<combinator>' )
            # grammars/Core.g:14:14: '<combinator>'
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

            # grammars/Core.g:15:7: ( ',' )
            # grammars/Core.g:15:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "DEFINITION"
    def mDEFINITION(self, ):
        try:
            _type = DEFINITION
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:16:12: ( '<definition>' )
            # grammars/Core.g:16:14: '<definition>'
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

            # grammars/Core.g:17:5: ( '/' )
            # grammars/Core.g:17:7: '/'
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

            # grammars/Core.g:18:5: ( '.' )
            # grammars/Core.g:18:7: '.'
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

            # grammars/Core.g:19:4: ( '==' )
            # grammars/Core.g:19:6: '=='
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

            # grammars/Core.g:20:4: ( '>' )
            # grammars/Core.g:20:6: '>'
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

            # grammars/Core.g:21:5: ( '>=' )
            # grammars/Core.g:21:7: '>='
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

            # grammars/Core.g:22:4: ( 'in' )
            # grammars/Core.g:22:6: 'in'
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

            # grammars/Core.g:23:4: ( '=' )
            # grammars/Core.g:23:6: '='
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

            # grammars/Core.g:24:8: ( '\\\\' )
            # grammars/Core.g:24:10: '\\\\'
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

            # grammars/Core.g:25:8: ( '{' )
            # grammars/Core.g:25:10: '{'
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

            # grammars/Core.g:26:5: ( 'let' )
            # grammars/Core.g:26:7: 'let'
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

            # grammars/Core.g:27:8: ( 'letrec' )
            # grammars/Core.g:27:10: 'letrec'
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

            # grammars/Core.g:28:8: ( '(' )
            # grammars/Core.g:28:10: '('
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

            # grammars/Core.g:29:4: ( '<' )
            # grammars/Core.g:29:6: '<'
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

            # grammars/Core.g:30:5: ( '<=' )
            # grammars/Core.g:30:7: '<='
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

            # grammars/Core.g:31:5: ( '-' )
            # grammars/Core.g:31:7: '-'
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

            # grammars/Core.g:32:5: ( '*' )
            # grammars/Core.g:32:7: '*'
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

            # grammars/Core.g:33:5: ( '!=' )
            # grammars/Core.g:33:7: '!='
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

            # grammars/Core.g:34:5: ( '!' )
            # grammars/Core.g:34:7: '!'
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

            # grammars/Core.g:35:4: ( 'of' )
            # grammars/Core.g:35:6: 'of'
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

            # grammars/Core.g:36:4: ( '|' )
            # grammars/Core.g:36:6: '|'
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

            # grammars/Core.g:37:6: ( 'pack' )
            # grammars/Core.g:37:8: 'pack'
            pass 
            self.match("pack")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PACK"



    # $ANTLR start "PROGRAM"
    def mPROGRAM(self, ):
        try:
            _type = PROGRAM
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:38:9: ( '<program>' )
            # grammars/Core.g:38:11: '<program>'
            pass 
            self.match("<program>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROGRAM"



    # $ANTLR start "RCURLY"
    def mRCURLY(self, ):
        try:
            _type = RCURLY
            _channel = DEFAULT_CHANNEL

            # grammars/Core.g:39:8: ( '}' )
            # grammars/Core.g:39:10: '}'
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

            # grammars/Core.g:40:8: ( ')' )
            # grammars/Core.g:40:10: ')'
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

            # grammars/Core.g:41:8: ( ';' )
            # grammars/Core.g:41:10: ';'
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

            # grammars/Core.g:133:7: ( ( '0' .. '9' )+ )
            # grammars/Core.g:133:9: ( '0' .. '9' )+
            pass 
            # grammars/Core.g:133:9: ( '0' .. '9' )+
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

            # grammars/Core.g:135:3: ( ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '?' | '!' )? )
            # grammars/Core.g:135:5: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '?' | '!' )?
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # grammars/Core.g:135:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
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


            # grammars/Core.g:135:63: ( '?' | '!' )?
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

            # grammars/Core.g:137:11: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # grammars/Core.g:137:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # grammars/Core.g:137:13: ( ' ' | '\\t' | '\\r' | '\\n' )+
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

            # grammars/Core.g:141:8: ( '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF ) )
            # grammars/Core.g:141:10: '#' (~ ( '\\n' | '\\r' ) )* ( ( '\\r' )? '\\n' | EOF )
            pass 
            self.match(35)

            # grammars/Core.g:141:14: (~ ( '\\n' | '\\r' ) )*
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


            # grammars/Core.g:141:32: ( ( '\\r' )? '\\n' | EOF )
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 10 or LA7_0 == 13) :
                alt7 = 1
            else:
                alt7 = 2

            if alt7 == 1:
                # grammars/Core.g:141:33: ( '\\r' )? '\\n'
                pass 
                # grammars/Core.g:141:33: ( '\\r' )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 13) :
                    alt6 = 1
                if alt6 == 1:
                    # grammars/Core.g:141:33: '\\r'
                    pass 
                    self.match(13)




                self.match(10)


            elif alt7 == 2:
                # grammars/Core.g:141:46: EOF
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
        # grammars/Core.g:1:8: ( ADD | ALTERNATIVE | AND | APPLICATION | ARROW | CASE | COLON | COMBINATOR | COMMA | DEFINITION | DIV | DOT | EQ | GT | GTE | IN | IS | LAMBDA | LCURLY | LET | LETREC | LPAREN | LT | LTE | MIN | MUL | NEQ | NOT | OF | OR | PACK | PROGRAM | RCURLY | RPAREN | SCOLON | NUMBER | ID | WHITESPACE | COMMENT )
        alt8 = 39
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # grammars/Core.g:1:10: ADD
            pass 
            self.mADD()



        elif alt8 == 2:
            # grammars/Core.g:1:14: ALTERNATIVE
            pass 
            self.mALTERNATIVE()



        elif alt8 == 3:
            # grammars/Core.g:1:26: AND
            pass 
            self.mAND()



        elif alt8 == 4:
            # grammars/Core.g:1:30: APPLICATION
            pass 
            self.mAPPLICATION()



        elif alt8 == 5:
            # grammars/Core.g:1:42: ARROW
            pass 
            self.mARROW()



        elif alt8 == 6:
            # grammars/Core.g:1:48: CASE
            pass 
            self.mCASE()



        elif alt8 == 7:
            # grammars/Core.g:1:53: COLON
            pass 
            self.mCOLON()



        elif alt8 == 8:
            # grammars/Core.g:1:59: COMBINATOR
            pass 
            self.mCOMBINATOR()



        elif alt8 == 9:
            # grammars/Core.g:1:70: COMMA
            pass 
            self.mCOMMA()



        elif alt8 == 10:
            # grammars/Core.g:1:76: DEFINITION
            pass 
            self.mDEFINITION()



        elif alt8 == 11:
            # grammars/Core.g:1:87: DIV
            pass 
            self.mDIV()



        elif alt8 == 12:
            # grammars/Core.g:1:91: DOT
            pass 
            self.mDOT()



        elif alt8 == 13:
            # grammars/Core.g:1:95: EQ
            pass 
            self.mEQ()



        elif alt8 == 14:
            # grammars/Core.g:1:98: GT
            pass 
            self.mGT()



        elif alt8 == 15:
            # grammars/Core.g:1:101: GTE
            pass 
            self.mGTE()



        elif alt8 == 16:
            # grammars/Core.g:1:105: IN
            pass 
            self.mIN()



        elif alt8 == 17:
            # grammars/Core.g:1:108: IS
            pass 
            self.mIS()



        elif alt8 == 18:
            # grammars/Core.g:1:111: LAMBDA
            pass 
            self.mLAMBDA()



        elif alt8 == 19:
            # grammars/Core.g:1:118: LCURLY
            pass 
            self.mLCURLY()



        elif alt8 == 20:
            # grammars/Core.g:1:125: LET
            pass 
            self.mLET()



        elif alt8 == 21:
            # grammars/Core.g:1:129: LETREC
            pass 
            self.mLETREC()



        elif alt8 == 22:
            # grammars/Core.g:1:136: LPAREN
            pass 
            self.mLPAREN()



        elif alt8 == 23:
            # grammars/Core.g:1:143: LT
            pass 
            self.mLT()



        elif alt8 == 24:
            # grammars/Core.g:1:146: LTE
            pass 
            self.mLTE()



        elif alt8 == 25:
            # grammars/Core.g:1:150: MIN
            pass 
            self.mMIN()



        elif alt8 == 26:
            # grammars/Core.g:1:154: MUL
            pass 
            self.mMUL()



        elif alt8 == 27:
            # grammars/Core.g:1:158: NEQ
            pass 
            self.mNEQ()



        elif alt8 == 28:
            # grammars/Core.g:1:162: NOT
            pass 
            self.mNOT()



        elif alt8 == 29:
            # grammars/Core.g:1:166: OF
            pass 
            self.mOF()



        elif alt8 == 30:
            # grammars/Core.g:1:169: OR
            pass 
            self.mOR()



        elif alt8 == 31:
            # grammars/Core.g:1:172: PACK
            pass 
            self.mPACK()



        elif alt8 == 32:
            # grammars/Core.g:1:177: PROGRAM
            pass 
            self.mPROGRAM()



        elif alt8 == 33:
            # grammars/Core.g:1:185: RCURLY
            pass 
            self.mRCURLY()



        elif alt8 == 34:
            # grammars/Core.g:1:192: RPAREN
            pass 
            self.mRPAREN()



        elif alt8 == 35:
            # grammars/Core.g:1:199: SCOLON
            pass 
            self.mSCOLON()



        elif alt8 == 36:
            # grammars/Core.g:1:206: NUMBER
            pass 
            self.mNUMBER()



        elif alt8 == 37:
            # grammars/Core.g:1:213: ID
            pass 
            self.mID()



        elif alt8 == 38:
            # grammars/Core.g:1:216: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt8 == 39:
            # grammars/Core.g:1:227: COMMENT
            pass 
            self.mCOMMENT()








    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\2\uffff\1\42\1\uffff\1\44\1\32\4\uffff\1\47\1\51\1\32\2\uffff"
        u"\1\32\2\uffff\1\55\1\32\1\uffff\1\32\17\uffff\1\32\4\uffff\1\63"
        u"\1\32\2\uffff\1\65\1\32\2\uffff\1\32\1\uffff\1\71\1\uffff\1\32"
        u"\1\73\1\32\1\uffff\1\75\1\uffff\1\32\1\uffff\1\77\1\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\100\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\11\1\uffff\1\75\1\uffff\1\76\1\141\4\uffff\2\75\1\156\2\uffff"
        u"\1\145\2\uffff\1\75\1\146\1\uffff\1\141\7\uffff\1\154\7\uffff\1"
        u"\163\4\uffff\1\41\1\164\2\uffff\1\41\1\143\2\uffff\1\145\1\uffff"
        u"\1\41\1\uffff\1\153\1\41\1\145\1\uffff\1\41\1\uffff\1\143\1\uffff"
        u"\1\41\1\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\1\175\1\uffff\1\160\1\uffff\1\76\1\141\4\uffff\2\75\1\156\2\uffff"
        u"\1\145\2\uffff\1\75\1\146\1\uffff\1\141\7\uffff\1\160\7\uffff\1"
        u"\163\4\uffff\1\172\1\164\2\uffff\1\172\1\143\2\uffff\1\145\1\uffff"
        u"\1\172\1\uffff\1\153\1\172\1\145\1\uffff\1\172\1\uffff\1\143\1"
        u"\uffff\1\172\1\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\2\uffff\1\7\1\11\1\13\1\14\3\uffff\1\22"
        u"\1\23\1\uffff\1\26\1\32\2\uffff\1\36\1\uffff\1\41\1\42\1\43\1\44"
        u"\1\45\1\46\1\47\1\uffff\1\10\1\12\1\30\1\40\1\27\1\5\1\31\1\uffff"
        u"\1\15\1\21\1\17\1\16\2\uffff\1\33\1\34\2\uffff\1\2\1\4\1\uffff"
        u"\1\20\1\uffff\1\35\3\uffff\1\24\1\uffff\1\6\1\uffff\1\37\1\uffff"
        u"\1\25"
        )

    DFA8_special = DFA.unpack(
        u"\100\uffff"
        )


    DFA8_transition = [
        DFA.unpack(u"\2\33\2\uffff\1\33\22\uffff\1\33\1\22\1\uffff\1\34\2"
        u"\uffff\1\3\1\uffff\1\20\1\27\1\21\1\1\1\7\1\4\1\11\1\10\12\31\1"
        u"\6\1\30\1\2\1\12\1\13\2\uffff\32\32\1\uffff\1\15\4\uffff\2\32\1"
        u"\5\5\32\1\14\2\32\1\17\2\32\1\23\1\25\12\32\1\16\1\24\1\26"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\40\43\uffff\1\35\1\uffff\1\36\1\37\13\uffff\1\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\60\3\uffff\1\61"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\21\32\1\70\10\32"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32\16\uffff\12\32\5\uffff\1\32\1\uffff\32\32\6\uffff"
        u"\32\32"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\76"),
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
