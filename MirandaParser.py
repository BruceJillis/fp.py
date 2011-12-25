# $ANTLR 3.4 grammars/Miranda.g 2011-12-25 17:16:34

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
CONCAT=10
DEDENT=11
DEFINITION=12
DIV=13
DOT=14
DOUBLE_QUOTE=15
EQ=16
EXP=17
FALSE=18
FLOAT=19
GT=20
GTE=21
ID=22
IDIV=23
INT=24
IS=25
LBRACKET=26
LIST=27
LPAREN=28
LT=29
LTE=30
MIN=31
MOD=32
MUL=33
NEQ=34
NOT=35
NUMERIC=36
OR=37
RBRACKET=38
RPAREN=39
SECTION=40
SINGLE_QUOTE=41
STRING=42
SUBTRACT=43
TRUE=44
TUPLE=45
WHITESPACE=46

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALPHANUMERIC", "AND", "CHAR", "COMMA", "COMMENT", "CONCAT", 
    "DEDENT", "DEFINITION", "DIV", "DOT", "DOUBLE_QUOTE", "EQ", "EXP", "FALSE", 
    "FLOAT", "GT", "GTE", "ID", "IDIV", "INT", "IS", "LBRACKET", "LIST", 
    "LPAREN", "LT", "LTE", "MIN", "MOD", "MUL", "NEQ", "NOT", "NUMERIC", 
    "OR", "RBRACKET", "RPAREN", "SECTION", "SINGLE_QUOTE", "STRING", "SUBTRACT", 
    "TRUE", "TUPLE", "WHITESPACE"
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
    # grammars/Miranda.g:94:1: program : ( definition DEDENT !)* expression EOF !;
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


                # grammars/Miranda.g:94:8: ( ( definition DEDENT !)* expression EOF !)
                # grammars/Miranda.g:94:10: ( definition DEDENT !)* expression EOF !
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:94:10: ( definition DEDENT !)*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        LA1_1 = self.input.LA(2)

                        if (LA1_1 == IS) :
                            alt1 = 1




                    if alt1 == 1:
                        # grammars/Miranda.g:94:11: definition DEDENT !
                        pass 
                        self._state.following.append(self.FOLLOW_definition_in_program523)
                        definition1 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition1.tree)


                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_program525)


                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_expression_in_program530)
                expression3 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression3.tree)


                EOF4 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program532)



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
    # grammars/Miranda.g:96:1: definition : ID IS expression -> ^( DEFINITION ID expression ) ;
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


                # grammars/Miranda.g:96:11: ( ID IS expression -> ^( DEFINITION ID expression ) )
                # grammars/Miranda.g:97:3: ID IS expression
                pass 
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_definition543) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID5)


                IS6 = self.match(self.input, IS, self.FOLLOW_IS_in_definition545) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS6)


                self._state.following.append(self.FOLLOW_expression_in_definition547)
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
                    # 98:3: -> ^( DEFINITION ID expression )
                    # grammars/Miranda.g:98:6: ^( DEFINITION ID expression )
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
    # grammars/Miranda.g:101:1: expression : expr1 ;
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


                # grammars/Miranda.g:101:11: ( expr1 )
                # grammars/Miranda.g:101:13: expr1
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr1_in_expression567)
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
    # grammars/Miranda.g:103:1: expr1 : expr2 ( OR ^ expression )* ;
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


                # grammars/Miranda.g:103:6: ( expr2 ( OR ^ expression )* )
                # grammars/Miranda.g:103:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1574)
                expr29 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr29.tree)


                # grammars/Miranda.g:103:14: ( OR ^ expression )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OR) :
                        LA2_2 = self.input.LA(2)

                        if (self.synpred2_Miranda()) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/Miranda.g:103:15: OR ^ expression
                        pass 
                        OR10 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1577)
                        if self._state.backtracking == 0:
                            OR10_tree = self._adaptor.createWithPayload(OR10)
                            root_0 = self._adaptor.becomeRoot(OR10_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr1580)
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
    # grammars/Miranda.g:105:1: expr2 : expr3 ( AND ^ expression )* ;
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


                # grammars/Miranda.g:105:6: ( expr3 ( AND ^ expression )* )
                # grammars/Miranda.g:105:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2589)
                expr312 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr312.tree)


                # grammars/Miranda.g:105:14: ( AND ^ expression )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == AND) :
                        LA3_2 = self.input.LA(2)

                        if (self.synpred3_Miranda()) :
                            alt3 = 1




                    if alt3 == 1:
                        # grammars/Miranda.g:105:15: AND ^ expression
                        pass 
                        AND13 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2592)
                        if self._state.backtracking == 0:
                            AND13_tree = self._adaptor.createWithPayload(AND13)
                            root_0 = self._adaptor.becomeRoot(AND13_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr2595)
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
    # grammars/Miranda.g:107:1: expr3 : expr4 ( relop expression )* ;
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


                # grammars/Miranda.g:107:6: ( expr4 ( relop expression )* )
                # grammars/Miranda.g:107:8: expr4 ( relop expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3604)
                expr415 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr415.tree)


                # grammars/Miranda.g:107:14: ( relop expression )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQ or (GT <= LA4_0 <= GTE) or (LT <= LA4_0 <= LTE) or LA4_0 == NEQ) :
                        LA4_2 = self.input.LA(2)

                        if (self.synpred4_Miranda()) :
                            alt4 = 1




                    if alt4 == 1:
                        # grammars/Miranda.g:107:15: relop expression
                        pass 
                        self._state.following.append(self.FOLLOW_relop_in_expr3607)
                        relop16 = self.relop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, relop16.tree)


                        self._state.following.append(self.FOLLOW_expression_in_expr3609)
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
    # grammars/Miranda.g:109:1: expr4 : expr5 ( ( ADD ^| MIN ^| CONCAT ^| SUBTRACT ^) expr5 )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD19 = None
        MIN20 = None
        CONCAT21 = None
        SUBTRACT22 = None
        expr518 = None

        expr523 = None


        ADD19_tree = None
        MIN20_tree = None
        CONCAT21_tree = None
        SUBTRACT22_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:109:6: ( expr5 ( ( ADD ^| MIN ^| CONCAT ^| SUBTRACT ^) expr5 )* )
                # grammars/Miranda.g:109:8: expr5 ( ( ADD ^| MIN ^| CONCAT ^| SUBTRACT ^) expr5 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4618)
                expr518 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr518.tree)


                # grammars/Miranda.g:109:14: ( ( ADD ^| MIN ^| CONCAT ^| SUBTRACT ^) expr5 )*
                while True: #loop6
                    alt6 = 2
                    LA6 = self.input.LA(1)
                    if LA6 == ADD:
                        LA6_2 = self.input.LA(2)

                        if (self.synpred8_Miranda()) :
                            alt6 = 1


                    elif LA6 == MIN:
                        LA6_3 = self.input.LA(2)

                        if (self.synpred8_Miranda()) :
                            alt6 = 1


                    elif LA6 == CONCAT:
                        LA6_4 = self.input.LA(2)

                        if (self.synpred8_Miranda()) :
                            alt6 = 1


                    elif LA6 == SUBTRACT:
                        LA6_5 = self.input.LA(2)

                        if (self.synpred8_Miranda()) :
                            alt6 = 1



                    if alt6 == 1:
                        # grammars/Miranda.g:109:15: ( ADD ^| MIN ^| CONCAT ^| SUBTRACT ^) expr5
                        pass 
                        # grammars/Miranda.g:109:15: ( ADD ^| MIN ^| CONCAT ^| SUBTRACT ^)
                        alt5 = 4
                        LA5 = self.input.LA(1)
                        if LA5 == ADD:
                            alt5 = 1
                        elif LA5 == MIN:
                            alt5 = 2
                        elif LA5 == CONCAT:
                            alt5 = 3
                        elif LA5 == SUBTRACT:
                            alt5 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 5, 0, self.input)

                            raise nvae


                        if alt5 == 1:
                            # grammars/Miranda.g:109:16: ADD ^
                            pass 
                            ADD19 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4622)
                            if self._state.backtracking == 0:
                                ADD19_tree = self._adaptor.createWithPayload(ADD19)
                                root_0 = self._adaptor.becomeRoot(ADD19_tree, root_0)




                        elif alt5 == 2:
                            # grammars/Miranda.g:109:21: MIN ^
                            pass 
                            MIN20 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4625)
                            if self._state.backtracking == 0:
                                MIN20_tree = self._adaptor.createWithPayload(MIN20)
                                root_0 = self._adaptor.becomeRoot(MIN20_tree, root_0)




                        elif alt5 == 3:
                            # grammars/Miranda.g:109:26: CONCAT ^
                            pass 
                            CONCAT21 = self.match(self.input, CONCAT, self.FOLLOW_CONCAT_in_expr4628)
                            if self._state.backtracking == 0:
                                CONCAT21_tree = self._adaptor.createWithPayload(CONCAT21)
                                root_0 = self._adaptor.becomeRoot(CONCAT21_tree, root_0)




                        elif alt5 == 4:
                            # grammars/Miranda.g:109:34: SUBTRACT ^
                            pass 
                            SUBTRACT22 = self.match(self.input, SUBTRACT, self.FOLLOW_SUBTRACT_in_expr4631)
                            if self._state.backtracking == 0:
                                SUBTRACT22_tree = self._adaptor.createWithPayload(SUBTRACT22)
                                root_0 = self._adaptor.becomeRoot(SUBTRACT22_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr5_in_expr4635)
                        expr523 = self.expr5()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr523.tree)



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
    # grammars/Miranda.g:111:1: expr5 : expr6 ( ( DIV ^| MUL ^) expr6 )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV25 = None
        MUL26 = None
        expr624 = None

        expr627 = None


        DIV25_tree = None
        MUL26_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:111:6: ( expr6 ( ( DIV ^| MUL ^) expr6 )* )
                # grammars/Miranda.g:111:8: expr6 ( ( DIV ^| MUL ^) expr6 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr5644)
                expr624 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr624.tree)


                # grammars/Miranda.g:111:14: ( ( DIV ^| MUL ^) expr6 )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == DIV) :
                        LA8_2 = self.input.LA(2)

                        if (self.synpred10_Miranda()) :
                            alt8 = 1


                    elif (LA8_0 == MUL) :
                        LA8_3 = self.input.LA(2)

                        if (self.synpred10_Miranda()) :
                            alt8 = 1




                    if alt8 == 1:
                        # grammars/Miranda.g:111:15: ( DIV ^| MUL ^) expr6
                        pass 
                        # grammars/Miranda.g:111:15: ( DIV ^| MUL ^)
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
                            # grammars/Miranda.g:111:16: DIV ^
                            pass 
                            DIV25 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5648)
                            if self._state.backtracking == 0:
                                DIV25_tree = self._adaptor.createWithPayload(DIV25)
                                root_0 = self._adaptor.becomeRoot(DIV25_tree, root_0)




                        elif alt7 == 2:
                            # grammars/Miranda.g:111:21: MUL ^
                            pass 
                            MUL26 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5651)
                            if self._state.backtracking == 0:
                                MUL26_tree = self._adaptor.createWithPayload(MUL26)
                                root_0 = self._adaptor.becomeRoot(MUL26_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr6_in_expr5655)
                        expr627 = self.expr6()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr627.tree)



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
    # grammars/Miranda.g:113:1: expr6 : expr7 ( ( IDIV ^| MOD ^) expr7 )* ;
    def expr6(self, ):
        retval = self.expr6_return()
        retval.start = self.input.LT(1)

        expr6_StartIndex = self.input.index()

        root_0 = None

        IDIV29 = None
        MOD30 = None
        expr728 = None

        expr731 = None


        IDIV29_tree = None
        MOD30_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:113:6: ( expr7 ( ( IDIV ^| MOD ^) expr7 )* )
                # grammars/Miranda.g:113:8: expr7 ( ( IDIV ^| MOD ^) expr7 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr7_in_expr6664)
                expr728 = self.expr7()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr728.tree)


                # grammars/Miranda.g:113:14: ( ( IDIV ^| MOD ^) expr7 )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == IDIV) :
                        LA10_2 = self.input.LA(2)

                        if (self.synpred12_Miranda()) :
                            alt10 = 1


                    elif (LA10_0 == MOD) :
                        LA10_3 = self.input.LA(2)

                        if (self.synpred12_Miranda()) :
                            alt10 = 1




                    if alt10 == 1:
                        # grammars/Miranda.g:113:15: ( IDIV ^| MOD ^) expr7
                        pass 
                        # grammars/Miranda.g:113:15: ( IDIV ^| MOD ^)
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == IDIV) :
                            alt9 = 1
                        elif (LA9_0 == MOD) :
                            alt9 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 9, 0, self.input)

                            raise nvae


                        if alt9 == 1:
                            # grammars/Miranda.g:113:16: IDIV ^
                            pass 
                            IDIV29 = self.match(self.input, IDIV, self.FOLLOW_IDIV_in_expr6668)
                            if self._state.backtracking == 0:
                                IDIV29_tree = self._adaptor.createWithPayload(IDIV29)
                                root_0 = self._adaptor.becomeRoot(IDIV29_tree, root_0)




                        elif alt9 == 2:
                            # grammars/Miranda.g:113:22: MOD ^
                            pass 
                            MOD30 = self.match(self.input, MOD, self.FOLLOW_MOD_in_expr6671)
                            if self._state.backtracking == 0:
                                MOD30_tree = self._adaptor.createWithPayload(MOD30)
                                root_0 = self._adaptor.becomeRoot(MOD30_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr7_in_expr6675)
                        expr731 = self.expr7()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr731.tree)



                    else:
                        break #loop10




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


    class expr7_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr7_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr7"
    # grammars/Miranda.g:115:1: expr7 : expr8 ( ( EXP ^) expr8 )* ;
    def expr7(self, ):
        retval = self.expr7_return()
        retval.start = self.input.LT(1)

        expr7_StartIndex = self.input.index()

        root_0 = None

        EXP33 = None
        expr832 = None

        expr834 = None


        EXP33_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:115:6: ( expr8 ( ( EXP ^) expr8 )* )
                # grammars/Miranda.g:115:8: expr8 ( ( EXP ^) expr8 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr8_in_expr7684)
                expr832 = self.expr8()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr832.tree)


                # grammars/Miranda.g:115:14: ( ( EXP ^) expr8 )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == EXP) :
                        LA11_2 = self.input.LA(2)

                        if (self.synpred13_Miranda()) :
                            alt11 = 1




                    if alt11 == 1:
                        # grammars/Miranda.g:115:15: ( EXP ^) expr8
                        pass 
                        # grammars/Miranda.g:115:15: ( EXP ^)
                        # grammars/Miranda.g:115:16: EXP ^
                        pass 
                        EXP33 = self.match(self.input, EXP, self.FOLLOW_EXP_in_expr7688)
                        if self._state.backtracking == 0:
                            EXP33_tree = self._adaptor.createWithPayload(EXP33)
                            root_0 = self._adaptor.becomeRoot(EXP33_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr8_in_expr7692)
                        expr834 = self.expr8()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr834.tree)



                    else:
                        break #loop11




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
                self.memoize(self.input, 10, expr7_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr7"


    class expr8_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr8_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr8"
    # grammars/Miranda.g:117:1: expr8 : ( aexpr )+ ;
    def expr8(self, ):
        retval = self.expr8_return()
        retval.start = self.input.LT(1)

        expr8_StartIndex = self.input.index()

        root_0 = None

        aexpr35 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:117:6: ( ( aexpr )+ )
                # grammars/Miranda.g:117:8: ( aexpr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:117:8: ( aexpr )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12 = self.input.LA(1)
                    if LA12 == ID:
                        LA12_15 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == INT:
                        LA12_16 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == FLOAT:
                        LA12_17 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == CHAR:
                        LA12_18 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == STRING:
                        LA12_19 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == NOT:
                        LA12_20 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == FALSE or LA12 == TRUE:
                        LA12_21 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == LPAREN:
                        LA12_22 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1


                    elif LA12 == LBRACKET:
                        LA12_23 = self.input.LA(2)

                        if (self.synpred14_Miranda()) :
                            alt12 = 1



                    if alt12 == 1:
                        # grammars/Miranda.g:117:8: aexpr
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr8701)
                        aexpr35 = self.aexpr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, aexpr35.tree)



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1




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
                self.memoize(self.input, 11, expr8_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr8"


    class aexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.aexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "aexpr"
    # grammars/Miranda.g:119:1: aexpr : ( ID | INT | FLOAT | CHAR | STRING | NOT expression | boolean | section | LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) | LPAREN ! expression RPAREN !| LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) );
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID36 = None
        INT37 = None
        FLOAT38 = None
        CHAR39 = None
        STRING40 = None
        NOT41 = None
        LPAREN45 = None
        COMMA47 = None
        RPAREN49 = None
        LPAREN50 = None
        RPAREN52 = None
        LBRACKET53 = None
        COMMA55 = None
        RBRACKET57 = None
        expression42 = None

        boolean43 = None

        section44 = None

        expression46 = None

        expression48 = None

        expression51 = None

        expression54 = None

        expression56 = None


        ID36_tree = None
        INT37_tree = None
        FLOAT38_tree = None
        CHAR39_tree = None
        STRING40_tree = None
        NOT41_tree = None
        LPAREN45_tree = None
        COMMA47_tree = None
        RPAREN49_tree = None
        LPAREN50_tree = None
        RPAREN52_tree = None
        LBRACKET53_tree = None
        COMMA55_tree = None
        RBRACKET57_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:120:4: ( ID | INT | FLOAT | CHAR | STRING | NOT expression | boolean | section | LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) | LPAREN ! expression RPAREN !| LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) )
                alt16 = 11
                LA16 = self.input.LA(1)
                if LA16 == ID:
                    alt16 = 1
                elif LA16 == INT:
                    alt16 = 2
                elif LA16 == FLOAT:
                    alt16 = 3
                elif LA16 == CHAR:
                    alt16 = 4
                elif LA16 == STRING:
                    alt16 = 5
                elif LA16 == NOT:
                    alt16 = 6
                elif LA16 == FALSE or LA16 == TRUE:
                    alt16 = 7
                elif LA16 == LPAREN:
                    LA16_8 = self.input.LA(2)

                    if (self.synpred22_Miranda()) :
                        alt16 = 8
                    elif (self.synpred24_Miranda()) :
                        alt16 = 9
                    elif (self.synpred25_Miranda()) :
                        alt16 = 10
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 16, 8, self.input)

                        raise nvae


                elif LA16 == LBRACKET:
                    alt16 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammars/Miranda.g:120:6: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID36 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr713)
                    if self._state.backtracking == 0:
                        ID36_tree = self._adaptor.createWithPayload(ID36)
                        self._adaptor.addChild(root_0, ID36_tree)




                elif alt16 == 2:
                    # grammars/Miranda.g:121:6: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT37 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr720)
                    if self._state.backtracking == 0:
                        INT37_tree = self._adaptor.createWithPayload(INT37)
                        self._adaptor.addChild(root_0, INT37_tree)




                elif alt16 == 3:
                    # grammars/Miranda.g:122:5: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()


                    FLOAT38 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr726)
                    if self._state.backtracking == 0:
                        FLOAT38_tree = self._adaptor.createWithPayload(FLOAT38)
                        self._adaptor.addChild(root_0, FLOAT38_tree)




                elif alt16 == 4:
                    # grammars/Miranda.g:123:6: CHAR
                    pass 
                    root_0 = self._adaptor.nil()


                    CHAR39 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_aexpr733)
                    if self._state.backtracking == 0:
                        CHAR39_tree = self._adaptor.createWithPayload(CHAR39)
                        self._adaptor.addChild(root_0, CHAR39_tree)




                elif alt16 == 5:
                    # grammars/Miranda.g:124:6: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING40 = self.match(self.input, STRING, self.FOLLOW_STRING_in_aexpr740)
                    if self._state.backtracking == 0:
                        STRING40_tree = self._adaptor.createWithPayload(STRING40)
                        self._adaptor.addChild(root_0, STRING40_tree)




                elif alt16 == 6:
                    # grammars/Miranda.g:125:6: NOT expression
                    pass 
                    root_0 = self._adaptor.nil()


                    NOT41 = self.match(self.input, NOT, self.FOLLOW_NOT_in_aexpr747)
                    if self._state.backtracking == 0:
                        NOT41_tree = self._adaptor.createWithPayload(NOT41)
                        self._adaptor.addChild(root_0, NOT41_tree)



                    self._state.following.append(self.FOLLOW_expression_in_aexpr749)
                    expression42 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression42.tree)



                elif alt16 == 7:
                    # grammars/Miranda.g:126:6: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_aexpr756)
                    boolean43 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean43.tree)



                elif alt16 == 8:
                    # grammars/Miranda.g:127:6: section
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_section_in_aexpr763)
                    section44 = self.section()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, section44.tree)



                elif alt16 == 9:
                    # grammars/Miranda.g:128:6: LPAREN expression ( COMMA expression )+ RPAREN
                    pass 
                    LPAREN45 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr770) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN45)


                    self._state.following.append(self.FOLLOW_expression_in_aexpr772)
                    expression46 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression46.tree)


                    # grammars/Miranda.g:128:24: ( COMMA expression )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == COMMA) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammars/Miranda.g:128:25: COMMA expression
                            pass 
                            COMMA47 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_aexpr775) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA47)


                            self._state.following.append(self.FOLLOW_expression_in_aexpr777)
                            expression48 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_expression.add(expression48.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    RPAREN49 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr781) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN49)


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
                        # 129:6: -> ^( TUPLE ( expression )* )
                        # grammars/Miranda.g:129:9: ^( TUPLE ( expression )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TUPLE, "TUPLE")
                        , root_1)

                        # grammars/Miranda.g:129:17: ( expression )*
                        while stream_expression.hasNext():
                            self._adaptor.addChild(root_1, stream_expression.nextTree())


                        stream_expression.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt16 == 10:
                    # grammars/Miranda.g:130:6: LPAREN ! expression RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN50 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr802)

                    self._state.following.append(self.FOLLOW_expression_in_aexpr805)
                    expression51 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression51.tree)


                    RPAREN52 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr807)


                elif alt16 == 11:
                    # grammars/Miranda.g:131:6: LBRACKET ( expression )? ( COMMA expression )* RBRACKET
                    pass 
                    LBRACKET53 = self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_aexpr815) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET53)


                    # grammars/Miranda.g:131:15: ( expression )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == CHAR or (FALSE <= LA14_0 <= FLOAT) or LA14_0 == ID or LA14_0 == INT or LA14_0 == LBRACKET or LA14_0 == LPAREN or LA14_0 == NOT or LA14_0 == STRING or LA14_0 == TRUE) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammars/Miranda.g:131:15: expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_aexpr817)
                        expression54 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression54.tree)





                    # grammars/Miranda.g:131:27: ( COMMA expression )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == COMMA) :
                            alt15 = 1


                        if alt15 == 1:
                            # grammars/Miranda.g:131:28: COMMA expression
                            pass 
                            COMMA55 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_aexpr821) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA55)


                            self._state.following.append(self.FOLLOW_expression_in_aexpr823)
                            expression56 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_expression.add(expression56.tree)



                        else:
                            break #loop15


                    RBRACKET57 = self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_aexpr827) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET57)


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
                        # 132:6: -> ^( LIST ( expression )* )
                        # grammars/Miranda.g:132:9: ^( LIST ( expression )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LIST, "LIST")
                        , root_1)

                        # grammars/Miranda.g:132:16: ( expression )*
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
                self.memoize(self.input, 12, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class section_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.section_return, self).__init__()

            self.tree = None





    # $ANTLR start "section"
    # grammars/Miranda.g:135:1: section : ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) );
    def section(self, ):
        retval = self.section_return()
        retval.start = self.input.LT(1)

        section_StartIndex = self.input.index()

        root_0 = None

        LPAREN58 = None
        RPAREN60 = None
        LPAREN61 = None
        RPAREN64 = None
        LPAREN65 = None
        RPAREN68 = None
        operator59 = None

        operator62 = None

        expression63 = None

        expression66 = None

        operator67 = None


        LPAREN58_tree = None
        RPAREN60_tree = None
        LPAREN61_tree = None
        RPAREN64_tree = None
        LPAREN65_tree = None
        RPAREN68_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_operator = RewriteRuleSubtreeStream(self._adaptor, "rule operator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:136:3: ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) )
                alt17 = 3
                LA17_0 = self.input.LA(1)

                if (LA17_0 == LPAREN) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == ADD or LA17_1 == AND or LA17_1 == CONCAT or LA17_1 == DIV or (EQ <= LA17_1 <= EXP) or (GT <= LA17_1 <= GTE) or LA17_1 == IDIV or (LT <= LA17_1 <= NEQ) or LA17_1 == OR or LA17_1 == SUBTRACT) :
                        LA17_2 = self.input.LA(3)

                        if (LA17_2 == RPAREN) :
                            alt17 = 1
                        elif (LA17_2 == CHAR or (FALSE <= LA17_2 <= FLOAT) or LA17_2 == ID or LA17_2 == INT or LA17_2 == LBRACKET or LA17_2 == LPAREN or LA17_2 == NOT or LA17_2 == STRING or LA17_2 == TRUE) :
                            alt17 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 17, 2, self.input)

                            raise nvae


                    elif (LA17_1 == CHAR or (FALSE <= LA17_1 <= FLOAT) or LA17_1 == ID or LA17_1 == INT or LA17_1 == LBRACKET or LA17_1 == LPAREN or LA17_1 == NOT or LA17_1 == STRING or LA17_1 == TRUE) :
                        alt17 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 17, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammars/Miranda.g:136:5: LPAREN operator RPAREN
                    pass 
                    LPAREN58 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section852) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN58)


                    self._state.following.append(self.FOLLOW_operator_in_section854)
                    operator59 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator59.tree)


                    RPAREN60 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section856) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN60)


                    # AST Rewrite
                    # elements: operator
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
                        # 137:4: -> ^( SECTION operator )
                        # grammars/Miranda.g:137:7: ^( SECTION operator )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt17 == 2:
                    # grammars/Miranda.g:138:5: LPAREN operator expression RPAREN
                    pass 
                    LPAREN61 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section873) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN61)


                    self._state.following.append(self.FOLLOW_operator_in_section875)
                    operator62 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator62.tree)


                    self._state.following.append(self.FOLLOW_expression_in_section877)
                    expression63 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression63.tree)


                    RPAREN64 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section879) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN64)


                    # AST Rewrite
                    # elements: operator, expression
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
                        # 139:4: -> ^( SECTION operator expression )
                        # grammars/Miranda.g:139:7: ^( SECTION operator expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt17 == 3:
                    # grammars/Miranda.g:140:5: LPAREN expression operator RPAREN
                    pass 
                    LPAREN65 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section898) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN65)


                    self._state.following.append(self.FOLLOW_expression_in_section900)
                    expression66 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression66.tree)


                    self._state.following.append(self.FOLLOW_operator_in_section902)
                    operator67 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator67.tree)


                    RPAREN68 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section904) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN68)


                    # AST Rewrite
                    # elements: expression, operator
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
                        # 141:4: -> ^( SECTION expression operator )
                        # grammars/Miranda.g:141:7: ^( SECTION expression operator )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

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
                self.memoize(self.input, 13, section_StartIndex, success)


            pass
        return retval

    # $ANTLR end "section"


    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.operator_return, self).__init__()

            self.tree = None





    # $ANTLR start "operator"
    # grammars/Miranda.g:143:10: fragment operator : ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP );
    def operator(self, ):
        retval = self.operator_return()
        retval.start = self.input.LT(1)

        operator_StartIndex = self.input.index()

        root_0 = None

        set69 = None

        set69_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:143:18: ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set69 = self.input.LT(1)

                if self.input.LA(1) == ADD or self.input.LA(1) == AND or self.input.LA(1) == CONCAT or self.input.LA(1) == DIV or (EQ <= self.input.LA(1) <= EXP) or (GT <= self.input.LA(1) <= GTE) or self.input.LA(1) == IDIV or (LT <= self.input.LA(1) <= NEQ) or self.input.LA(1) == OR or self.input.LA(1) == SUBTRACT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set69))

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
                self.memoize(self.input, 14, operator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "operator"


    class boolean_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.boolean_return, self).__init__()

            self.tree = None





    # $ANTLR start "boolean"
    # grammars/Miranda.g:145:1: boolean : ( TRUE | FALSE );
    def boolean(self, ):
        retval = self.boolean_return()
        retval.start = self.input.LT(1)

        boolean_StartIndex = self.input.index()

        root_0 = None

        set70 = None

        set70_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:145:8: ( TRUE | FALSE )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set70 = self.input.LT(1)

                if self.input.LA(1) == FALSE or self.input.LA(1) == TRUE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set70))

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
                self.memoize(self.input, 15, boolean_StartIndex, success)


            pass
        return retval

    # $ANTLR end "boolean"


    class relop_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.relop_return, self).__init__()

            self.tree = None





    # $ANTLR start "relop"
    # grammars/Miranda.g:147:1: relop : ( LT | LTE | EQ | NEQ | GTE | GT );
    def relop(self, ):
        retval = self.relop_return()
        retval.start = self.input.LT(1)

        relop_StartIndex = self.input.index()

        root_0 = None

        set71 = None

        set71_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:147:6: ( LT | LTE | EQ | NEQ | GTE | GT )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set71 = self.input.LT(1)

                if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set71))

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
                self.memoize(self.input, 16, relop_StartIndex, success)


            pass
        return retval

    # $ANTLR end "relop"

    # $ANTLR start "synpred2_Miranda"
    def synpred2_Miranda_fragment(self, ):
        # grammars/Miranda.g:103:15: ( OR expression )
        # grammars/Miranda.g:103:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred2_Miranda577)

        self._state.following.append(self.FOLLOW_expression_in_synpred2_Miranda580)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred2_Miranda"



    # $ANTLR start "synpred3_Miranda"
    def synpred3_Miranda_fragment(self, ):
        # grammars/Miranda.g:105:15: ( AND expression )
        # grammars/Miranda.g:105:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred3_Miranda592)

        self._state.following.append(self.FOLLOW_expression_in_synpred3_Miranda595)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred3_Miranda"



    # $ANTLR start "synpred4_Miranda"
    def synpred4_Miranda_fragment(self, ):
        # grammars/Miranda.g:107:15: ( relop expression )
        # grammars/Miranda.g:107:15: relop expression
        pass 
        self._state.following.append(self.FOLLOW_relop_in_synpred4_Miranda607)
        self.relop()

        self._state.following.pop()

        self._state.following.append(self.FOLLOW_expression_in_synpred4_Miranda609)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred4_Miranda"



    # $ANTLR start "synpred8_Miranda"
    def synpred8_Miranda_fragment(self, ):
        # grammars/Miranda.g:109:15: ( ( ADD | MIN | CONCAT | SUBTRACT ) expr5 )
        # grammars/Miranda.g:109:15: ( ADD | MIN | CONCAT | SUBTRACT ) expr5
        pass 
        if self.input.LA(1) == ADD or self.input.LA(1) == CONCAT or self.input.LA(1) == MIN or self.input.LA(1) == SUBTRACT:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr5_in_synpred8_Miranda635)
        self.expr5()

        self._state.following.pop()



    # $ANTLR end "synpred8_Miranda"



    # $ANTLR start "synpred10_Miranda"
    def synpred10_Miranda_fragment(self, ):
        # grammars/Miranda.g:111:15: ( ( DIV | MUL ) expr6 )
        # grammars/Miranda.g:111:15: ( DIV | MUL ) expr6
        pass 
        if self.input.LA(1) == DIV or self.input.LA(1) == MUL:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr6_in_synpred10_Miranda655)
        self.expr6()

        self._state.following.pop()



    # $ANTLR end "synpred10_Miranda"



    # $ANTLR start "synpred12_Miranda"
    def synpred12_Miranda_fragment(self, ):
        # grammars/Miranda.g:113:15: ( ( IDIV | MOD ) expr7 )
        # grammars/Miranda.g:113:15: ( IDIV | MOD ) expr7
        pass 
        if self.input.LA(1) == IDIV or self.input.LA(1) == MOD:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr7_in_synpred12_Miranda675)
        self.expr7()

        self._state.following.pop()



    # $ANTLR end "synpred12_Miranda"



    # $ANTLR start "synpred13_Miranda"
    def synpred13_Miranda_fragment(self, ):
        # grammars/Miranda.g:115:15: ( ( EXP ) expr8 )
        # grammars/Miranda.g:115:15: ( EXP ) expr8
        pass 
        # grammars/Miranda.g:115:15: ( EXP )
        # grammars/Miranda.g:115:16: EXP
        pass 
        self.match(self.input, EXP, self.FOLLOW_EXP_in_synpred13_Miranda688)




        self._state.following.append(self.FOLLOW_expr8_in_synpred13_Miranda692)
        self.expr8()

        self._state.following.pop()



    # $ANTLR end "synpred13_Miranda"



    # $ANTLR start "synpred14_Miranda"
    def synpred14_Miranda_fragment(self, ):
        # grammars/Miranda.g:117:8: ( aexpr )
        # grammars/Miranda.g:117:8: aexpr
        pass 
        self._state.following.append(self.FOLLOW_aexpr_in_synpred14_Miranda701)
        self.aexpr()

        self._state.following.pop()



    # $ANTLR end "synpred14_Miranda"



    # $ANTLR start "synpred22_Miranda"
    def synpred22_Miranda_fragment(self, ):
        # grammars/Miranda.g:127:6: ( section )
        # grammars/Miranda.g:127:6: section
        pass 
        self._state.following.append(self.FOLLOW_section_in_synpred22_Miranda763)
        self.section()

        self._state.following.pop()



    # $ANTLR end "synpred22_Miranda"



    # $ANTLR start "synpred24_Miranda"
    def synpred24_Miranda_fragment(self, ):
        # grammars/Miranda.g:128:6: ( LPAREN expression ( COMMA expression )+ RPAREN )
        # grammars/Miranda.g:128:6: LPAREN expression ( COMMA expression )+ RPAREN
        pass 
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred24_Miranda770)

        self._state.following.append(self.FOLLOW_expression_in_synpred24_Miranda772)
        self.expression()

        self._state.following.pop()

        # grammars/Miranda.g:128:24: ( COMMA expression )+
        cnt18 = 0
        while True: #loop18
            alt18 = 2
            LA18_0 = self.input.LA(1)

            if (LA18_0 == COMMA) :
                alt18 = 1


            if alt18 == 1:
                # grammars/Miranda.g:128:25: COMMA expression
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred24_Miranda775)

                self._state.following.append(self.FOLLOW_expression_in_synpred24_Miranda777)
                self.expression()

                self._state.following.pop()


            else:
                if cnt18 >= 1:
                    break #loop18

                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                eee = EarlyExitException(18, self.input)
                raise eee

            cnt18 += 1


        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred24_Miranda781)



    # $ANTLR end "synpred24_Miranda"



    # $ANTLR start "synpred25_Miranda"
    def synpred25_Miranda_fragment(self, ):
        # grammars/Miranda.g:130:6: ( LPAREN expression RPAREN )
        # grammars/Miranda.g:130:6: LPAREN expression RPAREN
        pass 
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred25_Miranda802)

        self._state.following.append(self.FOLLOW_expression_in_synpred25_Miranda805)
        self.expression()

        self._state.following.pop()

        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred25_Miranda807)



    # $ANTLR end "synpred25_Miranda"




    def synpred22_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred22_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

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

    def synpred12_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred12_Miranda_fragment()
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

    def synpred25_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred25_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred10_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred10_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred14_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred14_Miranda_fragment()
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

    def synpred8_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred8_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred24_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred24_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred13_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred13_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_definition_in_program523 = frozenset([11])
    FOLLOW_DEDENT_in_program525 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_program530 = frozenset([])
    FOLLOW_EOF_in_program532 = frozenset([1])
    FOLLOW_ID_in_definition543 = frozenset([25])
    FOLLOW_IS_in_definition545 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_definition547 = frozenset([1])
    FOLLOW_expr1_in_expression567 = frozenset([1])
    FOLLOW_expr2_in_expr1574 = frozenset([1, 37])
    FOLLOW_OR_in_expr1577 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_expr1580 = frozenset([1, 37])
    FOLLOW_expr3_in_expr2589 = frozenset([1, 6])
    FOLLOW_AND_in_expr2592 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_expr2595 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3604 = frozenset([1, 16, 20, 21, 29, 30, 34])
    FOLLOW_relop_in_expr3607 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_expr3609 = frozenset([1, 16, 20, 21, 29, 30, 34])
    FOLLOW_expr5_in_expr4618 = frozenset([1, 4, 10, 31, 43])
    FOLLOW_ADD_in_expr4622 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_MIN_in_expr4625 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_CONCAT_in_expr4628 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_SUBTRACT_in_expr4631 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr5_in_expr4635 = frozenset([1, 4, 10, 31, 43])
    FOLLOW_expr6_in_expr5644 = frozenset([1, 13, 33])
    FOLLOW_DIV_in_expr5648 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_MUL_in_expr5651 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr6_in_expr5655 = frozenset([1, 13, 33])
    FOLLOW_expr7_in_expr6664 = frozenset([1, 23, 32])
    FOLLOW_IDIV_in_expr6668 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_MOD_in_expr6671 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr7_in_expr6675 = frozenset([1, 23, 32])
    FOLLOW_expr8_in_expr7684 = frozenset([1, 17])
    FOLLOW_EXP_in_expr7688 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr8_in_expr7692 = frozenset([1, 17])
    FOLLOW_aexpr_in_expr8701 = frozenset([1, 7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_ID_in_aexpr713 = frozenset([1])
    FOLLOW_INT_in_aexpr720 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr726 = frozenset([1])
    FOLLOW_CHAR_in_aexpr733 = frozenset([1])
    FOLLOW_STRING_in_aexpr740 = frozenset([1])
    FOLLOW_NOT_in_aexpr747 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_aexpr749 = frozenset([1])
    FOLLOW_boolean_in_aexpr756 = frozenset([1])
    FOLLOW_section_in_aexpr763 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr770 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_aexpr772 = frozenset([8])
    FOLLOW_COMMA_in_aexpr775 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_aexpr777 = frozenset([8, 39])
    FOLLOW_RPAREN_in_aexpr781 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr802 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_aexpr805 = frozenset([39])
    FOLLOW_RPAREN_in_aexpr807 = frozenset([1])
    FOLLOW_LBRACKET_in_aexpr815 = frozenset([7, 8, 18, 19, 22, 24, 26, 28, 35, 38, 42, 44])
    FOLLOW_expression_in_aexpr817 = frozenset([8, 38])
    FOLLOW_COMMA_in_aexpr821 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_aexpr823 = frozenset([8, 38])
    FOLLOW_RBRACKET_in_aexpr827 = frozenset([1])
    FOLLOW_LPAREN_in_section852 = frozenset([4, 6, 10, 13, 16, 17, 20, 21, 23, 29, 30, 31, 32, 33, 34, 37, 43])
    FOLLOW_operator_in_section854 = frozenset([39])
    FOLLOW_RPAREN_in_section856 = frozenset([1])
    FOLLOW_LPAREN_in_section873 = frozenset([4, 6, 10, 13, 16, 17, 20, 21, 23, 29, 30, 31, 32, 33, 34, 37, 43])
    FOLLOW_operator_in_section875 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_section877 = frozenset([39])
    FOLLOW_RPAREN_in_section879 = frozenset([1])
    FOLLOW_LPAREN_in_section898 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_section900 = frozenset([4, 6, 10, 13, 16, 17, 20, 21, 23, 29, 30, 31, 32, 33, 34, 37, 43])
    FOLLOW_operator_in_section902 = frozenset([39])
    FOLLOW_RPAREN_in_section904 = frozenset([1])
    FOLLOW_OR_in_synpred2_Miranda577 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_synpred2_Miranda580 = frozenset([1])
    FOLLOW_AND_in_synpred3_Miranda592 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_synpred3_Miranda595 = frozenset([1])
    FOLLOW_relop_in_synpred4_Miranda607 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_synpred4_Miranda609 = frozenset([1])
    FOLLOW_set_in_synpred8_Miranda621 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr5_in_synpred8_Miranda635 = frozenset([1])
    FOLLOW_set_in_synpred10_Miranda647 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr6_in_synpred10_Miranda655 = frozenset([1])
    FOLLOW_set_in_synpred12_Miranda667 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr7_in_synpred12_Miranda675 = frozenset([1])
    FOLLOW_EXP_in_synpred13_Miranda688 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expr8_in_synpred13_Miranda692 = frozenset([1])
    FOLLOW_aexpr_in_synpred14_Miranda701 = frozenset([1])
    FOLLOW_section_in_synpred22_Miranda763 = frozenset([1])
    FOLLOW_LPAREN_in_synpred24_Miranda770 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_synpred24_Miranda772 = frozenset([8])
    FOLLOW_COMMA_in_synpred24_Miranda775 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_synpred24_Miranda777 = frozenset([8, 39])
    FOLLOW_RPAREN_in_synpred24_Miranda781 = frozenset([1])
    FOLLOW_LPAREN_in_synpred25_Miranda802 = frozenset([7, 18, 19, 22, 24, 26, 28, 35, 42, 44])
    FOLLOW_expression_in_synpred25_Miranda805 = frozenset([39])
    FOLLOW_RPAREN_in_synpred25_Miranda807 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MirandaLexer", MirandaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
