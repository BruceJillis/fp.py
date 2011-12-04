# $ANTLR 3.4 grammars/CoreAnalyzer.g 2011-12-04 14:47:50

import sys
from antlr3 import *
from antlr3.tree import *

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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "AND", "APPLICATION", "ARROW", "CASE", "COLON", "COMBINATOR", 
    "COMMA", "COMMENT", "DIV", "DOT", "EQ", "GT", "GTE", "ID", "IN", "IS", 
    "LAMBDA", "LCURLY", "LET", "LETREC", "LPAREN", "LT", "LTE", "MIN", "MUL", 
    "NEQ", "NOT", "NUMBER", "OF", "OR", "PACK", "RCURLY", "RPAREN", "SCOLON", 
    "WHITESPACE"
]




class CoreAnalyzer(TreeParser):
    grammarFileName = "grammars/CoreAnalyzer.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(CoreAnalyzer, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # grammars/CoreAnalyzer.g:10:1: start[info] : ( combinator[info] )+ ;
    def start(self, info):
        try:
            try:
                # grammars/CoreAnalyzer.g:11:2: ( ( combinator[info] )+ )
                # grammars/CoreAnalyzer.g:11:4: ( combinator[info] )+
                pass 
                # grammars/CoreAnalyzer.g:11:4: ( combinator[info] )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == COMBINATOR) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammars/CoreAnalyzer.g:11:4: combinator[info]
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_start62)
                        self.combinator(info)

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
    # grammars/CoreAnalyzer.g:14:1: combinator[info] : ^( COMBINATOR name= ID (params+= ID )* expression[info] ) ;
    def combinator(self, info):
        name = None
        params = None
        list_params = None

        try:
            try:
                # grammars/CoreAnalyzer.g:15:2: ( ^( COMBINATOR name= ID (params+= ID )* expression[info] ) )
                # grammars/CoreAnalyzer.g:15:4: ^( COMBINATOR name= ID (params+= ID )* expression[info] )
                pass 
                self.match(self.input, COMBINATOR, self.FOLLOW_COMBINATOR_in_combinator76)

                self.match(self.input, DOWN, None)
                name = self.match(self.input, ID, self.FOLLOW_ID_in_combinator80)

                # grammars/CoreAnalyzer.g:15:25: (params+= ID )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        LA2_2 = self.input.LA(2)

                        if ((ADD <= LA2_2 <= APPLICATION) or LA2_2 == CASE or LA2_2 == DIV or (EQ <= LA2_2 <= ID) or LA2_2 == LAMBDA or (LET <= LA2_2 <= LETREC) or (LT <= LA2_2 <= NEQ) or LA2_2 == NUMBER or (OR <= LA2_2 <= PACK)) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/CoreAnalyzer.g:15:26: params+= ID
                        pass 
                        params = self.match(self.input, ID, self.FOLLOW_ID_in_combinator85)
                        if list_params is None:
                            list_params = []
                        list_params.append(params)



                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_expression_in_combinator89)
                self.expression(info)

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                                                                        
                info.combinator(name.text, list_params)
                	
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "combinator"



    # $ANTLR start "expression"
    # grammars/CoreAnalyzer.g:20:1: expression[info] : ( ^( LET ( definition )+ expression[info] ) | ^( LETREC ( definition )+ expression[info] ) | ^( CASE expression[info] ( alternative )+ ) | ^( LAMBDA ( ID )+ expression[info] ) | ^( MUL expression[info] expression[info] ) | ^( DIV expression[info] expression[info] ) | ^( ADD expression[info] expression[info] ) | ^( MIN expression[info] expression[info] ) | ^( AND expression[info] expression[info] ) | ^( OR expression[info] expression[info] ) | ^( EQ expression[info] expression[info] ) | ^( NEQ expression[info] expression[info] ) | ^( LT expression[info] expression[info] ) | ^( LTE expression[info] expression[info] ) | ^( GT expression[info] expression[info] ) | ^( GTE expression[info] expression[info] ) | ^( APPLICATION expression[info] expression[info] ) | basic[info] );
    def expression(self, info):
        try:
            try:
                # grammars/CoreAnalyzer.g:21:2: ( ^( LET ( definition )+ expression[info] ) | ^( LETREC ( definition )+ expression[info] ) | ^( CASE expression[info] ( alternative )+ ) | ^( LAMBDA ( ID )+ expression[info] ) | ^( MUL expression[info] expression[info] ) | ^( DIV expression[info] expression[info] ) | ^( ADD expression[info] expression[info] ) | ^( MIN expression[info] expression[info] ) | ^( AND expression[info] expression[info] ) | ^( OR expression[info] expression[info] ) | ^( EQ expression[info] expression[info] ) | ^( NEQ expression[info] expression[info] ) | ^( LT expression[info] expression[info] ) | ^( LTE expression[info] expression[info] ) | ^( GT expression[info] expression[info] ) | ^( GTE expression[info] expression[info] ) | ^( APPLICATION expression[info] expression[info] ) | basic[info] )
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
                    # grammars/CoreAnalyzer.g:21:4: ^( LET ( definition )+ expression[info] )
                    pass 
                    self.match(self.input, LET, self.FOLLOW_LET_in_expression105)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreAnalyzer.g:21:10: ( definition )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == IS) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammars/CoreAnalyzer.g:21:10: definition
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression107)
                            self.definition()

                            self._state.following.pop()


                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression110)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 2:
                    # grammars/CoreAnalyzer.g:22:4: ^( LETREC ( definition )+ expression[info] )
                    pass 
                    self.match(self.input, LETREC, self.FOLLOW_LETREC_in_expression118)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreAnalyzer.g:22:13: ( definition )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == IS) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammars/CoreAnalyzer.g:22:13: definition
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression120)
                            self.definition()

                            self._state.following.pop()


                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression123)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 3:
                    # grammars/CoreAnalyzer.g:23:4: ^( CASE expression[info] ( alternative )+ )
                    pass 
                    self.match(self.input, CASE, self.FOLLOW_CASE_in_expression131)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression133)
                    self.expression(info)

                    self._state.following.pop()

                    # grammars/CoreAnalyzer.g:23:28: ( alternative )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == ARROW) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammars/CoreAnalyzer.g:23:28: alternative
                            pass 
                            self._state.following.append(self.FOLLOW_alternative_in_expression136)
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
                    # grammars/CoreAnalyzer.g:24:4: ^( LAMBDA ( ID )+ expression[info] )
                    pass 
                    self.match(self.input, LAMBDA, self.FOLLOW_LAMBDA_in_expression144)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreAnalyzer.g:24:13: ( ID )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == ID) :
                            LA6_2 = self.input.LA(2)

                            if ((ADD <= LA6_2 <= APPLICATION) or LA6_2 == CASE or LA6_2 == DIV or (EQ <= LA6_2 <= ID) or LA6_2 == LAMBDA or (LET <= LA6_2 <= LETREC) or (LT <= LA6_2 <= NEQ) or LA6_2 == NUMBER or (OR <= LA6_2 <= PACK)) :
                                alt6 = 1




                        if alt6 == 1:
                            # grammars/CoreAnalyzer.g:24:13: ID
                            pass 
                            self.match(self.input, ID, self.FOLLOW_ID_in_expression146)


                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression149)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 5:
                    # grammars/CoreAnalyzer.g:25:4: ^( MUL expression[info] expression[info] )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_expression157)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression159)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression162)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 6:
                    # grammars/CoreAnalyzer.g:26:4: ^( DIV expression[info] expression[info] )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_expression170)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression172)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression175)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 7:
                    # grammars/CoreAnalyzer.g:27:4: ^( ADD expression[info] expression[info] )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_expression183)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression185)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression188)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 8:
                    # grammars/CoreAnalyzer.g:28:4: ^( MIN expression[info] expression[info] )
                    pass 
                    self.match(self.input, MIN, self.FOLLOW_MIN_in_expression196)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression198)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression201)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 9:
                    # grammars/CoreAnalyzer.g:29:4: ^( AND expression[info] expression[info] )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expression209)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression211)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression214)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 10:
                    # grammars/CoreAnalyzer.g:30:4: ^( OR expression[info] expression[info] )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expression222)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression224)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression227)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 11:
                    # grammars/CoreAnalyzer.g:31:4: ^( EQ expression[info] expression[info] )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_expression235)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression237)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression240)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 12:
                    # grammars/CoreAnalyzer.g:32:4: ^( NEQ expression[info] expression[info] )
                    pass 
                    self.match(self.input, NEQ, self.FOLLOW_NEQ_in_expression248)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression250)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression253)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 13:
                    # grammars/CoreAnalyzer.g:33:4: ^( LT expression[info] expression[info] )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_expression261)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression263)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression266)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 14:
                    # grammars/CoreAnalyzer.g:34:4: ^( LTE expression[info] expression[info] )
                    pass 
                    self.match(self.input, LTE, self.FOLLOW_LTE_in_expression274)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression276)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression279)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 15:
                    # grammars/CoreAnalyzer.g:35:4: ^( GT expression[info] expression[info] )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_expression287)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression289)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression292)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 16:
                    # grammars/CoreAnalyzer.g:36:4: ^( GTE expression[info] expression[info] )
                    pass 
                    self.match(self.input, GTE, self.FOLLOW_GTE_in_expression300)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression302)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression305)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 17:
                    # grammars/CoreAnalyzer.g:37:4: ^( APPLICATION expression[info] expression[info] )
                    pass 
                    self.match(self.input, APPLICATION, self.FOLLOW_APPLICATION_in_expression313)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression315)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression318)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 18:
                    # grammars/CoreAnalyzer.g:38:4: basic[info]
                    pass 
                    self._state.following.append(self.FOLLOW_basic_in_expression325)
                    self.basic(info)

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "expression"



    # $ANTLR start "basic"
    # grammars/CoreAnalyzer.g:41:1: basic[info] : ( ID | NUMBER | ^( PACK NUMBER NUMBER ) );
    def basic(self, info):
        try:
            try:
                # grammars/CoreAnalyzer.g:42:2: ( ID | NUMBER | ^( PACK NUMBER NUMBER ) )
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
                    # grammars/CoreAnalyzer.g:42:4: ID
                    pass 
                    self.match(self.input, ID, self.FOLLOW_ID_in_basic337)


                elif alt8 == 2:
                    # grammars/CoreAnalyzer.g:43:4: NUMBER
                    pass 
                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic342)


                elif alt8 == 3:
                    # grammars/CoreAnalyzer.g:44:4: ^( PACK NUMBER NUMBER )
                    pass 
                    self.match(self.input, PACK, self.FOLLOW_PACK_in_basic348)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic350)

                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic352)

                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "basic"



    # $ANTLR start "alternative"
    # grammars/CoreAnalyzer.g:47:1: alternative : ^( ARROW NUMBER expression[info] ) ;
    def alternative(self, ):
        try:
            try:
                # grammars/CoreAnalyzer.g:48:2: ( ^( ARROW NUMBER expression[info] ) )
                # grammars/CoreAnalyzer.g:48:4: ^( ARROW NUMBER expression[info] )
                pass 
                self.match(self.input, ARROW, self.FOLLOW_ARROW_in_alternative364)

                self.match(self.input, DOWN, None)
                self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_alternative366)

                self._state.following.append(self.FOLLOW_expression_in_alternative368)
                self.expression(info)

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
    # grammars/CoreAnalyzer.g:51:1: definition : ^( IS ID expression[info] ) ;
    def definition(self, ):
        try:
            try:
                # grammars/CoreAnalyzer.g:52:2: ( ^( IS ID expression[info] ) )
                # grammars/CoreAnalyzer.g:52:4: ^( IS ID expression[info] )
                pass 
                self.match(self.input, IS, self.FOLLOW_IS_in_definition381)

                self.match(self.input, DOWN, None)
                self.match(self.input, ID, self.FOLLOW_ID_in_definition383)

                self._state.following.append(self.FOLLOW_expression_in_definition385)
                self.expression(info)

                self._state.following.pop()

                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "definition"



 

    FOLLOW_combinator_in_start62 = frozenset([1, 10])
    FOLLOW_COMBINATOR_in_combinator76 = frozenset([2])
    FOLLOW_ID_in_combinator80 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_ID_in_combinator85 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_combinator89 = frozenset([3])
    FOLLOW_LET_in_expression105 = frozenset([2])
    FOLLOW_definition_in_expression107 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression110 = frozenset([3])
    FOLLOW_LETREC_in_expression118 = frozenset([2])
    FOLLOW_definition_in_expression120 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression123 = frozenset([3])
    FOLLOW_CASE_in_expression131 = frozenset([2])
    FOLLOW_expression_in_expression133 = frozenset([7])
    FOLLOW_alternative_in_expression136 = frozenset([3, 7])
    FOLLOW_LAMBDA_in_expression144 = frozenset([2])
    FOLLOW_ID_in_expression146 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression149 = frozenset([3])
    FOLLOW_MUL_in_expression157 = frozenset([2])
    FOLLOW_expression_in_expression159 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression162 = frozenset([3])
    FOLLOW_DIV_in_expression170 = frozenset([2])
    FOLLOW_expression_in_expression172 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression175 = frozenset([3])
    FOLLOW_ADD_in_expression183 = frozenset([2])
    FOLLOW_expression_in_expression185 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression188 = frozenset([3])
    FOLLOW_MIN_in_expression196 = frozenset([2])
    FOLLOW_expression_in_expression198 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression201 = frozenset([3])
    FOLLOW_AND_in_expression209 = frozenset([2])
    FOLLOW_expression_in_expression211 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression214 = frozenset([3])
    FOLLOW_OR_in_expression222 = frozenset([2])
    FOLLOW_expression_in_expression224 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression227 = frozenset([3])
    FOLLOW_EQ_in_expression235 = frozenset([2])
    FOLLOW_expression_in_expression237 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression240 = frozenset([3])
    FOLLOW_NEQ_in_expression248 = frozenset([2])
    FOLLOW_expression_in_expression250 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression253 = frozenset([3])
    FOLLOW_LT_in_expression261 = frozenset([2])
    FOLLOW_expression_in_expression263 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression266 = frozenset([3])
    FOLLOW_LTE_in_expression274 = frozenset([2])
    FOLLOW_expression_in_expression276 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression279 = frozenset([3])
    FOLLOW_GT_in_expression287 = frozenset([2])
    FOLLOW_expression_in_expression289 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression292 = frozenset([3])
    FOLLOW_GTE_in_expression300 = frozenset([2])
    FOLLOW_expression_in_expression302 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression305 = frozenset([3])
    FOLLOW_APPLICATION_in_expression313 = frozenset([2])
    FOLLOW_expression_in_expression315 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression318 = frozenset([3])
    FOLLOW_basic_in_expression325 = frozenset([1])
    FOLLOW_ID_in_basic337 = frozenset([1])
    FOLLOW_NUMBER_in_basic342 = frozenset([1])
    FOLLOW_PACK_in_basic348 = frozenset([2])
    FOLLOW_NUMBER_in_basic350 = frozenset([32])
    FOLLOW_NUMBER_in_basic352 = frozenset([3])
    FOLLOW_ARROW_in_alternative364 = frozenset([2])
    FOLLOW_NUMBER_in_alternative366 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_alternative368 = frozenset([3])
    FOLLOW_IS_in_definition381 = frozenset([2])
    FOLLOW_ID_in_definition383 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_definition385 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(CoreAnalyzer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
