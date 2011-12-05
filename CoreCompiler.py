# $ANTLR 3.4 grammars/CoreCompiler.g 2011-12-05 01:10:32

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
                # grammars/CoreCompiler.g:15:4: ( ( combinator[info, code] )+ )
                # grammars/CoreCompiler.g:15:6: ( combinator[info, code] )+
                pass 
                # grammars/CoreCompiler.g:15:6: ( combinator[info, code] )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == COMBINATOR) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammars/CoreCompiler.g:15:6: combinator[info, code]
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_start78)
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
                # grammars/CoreCompiler.g:19:4: ( ^( COMBINATOR n= ID (i= ID )* expression[info, env, code] ) )
                # grammars/CoreCompiler.g:19:7: ^( COMBINATOR n= ID (i= ID )* expression[info, env, code] )
                pass 
                #action start
                env = Environment() 
                #action end


                self.match(self.input, COMBINATOR, self.FOLLOW_COMBINATOR_in_combinator104)

                self.match(self.input, DOWN, None)
                n = self.match(self.input, ID, self.FOLLOW_ID_in_combinator108)

                #action start
                info.current = n.text
                #action end


                # grammars/CoreCompiler.g:20:50: (i= ID )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        LA2_2 = self.input.LA(2)

                        if ((ADD <= LA2_2 <= APPLICATION) or LA2_2 == CASE or LA2_2 == DIV or (EQ <= LA2_2 <= ID) or LA2_2 == LAMBDA or (LET <= LA2_2 <= LETREC) or (LT <= LA2_2 <= NEQ) or LA2_2 == NUMBER or (OR <= LA2_2 <= PACK)) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/CoreCompiler.g:20:51: i= ID
                        pass 
                        i = self.match(self.input, ID, self.FOLLOW_ID_in_combinator115)

                        #action start
                        env.add(i.text) 
                        #action end



                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_expression_in_combinator122)
                self.expression(info, env, code)

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                                                                                                                            
                code.Update(env.count())
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
    # grammars/CoreCompiler.g:28:1: expression[info, env, code] : ( ^( LET ( definition[info, tmp, code, True] )+ expression[info, env2, code] ) | ^( LETREC ( definition[info, env2, code, False] )+ expression[info, env2, code] ) | ^( CASE expression[info, env, code] ( alternative )+ ) | ^( LAMBDA ( ID )+ expression[info, env, code] ) | ^( MUL expression[info, env, code] expression[info, env, code] ) | ^( DIV expression[info, env, code] expression[info, env, code] ) | ^( ADD expression[info, env, code] expression[info, env, code] ) | ^( MIN expression[info, env, code] expression[info, env, code] ) | ^( AND expression[info, env, code] expression[info, env, code] ) | ^( OR expression[info, env, code] expression[info, env, code] ) | ^( EQ expression[info, env, code] expression[info, env, code] ) | ^( NEQ expression[info, env, code] expression[info, env, code] ) | ^( LT expression[info, env, code] expression[info, env, code] ) | ^( LTE expression[info, env, code] expression[info, env, code] ) | ^( GT expression[info, env, code] expression[info, env, code] ) | ^( GTE expression[info, env, code] expression[info, env, code] ) | ^( APPLICATION expression[info, env, code] expression[info, env.increment(), code] ) | basic[info, env, code] );
    def expression(self, info, env, code):
        try:
            try:
                # grammars/CoreCompiler.g:29:4: ( ^( LET ( definition[info, tmp, code, True] )+ expression[info, env2, code] ) | ^( LETREC ( definition[info, env2, code, False] )+ expression[info, env2, code] ) | ^( CASE expression[info, env, code] ( alternative )+ ) | ^( LAMBDA ( ID )+ expression[info, env, code] ) | ^( MUL expression[info, env, code] expression[info, env, code] ) | ^( DIV expression[info, env, code] expression[info, env, code] ) | ^( ADD expression[info, env, code] expression[info, env, code] ) | ^( MIN expression[info, env, code] expression[info, env, code] ) | ^( AND expression[info, env, code] expression[info, env, code] ) | ^( OR expression[info, env, code] expression[info, env, code] ) | ^( EQ expression[info, env, code] expression[info, env, code] ) | ^( NEQ expression[info, env, code] expression[info, env, code] ) | ^( LT expression[info, env, code] expression[info, env, code] ) | ^( LTE expression[info, env, code] expression[info, env, code] ) | ^( GT expression[info, env, code] expression[info, env, code] ) | ^( GTE expression[info, env, code] expression[info, env, code] ) | ^( APPLICATION expression[info, env, code] expression[info, env.increment(), code] ) | basic[info, env, code] )
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
                    # grammars/CoreCompiler.g:29:6: ^( LET ( definition[info, tmp, code, True] )+ expression[info, env2, code] )
                    pass 
                    #action start
                          
                    n = 0
                    tmp = env.increment(0)
                       
                    #action end


                    self.match(self.input, LET, self.FOLLOW_LET_in_expression149)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreCompiler.g:34:13: ( definition[info, tmp, code, True] )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == IS) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammars/CoreCompiler.g:34:14: definition[info, tmp, code, True]
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression165)
                            self.definition(info, tmp, code, True)

                            self._state.following.pop()

                            #action start
                            n += 1; tmp = tmp.increment() 
                            #action end



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    #action start
                                 
                    n -= 1
                    nn = n + 1
                    env2 = env.increment(n + 1)
                    for m in tmp.mapping:
                       if m in env.mapping:
                          continue;
                       env2.addat(m, n)
                       n -= 1
                                
                    #action end


                    self._state.following.append(self.FOLLOW_expression_in_expression199)
                    self.expression(info, env2, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                                                              
                    code.Slide(nn)
                       
                    #action end



                elif alt7 == 2:
                    # grammars/CoreCompiler.g:48:6: ^( LETREC ( definition[info, env2, code, False] )+ expression[info, env2, code] )
                    pass 
                    #action start
                         
                    params = info.letrec(self.input.index())
                    n = len(params)
                    code.Alloc(n)
                    env2 = env.increment(n)
                    # bookkeeping for the environment
                    n_param = n - 1
                    for p in params:
                       env2.addat(p, n_param)
                       n_param -= 1
                    # bookkeeping for the updates of the local variable of the letrec
                    n_update = n - 1
                       
                    #action end


                    self.match(self.input, LETREC, self.FOLLOW_LETREC_in_expression218)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreCompiler.g:62:10: ( definition[info, env2, code, False] )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == IS) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammars/CoreCompiler.g:62:11: definition[info, env2, code, False]
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_expression231)
                            self.definition(info, env2, code, False)

                            self._state.following.pop()

                            #action start
                            code.Update(n_update); n_update -= 1
                            #action end



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression249)
                    self.expression(info, env2, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                            
                    code.Slide(n)
                       
                    #action end



                elif alt7 == 3:
                    # grammars/CoreCompiler.g:67:6: ^( CASE expression[info, env, code] ( alternative )+ )
                    pass 
                    self.match(self.input, CASE, self.FOLLOW_CASE_in_expression268)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression270)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    # grammars/CoreCompiler.g:67:41: ( alternative )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == ARROW) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammars/CoreCompiler.g:67:41: alternative
                            pass 
                            self._state.following.append(self.FOLLOW_alternative_in_expression273)
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
                    # grammars/CoreCompiler.g:68:6: ^( LAMBDA ( ID )+ expression[info, env, code] )
                    pass 
                    self.match(self.input, LAMBDA, self.FOLLOW_LAMBDA_in_expression283)

                    self.match(self.input, DOWN, None)
                    # grammars/CoreCompiler.g:68:15: ( ID )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == ID) :
                            LA6_2 = self.input.LA(2)

                            if ((ADD <= LA6_2 <= APPLICATION) or LA6_2 == CASE or LA6_2 == DIV or (EQ <= LA6_2 <= ID) or LA6_2 == LAMBDA or (LET <= LA6_2 <= LETREC) or (LT <= LA6_2 <= NEQ) or LA6_2 == NUMBER or (OR <= LA6_2 <= PACK)) :
                                alt6 = 1




                        if alt6 == 1:
                            # grammars/CoreCompiler.g:68:15: ID
                            pass 
                            self.match(self.input, ID, self.FOLLOW_ID_in_expression285)


                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    self._state.following.append(self.FOLLOW_expression_in_expression288)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 5:
                    # grammars/CoreCompiler.g:69:6: ^( MUL expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, MUL, self.FOLLOW_MUL_in_expression298)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression300)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression303)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 6:
                    # grammars/CoreCompiler.g:70:6: ^( DIV expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, DIV, self.FOLLOW_DIV_in_expression313)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression315)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression318)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 7:
                    # grammars/CoreCompiler.g:71:6: ^( ADD expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, ADD, self.FOLLOW_ADD_in_expression328)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression330)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression333)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 8:
                    # grammars/CoreCompiler.g:72:6: ^( MIN expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, MIN, self.FOLLOW_MIN_in_expression343)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression345)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression348)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 9:
                    # grammars/CoreCompiler.g:73:6: ^( AND expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expression358)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression360)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression363)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 10:
                    # grammars/CoreCompiler.g:74:6: ^( OR expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expression373)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression375)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression378)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 11:
                    # grammars/CoreCompiler.g:75:6: ^( EQ expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, EQ, self.FOLLOW_EQ_in_expression388)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression390)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression393)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 12:
                    # grammars/CoreCompiler.g:76:6: ^( NEQ expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, NEQ, self.FOLLOW_NEQ_in_expression403)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression405)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression408)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 13:
                    # grammars/CoreCompiler.g:77:6: ^( LT expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, LT, self.FOLLOW_LT_in_expression418)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression420)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression423)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 14:
                    # grammars/CoreCompiler.g:78:6: ^( LTE expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, LTE, self.FOLLOW_LTE_in_expression433)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression435)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression438)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 15:
                    # grammars/CoreCompiler.g:79:6: ^( GT expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, GT, self.FOLLOW_GT_in_expression448)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression450)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression453)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 16:
                    # grammars/CoreCompiler.g:80:6: ^( GTE expression[info, env, code] expression[info, env, code] )
                    pass 
                    self.match(self.input, GTE, self.FOLLOW_GTE_in_expression463)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression465)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression468)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                elif alt7 == 17:
                    # grammars/CoreCompiler.g:81:6: ^( APPLICATION expression[info, env, code] expression[info, env.increment(), code] )
                    pass 
                    self.match(self.input, APPLICATION, self.FOLLOW_APPLICATION_in_expression478)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expression_in_expression480)
                    self.expression(info, env, code)

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expression_in_expression483)
                    self.expression(info, env.increment(), code)

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                                                                                                            
                    code.Apply()
                       
                    #action end



                elif alt7 == 18:
                    # grammars/CoreCompiler.g:84:6: basic[info, env, code]
                    pass 
                    self._state.following.append(self.FOLLOW_basic_in_expression494)
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
    # grammars/CoreCompiler.g:87:1: basic[info, env, code] : ( ID | NUMBER | ^( PACK NUMBER NUMBER ) );
    def basic(self, info, env, code):
        ID1 = None
        NUMBER2 = None

        try:
            try:
                # grammars/CoreCompiler.g:88:4: ( ID | NUMBER | ^( PACK NUMBER NUMBER ) )
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
                    # grammars/CoreCompiler.g:88:6: ID
                    pass 
                    ID1 = self.match(self.input, ID, self.FOLLOW_ID_in_basic508)

                    #action start
                            
                    if ID1.text in info.combinators:
                       code.PushGlobal(ID1.text)
                    else:
                       code.Push(env.get(ID1.text), ID1.text)
                       
                    #action end



                elif alt8 == 2:
                    # grammars/CoreCompiler.g:94:6: NUMBER
                    pass 
                    NUMBER2 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic517)

                    #action start
                                
                    code.PushInt(NUMBER2.text)
                       
                    #action end



                elif alt8 == 3:
                    # grammars/CoreCompiler.g:97:6: ^( PACK NUMBER NUMBER )
                    pass 
                    self.match(self.input, PACK, self.FOLLOW_PACK_in_basic527)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic529)

                    self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_basic531)

                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "basic"



    # $ANTLR start "alternative"
    # grammars/CoreCompiler.g:100:1: alternative : ^( ARROW NUMBER expression[info, env, code] ) ;
    def alternative(self, ):
        try:
            try:
                # grammars/CoreCompiler.g:101:4: ( ^( ARROW NUMBER expression[info, env, code] ) )
                # grammars/CoreCompiler.g:101:6: ^( ARROW NUMBER expression[info, env, code] )
                pass 
                self.match(self.input, ARROW, self.FOLLOW_ARROW_in_alternative545)

                self.match(self.input, DOWN, None)
                self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_alternative547)

                self._state.following.append(self.FOLLOW_expression_in_alternative549)
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
    # grammars/CoreCompiler.g:104:1: definition[info, env, code, record] : ^( IS ID expression[info, env, code] ) ;
    def definition(self, info, env, code, record):
        ID3 = None

        try:
            try:
                # grammars/CoreCompiler.g:105:4: ( ^( IS ID expression[info, env, code] ) )
                # grammars/CoreCompiler.g:105:6: ^( IS ID expression[info, env, code] )
                pass 
                self.match(self.input, IS, self.FOLLOW_IS_in_definition565)

                self.match(self.input, DOWN, None)
                ID3 = self.match(self.input, ID, self.FOLLOW_ID_in_definition567)

                self._state.following.append(self.FOLLOW_expression_in_definition569)
                self.expression(info, env, code)

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                                                          
                if record:
                   env.add(ID3.text)
                   
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "definition"



 

    FOLLOW_combinator_in_start78 = frozenset([1, 10])
    FOLLOW_COMBINATOR_in_combinator104 = frozenset([2])
    FOLLOW_ID_in_combinator108 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_ID_in_combinator115 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_combinator122 = frozenset([3])
    FOLLOW_LET_in_expression149 = frozenset([2])
    FOLLOW_definition_in_expression165 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression199 = frozenset([3])
    FOLLOW_LETREC_in_expression218 = frozenset([2])
    FOLLOW_definition_in_expression231 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 20, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression249 = frozenset([3])
    FOLLOW_CASE_in_expression268 = frozenset([2])
    FOLLOW_expression_in_expression270 = frozenset([7])
    FOLLOW_alternative_in_expression273 = frozenset([3, 7])
    FOLLOW_LAMBDA_in_expression283 = frozenset([2])
    FOLLOW_ID_in_expression285 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression288 = frozenset([3])
    FOLLOW_MUL_in_expression298 = frozenset([2])
    FOLLOW_expression_in_expression300 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression303 = frozenset([3])
    FOLLOW_DIV_in_expression313 = frozenset([2])
    FOLLOW_expression_in_expression315 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression318 = frozenset([3])
    FOLLOW_ADD_in_expression328 = frozenset([2])
    FOLLOW_expression_in_expression330 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression333 = frozenset([3])
    FOLLOW_MIN_in_expression343 = frozenset([2])
    FOLLOW_expression_in_expression345 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression348 = frozenset([3])
    FOLLOW_AND_in_expression358 = frozenset([2])
    FOLLOW_expression_in_expression360 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression363 = frozenset([3])
    FOLLOW_OR_in_expression373 = frozenset([2])
    FOLLOW_expression_in_expression375 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression378 = frozenset([3])
    FOLLOW_EQ_in_expression388 = frozenset([2])
    FOLLOW_expression_in_expression390 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression393 = frozenset([3])
    FOLLOW_NEQ_in_expression403 = frozenset([2])
    FOLLOW_expression_in_expression405 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression408 = frozenset([3])
    FOLLOW_LT_in_expression418 = frozenset([2])
    FOLLOW_expression_in_expression420 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression423 = frozenset([3])
    FOLLOW_LTE_in_expression433 = frozenset([2])
    FOLLOW_expression_in_expression435 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression438 = frozenset([3])
    FOLLOW_GT_in_expression448 = frozenset([2])
    FOLLOW_expression_in_expression450 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression453 = frozenset([3])
    FOLLOW_GTE_in_expression463 = frozenset([2])
    FOLLOW_expression_in_expression465 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression468 = frozenset([3])
    FOLLOW_APPLICATION_in_expression478 = frozenset([2])
    FOLLOW_expression_in_expression480 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_expression483 = frozenset([3])
    FOLLOW_basic_in_expression494 = frozenset([1])
    FOLLOW_ID_in_basic508 = frozenset([1])
    FOLLOW_NUMBER_in_basic517 = frozenset([1])
    FOLLOW_PACK_in_basic527 = frozenset([2])
    FOLLOW_NUMBER_in_basic529 = frozenset([32])
    FOLLOW_NUMBER_in_basic531 = frozenset([3])
    FOLLOW_ARROW_in_alternative545 = frozenset([2])
    FOLLOW_NUMBER_in_alternative547 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_alternative549 = frozenset([3])
    FOLLOW_IS_in_definition565 = frozenset([2])
    FOLLOW_ID_in_definition567 = frozenset([4, 5, 6, 8, 13, 15, 16, 17, 18, 21, 23, 24, 26, 27, 28, 29, 30, 32, 34, 35])
    FOLLOW_expression_in_definition569 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(CoreCompiler)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
