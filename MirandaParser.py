# $ANTLR 3.4 grammars/Miranda.g 2011-12-25 16:03:44

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
WHITESPACE=32

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALPHANUMERIC", "AND", "CHAR", "COMMA", "COMMENT", "DEDENT", 
    "DEFINITION", "DIV", "DOT", "DOUBLE_QUOTE", "EQ", "FLOAT", "GT", "GTE", 
    "ID", "INT", "IS", "LPAREN", "LT", "LTE", "MIN", "MUL", "NEQ", "OR", 
    "RPAREN", "SINGLE_QUOTE", "STRING", "WHITESPACE"
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
    # grammars/Miranda.g:77:1: program : ( definition DEDENT !)* expression EOF !;
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


                # grammars/Miranda.g:77:8: ( ( definition DEDENT !)* expression EOF !)
                # grammars/Miranda.g:77:10: ( definition DEDENT !)* expression EOF !
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:77:10: ( definition DEDENT !)*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        LA1_1 = self.input.LA(2)

                        if (LA1_1 == IS) :
                            alt1 = 1




                    if alt1 == 1:
                        # grammars/Miranda.g:77:11: definition DEDENT !
                        pass 
                        self._state.following.append(self.FOLLOW_definition_in_program351)
                        definition1 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition1.tree)


                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_program353)


                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_expression_in_program358)
                expression3 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression3.tree)


                EOF4 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program360)



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
    # grammars/Miranda.g:79:1: definition : ID IS expression -> ^( DEFINITION ID expression ) ;
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


                # grammars/Miranda.g:79:11: ( ID IS expression -> ^( DEFINITION ID expression ) )
                # grammars/Miranda.g:80:3: ID IS expression
                pass 
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_definition371) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID5)


                IS6 = self.match(self.input, IS, self.FOLLOW_IS_in_definition373) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS6)


                self._state.following.append(self.FOLLOW_expression_in_definition375)
                expression7 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression7.tree)


                # AST Rewrite
                # elements: ID, expression
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
                    # 81:3: -> ^( DEFINITION ID expression )
                    # grammars/Miranda.g:81:6: ^( DEFINITION ID expression )
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
    # grammars/Miranda.g:84:1: expression : expr1 ;
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


                # grammars/Miranda.g:84:11: ( expr1 )
                # grammars/Miranda.g:84:13: expr1
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr1_in_expression395)
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
    # grammars/Miranda.g:86:1: expr1 : expr2 ( OR ^ expression )* ;
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


                # grammars/Miranda.g:86:6: ( expr2 ( OR ^ expression )* )
                # grammars/Miranda.g:86:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1402)
                expr29 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr29.tree)


                # grammars/Miranda.g:86:14: ( OR ^ expression )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OR) :
                        LA2_2 = self.input.LA(2)

                        if (self.synpred2_Miranda()) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/Miranda.g:86:15: OR ^ expression
                        pass 
                        OR10 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1405)
                        if self._state.backtracking == 0:
                            OR10_tree = self._adaptor.createWithPayload(OR10)
                            root_0 = self._adaptor.becomeRoot(OR10_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr1408)
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
    # grammars/Miranda.g:88:1: expr2 : expr3 ( AND ^ expression )* ;
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


                # grammars/Miranda.g:88:6: ( expr3 ( AND ^ expression )* )
                # grammars/Miranda.g:88:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2417)
                expr312 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr312.tree)


                # grammars/Miranda.g:88:14: ( AND ^ expression )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == AND) :
                        LA3_2 = self.input.LA(2)

                        if (self.synpred3_Miranda()) :
                            alt3 = 1




                    if alt3 == 1:
                        # grammars/Miranda.g:88:15: AND ^ expression
                        pass 
                        AND13 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2420)
                        if self._state.backtracking == 0:
                            AND13_tree = self._adaptor.createWithPayload(AND13)
                            root_0 = self._adaptor.becomeRoot(AND13_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr2423)
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
    # grammars/Miranda.g:90:1: expr3 : expr4 ( relop ^ expression )* ;
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


                # grammars/Miranda.g:90:6: ( expr4 ( relop ^ expression )* )
                # grammars/Miranda.g:90:8: expr4 ( relop ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3432)
                expr415 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr415.tree)


                # grammars/Miranda.g:90:14: ( relop ^ expression )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQ or (GT <= LA4_0 <= GTE) or (LT <= LA4_0 <= LTE) or LA4_0 == NEQ) :
                        LA4_2 = self.input.LA(2)

                        if (self.synpred4_Miranda()) :
                            alt4 = 1




                    if alt4 == 1:
                        # grammars/Miranda.g:90:15: relop ^ expression
                        pass 
                        self._state.following.append(self.FOLLOW_relop_in_expr3435)
                        relop16 = self.relop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(relop16.tree, root_0)


                        self._state.following.append(self.FOLLOW_expression_in_expr3438)
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
    # grammars/Miranda.g:92:1: expr4 : expr5 ( ( ADD ^| MIN ^) expr5 )* ;
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


                # grammars/Miranda.g:92:6: ( expr5 ( ( ADD ^| MIN ^) expr5 )* )
                # grammars/Miranda.g:92:8: expr5 ( ( ADD ^| MIN ^) expr5 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4447)
                expr518 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr518.tree)


                # grammars/Miranda.g:92:14: ( ( ADD ^| MIN ^) expr5 )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == ADD or LA6_0 == MIN) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammars/Miranda.g:92:15: ( ADD ^| MIN ^) expr5
                        pass 
                        # grammars/Miranda.g:92:15: ( ADD ^| MIN ^)
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
                            # grammars/Miranda.g:92:16: ADD ^
                            pass 
                            ADD19 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4451)
                            if self._state.backtracking == 0:
                                ADD19_tree = self._adaptor.createWithPayload(ADD19)
                                root_0 = self._adaptor.becomeRoot(ADD19_tree, root_0)




                        elif alt5 == 2:
                            # grammars/Miranda.g:92:21: MIN ^
                            pass 
                            MIN20 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4454)
                            if self._state.backtracking == 0:
                                MIN20_tree = self._adaptor.createWithPayload(MIN20)
                                root_0 = self._adaptor.becomeRoot(MIN20_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr5_in_expr4458)
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
    # grammars/Miranda.g:94:1: expr5 : expr6 ( ( DIV ^| MUL ^) expr6 )* ;
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


                # grammars/Miranda.g:94:6: ( expr6 ( ( DIV ^| MUL ^) expr6 )* )
                # grammars/Miranda.g:94:8: expr6 ( ( DIV ^| MUL ^) expr6 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr5467)
                expr622 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr622.tree)


                # grammars/Miranda.g:94:14: ( ( DIV ^| MUL ^) expr6 )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == DIV or LA8_0 == MUL) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammars/Miranda.g:94:15: ( DIV ^| MUL ^) expr6
                        pass 
                        # grammars/Miranda.g:94:15: ( DIV ^| MUL ^)
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
                            # grammars/Miranda.g:94:16: DIV ^
                            pass 
                            DIV23 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5471)
                            if self._state.backtracking == 0:
                                DIV23_tree = self._adaptor.createWithPayload(DIV23)
                                root_0 = self._adaptor.becomeRoot(DIV23_tree, root_0)




                        elif alt7 == 2:
                            # grammars/Miranda.g:94:21: MUL ^
                            pass 
                            MUL24 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5474)
                            if self._state.backtracking == 0:
                                MUL24_tree = self._adaptor.createWithPayload(MUL24)
                                root_0 = self._adaptor.becomeRoot(MUL24_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr6_in_expr5478)
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
    # grammars/Miranda.g:96:1: expr6 : ( aexpr )+ ;
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


                # grammars/Miranda.g:96:6: ( ( aexpr )+ )
                # grammars/Miranda.g:96:8: ( aexpr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:96:8: ( aexpr )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == CHAR or LA9_0 == FLOAT or (ID <= LA9_0 <= INT) or LA9_0 == LPAREN or LA9_0 == STRING) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammars/Miranda.g:96:8: aexpr
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr6487)
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
    # grammars/Miranda.g:98:1: aexpr : ( ID | INT | FLOAT | CHAR | STRING | LPAREN expression RPAREN );
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
        expression33 = None


        ID27_tree = None
        INT28_tree = None
        FLOAT29_tree = None
        CHAR30_tree = None
        STRING31_tree = None
        LPAREN32_tree = None
        RPAREN34_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:99:4: ( ID | INT | FLOAT | CHAR | STRING | LPAREN expression RPAREN )
                alt10 = 6
                LA10 = self.input.LA(1)
                if LA10 == ID:
                    alt10 = 1
                elif LA10 == INT:
                    alt10 = 2
                elif LA10 == FLOAT:
                    alt10 = 3
                elif LA10 == CHAR:
                    alt10 = 4
                elif LA10 == STRING:
                    alt10 = 5
                elif LA10 == LPAREN:
                    alt10 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # grammars/Miranda.g:99:6: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr499)
                    if self._state.backtracking == 0:
                        ID27_tree = self._adaptor.createWithPayload(ID27)
                        self._adaptor.addChild(root_0, ID27_tree)




                elif alt10 == 2:
                    # grammars/Miranda.g:100:6: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT28 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr506)
                    if self._state.backtracking == 0:
                        INT28_tree = self._adaptor.createWithPayload(INT28)
                        self._adaptor.addChild(root_0, INT28_tree)




                elif alt10 == 3:
                    # grammars/Miranda.g:101:5: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()


                    FLOAT29 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr512)
                    if self._state.backtracking == 0:
                        FLOAT29_tree = self._adaptor.createWithPayload(FLOAT29)
                        self._adaptor.addChild(root_0, FLOAT29_tree)




                elif alt10 == 4:
                    # grammars/Miranda.g:102:6: CHAR
                    pass 
                    root_0 = self._adaptor.nil()


                    CHAR30 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_aexpr519)
                    if self._state.backtracking == 0:
                        CHAR30_tree = self._adaptor.createWithPayload(CHAR30)
                        self._adaptor.addChild(root_0, CHAR30_tree)




                elif alt10 == 5:
                    # grammars/Miranda.g:103:6: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING31 = self.match(self.input, STRING, self.FOLLOW_STRING_in_aexpr526)
                    if self._state.backtracking == 0:
                        STRING31_tree = self._adaptor.createWithPayload(STRING31)
                        self._adaptor.addChild(root_0, STRING31_tree)




                elif alt10 == 6:
                    # grammars/Miranda.g:104:6: LPAREN expression RPAREN
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN32 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr533)
                    if self._state.backtracking == 0:
                        LPAREN32_tree = self._adaptor.createWithPayload(LPAREN32)
                        self._adaptor.addChild(root_0, LPAREN32_tree)



                    self._state.following.append(self.FOLLOW_expression_in_aexpr535)
                    expression33 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression33.tree)


                    RPAREN34 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr537)
                    if self._state.backtracking == 0:
                        RPAREN34_tree = self._adaptor.createWithPayload(RPAREN34)
                        self._adaptor.addChild(root_0, RPAREN34_tree)




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
    # grammars/Miranda.g:107:1: relop : ( LT | LTE | EQ | NEQ | GTE | GT );
    def relop(self, ):
        retval = self.relop_return()
        retval.start = self.input.LT(1)

        relop_StartIndex = self.input.index()

        root_0 = None

        set35 = None

        set35_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:107:6: ( LT | LTE | EQ | NEQ | GTE | GT )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set35 = self.input.LT(1)

                if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set35))

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
        # grammars/Miranda.g:86:15: ( OR expression )
        # grammars/Miranda.g:86:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred2_Miranda405)

        self._state.following.append(self.FOLLOW_expression_in_synpred2_Miranda408)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred2_Miranda"



    # $ANTLR start "synpred3_Miranda"
    def synpred3_Miranda_fragment(self, ):
        # grammars/Miranda.g:88:15: ( AND expression )
        # grammars/Miranda.g:88:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred3_Miranda420)

        self._state.following.append(self.FOLLOW_expression_in_synpred3_Miranda423)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred3_Miranda"



    # $ANTLR start "synpred4_Miranda"
    def synpred4_Miranda_fragment(self, ):
        # grammars/Miranda.g:90:15: ( relop expression )
        # grammars/Miranda.g:90:15: relop expression
        pass 
        self._state.following.append(self.FOLLOW_relop_in_synpred4_Miranda435)
        self.relop()

        self._state.following.pop()

        self._state.following.append(self.FOLLOW_expression_in_synpred4_Miranda438)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred4_Miranda"




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



 

    FOLLOW_definition_in_program351 = frozenset([10])
    FOLLOW_DEDENT_in_program353 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_program358 = frozenset([])
    FOLLOW_EOF_in_program360 = frozenset([1])
    FOLLOW_ID_in_definition371 = frozenset([21])
    FOLLOW_IS_in_definition373 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_definition375 = frozenset([1])
    FOLLOW_expr1_in_expression395 = frozenset([1])
    FOLLOW_expr2_in_expr1402 = frozenset([1, 28])
    FOLLOW_OR_in_expr1405 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_expr1408 = frozenset([1, 28])
    FOLLOW_expr3_in_expr2417 = frozenset([1, 6])
    FOLLOW_AND_in_expr2420 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_expr2423 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3432 = frozenset([1, 15, 17, 18, 23, 24, 27])
    FOLLOW_relop_in_expr3435 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_expr3438 = frozenset([1, 15, 17, 18, 23, 24, 27])
    FOLLOW_expr5_in_expr4447 = frozenset([1, 4, 25])
    FOLLOW_ADD_in_expr4451 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_MIN_in_expr4454 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expr5_in_expr4458 = frozenset([1, 4, 25])
    FOLLOW_expr6_in_expr5467 = frozenset([1, 12, 26])
    FOLLOW_DIV_in_expr5471 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_MUL_in_expr5474 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expr6_in_expr5478 = frozenset([1, 12, 26])
    FOLLOW_aexpr_in_expr6487 = frozenset([1, 7, 16, 19, 20, 22, 31])
    FOLLOW_ID_in_aexpr499 = frozenset([1])
    FOLLOW_INT_in_aexpr506 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr512 = frozenset([1])
    FOLLOW_CHAR_in_aexpr519 = frozenset([1])
    FOLLOW_STRING_in_aexpr526 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr533 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_aexpr535 = frozenset([29])
    FOLLOW_RPAREN_in_aexpr537 = frozenset([1])
    FOLLOW_OR_in_synpred2_Miranda405 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_synpred2_Miranda408 = frozenset([1])
    FOLLOW_AND_in_synpred3_Miranda420 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_synpred3_Miranda423 = frozenset([1])
    FOLLOW_relop_in_synpred4_Miranda435 = frozenset([7, 16, 19, 20, 22, 31])
    FOLLOW_expression_in_synpred4_Miranda438 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MirandaLexer", MirandaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
