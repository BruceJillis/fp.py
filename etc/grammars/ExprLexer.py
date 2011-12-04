# $ANTLR 3.4 Expr.g 2011-12-02 13:32:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__8=8
T__9=9
T__10=10
T__11=11
T__12=12
T__13=13
ID=4
INT=5
NEWLINE=6
WS=7


class ExprLexer(Lexer):

    grammarFileName = "Expr.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(ExprLexer, self).__init__(input, state)

        self.delegates = []






    # $ANTLR start "T__8"
    def mT__8(self, ):
        try:
            _type = T__8
            _channel = DEFAULT_CHANNEL

            # Expr.g:7:6: ( '(' )
            # Expr.g:7:8: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__8"



    # $ANTLR start "T__9"
    def mT__9(self, ):
        try:
            _type = T__9
            _channel = DEFAULT_CHANNEL

            # Expr.g:8:6: ( ')' )
            # Expr.g:8:8: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__9"



    # $ANTLR start "T__10"
    def mT__10(self, ):
        try:
            _type = T__10
            _channel = DEFAULT_CHANNEL

            # Expr.g:9:7: ( '*' )
            # Expr.g:9:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__10"



    # $ANTLR start "T__11"
    def mT__11(self, ):
        try:
            _type = T__11
            _channel = DEFAULT_CHANNEL

            # Expr.g:10:7: ( '+' )
            # Expr.g:10:9: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__11"



    # $ANTLR start "T__12"
    def mT__12(self, ):
        try:
            _type = T__12
            _channel = DEFAULT_CHANNEL

            # Expr.g:11:7: ( '-' )
            # Expr.g:11:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__12"



    # $ANTLR start "T__13"
    def mT__13(self, ):
        try:
            _type = T__13
            _channel = DEFAULT_CHANNEL

            # Expr.g:12:7: ( '=' )
            # Expr.g:12:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__13"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Expr.g:28:4: ( ( 'a' .. 'z' | 'A' .. 'Z' )+ )
            # Expr.g:28:6: ( 'a' .. 'z' | 'A' .. 'Z' )+
            pass 
            # Expr.g:28:6: ( 'a' .. 'z' | 'A' .. 'Z' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((65 <= LA1_0 <= 90) or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Expr.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
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

    # $ANTLR end "ID"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # Expr.g:30:5: ( ( '0' .. '9' )+ )
            # Expr.g:30:7: ( '0' .. '9' )+
            pass 
            # Expr.g:30:7: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # Expr.g:
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



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # Expr.g:32:9: ( ( '\\r' )? '\\n' )
            # Expr.g:32:11: ( '\\r' )? '\\n'
            pass 
            # Expr.g:32:11: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # Expr.g:32:11: '\\r'
                pass 
                self.match(13)




            self.match(10)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # Expr.g:34:4: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # Expr.g:34:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # Expr.g:34:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((9 <= LA4_0 <= 10) or LA4_0 == 13 or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # Expr.g:
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
            self.skip()
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # Expr.g:1:8: ( T__8 | T__9 | T__10 | T__11 | T__12 | T__13 | ID | INT | NEWLINE | WS )
        alt5 = 10
        LA5 = self.input.LA(1)
        if LA5 == 40:
            alt5 = 1
        elif LA5 == 41:
            alt5 = 2
        elif LA5 == 42:
            alt5 = 3
        elif LA5 == 43:
            alt5 = 4
        elif LA5 == 45:
            alt5 = 5
        elif LA5 == 61:
            alt5 = 6
        elif LA5 == 65 or LA5 == 66 or LA5 == 67 or LA5 == 68 or LA5 == 69 or LA5 == 70 or LA5 == 71 or LA5 == 72 or LA5 == 73 or LA5 == 74 or LA5 == 75 or LA5 == 76 or LA5 == 77 or LA5 == 78 or LA5 == 79 or LA5 == 80 or LA5 == 81 or LA5 == 82 or LA5 == 83 or LA5 == 84 or LA5 == 85 or LA5 == 86 or LA5 == 87 or LA5 == 88 or LA5 == 89 or LA5 == 90 or LA5 == 97 or LA5 == 98 or LA5 == 99 or LA5 == 100 or LA5 == 101 or LA5 == 102 or LA5 == 103 or LA5 == 104 or LA5 == 105 or LA5 == 106 or LA5 == 107 or LA5 == 108 or LA5 == 109 or LA5 == 110 or LA5 == 111 or LA5 == 112 or LA5 == 113 or LA5 == 114 or LA5 == 115 or LA5 == 116 or LA5 == 117 or LA5 == 118 or LA5 == 119 or LA5 == 120 or LA5 == 121 or LA5 == 122:
            alt5 = 7
        elif LA5 == 48 or LA5 == 49 or LA5 == 50 or LA5 == 51 or LA5 == 52 or LA5 == 53 or LA5 == 54 or LA5 == 55 or LA5 == 56 or LA5 == 57:
            alt5 = 8
        elif LA5 == 13:
            LA5_9 = self.input.LA(2)

            if (LA5_9 == 10) :
                LA5_10 = self.input.LA(3)

                if ((9 <= LA5_10 <= 10) or LA5_10 == 13 or LA5_10 == 32) :
                    alt5 = 10
                else:
                    alt5 = 9

            else:
                alt5 = 10

        elif LA5 == 10:
            LA5_10 = self.input.LA(2)

            if ((9 <= LA5_10 <= 10) or LA5_10 == 13 or LA5_10 == 32) :
                alt5 = 10
            else:
                alt5 = 9

        elif LA5 == 9 or LA5 == 32:
            alt5 = 10
        else:
            nvae = NoViableAltException("", 5, 0, self.input)

            raise nvae


        if alt5 == 1:
            # Expr.g:1:10: T__8
            pass 
            self.mT__8()



        elif alt5 == 2:
            # Expr.g:1:15: T__9
            pass 
            self.mT__9()



        elif alt5 == 3:
            # Expr.g:1:20: T__10
            pass 
            self.mT__10()



        elif alt5 == 4:
            # Expr.g:1:26: T__11
            pass 
            self.mT__11()



        elif alt5 == 5:
            # Expr.g:1:32: T__12
            pass 
            self.mT__12()



        elif alt5 == 6:
            # Expr.g:1:38: T__13
            pass 
            self.mT__13()



        elif alt5 == 7:
            # Expr.g:1:44: ID
            pass 
            self.mID()



        elif alt5 == 8:
            # Expr.g:1:47: INT
            pass 
            self.mINT()



        elif alt5 == 9:
            # Expr.g:1:51: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt5 == 10:
            # Expr.g:1:59: WS
            pass 
            self.mWS()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ExprLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
