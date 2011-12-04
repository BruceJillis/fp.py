# $ANTLR 3.4 grammars/CoreAnalyzer.g 2011-12-05 00:06:25

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
                # grammars/CoreAnalyzer.g:11:4: ( ( combinator[info] )+ )
                # grammars/CoreAnalyzer.g:11:6: ( combinator[info] )+
                pass 
                # grammars/CoreAnalyzer.g:11:6: ( combinator[info] )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == COMBINATOR) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammars/CoreAnalyzer.g:11:6: combinator[info]
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_start72)
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
    # grammars/CoreAnalyzer.g:14:1: combinator[info] : ^( COMBINATOR n= ID (p+= ID )* expression[info] ) ;
    def combinator(self, info):
        n = None
        p = None
        list_p = None

        try:
            try:
                # grammars/CoreAnalyzer.g:15:4: ( ^( COMBINATOR n= ID (p+= ID )* expression[info] ) )
                # grammars/CoreAnalyzer.g:15:6: ^( COMBINATOR n= ID (p+= ID )* expression[info] )
                pass 
                self.match(self.input, COMBINATOR, self.FOLLOW_COMBINATOR_in_combinator88)

                self.match(self.input, DOWN, None)
                n = self.match(self.input, ID, self.FOLLOW_ID_in_combinator92)

                #action start
                info.current = n.text
                #action end


                # grammars/CoreAnalyzer.g:15:49: (p+= ID )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        LA2_2 = self.input.LA(2)

                        if ((ADD <= LA2_2 <= APPLICATION) or LA2_2 == CASE or LA2_2 == DIV or (EQ <= LA2_2 <= ID) or LA2_2 == LAMBDA or (LET <= LA2_2 <= LETREC) or (LT <= LA2_2 <= NEQ) or LA2_2 == NUMBER or (OR <= LA2_2 <= PACK)) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/CoreAnalyzer.g:15:50: p+= ID
                        pass 
                        p = self.match(self.input, ID, self.FOLLOW_ID_in_combinator99)
                        if list_p is None:
                            list_p = []
                        list_p.append(p)



                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_expression_in_combinator103)
                self.expression(info)

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                                                                                           
                info.combinator(n.text, list_p)
                   
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "combinator"



    # $ANTLR start "expression"
    # grammars/CoreAnalyzer.g:20:1: expression[info] : ( ^( LET ( definition[info, None] )+ expression[info] ) | ^( LETREC ( definition[info, index] )+ expression[info] ) | ^( CASE expression[info] ( alternative[info] )+ ) | ^( LAMBDA ( ID )+ expression[info] ) | ^( MUL expression[info] expression[info] ) | ^( DIV expression[info] expression[info] ) | ^( ADD expression[info] expression[info] ) | ^( MIN expression[info] expression[info] ) | ^( AND expression[info] expression[info] ) | ^( OR expression[info] expression[info] ) | ^( EQ expression[info] expression[info] ) | ^( NEQ expression[info] expression[info] ) | ^( LT expression[info] expression[info] ) | ^( LTE expression[info] expression[info] ) | ^( GT expression[info] expression[info] ) | ^( GTE expression[info] expression[info] ) | ^( APPLICATION expression[info] expression[info] ) | basic[info] );
    def expression(self, info):
        try:
            try:
                # grammars/CoreAnalyzer.g:21:4: ( ^( LET ( definition[info, None] )+ expression[info] ) | ^( LETREC ( definition[info, index] )+ expression[info] ) | ^( CASE expression[info] ( alternative[info] )+ ) | ^( LAMBDA ( ID )+ expression[info] ) | ^( MUL expression[info] expression[info] ) | ^( DIV expression[info] expression[info] ) | ^( ADD expression[info] expression[info] ) | ^( MIN expression[info] expression[info] ) | ^( AND expression[info] expression[info] ) | ^( OR expression[info] expression[info] ) | ^( EQ expression[info] expression[info] ) | ^( NEQ expression[info] expression[info] ) | ^( LT expression[info] expression[info] ) | ^( LTE expression[info] expression[info] ) | ^( GT expression[info] expression[info] ) | ^( GTE expression[info] expression[info] ) | ^( APPLICATION expression[info] expression[info] ) | basic[info] )
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
                    # grammars/CoreAnalyzer.g:21:6: ^( LET ( definition[info, None] )+ expression[info] )
                    pass 
                    self.match(self.input, LET, self.FOLLOW_LET_in_expression121)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreAnalyzer.g:21:12: ( definition[info, None] )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == IS) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammars/CoreAnalyzer.g:21:12: definition[info, None]
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression123)
                            self.definition(info, None)

                            self._state.following.pop()


                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression127)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 2:
                    # grammars/CoreAnalyzer.g:22:6: ^( LETREC ( definition[info, index] )+ expression[info] )
                    pass 
                    #action start
                         
                    index = self.input.index()
                    print index
                       
                    #action end


                    self.match(self.input, LETREC, self.FOLLOW_LETREC_in_expression144)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreAnalyzer.g:26:15: ( definition[info, index] )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == IS) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammars/CoreAnalyzer.g:26:16: definition[info, index]
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression147)
                            self.definition(info, index)

                            self._state.following.pop()


                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression152)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 3:
                    # grammars/CoreAnalyzer.g:27:6: ^( CASE expression[info] ( alternative[info] )+ )
                    pass 
                    self.match(self.input, CASE, self.FOLLOW_CASE_in_expression162)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression164)
                    self.expression(info)

                    self._state.following.pop()

                    # grammars/CoreAnalyzer.g:27:30: ( alternative[info] )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == ARROW) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammars/CoreAnalyzer.g:27:30: alternative[info]
                            pass 
                            self._state.following.append(self.FOLLOW_alternative_in_expression167)
                            self.alternative(info)

                            self._state.following.pop()


                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    self.match(self.input, UP, None)



                elif alt7 == 4:
                    # grammars/CoreAnalyzer.g:28:6: ^( LAMBDA ( ID )+ expression[info] )
                    pass 
                    self.match(self.input, LAMBDA, self.FOLLOW_LAMBDA_in_expression178)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreAnalyzer.g:28:15: ( ID )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == ID) :
                            LA6_2 = self.input.LA(2)

                            if ((ADD <= LA6_2 <= APPLICATION) or LA6_2 == CASE or LA6_2 == DIV or (EQ <= LA6_2 <= ID) or LA6_2 == LAMBDA or (LET <= LA6_2 <= LETREC) or (LT <= LA6_2 <= NEQ) or LA6_2 == NUMBER or (OR <= LA6_2 <= PACK)) :
                                alt6 = 1




                        if alt6 == 1:
                            # grammars/CoreAnalyzer.g:28:15: ID
                            pass 
                            self.match(self.input, ID, self.FOLLOW_ID_in_expression180)


                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression183)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 5:
                    # grammars/CoreAnalyzer.g:29:6: ^( MUL expression[info] expression[info] )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_expression193)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression195)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression198)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 6:
                    # grammars/CoreAnalyzer.g:30:6: ^( DIV expression[info] expression[info] )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_expression208)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression210)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression213)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 7:
                    # grammars/CoreAnalyzer.g:31:6: ^( ADD expression[info] expression[info] )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_expression223)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression225)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression228)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 8:
                    # grammars/CoreAnalyzer.g:32:6: ^( MIN expression[info] expression[info] )
                    pass 
                    self.match(self.input, MIN, self.FOLLOW_MIN_in_expression238)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression240)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression243)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 9:
                    # grammars/CoreAnalyzer.g:33:6: ^( AND expression[info] expression[info] )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expression253)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression255)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression258)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 10:
                    # grammars/CoreAnalyzer.g:34:6: ^( OR expression[info] expression[info] )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expression268)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression270)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression273)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 11:
                    # grammars/CoreAnalyzer.g:35:6: ^( EQ expression[info] expression[info] )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_expression283)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression285)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression288)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 12:
                    # grammars/CoreAnalyzer.g:36:6: ^( NEQ expression[info] expression[info] )
                    pass 
                    self.match(self.input, NEQ, self.FOLLOW_NEQ_in_expression298)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression300)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression303)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 13:
                    # grammars/CoreAnalyzer.g:37:6: ^( LT expression[info] expression[info] )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_expression313)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression315)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression318)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 14:
                    # grammars/CoreAnalyzer.g:38:6: ^( LTE expression[info] expression[info] )
                    pass 
                    self.match(self.input, LTE, self.FOLLOW_LTE_in_expression328)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression330)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression333)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 15:
                    # grammars/CoreAnalyzer.g:39:6: ^( GT expression[info] expression[info] )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_expression343)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression345)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression348)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 16:
                    # grammars/CoreAnalyzer.g:40:6: ^( GTE expression[info] expression[info] )
                    pass 
                    self.match(self.input, GTE, self.FOLLOW_GTE_in_expression358)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression360)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression363)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 17:
                    # grammars/CoreAnalyzer.g:41:6: ^( APPLICATION expression[info] expression[info] )
                    pass 
                    self.match(self.input, APPLICATION, self.FOLLOW_APPLICATION_in_expression373)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression375)
                    self.expression(info)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression378)
                    self.expression(info)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 18:
                    # grammars/CoreAnalyzer.g:42:6: basic[info]
                    pass 
                    self._state.following.append(self.FOLLOW_basic_in_expression387)
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
    # grammars/CoreAnalyzer.g:45:1: basic[info] : ( ID | NUMBER | ^( PACK NUMBER NUMBER ) );
    def basic(self, info):
        try:
            try:
                # grammars/CoreAnalyzer.g:46:4: ( ID | NUMBER | ^( PACK NUMBER NUMBER ) )
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
                    # grammars/CoreAnalyzer.g:46:6: ID
                    pass 
                    self.match(self.input, ID, self.FOLLOW_ID_in_basic401)


                elif alt8 == 2:
                    # grammars/CoreAnalyzer.g:47:6: NUMBER
                    pass 
                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic408)


                elif alt8 == 3:
                    # grammars/CoreAnalyzer.g:48:6: ^( PACK NUMBER NUMBER )
                    pass 
                    self.match(self.input, PACK, self.FOLLOW_PACK_in_basic416)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic418)

                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic420)

                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "basic"



    # $ANTLR start "alternative"
    # grammars/CoreAnalyzer.g:51:1: alternative[info] : ^( ARROW NUMBER expression[info] ) ;
    def alternative(self, info):
        try:
            try:
                # grammars/CoreAnalyzer.g:52:4: ( ^( ARROW NUMBER expression[info] ) )
                # grammars/CoreAnalyzer.g:52:6: ^( ARROW NUMBER expression[info] )
                pass 
                self.match(self.input, ARROW, self.FOLLOW_ARROW_in_alternative435)

                self.match(self.input, DOWN, None)
                self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_alternative437)

                self._state.following.append(self.FOLLOW_expression_in_alternative439)
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
    # grammars/CoreAnalyzer.g:55:1: definition[info, index] : ^( IS ID expression[info] ) ;
    def definition(self, info, index):
        ID1 = None

        try:
            try:
                # grammars/CoreAnalyzer.g:56:4: ( ^( IS ID expression[info] ) )
                # grammars/CoreAnalyzer.g:56:6: ^( IS ID expression[info] )
                pass 
                self.match(self.input, IS, self.FOLLOW_IS_in_definition455)

                self.match(self.input, DOWN, None)
                ID1 = self.match(self.input, ID, self.FOLLOW_ID_in_definition457)

                self._state.following.append(self.FOLLOW_expression_in_definition459)
                self.expression(info)

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                                               
                if index != None:
                   info.letrec(index, ID1.text)
                   
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "definition"



 

    FOLLOW_combinator_in_start72 = frozenset([1, 10])
    FOLLOW_COMBINATOR_in_combinator88 = frozenset([2])
    FOLLOW_ID_in_combinator92 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_ID_in_combinator99 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_combinator103 = frozenset([3])
    FOLLOW_LET_in_expression121 = frozenset([2])
    FOLLOW_definition_in_expression123 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression127 = frozenset([3])
    FOLLOW_LETREC_in_expression144 = frozenset([2])
    FOLLOW_definition_in_expression147 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression152 = frozenset([3])
    FOLLOW_CASE_in_expression162 = frozenset([2])
    FOLLOW_expression_in_expression164 = frozenset([7])
    FOLLOW_alternative_in_expression167 = frozenset([3, 7])
    FOLLOW_LAMBDA_in_expression178 = frozenset([2])
    FOLLOW_ID_in_expression180 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression183 = frozenset([3])
    FOLLOW_MUL_in_expression193 = frozenset([2])
    FOLLOW_expression_in_expression195 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression198 = frozenset([3])
    FOLLOW_DIV_in_expression208 = frozenset([2])
    FOLLOW_expression_in_expression210 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression213 = frozenset([3])
    FOLLOW_ADD_in_expression223 = frozenset([2])
    FOLLOW_expression_in_expression225 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression228 = frozenset([3])
    FOLLOW_MIN_in_expression238 = frozenset([2])
    FOLLOW_expression_in_expression240 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression243 = frozenset([3])
    FOLLOW_AND_in_expression253 = frozenset([2])
    FOLLOW_expression_in_expression255 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression258 = frozenset([3])
    FOLLOW_OR_in_expression268 = frozenset([2])
    FOLLOW_expression_in_expression270 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression273 = frozenset([3])
    FOLLOW_EQ_in_expression283 = frozenset([2])
    FOLLOW_expression_in_expression285 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression288 = frozenset([3])
    FOLLOW_NEQ_in_expression298 = frozenset([2])
    FOLLOW_expression_in_expression300 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression303 = frozenset([3])
    FOLLOW_LT_in_expression313 = frozenset([2])
    FOLLOW_expression_in_expression315 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression318 = frozenset([3])
    FOLLOW_LTE_in_expression328 = frozenset([2])
    FOLLOW_expression_in_expression330 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression333 = frozenset([3])
    FOLLOW_GT_in_expression343 = frozenset([2])
    FOLLOW_expression_in_expression345 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression348 = frozenset([3])
    FOLLOW_GTE_in_expression358 = frozenset([2])
    FOLLOW_expression_in_expression360 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression363 = frozenset([3])
    FOLLOW_APPLICATION_in_expression373 = frozenset([2])
    FOLLOW_expression_in_expression375 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression378 = frozenset([3])
    FOLLOW_basic_in_expression387 = frozenset([1])
    FOLLOW_ID_in_basic401 = frozenset([1])
    FOLLOW_NUMBER_in_basic408 = frozenset([1])
    FOLLOW_PACK_in_basic416 = frozenset([2])
    FOLLOW_NUMBER_in_basic418 = frozenset([32])
    FOLLOW_NUMBER_in_basic420 = frozenset([3])
    FOLLOW_ARROW_in_alternative435 = frozenset([2])
    FOLLOW_NUMBER_in_alternative437 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_alternative439 = frozenset([3])
    FOLLOW_IS_in_definition455 = frozenset([2])
    FOLLOW_ID_in_definition457 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_definition459 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(CoreAnalyzer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
