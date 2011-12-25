# $ANTLR 3.4 grammars/Miranda.g 2011-12-25 16:11:36

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALPHANUMERIC", "AND", "CHAR", "COMMA", "COMMENT", "DEDENT", 
    "DEFINITION", "DIV", "DOT", "DOUBLE_QUOTE", "EQ", "FLOAT", "GT", "GTE", 
    "ID", "INT", "IS", "LPAREN", "LT", "LTE", "MIN", "MUL", "NEQ", "OR", 
    "RPAREN", "SINGLE_QUOTE", "STRING", "TUPLE", "WHITESPACE"
]




class MirandaParser(Parser):
    grammarFileName = "grammars/Miranda.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(MirandaParser, self).__init__(input, state, *args, **kwargs)

        self._state.ruleMemo = {}




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.program_return, self).__init__()

            self.tree = None





    # $ANTLR start "program"
    # grammars/Miranda.g:80:1: program : ( definition DEDENT !)* expression EOF !;
    def program(self, ):
        retval = self.program_return()
        retval.start = self.input.LT(1)

        program_StartIndex = self.input.index()

        root_0 = None

        DEDENT2 = None
        EOF4 = None
        definition1 = None

        expression3 = None


        DEDENT2_tree = None
        EOF4_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:80:8: ( ( definition DEDENT !)* expression EOF !)
                # grammars/Miranda.g:80:10: ( definition DEDENT !)* expression EOF !
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:80:10: ( definition DEDENT !)*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        LA1_1 = self.input.LA(2)

                        if (LA1_1 == IS) :
                            alt1 = 1




                    if alt1 == 1:
                        # grammars/Miranda.g:80:11: definition DEDENT !
                        pass 
                        self._state.following.append(self.FOLLOW_definition_in_program389)
                        definition1 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition1.tree)


                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_program391)


                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_expression_in_program396)
                expression3 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression3.tree)


                EOF4 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program398)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, program_StartIndex, success)


            pass
        return retval

    # $ANTLR end "program"


    class definition_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.definition_return, self).__init__()

            self.tree = None





    # $ANTLR start "definition"
    # grammars/Miranda.g:82:1: definition : ID IS expression -> ^( DEFINITION ID expression ) ;
    def definition(self, ):
        retval = self.definition_return()
        retval.start = self.input.LT(1)

        definition_StartIndex = self.input.index()

        root_0 = None

        ID5 = None
        IS6 = None
        expression7 = None


        ID5_tree = None
        IS6_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_IS = RewriteRuleTokenStream(self._adaptor, "token IS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:82:11: ( ID IS expression -> ^( DEFINITION ID expression ) )
                # grammars/Miranda.g:83:3: ID IS expression
                pass 
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_definition409) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID5)


                IS6 = self.match(self.input, IS, self.FOLLOW_IS_in_definition411) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS6)


                self._state.following.append(self.FOLLOW_expression_in_definition413)
                expression7 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression7.tree)


                # AST Rewrite
                # elements: expression, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 84:3: -> ^( DEFINITION ID expression )
                    # grammars/Miranda.g:84:6: ^( DEFINITION ID expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DEFINITION, "DEFINITION")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, definition_StartIndex, success)


            pass
        return retval

    # $ANTLR end "definition"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # grammars/Miranda.g:87:1: expression : expr1 ;
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        expr18 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:87:11: ( expr1 )
                # grammars/Miranda.g:87:13: expr1
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr1_in_expression433)
                expr18 = self.expr1()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr18.tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, expression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expression"


    class expr1_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr1_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr1"
    # grammars/Miranda.g:89:1: expr1 : expr2 ( OR ^ expression )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR10 = None
        expr29 = None

        expression11 = None


        OR10_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:89:6: ( expr2 ( OR ^ expression )* )
                # grammars/Miranda.g:89:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1440)
                expr29 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr29.tree)


                # grammars/Miranda.g:89:14: ( OR ^ expression )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OR) :
                        LA2_2 = self.input.LA(2)

                        if (self.synpred2_Miranda()) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/Miranda.g:89:15: OR ^ expression
                        pass 
                        OR10 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1443)
                        if self._state.backtracking == 0:
                            OR10_tree = self._adaptor.createWithPayload(OR10)
                            root_0 = self._adaptor.becomeRoot(OR10_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr1446)
                        expression11 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression11.tree)



                    else:
                        break #loop2




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, expr1_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr1"


    class expr2_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr2_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr2"
    # grammars/Miranda.g:91:1: expr2 : expr3 ( AND ^ expression )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND13 = None
        expr312 = None

        expression14 = None


        AND13_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:91:6: ( expr3 ( AND ^ expression )* )
                # grammars/Miranda.g:91:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2455)
                expr312 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr312.tree)


                # grammars/Miranda.g:91:14: ( AND ^ expression )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == AND) :
                        LA3_2 = self.input.LA(2)

                        if (self.synpred3_Miranda()) :
                            alt3 = 1




                    if alt3 == 1:
                        # grammars/Miranda.g:91:15: AND ^ expression
                        pass 
                        AND13 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2458)
                        if self._state.backtracking == 0:
                            AND13_tree = self._adaptor.createWithPayload(AND13)
                            root_0 = self._adaptor.becomeRoot(AND13_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr2461)
                        expression14 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression14.tree)



                    else:
                        break #loop3




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, expr2_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr2"


    class expr3_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr3_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr3"
    # grammars/Miranda.g:93:1: expr3 : expr4 ( relop ^ expression )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        expr415 = None

        relop16 = None

        expression17 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:93:6: ( expr4 ( relop ^ expression )* )
                # grammars/Miranda.g:93:8: expr4 ( relop ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3470)
                expr415 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr415.tree)


                # grammars/Miranda.g:93:14: ( relop ^ expression )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQ or (GT <= LA4_0 <= GTE) or (LT <= LA4_0 <= LTE) or LA4_0 == NEQ) :
                        LA4_2 = self.input.LA(2)

                        if (self.synpred4_Miranda()) :
                            alt4 = 1




                    if alt4 == 1:
                        # grammars/Miranda.g:93:15: relop ^ expression
                        pass 
                        self._state.following.append(self.FOLLOW_relop_in_expr3473)
                        relop16 = self.relop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(relop16.tree, root_0)


                        self._state.following.append(self.FOLLOW_expression_in_expr3476)
                        expression17 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression17.tree)



                    else:
                        break #loop4




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, expr3_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr3"


    class expr4_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr4_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr4"
    # grammars/Miranda.g:95:1: expr4 : expr5 ( ( ADD ^| MIN ^) expr5 )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD19 = None
        MIN20 = None
        expr518 = None

        expr521 = None


        ADD19_tree = None
        MIN20_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:95:6: ( expr5 ( ( ADD ^| MIN ^) expr5 )* )
                # grammars/Miranda.g:95:8: expr5 ( ( ADD ^| MIN ^) expr5 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4485)
                expr518 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr518.tree)


                # grammars/Miranda.g:95:14: ( ( ADD ^| MIN ^) expr5 )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == ADD or LA6_0 == MIN) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammars/Miranda.g:95:15: ( ADD ^| MIN ^) expr5
                        pass 
                        # grammars/Miranda.g:95:15: ( ADD ^| MIN ^)
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == ADD) :
                            alt5 = 1
                        elif (LA5_0 == MIN) :
                            alt5 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 5, 0, self.input)

                            raise nvae


                        if alt5 == 1:
                            # grammars/Miranda.g:95:16: ADD ^
                            pass 
                            ADD19 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4489)
                            if self._state.backtracking == 0:
                                ADD19_tree = self._adaptor.createWithPayload(ADD19)
                                root_0 = self._adaptor.becomeRoot(ADD19_tree, root_0)




                        elif alt5 == 2:
                            # grammars/Miranda.g:95:21: MIN ^
                            pass 
                            MIN20 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4492)
                            if self._state.backtracking == 0:
                                MIN20_tree = self._adaptor.createWithPayload(MIN20)
                                root_0 = self._adaptor.becomeRoot(MIN20_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr5_in_expr4496)
                        expr521 = self.expr5()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr521.tree)



                    else:
                        break #loop6




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, expr4_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr4"


    class expr5_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr5_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr5"
    # grammars/Miranda.g:97:1: expr5 : expr6 ( ( DIV ^| MUL ^) expr6 )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV23 = None
        MUL24 = None
        expr622 = None

        expr625 = None


        DIV23_tree = None
        MUL24_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:97:6: ( expr6 ( ( DIV ^| MUL ^) expr6 )* )
                # grammars/Miranda.g:97:8: expr6 ( ( DIV ^| MUL ^) expr6 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr5505)
                expr622 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr622.tree)


                # grammars/Miranda.g:97:14: ( ( DIV ^| MUL ^) expr6 )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == DIV or LA8_0 == MUL) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammars/Miranda.g:97:15: ( DIV ^| MUL ^) expr6
                        pass 
                        # grammars/Miranda.g:97:15: ( DIV ^| MUL ^)
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == DIV) :
                            alt7 = 1
                        elif (LA7_0 == MUL) :
                            alt7 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 7, 0, self.input)

                            raise nvae


                        if alt7 == 1:
                            # grammars/Miranda.g:97:16: DIV ^
                            pass 
                            DIV23 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5509)
                            if self._state.backtracking == 0:
                                DIV23_tree = self._adaptor.createWithPayload(DIV23)
                                root_0 = self._adaptor.becomeRoot(DIV23_tree, root_0)




                        elif alt7 == 2:
                            # grammars/Miranda.g:97:21: MUL ^
                            pass 
                            MUL24 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5512)
                            if self._state.backtracking == 0:
                                MUL24_tree = self._adaptor.createWithPayload(MUL24)
                                root_0 = self._adaptor.becomeRoot(MUL24_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr6_in_expr5516)
                        expr625 = self.expr6()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr625.tree)



                    else:
                        break #loop8




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, expr5_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr5"


    class expr6_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr6_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr6"
    # grammars/Miranda.g:99:1: expr6 : ( aexpr )+ ;
    def expr6(self, ):
        retval = self.expr6_return()
        retval.start = self.input.LT(1)

        expr6_StartIndex = self.input.index()

        root_0 = None

        aexpr26 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:99:6: ( ( aexpr )+ )
                # grammars/Miranda.g:99:8: ( aexpr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:99:8: ( aexpr )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == CHAR or LA9_0 == FLOAT or (ID <= LA9_0 <= INT) or LA9_0 == LPAREN or LA9_0 == STRING) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammars/Miranda.g:99:8: aexpr
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr6525)
                        aexpr26 = self.aexpr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, aexpr26.tree)



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, expr6_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr6"


    class aexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.aexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "aexpr"
    # grammars/Miranda.g:101:1: aexpr : ( ID | INT | FLOAT | CHAR | STRING | LPAREN ! expression RPAREN !| LPAREN expression ( COMMA expression )* RPAREN -> ^( TUPLE ( expression )* ) );
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID27 = None
        INT28 = None
        FLOAT29 = None
        CHAR30 = None
        STRING31 = None
        LPAREN32 = None
        RPAREN34 = None
        LPAREN35 = None
        COMMA37 = None
        RPAREN39 = None
        expression33 = None

        expression36 = None

        expression38 = None


        ID27_tree = None
        INT28_tree = None
        FLOAT29_tree = None
        CHAR30_tree = None
        STRING31_tree = None
        LPAREN32_tree = None
        RPAREN34_tree = None
        LPAREN35_tree = None
        COMMA37_tree = None
        RPAREN39_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:102:4: ( ID | INT | FLOAT | CHAR | STRING | LPAREN ! expression RPAREN !| LPAREN expression ( COMMA expression )* RPAREN -> ^( TUPLE ( expression )* ) )
                alt11 = 7
                LA11 = self.input.LA(1)
                if LA11 == ID:
                    alt11 = 1
                elif LA11 == INT:
                    alt11 = 2
                elif LA11 == FLOAT:
                    alt11 = 3
                elif LA11 == CHAR:
                    alt11 = 4
                elif LA11 == STRING:
                    alt11 = 5
                elif LA11 == LPAREN:
                    LA11_6 = self.input.LA(2)

                    if (self.synpred15_Miranda()) :
                        alt11 = 6
                    elif (True) :
                        alt11 = 7
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 11, 6, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # grammars/Miranda.g:102:6: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr537)
                    if self._state.backtracking == 0:
                        ID27_tree = self._adaptor.createWithPayload(ID27)
                        self._adaptor.addChild(root_0, ID27_tree)




                elif alt11 == 2:
                    # grammars/Miranda.g:103:6: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT28 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr544)
                    if self._state.backtracking == 0:
                        INT28_tree = self._adaptor.createWithPayload(INT28)
                        self._adaptor.addChild(root_0, INT28_tree)




                elif alt11 == 3:
                    # grammars/Miranda.g:104:5: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()


                    FLOAT29 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr550)
                    if self._state.backtracking == 0:
                        FLOAT29_tree = self._adaptor.createWithPayload(FLOAT29)
                        self._adaptor.addChild(root_0, FLOAT29_tree)




                elif alt11 == 4:
                    # grammars/Miranda.g:105:6: CHAR
                    pass 
                    root_0 = self._adaptor.nil()


                    CHAR30 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_aexpr557)
                    if self._state.backtracking == 0:
                        CHAR30_tree = self._adaptor.createWithPayload(CHAR30)
                        self._adaptor.addChild(root_0, CHAR30_tree)




                elif alt11 == 5:
                    # grammars/Miranda.g:106:6: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING31 = self.match(self.input, STRING, self.FOLLOW_STRING_in_aexpr564)
                    if self._state.backtracking == 0:
                        STRING31_tree = self._adaptor.createWithPayload(STRING31)
                        self._adaptor.addChild(root_0, STRING31_tree)




                elif alt11 == 6:
                    # grammars/Miranda.g:107:6: LPAREN ! expression RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN32 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr571)

                    self._state.following.append(self.FOLLOW_expression_in_aexpr574)
                    expression33 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression33.tree)


                    RPAREN34 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr576)


                elif alt11 == 7:
                    # grammars/Miranda.g:108:6: LPAREN expression ( COMMA expression )* RPAREN
                    pass 
                    LPAREN35 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr584) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN35)


                    self._state.following.append(self.FOLLOW_expression_in_aexpr586)
                    expression36 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression36.tree)


                    # grammars/Miranda.g:108:24: ( COMMA expression )*
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == COMMA) :
                            alt10 = 1


                        if alt10 == 1:
                            # grammars/Miranda.g:108:25: COMMA expression
                            pass 
                            COMMA37 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_aexpr589) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA37)


                            self._state.following.append(self.FOLLOW_expression_in_aexpr591)
                            expression38 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_expression.add(expression38.tree)



                        else:
                            break #loop10


                    RPAREN39 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr595) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN39)


                    # AST Rewrite
                    # elements: expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 109:6: -> ^( TUPLE ( expression )* )
                        # grammars/Miranda.g:109:9: ^( TUPLE ( expression )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TUPLE, "TUPLE")
                        , root_1)

                        # grammars/Miranda.g:109:17: ( expression )*
                        while stream_expression.hasNext():
                            self._adaptor.addChild(root_1, stream_expression.nextTree())


                        stream_expression.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class relop_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.relop_return, self).__init__()

            self.tree = None





    # $ANTLR start "relop"
    # grammars/Miranda.g:112:1: relop : ( LT | LTE | EQ | NEQ | GTE | GT );
    def relop(self, ):
        retval = self.relop_return()
        retval.start = self.input.LT(1)

        relop_StartIndex = self.input.index()

        root_0 = None

        set40 = None

        set40_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:112:6: ( LT | LTE | EQ | NEQ | GTE | GT )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set40 = self.input.LT(1)

                if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set40))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, relop_StartIndex, success)


            pass
        return retval

    # $ANTLR end "relop"

    # $ANTLR start "synpred2_Miranda"
    def synpred2_Miranda_fragment(self, ):
        # grammars/Miranda.g:89:15: ( OR expression )
        # grammars/Miranda.g:89:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred2_Miranda443)

        self._state.following.append(self.FOLLOW_expression_in_synpred2_Miranda446)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred2_Miranda"



    # $ANTLR start "synpred3_Miranda"
    def synpred3_Miranda_fragment(self, ):
        # grammars/Miranda.g:91:15: ( AND expression )
        # grammars/Miranda.g:91:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred3_Miranda458)

        self._state.following.append(self.FOLLOW_expression_in_synpred3_Miranda461)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred3_Miranda"



    # $ANTLR start "synpred4_Miranda"
    def synpred4_Miranda_fragment(self, ):
        # grammars/Miranda.g:93:15: ( relop expression )
        # grammars/Miranda.g:93:15: relop expression
        pass 
        self._state.following.append(self.FOLLOW_relop_in_synpred4_Miranda473)
        self.relop()

        self._state.following.pop()

        self._state.following.append(self.FOLLOW_expression_in_synpred4_Miranda476)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred4_Miranda"



    # $ANTLR start "synpred15_Miranda"
    def synpred15_Miranda_fragment(self, ):
        # grammars/Miranda.g:107:6: ( LPAREN expression RPAREN )
        # grammars/Miranda.g:107:6: LPAREN expression RPAREN
        pass 
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred15_Miranda571)

        self._state.following.append(self.FOLLOW_expression_in_synpred15_Miranda574)
        self.expression()

        self._state.following.pop()

        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred15_Miranda576)



    # $ANTLR end "synpred15_Miranda"




    def synpred2_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred3_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred3_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred15_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred4_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred4_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_definition_in_program389 = frozenset([10])
    FOLLOW_DEDENT_in_program391 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_program396 = frozenset([])
    FOLLOW_EOF_in_program398 = frozenset([1])
    FOLLOW_ID_in_definition409 = frozenset([21])
    FOLLOW_IS_in_definition411 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_definition413 = frozenset([1])
    FOLLOW_expr1_in_expression433 = frozenset([1])
    FOLLOW_expr2_in_expr1440 = frozenset([1, 28])
    FOLLOW_OR_in_expr1443 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_expr1446 = frozenset([1, 28])
    FOLLOW_expr3_in_expr2455 = frozenset([1, 6])
    FOLLOW_AND_in_expr2458 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_expr2461 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3470 = frozenset([1, 15, 17, 18, 23, 24, 27])
    FOLLOW_relop_in_expr3473 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_expr3476 = frozenset([1, 15, 17, 18, 23, 24, 27])
    FOLLOW_expr5_in_expr4485 = frozenset([1, 4, 25])
    FOLLOW_ADD_in_expr4489 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_MIN_in_expr4492 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expr5_in_expr4496 = frozenset([1, 4, 25])
    FOLLOW_expr6_in_expr5505 = frozenset([1, 12, 26])
    FOLLOW_DIV_in_expr5509 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_MUL_in_expr5512 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expr6_in_expr5516 = frozenset([1, 12, 26])
    FOLLOW_aexpr_in_expr6525 = frozenset([1, 7, 16, 19, 20, 22, 31])
    FOLLOW_ID_in_aexpr537 = frozenset([1])
    FOLLOW_INT_in_aexpr544 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr550 = frozenset([1])
    FOLLOW_CHAR_in_aexpr557 = frozenset([1])
    FOLLOW_STRING_in_aexpr564 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr571 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_aexpr574 = frozenset([29])
    FOLLOW_RPAREN_in_aexpr576 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr584 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_aexpr586 = frozenset([8, 29])
    FOLLOW_COMMA_in_aexpr589 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_aexpr591 = frozenset([8, 29])
    FOLLOW_RPAREN_in_aexpr595 = frozenset([1])
    FOLLOW_OR_in_synpred2_Miranda443 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_synpred2_Miranda446 = frozenset([1])
    FOLLOW_AND_in_synpred3_Miranda458 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_synpred3_Miranda461 = frozenset([1])
    FOLLOW_relop_in_synpred4_Miranda473 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_synpred4_Miranda476 = frozenset([1])
    FOLLOW_LPAREN_in_synpred15_Miranda571 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_synpred15_Miranda574 = frozenset([29])
    FOLLOW_RPAREN_in_synpred15_Miranda576 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MirandaLexer", MirandaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
