# $ANTLR 3.4 grammars/Core.g 2011-12-04 14:47:47

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




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




class CoreParser(Parser):
    grammarFileName = "grammars/Core.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(CoreParser, self).__init__(input, state, *args, **kwargs)

        self._state.ruleMemo = {}




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # grammars/Core.g:51:1: start : ( COMMENT | combinator ) ( SCOLON ! combinator | COMMENT )* ( SCOLON !)? EOF !;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)

        start_StartIndex = self.input.index()

        root_0 = None

        COMMENT1 = None
        SCOLON3 = None
        COMMENT5 = None
        SCOLON6 = None
        EOF7 = None
        combinator2 = None

        combinator4 = None


        COMMENT1_tree = None
        SCOLON3_tree = None
        COMMENT5_tree = None
        SCOLON6_tree = None
        EOF7_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:51:6: ( ( COMMENT | combinator ) ( SCOLON ! combinator | COMMENT )* ( SCOLON !)? EOF !)
                # grammars/Core.g:51:8: ( COMMENT | combinator ) ( SCOLON ! combinator | COMMENT )* ( SCOLON !)? EOF !
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Core.g:51:8: ( COMMENT | combinator )
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == COMMENT) :
                    alt1 = 1
                elif (LA1_0 == ID) :
                    alt1 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae


                if alt1 == 1:
                    # grammars/Core.g:51:9: COMMENT
                    pass 
                    COMMENT1 = self.match(self.input, COMMENT, self.FOLLOW_COMMENT_in_start508)
                    if self._state.backtracking == 0:
                        COMMENT1_tree = self._adaptor.createWithPayload(COMMENT1)
                        self._adaptor.addChild(root_0, COMMENT1_tree)




                elif alt1 == 2:
                    # grammars/Core.g:51:19: combinator
                    pass 
                    self._state.following.append(self.FOLLOW_combinator_in_start512)
                    combinator2 = self.combinator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, combinator2.tree)





                # grammars/Core.g:51:31: ( SCOLON ! combinator | COMMENT )*
                while True: #loop2
                    alt2 = 3
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == SCOLON) :
                        LA2_1 = self.input.LA(2)

                        if (LA2_1 == ID) :
                            alt2 = 1


                    elif (LA2_0 == COMMENT) :
                        alt2 = 2


                    if alt2 == 1:
                        # grammars/Core.g:51:32: SCOLON ! combinator
                        pass 
                        SCOLON3 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_start516)

                        self._state.following.append(self.FOLLOW_combinator_in_start519)
                        combinator4 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator4.tree)



                    elif alt2 == 2:
                        # grammars/Core.g:51:53: COMMENT
                        pass 
                        COMMENT5 = self.match(self.input, COMMENT, self.FOLLOW_COMMENT_in_start523)
                        if self._state.backtracking == 0:
                            COMMENT5_tree = self._adaptor.createWithPayload(COMMENT5)
                            self._adaptor.addChild(root_0, COMMENT5_tree)




                    else:
                        break #loop2


                # grammars/Core.g:51:69: ( SCOLON !)?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == SCOLON) :
                    alt3 = 1
                if alt3 == 1:
                    # grammars/Core.g:51:69: SCOLON !
                    pass 
                    SCOLON6 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_start527)




                EOF7 = self.match(self.input, EOF, self.FOLLOW_EOF_in_start531)



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
                self.memoize(self.input, 1, start_StartIndex, success)


            pass
        return retval

    # $ANTLR end "start"


    class combinator_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.combinator_return, self).__init__()

            self.tree = None





    # $ANTLR start "combinator"
    # grammars/Core.g:53:1: combinator : i= ID ( ID )* IS expression -> ^( COMBINATOR[i] ID ( ID )* expression ) ;
    def combinator(self, ):
        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        combinator_StartIndex = self.input.index()

        root_0 = None

        i = None
        ID8 = None
        IS9 = None
        expression10 = None


        i_tree = None
        ID8_tree = None
        IS9_tree = None
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


                # grammars/Core.g:53:11: (i= ID ( ID )* IS expression -> ^( COMBINATOR[i] ID ( ID )* expression ) )
                # grammars/Core.g:53:13: i= ID ( ID )* IS expression
                pass 
                i = self.match(self.input, ID, self.FOLLOW_ID_in_combinator541) 
                if self._state.backtracking == 0:
                    stream_ID.add(i)


                # grammars/Core.g:53:18: ( ID )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammars/Core.g:53:18: ID
                        pass 
                        ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_combinator543) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ID8)



                    else:
                        break #loop4


                IS9 = self.match(self.input, IS, self.FOLLOW_IS_in_combinator546) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS9)


                self._state.following.append(self.FOLLOW_expression_in_combinator548)
                expression10 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression10.tree)


                # AST Rewrite
                # elements: ID, expression, ID
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
                    # 53:36: -> ^( COMBINATOR[i] ID ( ID )* expression )
                    # grammars/Core.g:53:39: ^( COMBINATOR[i] ID ( ID )* expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(COMBINATOR, i)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammars/Core.g:53:58: ( ID )*
                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset();

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
                self.memoize(self.input, 2, combinator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "combinator"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # grammars/Core.g:55:1: expression : ( LET ^ definitions IN ! expression | LETREC ^ definitions IN ! expression | CASE ^ expression OF ! alternatives | LAMBDA ^ ( ID )+ DOT ! expression | expr1 );
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        LET11 = None
        IN13 = None
        LETREC15 = None
        IN17 = None
        CASE19 = None
        OF21 = None
        LAMBDA23 = None
        ID24 = None
        DOT25 = None
        definitions12 = None

        expression14 = None

        definitions16 = None

        expression18 = None

        expression20 = None

        alternatives22 = None

        expression26 = None

        expr127 = None


        LET11_tree = None
        IN13_tree = None
        LETREC15_tree = None
        IN17_tree = None
        CASE19_tree = None
        OF21_tree = None
        LAMBDA23_tree = None
        ID24_tree = None
        DOT25_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:55:11: ( LET ^ definitions IN ! expression | LETREC ^ definitions IN ! expression | CASE ^ expression OF ! alternatives | LAMBDA ^ ( ID )+ DOT ! expression | expr1 )
                alt6 = 5
                LA6 = self.input.LA(1)
                if LA6 == LET:
                    alt6 = 1
                elif LA6 == LETREC:
                    alt6 = 2
                elif LA6 == CASE:
                    alt6 = 3
                elif LA6 == LAMBDA:
                    alt6 = 4
                elif LA6 == ID or LA6 == LPAREN or LA6 == NUMBER or LA6 == PACK:
                    alt6 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammars/Core.g:55:13: LET ^ definitions IN ! expression
                    pass 
                    root_0 = self._adaptor.nil()


                    LET11 = self.match(self.input, LET, self.FOLLOW_LET_in_expression569)
                    if self._state.backtracking == 0:
                        LET11_tree = self._adaptor.createWithPayload(LET11)
                        root_0 = self._adaptor.becomeRoot(LET11_tree, root_0)



                    self._state.following.append(self.FOLLOW_definitions_in_expression572)
                    definitions12 = self.definitions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, definitions12.tree)


                    IN13 = self.match(self.input, IN, self.FOLLOW_IN_in_expression574)

                    self._state.following.append(self.FOLLOW_expression_in_expression577)
                    expression14 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression14.tree)



                elif alt6 == 2:
                    # grammars/Core.g:56:13: LETREC ^ definitions IN ! expression
                    pass 
                    root_0 = self._adaptor.nil()


                    LETREC15 = self.match(self.input, LETREC, self.FOLLOW_LETREC_in_expression591)
                    if self._state.backtracking == 0:
                        LETREC15_tree = self._adaptor.createWithPayload(LETREC15)
                        root_0 = self._adaptor.becomeRoot(LETREC15_tree, root_0)



                    self._state.following.append(self.FOLLOW_definitions_in_expression594)
                    definitions16 = self.definitions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, definitions16.tree)


                    IN17 = self.match(self.input, IN, self.FOLLOW_IN_in_expression596)

                    self._state.following.append(self.FOLLOW_expression_in_expression599)
                    expression18 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression18.tree)



                elif alt6 == 3:
                    # grammars/Core.g:57:13: CASE ^ expression OF ! alternatives
                    pass 
                    root_0 = self._adaptor.nil()


                    CASE19 = self.match(self.input, CASE, self.FOLLOW_CASE_in_expression613)
                    if self._state.backtracking == 0:
                        CASE19_tree = self._adaptor.createWithPayload(CASE19)
                        root_0 = self._adaptor.becomeRoot(CASE19_tree, root_0)



                    self._state.following.append(self.FOLLOW_expression_in_expression616)
                    expression20 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression20.tree)


                    OF21 = self.match(self.input, OF, self.FOLLOW_OF_in_expression618)

                    self._state.following.append(self.FOLLOW_alternatives_in_expression621)
                    alternatives22 = self.alternatives()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, alternatives22.tree)



                elif alt6 == 4:
                    # grammars/Core.g:58:13: LAMBDA ^ ( ID )+ DOT ! expression
                    pass 
                    root_0 = self._adaptor.nil()


                    LAMBDA23 = self.match(self.input, LAMBDA, self.FOLLOW_LAMBDA_in_expression635)
                    if self._state.backtracking == 0:
                        LAMBDA23_tree = self._adaptor.createWithPayload(LAMBDA23)
                        root_0 = self._adaptor.becomeRoot(LAMBDA23_tree, root_0)



                    # grammars/Core.g:58:21: ( ID )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == ID) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammars/Core.g:58:21: ID
                            pass 
                            ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_expression638)
                            if self._state.backtracking == 0:
                                ID24_tree = self._adaptor.createWithPayload(ID24)
                                self._adaptor.addChild(root_0, ID24_tree)




                        else:
                            if cnt5 >= 1:
                                break #loop5

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    DOT25 = self.match(self.input, DOT, self.FOLLOW_DOT_in_expression641)

                    self._state.following.append(self.FOLLOW_expression_in_expression644)
                    expression26 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression26.tree)



                elif alt6 == 5:
                    # grammars/Core.g:59:13: expr1
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expr1_in_expression658)
                    expr127 = self.expr1()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr127.tree)



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


    class alternatives_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.alternatives_return, self).__init__()

            self.tree = None





    # $ANTLR start "alternatives"
    # grammars/Core.g:62:1: alternatives : alternative ( SCOLON ! alternative )* ;
    def alternatives(self, ):
        retval = self.alternatives_return()
        retval.start = self.input.LT(1)

        alternatives_StartIndex = self.input.index()

        root_0 = None

        SCOLON29 = None
        alternative28 = None

        alternative30 = None


        SCOLON29_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:62:13: ( alternative ( SCOLON ! alternative )* )
                # grammars/Core.g:62:15: alternative ( SCOLON ! alternative )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_alternative_in_alternatives676)
                alternative28 = self.alternative()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, alternative28.tree)


                # grammars/Core.g:62:27: ( SCOLON ! alternative )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == SCOLON) :
                        LA7_1 = self.input.LA(2)

                        if (self.synpred11_Core()) :
                            alt7 = 1




                    if alt7 == 1:
                        # grammars/Core.g:62:28: SCOLON ! alternative
                        pass 
                        SCOLON29 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_alternatives679)

                        self._state.following.append(self.FOLLOW_alternative_in_alternatives682)
                        alternative30 = self.alternative()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, alternative30.tree)



                    else:
                        break #loop7




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
                self.memoize(self.input, 4, alternatives_StartIndex, success)


            pass
        return retval

    # $ANTLR end "alternatives"


    class alternative_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.alternative_return, self).__init__()

            self.tree = None





    # $ANTLR start "alternative"
    # grammars/Core.g:63:1: alternative : LT ! NUMBER GT ! ARROW ^ expression ;
    def alternative(self, ):
        retval = self.alternative_return()
        retval.start = self.input.LT(1)

        alternative_StartIndex = self.input.index()

        root_0 = None

        LT31 = None
        NUMBER32 = None
        GT33 = None
        ARROW34 = None
        expression35 = None


        LT31_tree = None
        NUMBER32_tree = None
        GT33_tree = None
        ARROW34_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:63:12: ( LT ! NUMBER GT ! ARROW ^ expression )
                # grammars/Core.g:63:14: LT ! NUMBER GT ! ARROW ^ expression
                pass 
                root_0 = self._adaptor.nil()


                LT31 = self.match(self.input, LT, self.FOLLOW_LT_in_alternative690)

                NUMBER32 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_alternative693)
                if self._state.backtracking == 0:
                    NUMBER32_tree = self._adaptor.createWithPayload(NUMBER32)
                    self._adaptor.addChild(root_0, NUMBER32_tree)



                GT33 = self.match(self.input, GT, self.FOLLOW_GT_in_alternative695)

                ARROW34 = self.match(self.input, ARROW, self.FOLLOW_ARROW_in_alternative698)
                if self._state.backtracking == 0:
                    ARROW34_tree = self._adaptor.createWithPayload(ARROW34)
                    root_0 = self._adaptor.becomeRoot(ARROW34_tree, root_0)



                self._state.following.append(self.FOLLOW_expression_in_alternative701)
                expression35 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression35.tree)




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
                self.memoize(self.input, 5, alternative_StartIndex, success)


            pass
        return retval

    # $ANTLR end "alternative"


    class definitions_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.definitions_return, self).__init__()

            self.tree = None





    # $ANTLR start "definitions"
    # grammars/Core.g:65:1: definitions : definition ( SCOLON ! definition )* ;
    def definitions(self, ):
        retval = self.definitions_return()
        retval.start = self.input.LT(1)

        definitions_StartIndex = self.input.index()

        root_0 = None

        SCOLON37 = None
        definition36 = None

        definition38 = None


        SCOLON37_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:65:12: ( definition ( SCOLON ! definition )* )
                # grammars/Core.g:65:14: definition ( SCOLON ! definition )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_definition_in_definitions708)
                definition36 = self.definition()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, definition36.tree)


                # grammars/Core.g:65:25: ( SCOLON ! definition )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == SCOLON) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammars/Core.g:65:26: SCOLON ! definition
                        pass 
                        SCOLON37 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_definitions711)

                        self._state.following.append(self.FOLLOW_definition_in_definitions714)
                        definition38 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition38.tree)



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
                self.memoize(self.input, 6, definitions_StartIndex, success)


            pass
        return retval

    # $ANTLR end "definitions"


    class definition_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.definition_return, self).__init__()

            self.tree = None





    # $ANTLR start "definition"
    # grammars/Core.g:66:1: definition : ID IS ^ expression ;
    def definition(self, ):
        retval = self.definition_return()
        retval.start = self.input.LT(1)

        definition_StartIndex = self.input.index()

        root_0 = None

        ID39 = None
        IS40 = None
        expression41 = None


        ID39_tree = None
        IS40_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:66:11: ( ID IS ^ expression )
                # grammars/Core.g:66:13: ID IS ^ expression
                pass 
                root_0 = self._adaptor.nil()


                ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_definition722)
                if self._state.backtracking == 0:
                    ID39_tree = self._adaptor.createWithPayload(ID39)
                    self._adaptor.addChild(root_0, ID39_tree)



                IS40 = self.match(self.input, IS, self.FOLLOW_IS_in_definition724)
                if self._state.backtracking == 0:
                    IS40_tree = self._adaptor.createWithPayload(IS40)
                    root_0 = self._adaptor.becomeRoot(IS40_tree, root_0)



                self._state.following.append(self.FOLLOW_expression_in_definition727)
                expression41 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression41.tree)




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
                self.memoize(self.input, 7, definition_StartIndex, success)


            pass
        return retval

    # $ANTLR end "definition"


    class expr1_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr1_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr1"
    # grammars/Core.g:68:1: expr1 : expr2 ( OR ^ expr1 )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR43 = None
        expr242 = None

        expr144 = None


        OR43_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:68:6: ( expr2 ( OR ^ expr1 )* )
                # grammars/Core.g:68:8: expr2 ( OR ^ expr1 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1734)
                expr242 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr242.tree)


                # grammars/Core.g:68:14: ( OR ^ expr1 )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OR) :
                        LA9_2 = self.input.LA(2)

                        if (self.synpred13_Core()) :
                            alt9 = 1




                    if alt9 == 1:
                        # grammars/Core.g:68:15: OR ^ expr1
                        pass 
                        OR43 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1737)
                        if self._state.backtracking == 0:
                            OR43_tree = self._adaptor.createWithPayload(OR43)
                            root_0 = self._adaptor.becomeRoot(OR43_tree, root_0)



                        self._state.following.append(self.FOLLOW_expr1_in_expr1740)
                        expr144 = self.expr1()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr144.tree)



                    else:
                        break #loop9




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
                self.memoize(self.input, 8, expr1_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr1"


    class expr2_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr2_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr2"
    # grammars/Core.g:71:1: expr2 : expr3 ( AND ^ expr2 )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND46 = None
        expr345 = None

        expr247 = None


        AND46_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:71:6: ( expr3 ( AND ^ expr2 )* )
                # grammars/Core.g:71:8: expr3 ( AND ^ expr2 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2755)
                expr345 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr345.tree)


                # grammars/Core.g:71:14: ( AND ^ expr2 )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == AND) :
                        LA10_2 = self.input.LA(2)

                        if (self.synpred14_Core()) :
                            alt10 = 1




                    if alt10 == 1:
                        # grammars/Core.g:71:15: AND ^ expr2
                        pass 
                        AND46 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2758)
                        if self._state.backtracking == 0:
                            AND46_tree = self._adaptor.createWithPayload(AND46)
                            root_0 = self._adaptor.becomeRoot(AND46_tree, root_0)



                        self._state.following.append(self.FOLLOW_expr2_in_expr2761)
                        expr247 = self.expr2()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr247.tree)



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
                self.memoize(self.input, 9, expr2_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr2"


    class expr3_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr3_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr3"
    # grammars/Core.g:74:1: expr3 : expr4 ( relop ^ expr4 )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        expr448 = None

        relop49 = None

        expr450 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:74:6: ( expr4 ( relop ^ expr4 )* )
                # grammars/Core.g:74:8: expr4 ( relop ^ expr4 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3776)
                expr448 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr448.tree)


                # grammars/Core.g:74:14: ( relop ^ expr4 )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((EQ <= LA11_0 <= GTE) or (LT <= LA11_0 <= LTE) or LA11_0 == NEQ) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammars/Core.g:74:15: relop ^ expr4
                        pass 
                        self._state.following.append(self.FOLLOW_relop_in_expr3779)
                        relop49 = self.relop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(relop49.tree, root_0)


                        self._state.following.append(self.FOLLOW_expr4_in_expr3782)
                        expr450 = self.expr4()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr450.tree)



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
                self.memoize(self.input, 10, expr3_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr3"


    class expr4_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr4_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr4"
    # grammars/Core.g:77:1: expr4 : expr5 ( ( ADD ^| MIN ^) expr4 )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD52 = None
        MIN53 = None
        expr551 = None

        expr454 = None


        ADD52_tree = None
        MIN53_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:77:6: ( expr5 ( ( ADD ^| MIN ^) expr4 )* )
                # grammars/Core.g:77:8: expr5 ( ( ADD ^| MIN ^) expr4 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4797)
                expr551 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr551.tree)


                # grammars/Core.g:77:14: ( ( ADD ^| MIN ^) expr4 )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == ADD) :
                        LA13_2 = self.input.LA(2)

                        if (self.synpred17_Core()) :
                            alt13 = 1


                    elif (LA13_0 == MIN) :
                        LA13_3 = self.input.LA(2)

                        if (self.synpred17_Core()) :
                            alt13 = 1




                    if alt13 == 1:
                        # grammars/Core.g:77:15: ( ADD ^| MIN ^) expr4
                        pass 
                        # grammars/Core.g:77:15: ( ADD ^| MIN ^)
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == ADD) :
                            alt12 = 1
                        elif (LA12_0 == MIN) :
                            alt12 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 12, 0, self.input)

                            raise nvae


                        if alt12 == 1:
                            # grammars/Core.g:77:16: ADD ^
                            pass 
                            ADD52 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4801)
                            if self._state.backtracking == 0:
                                ADD52_tree = self._adaptor.createWithPayload(ADD52)
                                root_0 = self._adaptor.becomeRoot(ADD52_tree, root_0)




                        elif alt12 == 2:
                            # grammars/Core.g:77:21: MIN ^
                            pass 
                            MIN53 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4804)
                            if self._state.backtracking == 0:
                                MIN53_tree = self._adaptor.createWithPayload(MIN53)
                                root_0 = self._adaptor.becomeRoot(MIN53_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr4_in_expr4808)
                        expr454 = self.expr4()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr454.tree)



                    else:
                        break #loop13




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
                self.memoize(self.input, 11, expr4_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr4"


    class expr5_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr5_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr5"
    # grammars/Core.g:80:1: expr5 : expr6 ( ( DIV ^| MUL ^) expr6 )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV56 = None
        MUL57 = None
        expr655 = None

        expr658 = None


        DIV56_tree = None
        MUL57_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:80:6: ( expr6 ( ( DIV ^| MUL ^) expr6 )* )
                # grammars/Core.g:80:8: expr6 ( ( DIV ^| MUL ^) expr6 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr5823)
                expr655 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr655.tree)


                # grammars/Core.g:80:14: ( ( DIV ^| MUL ^) expr6 )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == DIV or LA15_0 == MUL) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammars/Core.g:80:15: ( DIV ^| MUL ^) expr6
                        pass 
                        # grammars/Core.g:80:15: ( DIV ^| MUL ^)
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == DIV) :
                            alt14 = 1
                        elif (LA14_0 == MUL) :
                            alt14 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 14, 0, self.input)

                            raise nvae


                        if alt14 == 1:
                            # grammars/Core.g:80:16: DIV ^
                            pass 
                            DIV56 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5827)
                            if self._state.backtracking == 0:
                                DIV56_tree = self._adaptor.createWithPayload(DIV56)
                                root_0 = self._adaptor.becomeRoot(DIV56_tree, root_0)




                        elif alt14 == 2:
                            # grammars/Core.g:80:21: MUL ^
                            pass 
                            MUL57 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5830)
                            if self._state.backtracking == 0:
                                MUL57_tree = self._adaptor.createWithPayload(MUL57)
                                root_0 = self._adaptor.becomeRoot(MUL57_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr6_in_expr5834)
                        expr658 = self.expr6()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr658.tree)



                    else:
                        break #loop15




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
                self.memoize(self.input, 12, expr5_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr5"


    class expr6_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr6_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr6"
    # grammars/Core.g:83:1: expr6 : (lst+= aexpr !)+ ;
    def expr6(self, ):
        retval = self.expr6_return()
        retval.start = self.input.LT(1)

        expr6_StartIndex = self.input.index()

        root_0 = None

        list_lst = None
        lst = None

        lst = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:83:6: ( (lst+= aexpr !)+ )
                # grammars/Core.g:83:8: (lst+= aexpr !)+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Core.g:83:8: (lst+= aexpr !)+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ID or LA16_0 == LPAREN or LA16_0 == NUMBER or LA16_0 == PACK) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammars/Core.g:83:9: lst+= aexpr !
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr6852)
                        lst = self.aexpr()

                        self._state.following.pop()
                        if list_lst is None:
                            list_lst = []
                        list_lst.append(lst.tree)



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1


                if self._state.backtracking == 0:
                    pass
                                          
                    if len(list_lst) >= 2:
                       chain = self._adaptor.nil()
                       b = self._adaptor.createFromType(APPLICATION, "APPLICATION")
                       list_lst.reverse()
                       item = list_lst.pop()
                       b.addChild(list_lst.pop())
                       b.addChild(item)
                       chain = self._adaptor.becomeRoot(b, chain)
                       while len(list_lst) > 0:
                          a = self._adaptor.createFromType(APPLICATION, "APPLICATION")
                          a.addChild(list_lst.pop())
                          a.addChild(chain)
                          chain = a
                       self._adaptor.addChild(root_0, chain)
                    else:
                       self._adaptor.addChild(root_0, list_lst[0])
                       





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
                self.memoize(self.input, 13, expr6_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr6"


    class aexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.aexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "aexpr"
    # grammars/Core.g:103:1: aexpr : ( ID | NUMBER | PACK ^ LCURLY ! NUMBER COMMA ! NUMBER RCURLY !| LPAREN ! expr1 RPAREN !);
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID59 = None
        NUMBER60 = None
        PACK61 = None
        LCURLY62 = None
        NUMBER63 = None
        COMMA64 = None
        NUMBER65 = None
        RCURLY66 = None
        LPAREN67 = None
        RPAREN69 = None
        expr168 = None


        ID59_tree = None
        NUMBER60_tree = None
        PACK61_tree = None
        LCURLY62_tree = None
        NUMBER63_tree = None
        COMMA64_tree = None
        NUMBER65_tree = None
        RCURLY66_tree = None
        LPAREN67_tree = None
        RPAREN69_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:103:6: ( ID | NUMBER | PACK ^ LCURLY ! NUMBER COMMA ! NUMBER RCURLY !| LPAREN ! expr1 RPAREN !)
                alt17 = 4
                LA17 = self.input.LA(1)
                if LA17 == ID:
                    alt17 = 1
                elif LA17 == NUMBER:
                    alt17 = 2
                elif LA17 == PACK:
                    alt17 = 3
                elif LA17 == LPAREN:
                    alt17 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammars/Core.g:103:8: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr865)
                    if self._state.backtracking == 0:
                        ID59_tree = self._adaptor.createWithPayload(ID59)
                        self._adaptor.addChild(root_0, ID59_tree)




                elif alt17 == 2:
                    # grammars/Core.g:104:8: NUMBER
                    pass 
                    root_0 = self._adaptor.nil()


                    NUMBER60 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_aexpr874)
                    if self._state.backtracking == 0:
                        NUMBER60_tree = self._adaptor.createWithPayload(NUMBER60)
                        self._adaptor.addChild(root_0, NUMBER60_tree)




                elif alt17 == 3:
                    # grammars/Core.g:105:8: PACK ^ LCURLY ! NUMBER COMMA ! NUMBER RCURLY !
                    pass 
                    root_0 = self._adaptor.nil()


                    PACK61 = self.match(self.input, PACK, self.FOLLOW_PACK_in_aexpr883)
                    if self._state.backtracking == 0:
                        PACK61_tree = self._adaptor.createWithPayload(PACK61)
                        root_0 = self._adaptor.becomeRoot(PACK61_tree, root_0)



                    LCURLY62 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_aexpr886)

                    NUMBER63 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_aexpr889)
                    if self._state.backtracking == 0:
                        NUMBER63_tree = self._adaptor.createWithPayload(NUMBER63)
                        self._adaptor.addChild(root_0, NUMBER63_tree)



                    COMMA64 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_aexpr891)

                    NUMBER65 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_aexpr894)
                    if self._state.backtracking == 0:
                        NUMBER65_tree = self._adaptor.createWithPayload(NUMBER65)
                        self._adaptor.addChild(root_0, NUMBER65_tree)



                    RCURLY66 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_aexpr896)


                elif alt17 == 4:
                    # grammars/Core.g:106:8: LPAREN ! expr1 RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN67 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr906)

                    self._state.following.append(self.FOLLOW_expr1_in_aexpr909)
                    expr168 = self.expr1()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr168.tree)


                    RPAREN69 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr911)


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
                self.memoize(self.input, 14, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class relop_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.relop_return, self).__init__()

            self.tree = None





    # $ANTLR start "relop"
    # grammars/Core.g:109:1: relop : ( LT | LTE | EQ | NEQ | GTE | GT );
    def relop(self, ):
        retval = self.relop_return()
        retval.start = self.input.LT(1)

        relop_StartIndex = self.input.index()

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


                # grammars/Core.g:109:6: ( LT | LTE | EQ | NEQ | GTE | GT )
                # grammars/Core.g:
                pass 
                root_0 = self._adaptor.nil()


                set70 = self.input.LT(1)

                if (EQ <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
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
                self.memoize(self.input, 15, relop_StartIndex, success)


            pass
        return retval

    # $ANTLR end "relop"

    # $ANTLR start "synpred11_Core"
    def synpred11_Core_fragment(self, ):
        # grammars/Core.g:62:28: ( SCOLON alternative )
        # grammars/Core.g:62:28: SCOLON alternative
        pass 
        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_synpred11_Core679)

        self._state.following.append(self.FOLLOW_alternative_in_synpred11_Core682)
        self.alternative()

        self._state.following.pop()



    # $ANTLR end "synpred11_Core"



    # $ANTLR start "synpred13_Core"
    def synpred13_Core_fragment(self, ):
        # grammars/Core.g:68:15: ( OR expr1 )
        # grammars/Core.g:68:15: OR expr1
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred13_Core737)

        self._state.following.append(self.FOLLOW_expr1_in_synpred13_Core740)
        self.expr1()

        self._state.following.pop()



    # $ANTLR end "synpred13_Core"



    # $ANTLR start "synpred14_Core"
    def synpred14_Core_fragment(self, ):
        # grammars/Core.g:71:15: ( AND expr2 )
        # grammars/Core.g:71:15: AND expr2
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred14_Core758)

        self._state.following.append(self.FOLLOW_expr2_in_synpred14_Core761)
        self.expr2()

        self._state.following.pop()



    # $ANTLR end "synpred14_Core"



    # $ANTLR start "synpred17_Core"
    def synpred17_Core_fragment(self, ):
        # grammars/Core.g:77:15: ( ( ADD | MIN ) expr4 )
        # grammars/Core.g:77:15: ( ADD | MIN ) expr4
        pass 
        if self.input.LA(1) == ADD or self.input.LA(1) == MIN:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr4_in_synpred17_Core808)
        self.expr4()

        self._state.following.pop()



    # $ANTLR end "synpred17_Core"




    def synpred11_Core(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred11_Core_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred14_Core(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred14_Core_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred13_Core(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred13_Core_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred17_Core(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_Core_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_COMMENT_in_start508 = frozenset([12, 38])
    FOLLOW_combinator_in_start512 = frozenset([12, 38])
    FOLLOW_SCOLON_in_start516 = frozenset([18])
    FOLLOW_combinator_in_start519 = frozenset([12, 38])
    FOLLOW_COMMENT_in_start523 = frozenset([12, 38])
    FOLLOW_SCOLON_in_start527 = frozenset([])
    FOLLOW_EOF_in_start531 = frozenset([1])
    FOLLOW_ID_in_combinator541 = frozenset([18, 20])
    FOLLOW_ID_in_combinator543 = frozenset([18, 20])
    FOLLOW_IS_in_combinator546 = frozenset([8, 18, 21, 23, 24, 25, 32, 35])
    FOLLOW_expression_in_combinator548 = frozenset([1])
    FOLLOW_LET_in_expression569 = frozenset([18])
    FOLLOW_definitions_in_expression572 = frozenset([19])
    FOLLOW_IN_in_expression574 = frozenset([8, 18, 21, 23, 24, 25, 32, 35])
    FOLLOW_expression_in_expression577 = frozenset([1])
    FOLLOW_LETREC_in_expression591 = frozenset([18])
    FOLLOW_definitions_in_expression594 = frozenset([19])
    FOLLOW_IN_in_expression596 = frozenset([8, 18, 21, 23, 24, 25, 32, 35])
    FOLLOW_expression_in_expression599 = frozenset([1])
    FOLLOW_CASE_in_expression613 = frozenset([8, 18, 21, 23, 24, 25, 32, 35])
    FOLLOW_expression_in_expression616 = frozenset([33])
    FOLLOW_OF_in_expression618 = frozenset([26])
    FOLLOW_alternatives_in_expression621 = frozenset([1])
    FOLLOW_LAMBDA_in_expression635 = frozenset([18])
    FOLLOW_ID_in_expression638 = frozenset([14, 18])
    FOLLOW_DOT_in_expression641 = frozenset([8, 18, 21, 23, 24, 25, 32, 35])
    FOLLOW_expression_in_expression644 = frozenset([1])
    FOLLOW_expr1_in_expression658 = frozenset([1])
    FOLLOW_alternative_in_alternatives676 = frozenset([1, 38])
    FOLLOW_SCOLON_in_alternatives679 = frozenset([26])
    FOLLOW_alternative_in_alternatives682 = frozenset([1, 38])
    FOLLOW_LT_in_alternative690 = frozenset([32])
    FOLLOW_NUMBER_in_alternative693 = frozenset([16])
    FOLLOW_GT_in_alternative695 = frozenset([7])
    FOLLOW_ARROW_in_alternative698 = frozenset([8, 18, 21, 23, 24, 25, 32, 35])
    FOLLOW_expression_in_alternative701 = frozenset([1])
    FOLLOW_definition_in_definitions708 = frozenset([1, 38])
    FOLLOW_SCOLON_in_definitions711 = frozenset([18])
    FOLLOW_definition_in_definitions714 = frozenset([1, 38])
    FOLLOW_ID_in_definition722 = frozenset([20])
    FOLLOW_IS_in_definition724 = frozenset([8, 18, 21, 23, 24, 25, 32, 35])
    FOLLOW_expression_in_definition727 = frozenset([1])
    FOLLOW_expr2_in_expr1734 = frozenset([1, 34])
    FOLLOW_OR_in_expr1737 = frozenset([18, 25, 32, 35])
    FOLLOW_expr1_in_expr1740 = frozenset([1, 34])
    FOLLOW_expr3_in_expr2755 = frozenset([1, 5])
    FOLLOW_AND_in_expr2758 = frozenset([18, 25, 32, 35])
    FOLLOW_expr2_in_expr2761 = frozenset([1, 5])
    FOLLOW_expr4_in_expr3776 = frozenset([1, 15, 16, 17, 26, 27, 30])
    FOLLOW_relop_in_expr3779 = frozenset([18, 25, 32, 35])
    FOLLOW_expr4_in_expr3782 = frozenset([1, 15, 16, 17, 26, 27, 30])
    FOLLOW_expr5_in_expr4797 = frozenset([1, 4, 28])
    FOLLOW_ADD_in_expr4801 = frozenset([18, 25, 32, 35])
    FOLLOW_MIN_in_expr4804 = frozenset([18, 25, 32, 35])
    FOLLOW_expr4_in_expr4808 = frozenset([1, 4, 28])
    FOLLOW_expr6_in_expr5823 = frozenset([1, 13, 29])
    FOLLOW_DIV_in_expr5827 = frozenset([18, 25, 32, 35])
    FOLLOW_MUL_in_expr5830 = frozenset([18, 25, 32, 35])
    FOLLOW_expr6_in_expr5834 = frozenset([1, 13, 29])
    FOLLOW_aexpr_in_expr6852 = frozenset([1, 18, 25, 32, 35])
    FOLLOW_ID_in_aexpr865 = frozenset([1])
    FOLLOW_NUMBER_in_aexpr874 = frozenset([1])
    FOLLOW_PACK_in_aexpr883 = frozenset([22])
    FOLLOW_LCURLY_in_aexpr886 = frozenset([32])
    FOLLOW_NUMBER_in_aexpr889 = frozenset([11])
    FOLLOW_COMMA_in_aexpr891 = frozenset([32])
    FOLLOW_NUMBER_in_aexpr894 = frozenset([36])
    FOLLOW_RCURLY_in_aexpr896 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr906 = frozenset([18, 25, 32, 35])
    FOLLOW_expr1_in_aexpr909 = frozenset([37])
    FOLLOW_RPAREN_in_aexpr911 = frozenset([1])
    FOLLOW_SCOLON_in_synpred11_Core679 = frozenset([26])
    FOLLOW_alternative_in_synpred11_Core682 = frozenset([1])
    FOLLOW_OR_in_synpred13_Core737 = frozenset([18, 25, 32, 35])
    FOLLOW_expr1_in_synpred13_Core740 = frozenset([1])
    FOLLOW_AND_in_synpred14_Core758 = frozenset([18, 25, 32, 35])
    FOLLOW_expr2_in_synpred14_Core761 = frozenset([1])
    FOLLOW_set_in_synpred17_Core800 = frozenset([18, 25, 32, 35])
    FOLLOW_expr4_in_synpred17_Core808 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("CoreLexer", CoreParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
