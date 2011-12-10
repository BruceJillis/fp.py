# $ANTLR 3.4 grammars/Core.g 2011-12-10 23:48:13

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *


        
from common import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ADD=4
ALTERNATIVE=5
AND=6
APPLICATION=7
ARROW=8
CASE=9
COLON=10
COMBINATOR=11
COMMA=12
COMMENT=13
DEFINITION=14
DIV=15
DOT=16
EQ=17
GT=18
GTE=19
ID=20
IN=21
IS=22
LAMBDA=23
LCURLY=24
LET=25
LETREC=26
LPAREN=27
LT=28
LTE=29
MIN=30
MUL=31
NEQ=32
NOT=33
NUMBER=34
OF=35
OR=36
PACK=37
PROGRAM=38
RCURLY=39
RPAREN=40
SCOLON=41
WHITESPACE=42

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALTERNATIVE", "AND", "APPLICATION", "ARROW", "CASE", "COLON", 
    "COMBINATOR", "COMMA", "COMMENT", "DEFINITION", "DIV", "DOT", "EQ", 
    "GT", "GTE", "ID", "IN", "IS", "LAMBDA", "LCURLY", "LET", "LETREC", 
    "LPAREN", "LT", "LTE", "MIN", "MUL", "NEQ", "NOT", "NUMBER", "OF", "OR", 
    "PACK", "PROGRAM", "RCURLY", "RPAREN", "SCOLON", "WHITESPACE"
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


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.program_return, self).__init__()

            self.tree = None





    # $ANTLR start "program"
    # grammars/Core.g:58:1: program : ( COMMENT | combinator ) ( SCOLON combinator | COMMENT )* ( SCOLON )? EOF -> ^( PROGRAM ( combinator )+ ) ;
    def program(self, ):
        retval = self.program_return()
        retval.start = self.input.LT(1)

        program_StartIndex = self.input.index()

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
        stream_COMMENT = RewriteRuleTokenStream(self._adaptor, "token COMMENT")
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_SCOLON = RewriteRuleTokenStream(self._adaptor, "token SCOLON")
        stream_combinator = RewriteRuleSubtreeStream(self._adaptor, "rule combinator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:59:4: ( ( COMMENT | combinator ) ( SCOLON combinator | COMMENT )* ( SCOLON )? EOF -> ^( PROGRAM ( combinator )+ ) )
                # grammars/Core.g:59:6: ( COMMENT | combinator ) ( SCOLON combinator | COMMENT )* ( SCOLON )? EOF
                pass 
                # grammars/Core.g:59:6: ( COMMENT | combinator )
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
                    # grammars/Core.g:59:7: COMMENT
                    pass 
                    COMMENT1 = self.match(self.input, COMMENT, self.FOLLOW_COMMENT_in_program550) 
                    if self._state.backtracking == 0:
                        stream_COMMENT.add(COMMENT1)



                elif alt1 == 2:
                    # grammars/Core.g:59:17: combinator
                    pass 
                    self._state.following.append(self.FOLLOW_combinator_in_program554)
                    combinator2 = self.combinator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_combinator.add(combinator2.tree)





                # grammars/Core.g:59:29: ( SCOLON combinator | COMMENT )*
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
                        # grammars/Core.g:59:30: SCOLON combinator
                        pass 
                        SCOLON3 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_program558) 
                        if self._state.backtracking == 0:
                            stream_SCOLON.add(SCOLON3)


                        self._state.following.append(self.FOLLOW_combinator_in_program560)
                        combinator4 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_combinator.add(combinator4.tree)



                    elif alt2 == 2:
                        # grammars/Core.g:59:50: COMMENT
                        pass 
                        COMMENT5 = self.match(self.input, COMMENT, self.FOLLOW_COMMENT_in_program564) 
                        if self._state.backtracking == 0:
                            stream_COMMENT.add(COMMENT5)



                    else:
                        break #loop2


                # grammars/Core.g:59:60: ( SCOLON )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == SCOLON) :
                    alt3 = 1
                if alt3 == 1:
                    # grammars/Core.g:59:60: SCOLON
                    pass 
                    SCOLON6 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_program568) 
                    if self._state.backtracking == 0:
                        stream_SCOLON.add(SCOLON6)





                EOF7 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program571) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF7)


                # AST Rewrite
                # elements: combinator
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
                    # 60:6: -> ^( PROGRAM ( combinator )+ )
                    # grammars/Core.g:60:9: ^( PROGRAM ( combinator )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    ProgramNode(PROGRAM)
                    , root_1)

                    # grammars/Core.g:60:32: ( combinator )+
                    if not (stream_combinator.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_combinator.hasNext():
                        self._adaptor.addChild(root_1, stream_combinator.nextTree())


                    stream_combinator.reset()

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
                self.memoize(self.input, 1, program_StartIndex, success)


            pass
        return retval

    # $ANTLR end "program"


    class combinator_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.combinator_return, self).__init__()

            self.tree = None





    # $ANTLR start "combinator"
    # grammars/Core.g:63:1: combinator : ID ( ID )* IS expression -> ^( COMBINATOR ID ( ID )* expression ) ;
    def combinator(self, ):
        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        combinator_StartIndex = self.input.index()

        root_0 = None

        ID8 = None
        ID9 = None
        IS10 = None
        expression11 = None


        ID8_tree = None
        ID9_tree = None
        IS10_tree = None
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


                # grammars/Core.g:64:4: ( ID ( ID )* IS expression -> ^( COMBINATOR ID ( ID )* expression ) )
                # grammars/Core.g:64:6: ID ( ID )* IS expression
                pass 
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_combinator601) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID8)


                # grammars/Core.g:64:9: ( ID )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammars/Core.g:64:9: ID
                        pass 
                        ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_combinator603) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ID9)



                    else:
                        break #loop4


                IS10 = self.match(self.input, IS, self.FOLLOW_IS_in_combinator606) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS10)


                self._state.following.append(self.FOLLOW_expression_in_combinator608)
                expression11 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression11.tree)


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
                    # 65:6: -> ^( COMBINATOR ID ( ID )* expression )
                    # grammars/Core.g:65:9: ^( COMBINATOR ID ( ID )* expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    CombinatorNode(COMBINATOR)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    IdentifierNode(stream_ID.nextToken())
                    )

                    # grammars/Core.g:65:57: ( ID )*
                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        IdentifierNode(stream_ID.nextToken())
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
    # grammars/Core.g:68:1: expression : ( LET definitions IN expression -> ^( LET definitions expression ) | LETREC definitions IN expression -> ^( LETREC definitions expression ) | CASE expression OF alternatives -> ^( CASE expression alternatives ) | LAMBDA ( ID )+ DOT expression -> ^( LAMBDA ( ID )+ expression ) | expr1 );
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        LET12 = None
        IN14 = None
        LETREC16 = None
        IN18 = None
        CASE20 = None
        OF22 = None
        LAMBDA24 = None
        ID25 = None
        DOT26 = None
        definitions13 = None

        expression15 = None

        definitions17 = None

        expression19 = None

        expression21 = None

        alternatives23 = None

        expression27 = None

        expr128 = None


        LET12_tree = None
        IN14_tree = None
        LETREC16_tree = None
        IN18_tree = None
        CASE20_tree = None
        OF22_tree = None
        LAMBDA24_tree = None
        ID25_tree = None
        DOT26_tree = None
        stream_LETREC = RewriteRuleTokenStream(self._adaptor, "token LETREC")
        stream_IN = RewriteRuleTokenStream(self._adaptor, "token IN")
        stream_LAMBDA = RewriteRuleTokenStream(self._adaptor, "token LAMBDA")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_OF = RewriteRuleTokenStream(self._adaptor, "token OF")
        stream_LET = RewriteRuleTokenStream(self._adaptor, "token LET")
        stream_CASE = RewriteRuleTokenStream(self._adaptor, "token CASE")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_alternatives = RewriteRuleSubtreeStream(self._adaptor, "rule alternatives")
        stream_definitions = RewriteRuleSubtreeStream(self._adaptor, "rule definitions")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:69:4: ( LET definitions IN expression -> ^( LET definitions expression ) | LETREC definitions IN expression -> ^( LETREC definitions expression ) | CASE expression OF alternatives -> ^( CASE expression alternatives ) | LAMBDA ( ID )+ DOT expression -> ^( LAMBDA ( ID )+ expression ) | expr1 )
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
                    # grammars/Core.g:69:6: LET definitions IN expression
                    pass 
                    LET12 = self.match(self.input, LET, self.FOLLOW_LET_in_expression649) 
                    if self._state.backtracking == 0:
                        stream_LET.add(LET12)


                    self._state.following.append(self.FOLLOW_definitions_in_expression651)
                    definitions13 = self.definitions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_definitions.add(definitions13.tree)


                    IN14 = self.match(self.input, IN, self.FOLLOW_IN_in_expression653) 
                    if self._state.backtracking == 0:
                        stream_IN.add(IN14)


                    self._state.following.append(self.FOLLOW_expression_in_expression655)
                    expression15 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression15.tree)


                    # AST Rewrite
                    # elements: definitions, LET, expression
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
                        # 70:6: -> ^( LET definitions expression )
                        # grammars/Core.g:70:9: ^( LET definitions expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        LetNode(stream_LET.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_1, stream_definitions.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 2:
                    # grammars/Core.g:71:6: LETREC definitions IN expression
                    pass 
                    LETREC16 = self.match(self.input, LETREC, self.FOLLOW_LETREC_in_expression680) 
                    if self._state.backtracking == 0:
                        stream_LETREC.add(LETREC16)


                    self._state.following.append(self.FOLLOW_definitions_in_expression682)
                    definitions17 = self.definitions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_definitions.add(definitions17.tree)


                    IN18 = self.match(self.input, IN, self.FOLLOW_IN_in_expression684) 
                    if self._state.backtracking == 0:
                        stream_IN.add(IN18)


                    self._state.following.append(self.FOLLOW_expression_in_expression686)
                    expression19 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression19.tree)


                    # AST Rewrite
                    # elements: definitions, LETREC, expression
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
                        # 72:6: -> ^( LETREC definitions expression )
                        # grammars/Core.g:72:9: ^( LETREC definitions expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        LetRecNode(stream_LETREC.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_1, stream_definitions.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 3:
                    # grammars/Core.g:73:6: CASE expression OF alternatives
                    pass 
                    CASE20 = self.match(self.input, CASE, self.FOLLOW_CASE_in_expression711) 
                    if self._state.backtracking == 0:
                        stream_CASE.add(CASE20)


                    self._state.following.append(self.FOLLOW_expression_in_expression713)
                    expression21 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression21.tree)


                    OF22 = self.match(self.input, OF, self.FOLLOW_OF_in_expression715) 
                    if self._state.backtracking == 0:
                        stream_OF.add(OF22)


                    self._state.following.append(self.FOLLOW_alternatives_in_expression717)
                    alternatives23 = self.alternatives()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alternatives.add(alternatives23.tree)


                    # AST Rewrite
                    # elements: expression, alternatives, CASE
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
                        # 74:6: -> ^( CASE expression alternatives )
                        # grammars/Core.g:74:9: ^( CASE expression alternatives )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        CaseNode(stream_CASE.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_1, stream_alternatives.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 4:
                    # grammars/Core.g:75:6: LAMBDA ( ID )+ DOT expression
                    pass 
                    LAMBDA24 = self.match(self.input, LAMBDA, self.FOLLOW_LAMBDA_in_expression742) 
                    if self._state.backtracking == 0:
                        stream_LAMBDA.add(LAMBDA24)


                    # grammars/Core.g:75:13: ( ID )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == ID) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammars/Core.g:75:13: ID
                            pass 
                            ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_expression744) 
                            if self._state.backtracking == 0:
                                stream_ID.add(ID25)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    DOT26 = self.match(self.input, DOT, self.FOLLOW_DOT_in_expression747) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT26)


                    self._state.following.append(self.FOLLOW_expression_in_expression749)
                    expression27 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression27.tree)


                    # AST Rewrite
                    # elements: ID, expression, LAMBDA
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
                        # 76:6: -> ^( LAMBDA ( ID )+ expression )
                        # grammars/Core.g:76:9: ^( LAMBDA ( ID )+ expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        LambdaNode(stream_LAMBDA.nextToken())
                        , root_1)

                        # grammars/Core.g:76:30: ( ID )+
                        if not (stream_ID.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_ID.hasNext():
                            self._adaptor.addChild(root_1, 
                            IdentifierNode(stream_ID.nextToken())
                            )


                        stream_ID.reset()

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 5:
                    # grammars/Core.g:77:6: expr1
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expr1_in_expression778)
                    expr128 = self.expr1()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr128.tree)



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
    # grammars/Core.g:80:1: alternatives : alternative ( SCOLON ! alternative )* ;
    def alternatives(self, ):
        retval = self.alternatives_return()
        retval.start = self.input.LT(1)

        alternatives_StartIndex = self.input.index()

        root_0 = None

        SCOLON30 = None
        alternative29 = None

        alternative31 = None


        SCOLON30_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:80:13: ( alternative ( SCOLON ! alternative )* )
                # grammars/Core.g:80:15: alternative ( SCOLON ! alternative )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_alternative_in_alternatives786)
                alternative29 = self.alternative()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, alternative29.tree)


                # grammars/Core.g:80:27: ( SCOLON ! alternative )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == SCOLON) :
                        LA7_1 = self.input.LA(2)

                        if (self.synpred11_Core()) :
                            alt7 = 1




                    if alt7 == 1:
                        # grammars/Core.g:80:28: SCOLON ! alternative
                        pass 
                        SCOLON30 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_alternatives789)

                        self._state.following.append(self.FOLLOW_alternative_in_alternatives792)
                        alternative31 = self.alternative()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, alternative31.tree)



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
    # grammars/Core.g:81:1: alternative : LT NUMBER GT ARROW expression -> ^( ALTERNATIVE NUMBER expression ) ;
    def alternative(self, ):
        retval = self.alternative_return()
        retval.start = self.input.LT(1)

        alternative_StartIndex = self.input.index()

        root_0 = None

        LT32 = None
        NUMBER33 = None
        GT34 = None
        ARROW35 = None
        expression36 = None


        LT32_tree = None
        NUMBER33_tree = None
        GT34_tree = None
        ARROW35_tree = None
        stream_GT = RewriteRuleTokenStream(self._adaptor, "token GT")
        stream_ARROW = RewriteRuleTokenStream(self._adaptor, "token ARROW")
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_NUMBER = RewriteRuleTokenStream(self._adaptor, "token NUMBER")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:82:4: ( LT NUMBER GT ARROW expression -> ^( ALTERNATIVE NUMBER expression ) )
                # grammars/Core.g:82:6: LT NUMBER GT ARROW expression
                pass 
                LT32 = self.match(self.input, LT, self.FOLLOW_LT_in_alternative805) 
                if self._state.backtracking == 0:
                    stream_LT.add(LT32)


                NUMBER33 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_alternative807) 
                if self._state.backtracking == 0:
                    stream_NUMBER.add(NUMBER33)


                GT34 = self.match(self.input, GT, self.FOLLOW_GT_in_alternative809) 
                if self._state.backtracking == 0:
                    stream_GT.add(GT34)


                ARROW35 = self.match(self.input, ARROW, self.FOLLOW_ARROW_in_alternative811) 
                if self._state.backtracking == 0:
                    stream_ARROW.add(ARROW35)


                self._state.following.append(self.FOLLOW_expression_in_alternative813)
                expression36 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression36.tree)


                # AST Rewrite
                # elements: NUMBER, expression
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
                    # 83:6: -> ^( ALTERNATIVE NUMBER expression )
                    # grammars/Core.g:83:9: ^( ALTERNATIVE NUMBER expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    AlternativeNode(ALTERNATIVE)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    NumberNode(stream_NUMBER.nextToken())
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
                self.memoize(self.input, 5, alternative_StartIndex, success)


            pass
        return retval

    # $ANTLR end "alternative"


    class definitions_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.definitions_return, self).__init__()

            self.tree = None





    # $ANTLR start "definitions"
    # grammars/Core.g:86:1: definitions : definition ( COMMA ! definition )* ;
    def definitions(self, ):
        retval = self.definitions_return()
        retval.start = self.input.LT(1)

        definitions_StartIndex = self.input.index()

        root_0 = None

        COMMA38 = None
        definition37 = None

        definition39 = None


        COMMA38_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:86:12: ( definition ( COMMA ! definition )* )
                # grammars/Core.g:86:14: definition ( COMMA ! definition )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_definition_in_definitions842)
                definition37 = self.definition()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, definition37.tree)


                # grammars/Core.g:86:25: ( COMMA ! definition )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == COMMA) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammars/Core.g:86:26: COMMA ! definition
                        pass 
                        COMMA38 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_definitions845)

                        self._state.following.append(self.FOLLOW_definition_in_definitions848)
                        definition39 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition39.tree)



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
    # grammars/Core.g:87:1: definition : ID IS expression -> ^( DEFINITION ID expression ) ;
    def definition(self, ):
        retval = self.definition_return()
        retval.start = self.input.LT(1)

        definition_StartIndex = self.input.index()

        root_0 = None

        ID40 = None
        IS41 = None
        expression42 = None


        ID40_tree = None
        IS41_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_IS = RewriteRuleTokenStream(self._adaptor, "token IS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:88:4: ( ID IS expression -> ^( DEFINITION ID expression ) )
                # grammars/Core.g:88:6: ID IS expression
                pass 
                ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_definition861) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID40)


                IS41 = self.match(self.input, IS, self.FOLLOW_IS_in_definition863) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS41)


                self._state.following.append(self.FOLLOW_expression_in_definition865)
                expression42 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression42.tree)


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
                    # 89:6: -> ^( DEFINITION ID expression )
                    # grammars/Core.g:89:9: ^( DEFINITION ID expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    DefinitionNode(DEFINITION)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    IdentifierNode(stream_ID.nextToken())
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
                self.memoize(self.input, 7, definition_StartIndex, success)


            pass
        return retval

    # $ANTLR end "definition"


    class expr1_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr1_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr1"
    # grammars/Core.g:92:1: expr1 : expr2 ( OR ^ expr1 )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR44 = None
        expr243 = None

        expr145 = None


        OR44_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:92:6: ( expr2 ( OR ^ expr1 )* )
                # grammars/Core.g:92:8: expr2 ( OR ^ expr1 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1894)
                expr243 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr243.tree)


                # grammars/Core.g:92:14: ( OR ^ expr1 )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OR) :
                        LA9_2 = self.input.LA(2)

                        if (self.synpred13_Core()) :
                            alt9 = 1




                    if alt9 == 1:
                        # grammars/Core.g:92:15: OR ^ expr1
                        pass 
                        OR44 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1897)
                        if self._state.backtracking == 0:
                            OR44_tree = OrNode(OR44) 
                            root_0 = self._adaptor.becomeRoot(OR44_tree, root_0)



                        self._state.following.append(self.FOLLOW_expr1_in_expr1903)
                        expr145 = self.expr1()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr145.tree)



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
    # grammars/Core.g:94:1: expr2 : expr3 ( AND ^ expr2 )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND47 = None
        expr346 = None

        expr248 = None


        AND47_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:94:6: ( expr3 ( AND ^ expr2 )* )
                # grammars/Core.g:94:8: expr3 ( AND ^ expr2 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2912)
                expr346 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr346.tree)


                # grammars/Core.g:94:14: ( AND ^ expr2 )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == AND) :
                        LA10_2 = self.input.LA(2)

                        if (self.synpred14_Core()) :
                            alt10 = 1




                    if alt10 == 1:
                        # grammars/Core.g:94:15: AND ^ expr2
                        pass 
                        AND47 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2915)
                        if self._state.backtracking == 0:
                            AND47_tree = AndNode(AND47) 
                            root_0 = self._adaptor.becomeRoot(AND47_tree, root_0)



                        self._state.following.append(self.FOLLOW_expr2_in_expr2921)
                        expr248 = self.expr2()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr248.tree)



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
    # grammars/Core.g:96:1: expr3 : expr4 ( relop ^ expr4 )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        expr449 = None

        relop50 = None

        expr451 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:96:6: ( expr4 ( relop ^ expr4 )* )
                # grammars/Core.g:96:8: expr4 ( relop ^ expr4 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3930)
                expr449 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr449.tree)


                # grammars/Core.g:96:14: ( relop ^ expr4 )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((EQ <= LA11_0 <= GTE) or (LT <= LA11_0 <= LTE) or LA11_0 == NEQ) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammars/Core.g:96:15: relop ^ expr4
                        pass 
                        self._state.following.append(self.FOLLOW_relop_in_expr3933)
                        relop50 = self.relop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(relop50.tree, root_0)


                        self._state.following.append(self.FOLLOW_expr4_in_expr3936)
                        expr451 = self.expr4()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr451.tree)



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
    # grammars/Core.g:98:1: expr4 : expr5 ( ( ADD ^| MIN ^) expr4 )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD53 = None
        MIN54 = None
        expr552 = None

        expr455 = None


        ADD53_tree = None
        MIN54_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:98:6: ( expr5 ( ( ADD ^| MIN ^) expr4 )* )
                # grammars/Core.g:98:8: expr5 ( ( ADD ^| MIN ^) expr4 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4945)
                expr552 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr552.tree)


                # grammars/Core.g:98:14: ( ( ADD ^| MIN ^) expr4 )*
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
                        # grammars/Core.g:98:15: ( ADD ^| MIN ^) expr4
                        pass 
                        # grammars/Core.g:98:15: ( ADD ^| MIN ^)
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
                            # grammars/Core.g:98:16: ADD ^
                            pass 
                            ADD53 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4949)
                            if self._state.backtracking == 0:
                                ADD53_tree = AddNode(ADD53) 
                                root_0 = self._adaptor.becomeRoot(ADD53_tree, root_0)




                        elif alt12 == 2:
                            # grammars/Core.g:98:30: MIN ^
                            pass 
                            MIN54 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4955)
                            if self._state.backtracking == 0:
                                MIN54_tree = MinNode(MIN54) 
                                root_0 = self._adaptor.becomeRoot(MIN54_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr4_in_expr4962)
                        expr455 = self.expr4()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr455.tree)



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
    # grammars/Core.g:100:1: expr5 : expr6 ( ( DIV ^| MUL ^) expr6 )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV57 = None
        MUL58 = None
        expr656 = None

        expr659 = None


        DIV57_tree = None
        MUL58_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:100:6: ( expr6 ( ( DIV ^| MUL ^) expr6 )* )
                # grammars/Core.g:100:8: expr6 ( ( DIV ^| MUL ^) expr6 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr5971)
                expr656 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr656.tree)


                # grammars/Core.g:100:14: ( ( DIV ^| MUL ^) expr6 )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == DIV or LA15_0 == MUL) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammars/Core.g:100:15: ( DIV ^| MUL ^) expr6
                        pass 
                        # grammars/Core.g:100:15: ( DIV ^| MUL ^)
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
                            # grammars/Core.g:100:16: DIV ^
                            pass 
                            DIV57 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5975)
                            if self._state.backtracking == 0:
                                DIV57_tree = DivNode(DIV57) 
                                root_0 = self._adaptor.becomeRoot(DIV57_tree, root_0)




                        elif alt14 == 2:
                            # grammars/Core.g:100:30: MUL ^
                            pass 
                            MUL58 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5981)
                            if self._state.backtracking == 0:
                                MUL58_tree = MulNode(MUL58) 
                                root_0 = self._adaptor.becomeRoot(MUL58_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr6_in_expr5988)
                        expr659 = self.expr6()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr659.tree)



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
    # grammars/Core.g:102:1: expr6 : (lst+= aexpr !)+ ;
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


                # grammars/Core.g:102:6: ( (lst+= aexpr !)+ )
                # grammars/Core.g:102:8: (lst+= aexpr !)+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Core.g:102:8: (lst+= aexpr !)+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ID or LA16_0 == LPAREN or LA16_0 == NUMBER or LA16_0 == PACK) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammars/Core.g:102:9: lst+= aexpr !
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr61000)
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
                                          
                    # format linear list as application spine
                    if len(list_lst) >= 2:
                       chain = self._adaptor.nil()
                       b = ApplicationNode(APPLICATION)
                       list_lst.reverse()
                       item = list_lst.pop()
                       b.addChild(list_lst.pop())         
                       b.addChild(item)
                       chain = self._adaptor.becomeRoot(b, chain)
                       while len(list_lst) > 0:
                          a = ApplicationNode(APPLICATION)
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
    # grammars/Core.g:123:1: aexpr : ( ID -> ^( ID ID ) | NUMBER -> ^( NUMBER NUMBER ) | PACK LCURLY NUMBER COMMA NUMBER RCURLY -> ^( PACK NUMBER NUMBER ) | LPAREN expr1 RPAREN -> expr1 );
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID60 = None
        NUMBER61 = None
        PACK62 = None
        LCURLY63 = None
        NUMBER64 = None
        COMMA65 = None
        NUMBER66 = None
        RCURLY67 = None
        LPAREN68 = None
        RPAREN70 = None
        expr169 = None


        ID60_tree = None
        NUMBER61_tree = None
        PACK62_tree = None
        LCURLY63_tree = None
        NUMBER64_tree = None
        COMMA65_tree = None
        NUMBER66_tree = None
        RCURLY67_tree = None
        LPAREN68_tree = None
        RPAREN70_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_PACK = RewriteRuleTokenStream(self._adaptor, "token PACK")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_NUMBER = RewriteRuleTokenStream(self._adaptor, "token NUMBER")
        stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "rule expr1")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:124:4: ( ID -> ^( ID ID ) | NUMBER -> ^( NUMBER NUMBER ) | PACK LCURLY NUMBER COMMA NUMBER RCURLY -> ^( PACK NUMBER NUMBER ) | LPAREN expr1 RPAREN -> expr1 )
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
                    # grammars/Core.g:124:6: ID
                    pass 
                    ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr1018) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID60)


                    # AST Rewrite
                    # elements: ID, ID
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
                        # 125:6: -> ^( ID ID )
                        # grammars/Core.g:125:9: ^( ID ID )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IdentifierNode(stream_ID.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt17 == 2:
                    # grammars/Core.g:126:6: NUMBER
                    pass 
                    NUMBER61 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_aexpr1041) 
                    if self._state.backtracking == 0:
                        stream_NUMBER.add(NUMBER61)


                    # AST Rewrite
                    # elements: NUMBER, NUMBER
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
                        # 127:6: -> ^( NUMBER NUMBER )
                        # grammars/Core.g:127:9: ^( NUMBER NUMBER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        NumberNode(stream_NUMBER.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        NumberNode(stream_NUMBER.nextToken())
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt17 == 3:
                    # grammars/Core.g:128:6: PACK LCURLY NUMBER COMMA NUMBER RCURLY
                    pass 
                    PACK62 = self.match(self.input, PACK, self.FOLLOW_PACK_in_aexpr1067) 
                    if self._state.backtracking == 0:
                        stream_PACK.add(PACK62)


                    LCURLY63 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_aexpr1069) 
                    if self._state.backtracking == 0:
                        stream_LCURLY.add(LCURLY63)


                    NUMBER64 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_aexpr1071) 
                    if self._state.backtracking == 0:
                        stream_NUMBER.add(NUMBER64)


                    COMMA65 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_aexpr1073) 
                    if self._state.backtracking == 0:
                        stream_COMMA.add(COMMA65)


                    NUMBER66 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_aexpr1075) 
                    if self._state.backtracking == 0:
                        stream_NUMBER.add(NUMBER66)


                    RCURLY67 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_aexpr1077) 
                    if self._state.backtracking == 0:
                        stream_RCURLY.add(RCURLY67)


                    # AST Rewrite
                    # elements: NUMBER, NUMBER, PACK
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
                        # 129:6: -> ^( PACK NUMBER NUMBER )
                        # grammars/Core.g:129:9: ^( PACK NUMBER NUMBER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        ConstructorNode(stream_PACK.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        NumberNode(stream_NUMBER.nextToken())
                        )

                        self._adaptor.addChild(root_1, 
                        NumberNode(stream_NUMBER.nextToken())
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt17 == 4:
                    # grammars/Core.g:130:6: LPAREN expr1 RPAREN
                    pass 
                    LPAREN68 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr1108) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN68)


                    self._state.following.append(self.FOLLOW_expr1_in_aexpr1110)
                    expr169 = self.expr1()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr1.add(expr169.tree)


                    RPAREN70 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr1112) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN70)


                    # AST Rewrite
                    # elements: expr1
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
                        # 131:6: -> expr1
                        self._adaptor.addChild(root_0, stream_expr1.nextTree())




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
                self.memoize(self.input, 14, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class relop_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.relop_return, self).__init__()

            self.tree = None





    # $ANTLR start "relop"
    # grammars/Core.g:134:1: relop : ( LT | LTE | EQ | NEQ | GTE | GT );
    def relop(self, ):
        retval = self.relop_return()
        retval.start = self.input.LT(1)

        relop_StartIndex = self.input.index()

        root_0 = None

        LT71 = None
        LTE72 = None
        EQ73 = None
        NEQ74 = None
        GTE75 = None
        GT76 = None

        LT71_tree = None
        LTE72_tree = None
        EQ73_tree = None
        NEQ74_tree = None
        GTE75_tree = None
        GT76_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:134:6: ( LT | LTE | EQ | NEQ | GTE | GT )
                alt18 = 6
                LA18 = self.input.LA(1)
                if LA18 == LT:
                    alt18 = 1
                elif LA18 == LTE:
                    alt18 = 2
                elif LA18 == EQ:
                    alt18 = 3
                elif LA18 == NEQ:
                    alt18 = 4
                elif LA18 == GTE:
                    alt18 = 5
                elif LA18 == GT:
                    alt18 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammars/Core.g:134:8: LT
                    pass 
                    root_0 = self._adaptor.nil()


                    LT71 = self.match(self.input, LT, self.FOLLOW_LT_in_relop1129)
                    if self._state.backtracking == 0:
                        LT71_tree = LessThanNode(LT71) 
                        self._adaptor.addChild(root_0, LT71_tree)




                elif alt18 == 2:
                    # grammars/Core.g:134:27: LTE
                    pass 
                    root_0 = self._adaptor.nil()


                    LTE72 = self.match(self.input, LTE, self.FOLLOW_LTE_in_relop1136)
                    if self._state.backtracking == 0:
                        LTE72_tree = LessThanEqualNode(LTE72) 
                        self._adaptor.addChild(root_0, LTE72_tree)




                elif alt18 == 3:
                    # grammars/Core.g:134:52: EQ
                    pass 
                    root_0 = self._adaptor.nil()


                    EQ73 = self.match(self.input, EQ, self.FOLLOW_EQ_in_relop1143)
                    if self._state.backtracking == 0:
                        EQ73_tree = EqualNode(EQ73) 
                        self._adaptor.addChild(root_0, EQ73_tree)




                elif alt18 == 4:
                    # grammars/Core.g:134:68: NEQ
                    pass 
                    root_0 = self._adaptor.nil()


                    NEQ74 = self.match(self.input, NEQ, self.FOLLOW_NEQ_in_relop1150)
                    if self._state.backtracking == 0:
                        NEQ74_tree = NotEqualNode(NEQ74) 
                        self._adaptor.addChild(root_0, NEQ74_tree)




                elif alt18 == 5:
                    # grammars/Core.g:134:88: GTE
                    pass 
                    root_0 = self._adaptor.nil()


                    GTE75 = self.match(self.input, GTE, self.FOLLOW_GTE_in_relop1157)
                    if self._state.backtracking == 0:
                        GTE75_tree = GreaterThanEqualNode(GTE75) 
                        self._adaptor.addChild(root_0, GTE75_tree)




                elif alt18 == 6:
                    # grammars/Core.g:134:116: GT
                    pass 
                    root_0 = self._adaptor.nil()


                    GT76 = self.match(self.input, GT, self.FOLLOW_GT_in_relop1164)
                    if self._state.backtracking == 0:
                        GT76_tree = GreaterThanNode(GT76) 
                        self._adaptor.addChild(root_0, GT76_tree)




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
        # grammars/Core.g:80:28: ( SCOLON alternative )
        # grammars/Core.g:80:28: SCOLON alternative
        pass 
        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_synpred11_Core789)

        self._state.following.append(self.FOLLOW_alternative_in_synpred11_Core792)
        self.alternative()

        self._state.following.pop()



    # $ANTLR end "synpred11_Core"



    # $ANTLR start "synpred13_Core"
    def synpred13_Core_fragment(self, ):
        # grammars/Core.g:92:15: ( OR expr1 )
        # grammars/Core.g:92:15: OR expr1
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred13_Core897)

        self._state.following.append(self.FOLLOW_expr1_in_synpred13_Core903)
        self.expr1()

        self._state.following.pop()



    # $ANTLR end "synpred13_Core"



    # $ANTLR start "synpred14_Core"
    def synpred14_Core_fragment(self, ):
        # grammars/Core.g:94:15: ( AND expr2 )
        # grammars/Core.g:94:15: AND expr2
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred14_Core915)

        self._state.following.append(self.FOLLOW_expr2_in_synpred14_Core921)
        self.expr2()

        self._state.following.pop()



    # $ANTLR end "synpred14_Core"



    # $ANTLR start "synpred17_Core"
    def synpred17_Core_fragment(self, ):
        # grammars/Core.g:98:15: ( ( ADD | MIN ) expr4 )
        # grammars/Core.g:98:15: ( ADD | MIN ) expr4
        pass 
        if self.input.LA(1) == ADD or self.input.LA(1) == MIN:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr4_in_synpred17_Core962)
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



 

    FOLLOW_COMMENT_in_program550 = frozenset([13, 41])
    FOLLOW_combinator_in_program554 = frozenset([13, 41])
    FOLLOW_SCOLON_in_program558 = frozenset([20])
    FOLLOW_combinator_in_program560 = frozenset([13, 41])
    FOLLOW_COMMENT_in_program564 = frozenset([13, 41])
    FOLLOW_SCOLON_in_program568 = frozenset([])
    FOLLOW_EOF_in_program571 = frozenset([1])
    FOLLOW_ID_in_combinator601 = frozenset([20, 22])
    FOLLOW_ID_in_combinator603 = frozenset([20, 22])
    FOLLOW_IS_in_combinator606 = frozenset([9, 20, 23, 25, 26, 27, 34, 37])
    FOLLOW_expression_in_combinator608 = frozenset([1])
    FOLLOW_LET_in_expression649 = frozenset([20])
    FOLLOW_definitions_in_expression651 = frozenset([21])
    FOLLOW_IN_in_expression653 = frozenset([9, 20, 23, 25, 26, 27, 34, 37])
    FOLLOW_expression_in_expression655 = frozenset([1])
    FOLLOW_LETREC_in_expression680 = frozenset([20])
    FOLLOW_definitions_in_expression682 = frozenset([21])
    FOLLOW_IN_in_expression684 = frozenset([9, 20, 23, 25, 26, 27, 34, 37])
    FOLLOW_expression_in_expression686 = frozenset([1])
    FOLLOW_CASE_in_expression711 = frozenset([9, 20, 23, 25, 26, 27, 34, 37])
    FOLLOW_expression_in_expression713 = frozenset([35])
    FOLLOW_OF_in_expression715 = frozenset([28])
    FOLLOW_alternatives_in_expression717 = frozenset([1])
    FOLLOW_LAMBDA_in_expression742 = frozenset([20])
    FOLLOW_ID_in_expression744 = frozenset([16, 20])
    FOLLOW_DOT_in_expression747 = frozenset([9, 20, 23, 25, 26, 27, 34, 37])
    FOLLOW_expression_in_expression749 = frozenset([1])
    FOLLOW_expr1_in_expression778 = frozenset([1])
    FOLLOW_alternative_in_alternatives786 = frozenset([1, 41])
    FOLLOW_SCOLON_in_alternatives789 = frozenset([28])
    FOLLOW_alternative_in_alternatives792 = frozenset([1, 41])
    FOLLOW_LT_in_alternative805 = frozenset([34])
    FOLLOW_NUMBER_in_alternative807 = frozenset([18])
    FOLLOW_GT_in_alternative809 = frozenset([8])
    FOLLOW_ARROW_in_alternative811 = frozenset([9, 20, 23, 25, 26, 27, 34, 37])
    FOLLOW_expression_in_alternative813 = frozenset([1])
    FOLLOW_definition_in_definitions842 = frozenset([1, 12])
    FOLLOW_COMMA_in_definitions845 = frozenset([20])
    FOLLOW_definition_in_definitions848 = frozenset([1, 12])
    FOLLOW_ID_in_definition861 = frozenset([22])
    FOLLOW_IS_in_definition863 = frozenset([9, 20, 23, 25, 26, 27, 34, 37])
    FOLLOW_expression_in_definition865 = frozenset([1])
    FOLLOW_expr2_in_expr1894 = frozenset([1, 36])
    FOLLOW_OR_in_expr1897 = frozenset([20, 27, 34, 37])
    FOLLOW_expr1_in_expr1903 = frozenset([1, 36])
    FOLLOW_expr3_in_expr2912 = frozenset([1, 6])
    FOLLOW_AND_in_expr2915 = frozenset([20, 27, 34, 37])
    FOLLOW_expr2_in_expr2921 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3930 = frozenset([1, 17, 18, 19, 28, 29, 32])
    FOLLOW_relop_in_expr3933 = frozenset([20, 27, 34, 37])
    FOLLOW_expr4_in_expr3936 = frozenset([1, 17, 18, 19, 28, 29, 32])
    FOLLOW_expr5_in_expr4945 = frozenset([1, 4, 30])
    FOLLOW_ADD_in_expr4949 = frozenset([20, 27, 34, 37])
    FOLLOW_MIN_in_expr4955 = frozenset([20, 27, 34, 37])
    FOLLOW_expr4_in_expr4962 = frozenset([1, 4, 30])
    FOLLOW_expr6_in_expr5971 = frozenset([1, 15, 31])
    FOLLOW_DIV_in_expr5975 = frozenset([20, 27, 34, 37])
    FOLLOW_MUL_in_expr5981 = frozenset([20, 27, 34, 37])
    FOLLOW_expr6_in_expr5988 = frozenset([1, 15, 31])
    FOLLOW_aexpr_in_expr61000 = frozenset([1, 20, 27, 34, 37])
    FOLLOW_ID_in_aexpr1018 = frozenset([1])
    FOLLOW_NUMBER_in_aexpr1041 = frozenset([1])
    FOLLOW_PACK_in_aexpr1067 = frozenset([24])
    FOLLOW_LCURLY_in_aexpr1069 = frozenset([34])
    FOLLOW_NUMBER_in_aexpr1071 = frozenset([12])
    FOLLOW_COMMA_in_aexpr1073 = frozenset([34])
    FOLLOW_NUMBER_in_aexpr1075 = frozenset([39])
    FOLLOW_RCURLY_in_aexpr1077 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr1108 = frozenset([20, 27, 34, 37])
    FOLLOW_expr1_in_aexpr1110 = frozenset([40])
    FOLLOW_RPAREN_in_aexpr1112 = frozenset([1])
    FOLLOW_LT_in_relop1129 = frozenset([1])
    FOLLOW_LTE_in_relop1136 = frozenset([1])
    FOLLOW_EQ_in_relop1143 = frozenset([1])
    FOLLOW_NEQ_in_relop1150 = frozenset([1])
    FOLLOW_GTE_in_relop1157 = frozenset([1])
    FOLLOW_GT_in_relop1164 = frozenset([1])
    FOLLOW_SCOLON_in_synpred11_Core789 = frozenset([28])
    FOLLOW_alternative_in_synpred11_Core792 = frozenset([1])
    FOLLOW_OR_in_synpred13_Core897 = frozenset([20, 27, 34, 37])
    FOLLOW_expr1_in_synpred13_Core903 = frozenset([1])
    FOLLOW_AND_in_synpred14_Core915 = frozenset([20, 27, 34, 37])
    FOLLOW_expr2_in_synpred14_Core921 = frozenset([1])
    FOLLOW_set_in_synpred17_Core948 = frozenset([20, 27, 34, 37])
    FOLLOW_expr4_in_synpred17_Core962 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("CoreLexer", CoreParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
