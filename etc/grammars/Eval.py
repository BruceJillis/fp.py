# $ANTLR 3.4 Eval.g 2011-12-02 13:32:33

import sys
from antlr3 import *
from antlr3.tree import *

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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ID", "INT", "NEWLINE", "WS", "'('", "')'", "'*'", "'+'", "'-'", "'='"
]




class Eval(TreeParser):
    grammarFileName = "Eval.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(Eval, self).__init__(input, state, *args, **kwargs)



        self.memory = {}

        self.delegates = []






    # $ANTLR start "prog"
    # Eval.g:12:1: prog : ( stat )+ ;
    def prog(self, ):
        try:
            try:
                # Eval.g:12:5: ( ( stat )+ )
                # Eval.g:12:9: ( stat )+
                pass 
                # Eval.g:12:9: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((ID <= LA1_0 <= INT) or (10 <= LA1_0 <= 13)) :
                        alt1 = 1


                    if alt1 == 1:
                        # Eval.g:12:9: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog52)
                        self.stat()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "prog"



    # $ANTLR start "stat"
    # Eval.g:14:1: stat : ( expr | ^( '=' ID expr ) );
    def stat(self, ):
        ID2 = None
        expr1 = None

        expr3 = None


        try:
            try:
                # Eval.g:14:5: ( expr | ^( '=' ID expr ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((ID <= LA2_0 <= INT) or (10 <= LA2_0 <= 12)) :
                    alt2 = 1
                elif (LA2_0 == 13) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # Eval.g:14:9: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_stat63)
                    expr1 = self.expr()

                    self._state.following.pop()

                    #action start
                    print expr1
                    #action end



                elif alt2 == 2:
                    # Eval.g:16:9: ^( '=' ID expr )
                    pass 
                    self.match(self.input, 13, self.FOLLOW_13_in_stat84)

                    self.match(self.input, DOWN, None)
                    ID2 = self.match(self.input, ID, self.FOLLOW_ID_in_stat86)

                    self._state.following.append(self.FOLLOW_expr_in_stat88)
                    expr3 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    self.memory[ID2.getText()] = int(expr3)
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "stat"



    # $ANTLR start "expr"
    # Eval.g:22:1: expr returns [value] : ( ^( '+' a= expr b= expr ) | ^( '-' a= expr b= expr ) | ^( '*' a= expr b= expr ) | ID | INT );
    def expr(self, ):
        value = None


        ID4 = None
        INT5 = None
        a = None

        b = None


        try:
            try:
                # Eval.g:23:5: ( ^( '+' a= expr b= expr ) | ^( '-' a= expr b= expr ) | ^( '*' a= expr b= expr ) | ID | INT )
                alt3 = 5
                LA3 = self.input.LA(1)
                if LA3 == 11:
                    alt3 = 1
                elif LA3 == 12:
                    alt3 = 2
                elif LA3 == 10:
                    alt3 = 3
                elif LA3 == ID:
                    alt3 = 4
                elif LA3 == INT:
                    alt3 = 5
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # Eval.g:23:9: ^( '+' a= expr b= expr )
                    pass 
                    self.match(self.input, 11, self.FOLLOW_11_in_expr125)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr129)
                    a = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr133)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value =  a+b
                    #action end



                elif alt3 == 2:
                    # Eval.g:24:9: ^( '-' a= expr b= expr )
                    pass 
                    self.match(self.input, 12, self.FOLLOW_12_in_expr147)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr151)
                    a = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr155)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value =  a-b
                    #action end



                elif alt3 == 3:
                    # Eval.g:25:9: ^( '*' a= expr b= expr )
                    pass 
                    self.match(self.input, 10, self.FOLLOW_10_in_expr169)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr173)
                    a = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr177)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value =  a*b
                    #action end



                elif alt3 == 4:
                    # Eval.g:26:9: ID
                    pass 
                    ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_expr190)

                    #action start
                            
                    k = ID4.getText()
                    if k in self.memory:
                    	value = self.memory[k]
                    else:
                    	print >> sys.stderr, "undefined variable "+k
                            
                    #action end



                elif alt3 == 5:
                    # Eval.g:34:9: INT
                    pass 
                    INT5 = self.match(self.input, INT, self.FOLLOW_INT_in_expr210)

                    #action start
                    value = int(INT5.getText())
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "expr"



 

    FOLLOW_stat_in_prog52 = frozenset([1, 4, 5, 10, 11, 12, 13])
    FOLLOW_expr_in_stat63 = frozenset([1])
    FOLLOW_13_in_stat84 = frozenset([2])
    FOLLOW_ID_in_stat86 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_stat88 = frozenset([3])
    FOLLOW_11_in_expr125 = frozenset([2])
    FOLLOW_expr_in_expr129 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_expr133 = frozenset([3])
    FOLLOW_12_in_expr147 = frozenset([2])
    FOLLOW_expr_in_expr151 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_expr155 = frozenset([3])
    FOLLOW_10_in_expr169 = frozenset([2])
    FOLLOW_expr_in_expr173 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_expr177 = frozenset([3])
    FOLLOW_ID_in_expr190 = frozenset([1])
    FOLLOW_INT_in_expr210 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Eval)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
