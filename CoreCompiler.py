# $ANTLR 3.4 grammars/CoreCompiler.g 2011-12-04 17:45:58

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset

        
from common import Environment



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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "AND", "APPLICATION", "ARROW", "CASE", "COLON", "COMBINATOR", 
    "COMMA", "COMMENT", "DIV", "DOT", "EQ", "GT", "GTE", "ID", "IN", "IS", 
    "LAMBDA", "LCURLY", "LET", "LETREC", "LPAREN", "LT", "LTE", "MIN", "MUL", 
    "NEQ", "NOT", "NUMBER", "OF", "OR", "PACK", "RCURLY", "RPAREN", "SCOLON", 
    "WHITESPACE"
]




class CoreCompiler(TreeParser):
    grammarFileName = "grammars/CoreCompiler.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(CoreCompiler, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # grammars/CoreCompiler.g:14:1: start[info, code] : ( combinator[info, code] )+ ;
    def start(self, info, code):
        try:
            try:
                # grammars/CoreCompiler.g:15:2: ( ( combinator[info, code] )+ )
                # grammars/CoreCompiler.g:15:4: ( combinator[info, code] )+
                pass 
                # grammars/CoreCompiler.g:15:4: ( combinator[info, code] )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == COMBINATOR) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammars/CoreCompiler.g:15:4: combinator[info, code]
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_start68)
                        self.combinator(info, code)

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

    # $ANTLR end "start"



    # $ANTLR start "combinator"
    # grammars/CoreCompiler.g:18:1: combinator[info, code] : ^( COMBINATOR n= ID (i= ID )* expression[info, env, code] ) ;
    def combinator(self, info, code):
        n = None
        i = None

        try:
            try:
                # grammars/CoreCompiler.g:19:2: ( ^( COMBINATOR n= ID (i= ID )* expression[info, env, code] ) )
                # grammars/CoreCompiler.g:19:4: ^( COMBINATOR n= ID (i= ID )* expression[info, env, code] )
                pass 
                #action start
                env = Environment() 
                #action end


                self.match(self.input, COMBINATOR, self.FOLLOW_COMBINATOR_in_combinator87)

                self.match(self.input, DOWN, None)
                n = self.match(self.input, ID, self.FOLLOW_ID_in_combinator91)

                # grammars/CoreCompiler.g:20:21: (i= ID )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        LA2_2 = self.input.LA(2)

                        if ((ADD <= LA2_2 <= APPLICATION) or LA2_2 == CASE or LA2_2 == DIV or (EQ <= LA2_2 <= ID) or LA2_2 == LAMBDA or (LET <= LA2_2 <= LETREC) or (LT <= LA2_2 <= NEQ) or LA2_2 == NUMBER or (OR <= LA2_2 <= PACK)) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/CoreCompiler.g:20:22: i= ID
                        pass 
                        i = self.match(self.input, ID, self.FOLLOW_ID_in_combinator96)

                        #action start
                        env.add(i.text) 
                        #action end



                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_expression_in_combinator103)
                self.expression(info, env, code)

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                                                                                               
                code.Update(env.count())
                if env.count() > 0:
                	code.Pop(env.count())
                code.Unwind()
                code.store(n.text, env)
                	
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "combinator"



    # $ANTLR start "expression"
    # grammars/CoreCompiler.g:29:1: expression[info, env, code] : ( ^( LET ( definition )+ expression[info, env, code] ) | ^( LETREC ( definition )+ expression[info, env, code] ) | ^( CASE expression[info, env, code] ( alternative )+ ) | ^( LAMBDA ( ID )+ expression[info, env, code] ) | ^( MUL expression[info, env, code] expression[info, env, code] ) | ^( DIV expression[info, env, code] expression[info, env, code] ) | ^( ADD expression[info, env, code] expression[info, env, code] ) | ^( MIN expression[info, env, code] expression[info, env, code] ) | ^( AND expression[info, env, code] expression[info, env, code] ) | ^( OR expression[info, env, code] expression[info, env, code] ) | ^( EQ expression[info, env, code] expression[info, env, code] ) | ^( NEQ expression[info, env, code] expression[info, env, code] ) | ^( LT expression[info, env, code] expression[info, env, code] ) | ^( LTE expression[info, env, code] expression[info, env, code] ) | ^( GT expression[info, env, code] expression[info, env, code] ) | ^( GTE expression[info, env, code] expression[info, env, code] ) | ^( APPLICATION expression[info, env, code] expression[info, env.increment(), code] ) | basic[info, env, code] );
    def expression(self, info, env, code):
        try:
            try:
                # grammars/CoreCompiler.g:30:2: ( ^( LET ( definition )+ expression[info, env, code] ) | ^( LETREC ( definition )+ expression[info, env, code] ) | ^( CASE expression[info, env, code] ( alternative )+ ) | ^( LAMBDA ( ID )+ expression[info, env, code] ) | ^( MUL expression[info, env, code] expression[info, env, code] ) | ^( DIV expression[info, env, code] expression[info, env, code] ) | ^( ADD expression[info, env, code] expression[info, env, code] ) | ^( MIN expression[info, env, code] expression[info, env, code] ) | ^( AND expression[info, env, code] expression[info, env, code] ) | ^( OR expression[info, env, code] expression[info, env, code] ) | ^( EQ expression[info, env, code] expression[info, env, code] ) | ^( NEQ expression[info, env, code] expression[info, env, code] ) | ^( LT expression[info, env, code] expression[info, env, code] ) | ^( LTE expression[info, env, code] expression[info, env, code] ) | ^( GT expression[info, env, code] expression[info, env, code] ) | ^( GTE expression[info, env, code] expression[info, env, code] ) | ^( APPLICATION expression[info, env, code] expression[info, env.increment(), code] ) | basic[info, env, code] )
                alt7 = 18
                LA7 = self.input.LA(1)
                if LA7 == LET:
                    alt7 = 1
                elif LA7 == LETREC:
                    alt7 = 2
                elif LA7 == CASE:
                    alt7 = 3
                elif LA7 == LAMBDA:
                    alt7 = 4
                elif LA7 == MUL:
                    alt7 = 5
                elif LA7 == DIV:
                    alt7 = 6
                elif LA7 == ADD:
                    alt7 = 7
                elif LA7 == MIN:
                    alt7 = 8
                elif LA7 == AND:
                    alt7 = 9
                elif LA7 == OR:
                    alt7 = 10
                elif LA7 == EQ:
                    alt7 = 11
                elif LA7 == NEQ:
                    alt7 = 12
                elif LA7 == LT:
                    alt7 = 13
                elif LA7 == LTE:
                    alt7 = 14
                elif LA7 == GT:
                    alt7 = 15
                elif LA7 == GTE:
                    alt7 = 16
                elif LA7 == APPLICATION:
                    alt7 = 17
                elif LA7 == ID or LA7 == NUMBER or LA7 == PACK:
                    alt7 = 18
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammars/CoreCompiler.g:30:4: ^( LET ( definition )+ expression[info, env, code] )
                    pass 
                    self.match(self.input, LET, self.FOLLOW_LET_in_expression119)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreCompiler.g:30:10: ( definition )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == IS) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammars/CoreCompiler.g:30:10: definition
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression121)
                            self.definition()

                            self._state.following.pop()


                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression124)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 2:
                    # grammars/CoreCompiler.g:31:4: ^( LETREC ( definition )+ expression[info, env, code] )
                    pass 
                    self.match(self.input, LETREC, self.FOLLOW_LETREC_in_expression132)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreCompiler.g:31:13: ( definition )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == IS) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammars/CoreCompiler.g:31:13: definition
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression134)
                            self.definition()

                            self._state.following.pop()


                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression137)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 3:
                    # grammars/CoreCompiler.g:32:4: ^( CASE expression[info, env, code] ( alternative )+ )
                    pass 
                    self.match(self.input, CASE, self.FOLLOW_CASE_in_expression145)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression147)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    # grammars/CoreCompiler.g:32:39: ( alternative )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == ARROW) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammars/CoreCompiler.g:32:39: alternative
                            pass 
                            self._state.following.append(self.FOLLOW_alternative_in_expression150)
                            self.alternative()

                            self._state.following.pop()


                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    self.match(self.input, UP, None)



                elif alt7 == 4:
                    # grammars/CoreCompiler.g:33:4: ^( LAMBDA ( ID )+ expression[info, env, code] )
                    pass 
                    self.match(self.input, LAMBDA, self.FOLLOW_LAMBDA_in_expression158)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreCompiler.g:33:13: ( ID )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == ID) :
                            LA6_2 = self.input.LA(2)

                            if ((ADD <= LA6_2 <= APPLICATION) or LA6_2 == CASE or LA6_2 == DIV or (EQ <= LA6_2 <= ID) or LA6_2 == LAMBDA or (LET <= LA6_2 <= LETREC) or (LT <= LA6_2 <= NEQ) or LA6_2 == NUMBER or (OR <= LA6_2 <= PACK)) :
                                alt6 = 1




                        if alt6 == 1:
                            # grammars/CoreCompiler.g:33:13: ID
                            pass 
                            self.match(self.input, ID, self.FOLLOW_ID_in_expression160)


                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression163)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 5:
                    # grammars/CoreCompiler.g:34:4: ^( MUL expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_expression171)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression173)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression176)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 6:
                    # grammars/CoreCompiler.g:35:4: ^( DIV expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_expression184)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression186)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression189)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 7:
                    # grammars/CoreCompiler.g:36:4: ^( ADD expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_expression197)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression199)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression202)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 8:
                    # grammars/CoreCompiler.g:37:4: ^( MIN expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, MIN, self.FOLLOW_MIN_in_expression210)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression212)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression215)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 9:
                    # grammars/CoreCompiler.g:38:4: ^( AND expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expression223)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression225)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression228)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 10:
                    # grammars/CoreCompiler.g:39:4: ^( OR expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expression236)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression238)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression241)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 11:
                    # grammars/CoreCompiler.g:40:4: ^( EQ expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_expression249)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression251)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression254)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 12:
                    # grammars/CoreCompiler.g:41:4: ^( NEQ expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, NEQ, self.FOLLOW_NEQ_in_expression262)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression264)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression267)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 13:
                    # grammars/CoreCompiler.g:42:4: ^( LT expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_expression275)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression277)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression280)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 14:
                    # grammars/CoreCompiler.g:43:4: ^( LTE expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, LTE, self.FOLLOW_LTE_in_expression288)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression290)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression293)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 15:
                    # grammars/CoreCompiler.g:44:4: ^( GT expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_expression301)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression303)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression306)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 16:
                    # grammars/CoreCompiler.g:45:4: ^( GTE expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, GTE, self.FOLLOW_GTE_in_expression314)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression316)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression319)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 17:
                    # grammars/CoreCompiler.g:46:4: ^( APPLICATION expression[info, env, code] expression[info, env.increment(), code] )
                    pass 
                    self.match(self.input, APPLICATION, self.FOLLOW_APPLICATION_in_expression327)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression329)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression332)
                    self.expression(info, env.increment(), code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                                                                                                          
                    code.Apply()
                    	
                    #action end



                elif alt7 == 18:
                    # grammars/CoreCompiler.g:49:4: basic[info, env, code]
                    pass 
                    self._state.following.append(self.FOLLOW_basic_in_expression341)
                    self.basic(info, env, code)

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "expression"



    # $ANTLR start "basic"
    # grammars/CoreCompiler.g:52:1: basic[info, env, code] : ( ID | NUMBER | ^( PACK NUMBER NUMBER ) );
    def basic(self, info, env, code):
        ID1 = None
        NUMBER2 = None

        try:
            try:
                # grammars/CoreCompiler.g:53:2: ( ID | NUMBER | ^( PACK NUMBER NUMBER ) )
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == ID:
                    alt8 = 1
                elif LA8 == NUMBER:
                    alt8 = 2
                elif LA8 == PACK:
                    alt8 = 3
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # grammars/CoreCompiler.g:53:4: ID
                    pass 
                    ID1 = self.match(self.input, ID, self.FOLLOW_ID_in_basic353)

                    #action start
                          
                    if ID1.text in info.combinators:
                    	code.PushGlobal(ID1.text)
                    else:
                    	code.Push(env.get(ID1.text), ID1.text)
                    	
                    #action end



                elif alt8 == 2:
                    # grammars/CoreCompiler.g:59:4: NUMBER
                    pass 
                    NUMBER2 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic360)

                    #action start
                              
                    code.PushInt(NUMBER2.text)
                    	
                    #action end



                elif alt8 == 3:
                    # grammars/CoreCompiler.g:62:4: ^( PACK NUMBER NUMBER )
                    pass 
                    self.match(self.input, PACK, self.FOLLOW_PACK_in_basic368)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic370)

                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic372)

                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "basic"



    # $ANTLR start "alternative"
    # grammars/CoreCompiler.g:65:1: alternative : ^( ARROW NUMBER expression[info, env, code] ) ;
    def alternative(self, ):
        try:
            try:
                # grammars/CoreCompiler.g:66:2: ( ^( ARROW NUMBER expression[info, env, code] ) )
                # grammars/CoreCompiler.g:66:4: ^( ARROW NUMBER expression[info, env, code] )
                pass 
                self.match(self.input, ARROW, self.FOLLOW_ARROW_in_alternative384)

                self.match(self.input, DOWN, None)
                self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_alternative386)

                self._state.following.append(self.FOLLOW_expression_in_alternative388)
                self.expression(info, env, code)

                self._state.following.pop()

                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "alternative"



    # $ANTLR start "definition"
    # grammars/CoreCompiler.g:69:1: definition : ^( IS ID expression[info, env, code] ) ;
    def definition(self, ):
        try:
            try:
                # grammars/CoreCompiler.g:70:2: ( ^( IS ID expression[info, env, code] ) )
                # grammars/CoreCompiler.g:70:4: ^( IS ID expression[info, env, code] )
                pass 
                self.match(self.input, IS, self.FOLLOW_IS_in_definition401)

                self.match(self.input, DOWN, None)
                self.match(self.input, ID, self.FOLLOW_ID_in_definition403)

                self._state.following.append(self.FOLLOW_expression_in_definition405)
                self.expression(info, env, code)

                self._state.following.pop()

                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "definition"



 

    FOLLOW_combinator_in_start68 = frozenset([1, 10])
    FOLLOW_COMBINATOR_in_combinator87 = frozenset([2])
    FOLLOW_ID_in_combinator91 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_ID_in_combinator96 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_combinator103 = frozenset([3])
    FOLLOW_LET_in_expression119 = frozenset([2])
    FOLLOW_definition_in_expression121 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression124 = frozenset([3])
    FOLLOW_LETREC_in_expression132 = frozenset([2])
    FOLLOW_definition_in_expression134 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression137 = frozenset([3])
    FOLLOW_CASE_in_expression145 = frozenset([2])
    FOLLOW_expression_in_expression147 = frozenset([7])
    FOLLOW_alternative_in_expression150 = frozenset([3, 7])
    FOLLOW_LAMBDA_in_expression158 = frozenset([2])
    FOLLOW_ID_in_expression160 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression163 = frozenset([3])
    FOLLOW_MUL_in_expression171 = frozenset([2])
    FOLLOW_expression_in_expression173 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression176 = frozenset([3])
    FOLLOW_DIV_in_expression184 = frozenset([2])
    FOLLOW_expression_in_expression186 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression189 = frozenset([3])
    FOLLOW_ADD_in_expression197 = frozenset([2])
    FOLLOW_expression_in_expression199 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression202 = frozenset([3])
    FOLLOW_MIN_in_expression210 = frozenset([2])
    FOLLOW_expression_in_expression212 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression215 = frozenset([3])
    FOLLOW_AND_in_expression223 = frozenset([2])
    FOLLOW_expression_in_expression225 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression228 = frozenset([3])
    FOLLOW_OR_in_expression236 = frozenset([2])
    FOLLOW_expression_in_expression238 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression241 = frozenset([3])
    FOLLOW_EQ_in_expression249 = frozenset([2])
    FOLLOW_expression_in_expression251 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression254 = frozenset([3])
    FOLLOW_NEQ_in_expression262 = frozenset([2])
    FOLLOW_expression_in_expression264 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression267 = frozenset([3])
    FOLLOW_LT_in_expression275 = frozenset([2])
    FOLLOW_expression_in_expression277 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression280 = frozenset([3])
    FOLLOW_LTE_in_expression288 = frozenset([2])
    FOLLOW_expression_in_expression290 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression293 = frozenset([3])
    FOLLOW_GT_in_expression301 = frozenset([2])
    FOLLOW_expression_in_expression303 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression306 = frozenset([3])
    FOLLOW_GTE_in_expression314 = frozenset([2])
    FOLLOW_expression_in_expression316 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression319 = frozenset([3])
    FOLLOW_APPLICATION_in_expression327 = frozenset([2])
    FOLLOW_expression_in_expression329 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression332 = frozenset([3])
    FOLLOW_basic_in_expression341 = frozenset([1])
    FOLLOW_ID_in_basic353 = frozenset([1])
    FOLLOW_NUMBER_in_basic360 = frozenset([1])
    FOLLOW_PACK_in_basic368 = frozenset([2])
    FOLLOW_NUMBER_in_basic370 = frozenset([32])
    FOLLOW_NUMBER_in_basic372 = frozenset([3])
    FOLLOW_ARROW_in_alternative384 = frozenset([2])
    FOLLOW_NUMBER_in_alternative386 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_alternative388 = frozenset([3])
    FOLLOW_IS_in_definition401 = frozenset([2])
    FOLLOW_ID_in_definition403 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_definition405 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(CoreCompiler)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
