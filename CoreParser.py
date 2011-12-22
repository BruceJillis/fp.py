# $ANTLR 3.4 grammars/Core.g 2011-12-22 22:24:54

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *


        
from ast import *



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
FLOAT=18
GT=19
GTE=20
ID=21
IN=22
INT=23
IS=24
LAMBDA=25
LCURLY=26
LET=27
LETREC=28
LPAREN=29
LT=30
LTE=31
MIN=32
MUL=33
NEQ=34
NOT=35
OF=36
OR=37
PACK=38
PROGRAM=39
RCURLY=40
RPAREN=41
SCOLON=42
WHITESPACE=43

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALTERNATIVE", "AND", "APPLICATION", "ARROW", "CASE", "COLON", 
    "COMBINATOR", "COMMA", "COMMENT", "DEFINITION", "DIV", "DOT", "EQ", 
    "FLOAT", "GT", "GTE", "ID", "IN", "INT", "IS", "LAMBDA", "LCURLY", "LET", 
    "LETREC", "LPAREN", "LT", "LTE", "MIN", "MUL", "NEQ", "NOT", "OF", "OR", 
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
                    COMMENT1 = self.match(self.input, COMMENT, self.FOLLOW_COMMENT_in_program552) 
                    if self._state.backtracking == 0:
                        stream_COMMENT.add(COMMENT1)



                elif alt1 == 2:
                    # grammars/Core.g:59:17: combinator
                    pass 
                    self._state.following.append(self.FOLLOW_combinator_in_program556)
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
                        SCOLON3 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_program560) 
                        if self._state.backtracking == 0:
                            stream_SCOLON.add(SCOLON3)


                        self._state.following.append(self.FOLLOW_combinator_in_program562)
                        combinator4 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_combinator.add(combinator4.tree)



                    elif alt2 == 2:
                        # grammars/Core.g:59:50: COMMENT
                        pass 
                        COMMENT5 = self.match(self.input, COMMENT, self.FOLLOW_COMMENT_in_program566) 
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
                    SCOLON6 = self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_program570) 
                    if self._state.backtracking == 0:
                        stream_SCOLON.add(SCOLON6)





                EOF7 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program573) 
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
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_combinator603) 
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
                        ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_combinator605) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ID9)



                    else:
                        break #loop4


                IS10 = self.match(self.input, IS, self.FOLLOW_IS_in_combinator608) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS10)


                self._state.following.append(self.FOLLOW_expression_in_combinator610)
                expression11 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression11.tree)


                # AST Rewrite
                # elements: expression, ID, ID
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
                elif LA6 == FLOAT or LA6 == ID or LA6 == INT or LA6 == LPAREN or LA6 == PACK:
                    alt6 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammars/Core.g:69:6: LET definitions IN expression
                    pass 
                    LET12 = self.match(self.input, LET, self.FOLLOW_LET_in_expression651) 
                    if self._state.backtracking == 0:
                        stream_LET.add(LET12)


                    self._state.following.append(self.FOLLOW_definitions_in_expression653)
                    definitions13 = self.definitions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_definitions.add(definitions13.tree)


                    IN14 = self.match(self.input, IN, self.FOLLOW_IN_in_expression655) 
                    if self._state.backtracking == 0:
                        stream_IN.add(IN14)


                    self._state.following.append(self.FOLLOW_expression_in_expression657)
                    expression15 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression15.tree)


                    # AST Rewrite
                    # elements: LET, expression, definitions
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
                    LETREC16 = self.match(self.input, LETREC, self.FOLLOW_LETREC_in_expression682) 
                    if self._state.backtracking == 0:
                        stream_LETREC.add(LETREC16)


                    self._state.following.append(self.FOLLOW_definitions_in_expression684)
                    definitions17 = self.definitions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_definitions.add(definitions17.tree)


                    IN18 = self.match(self.input, IN, self.FOLLOW_IN_in_expression686) 
                    if self._state.backtracking == 0:
                        stream_IN.add(IN18)


                    self._state.following.append(self.FOLLOW_expression_in_expression688)
                    expression19 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression19.tree)


                    # AST Rewrite
                    # elements: LETREC, expression, definitions
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
                    CASE20 = self.match(self.input, CASE, self.FOLLOW_CASE_in_expression713) 
                    if self._state.backtracking == 0:
                        stream_CASE.add(CASE20)


                    self._state.following.append(self.FOLLOW_expression_in_expression715)
                    expression21 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression21.tree)


                    OF22 = self.match(self.input, OF, self.FOLLOW_OF_in_expression717) 
                    if self._state.backtracking == 0:
                        stream_OF.add(OF22)


                    self._state.following.append(self.FOLLOW_alternatives_in_expression719)
                    alternatives23 = self.alternatives()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alternatives.add(alternatives23.tree)


                    # AST Rewrite
                    # elements: CASE, expression, alternatives
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
                    LAMBDA24 = self.match(self.input, LAMBDA, self.FOLLOW_LAMBDA_in_expression744) 
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
                            ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_expression746) 
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


                    DOT26 = self.match(self.input, DOT, self.FOLLOW_DOT_in_expression749) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT26)


                    self._state.following.append(self.FOLLOW_expression_in_expression751)
                    expression27 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression27.tree)


                    # AST Rewrite
                    # elements: LAMBDA, ID, expression
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


                    self._state.following.append(self.FOLLOW_expr1_in_expression780)
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
    # grammars/Core.g:80:1: alternatives : alternative ( COMMA ! alternative )* ;
    def alternatives(self, ):
        retval = self.alternatives_return()
        retval.start = self.input.LT(1)

        alternatives_StartIndex = self.input.index()

        root_0 = None

        COMMA30 = None
        alternative29 = None

        alternative31 = None


        COMMA30_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:80:13: ( alternative ( COMMA ! alternative )* )
                # grammars/Core.g:80:15: alternative ( COMMA ! alternative )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_alternative_in_alternatives788)
                alternative29 = self.alternative()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, alternative29.tree)


                # grammars/Core.g:80:27: ( COMMA ! alternative )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == COMMA) :
                        LA7_2 = self.input.LA(2)

                        if (self.synpred11_Core()) :
                            alt7 = 1




                    if alt7 == 1:
                        # grammars/Core.g:80:28: COMMA ! alternative
                        pass 
                        COMMA30 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_alternatives791)

                        self._state.following.append(self.FOLLOW_alternative_in_alternatives794)
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
    # grammars/Core.g:81:1: alternative : LT INT GT ( ID )* ARROW expression -> ^( ALTERNATIVE INT ( ID )* expression ) ;
    def alternative(self, ):
        retval = self.alternative_return()
        retval.start = self.input.LT(1)

        alternative_StartIndex = self.input.index()

        root_0 = None

        LT32 = None
        INT33 = None
        GT34 = None
        ID35 = None
        ARROW36 = None
        expression37 = None


        LT32_tree = None
        INT33_tree = None
        GT34_tree = None
        ID35_tree = None
        ARROW36_tree = None
        stream_GT = RewriteRuleTokenStream(self._adaptor, "token GT")
        stream_ARROW = RewriteRuleTokenStream(self._adaptor, "token ARROW")
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:82:4: ( LT INT GT ( ID )* ARROW expression -> ^( ALTERNATIVE INT ( ID )* expression ) )
                # grammars/Core.g:82:6: LT INT GT ( ID )* ARROW expression
                pass 
                LT32 = self.match(self.input, LT, self.FOLLOW_LT_in_alternative807) 
                if self._state.backtracking == 0:
                    stream_LT.add(LT32)


                INT33 = self.match(self.input, INT, self.FOLLOW_INT_in_alternative809) 
                if self._state.backtracking == 0:
                    stream_INT.add(INT33)


                GT34 = self.match(self.input, GT, self.FOLLOW_GT_in_alternative811) 
                if self._state.backtracking == 0:
                    stream_GT.add(GT34)


                # grammars/Core.g:82:16: ( ID )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == ID) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammars/Core.g:82:16: ID
                        pass 
                        ID35 = self.match(self.input, ID, self.FOLLOW_ID_in_alternative813) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ID35)



                    else:
                        break #loop8


                ARROW36 = self.match(self.input, ARROW, self.FOLLOW_ARROW_in_alternative816) 
                if self._state.backtracking == 0:
                    stream_ARROW.add(ARROW36)


                self._state.following.append(self.FOLLOW_expression_in_alternative818)
                expression37 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression37.tree)


                # AST Rewrite
                # elements: INT, ID, expression
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
                    # 83:6: -> ^( ALTERNATIVE INT ( ID )* expression )
                    # grammars/Core.g:83:9: ^( ALTERNATIVE INT ( ID )* expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    AlternativeNode(ALTERNATIVE)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    IntNode(stream_INT.nextToken())
                    )

                    # grammars/Core.g:83:53: ( ID )*
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

        COMMA39 = None
        definition38 = None

        definition40 = None


        COMMA39_tree = None

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


                self._state.following.append(self.FOLLOW_definition_in_definitions853)
                definition38 = self.definition()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, definition38.tree)


                # grammars/Core.g:86:25: ( COMMA ! definition )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == COMMA) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammars/Core.g:86:26: COMMA ! definition
                        pass 
                        COMMA39 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_definitions856)

                        self._state.following.append(self.FOLLOW_definition_in_definitions859)
                        definition40 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition40.tree)



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

        ID41 = None
        IS42 = None
        expression43 = None


        ID41_tree = None
        IS42_tree = None
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
                ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_definition872) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID41)


                IS42 = self.match(self.input, IS, self.FOLLOW_IS_in_definition874) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS42)


                self._state.following.append(self.FOLLOW_expression_in_definition876)
                expression43 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression43.tree)


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
    # grammars/Core.g:92:1: expr1 : expr2 ( OR ^ expression )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR45 = None
        expr244 = None

        expression46 = None


        OR45_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:92:6: ( expr2 ( OR ^ expression )* )
                # grammars/Core.g:92:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1905)
                expr244 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr244.tree)


                # grammars/Core.g:92:14: ( OR ^ expression )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == OR) :
                        LA10_2 = self.input.LA(2)

                        if (self.synpred14_Core()) :
                            alt10 = 1




                    if alt10 == 1:
                        # grammars/Core.g:92:15: OR ^ expression
                        pass 
                        OR45 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1908)
                        if self._state.backtracking == 0:
                            OR45_tree = OrNode(OR45) 
                            root_0 = self._adaptor.becomeRoot(OR45_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr1914)
                        expression46 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression46.tree)



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
                self.memoize(self.input, 8, expr1_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr1"


    class expr2_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr2_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr2"
    # grammars/Core.g:94:1: expr2 : expr3 ( AND ^ expression )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND48 = None
        expr347 = None

        expression49 = None


        AND48_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:94:6: ( expr3 ( AND ^ expression )* )
                # grammars/Core.g:94:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2923)
                expr347 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr347.tree)


                # grammars/Core.g:94:14: ( AND ^ expression )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == AND) :
                        LA11_2 = self.input.LA(2)

                        if (self.synpred15_Core()) :
                            alt11 = 1




                    if alt11 == 1:
                        # grammars/Core.g:94:15: AND ^ expression
                        pass 
                        AND48 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2926)
                        if self._state.backtracking == 0:
                            AND48_tree = AndNode(AND48) 
                            root_0 = self._adaptor.becomeRoot(AND48_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr2932)
                        expression49 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression49.tree)



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
                self.memoize(self.input, 9, expr2_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr2"


    class expr3_return(ParserRuleReturnScope):
        def __init__(self):
            super(CoreParser.expr3_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr3"
    # grammars/Core.g:96:1: expr3 : expr4 ( relop ^ expression )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        expr450 = None

        relop51 = None

        expression52 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:96:6: ( expr4 ( relop ^ expression )* )
                # grammars/Core.g:96:8: expr4 ( relop ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3941)
                expr450 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr450.tree)


                # grammars/Core.g:96:14: ( relop ^ expression )*
                while True: #loop12
                    alt12 = 2
                    LA12 = self.input.LA(1)
                    if LA12 == LT:
                        LA12_2 = self.input.LA(2)

                        if (self.synpred16_Core()) :
                            alt12 = 1


                    elif LA12 == LTE:
                        LA12_3 = self.input.LA(2)

                        if (self.synpred16_Core()) :
                            alt12 = 1


                    elif LA12 == EQ:
                        LA12_4 = self.input.LA(2)

                        if (self.synpred16_Core()) :
                            alt12 = 1


                    elif LA12 == NEQ:
                        LA12_5 = self.input.LA(2)

                        if (self.synpred16_Core()) :
                            alt12 = 1


                    elif LA12 == GTE:
                        LA12_6 = self.input.LA(2)

                        if (self.synpred16_Core()) :
                            alt12 = 1


                    elif LA12 == GT:
                        LA12_7 = self.input.LA(2)

                        if (self.synpred16_Core()) :
                            alt12 = 1



                    if alt12 == 1:
                        # grammars/Core.g:96:15: relop ^ expression
                        pass 
                        self._state.following.append(self.FOLLOW_relop_in_expr3944)
                        relop51 = self.relop()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(relop51.tree, root_0)


                        self._state.following.append(self.FOLLOW_expression_in_expr3947)
                        expression52 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression52.tree)



                    else:
                        break #loop12




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
    # grammars/Core.g:98:1: expr4 : expr5 ( ( ADD ^| MIN ^) expr5 )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD54 = None
        MIN55 = None
        expr553 = None

        expr556 = None


        ADD54_tree = None
        MIN55_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:98:6: ( expr5 ( ( ADD ^| MIN ^) expr5 )* )
                # grammars/Core.g:98:8: expr5 ( ( ADD ^| MIN ^) expr5 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4956)
                expr553 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr553.tree)


                # grammars/Core.g:98:14: ( ( ADD ^| MIN ^) expr5 )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == ADD or LA14_0 == MIN) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammars/Core.g:98:15: ( ADD ^| MIN ^) expr5
                        pass 
                        # grammars/Core.g:98:15: ( ADD ^| MIN ^)
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == ADD) :
                            alt13 = 1
                        elif (LA13_0 == MIN) :
                            alt13 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 13, 0, self.input)

                            raise nvae


                        if alt13 == 1:
                            # grammars/Core.g:98:16: ADD ^
                            pass 
                            ADD54 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4960)
                            if self._state.backtracking == 0:
                                ADD54_tree = AddNode(ADD54) 
                                root_0 = self._adaptor.becomeRoot(ADD54_tree, root_0)




                        elif alt13 == 2:
                            # grammars/Core.g:98:30: MIN ^
                            pass 
                            MIN55 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4966)
                            if self._state.backtracking == 0:
                                MIN55_tree = MinNode(MIN55) 
                                root_0 = self._adaptor.becomeRoot(MIN55_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr5_in_expr4973)
                        expr556 = self.expr5()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr556.tree)



                    else:
                        break #loop14




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

        DIV58 = None
        MUL59 = None
        expr657 = None

        expr660 = None


        DIV58_tree = None
        MUL59_tree = None

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


                self._state.following.append(self.FOLLOW_expr6_in_expr5982)
                expr657 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr657.tree)


                # grammars/Core.g:100:14: ( ( DIV ^| MUL ^) expr6 )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == DIV or LA16_0 == MUL) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammars/Core.g:100:15: ( DIV ^| MUL ^) expr6
                        pass 
                        # grammars/Core.g:100:15: ( DIV ^| MUL ^)
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == DIV) :
                            alt15 = 1
                        elif (LA15_0 == MUL) :
                            alt15 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 15, 0, self.input)

                            raise nvae


                        if alt15 == 1:
                            # grammars/Core.g:100:16: DIV ^
                            pass 
                            DIV58 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5986)
                            if self._state.backtracking == 0:
                                DIV58_tree = DivNode(DIV58) 
                                root_0 = self._adaptor.becomeRoot(DIV58_tree, root_0)




                        elif alt15 == 2:
                            # grammars/Core.g:100:30: MUL ^
                            pass 
                            MUL59 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5992)
                            if self._state.backtracking == 0:
                                MUL59_tree = MulNode(MUL59) 
                                root_0 = self._adaptor.becomeRoot(MUL59_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr6_in_expr5999)
                        expr660 = self.expr6()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr660.tree)



                    else:
                        break #loop16




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
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == FLOAT or LA17_0 == ID or LA17_0 == INT or LA17_0 == LPAREN or LA17_0 == PACK) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammars/Core.g:102:9: lst+= aexpr !
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr61011)
                        lst = self.aexpr()

                        self._state.following.pop()
                        if list_lst is None:
                            list_lst = []
                        list_lst.append(lst.tree)



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1


                if self._state.backtracking == 0:
                    pass
                                          
                    self._adaptor.addChild(root_0, mk_ap_chain(list_lst))






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
    # grammars/Core.g:106:1: aexpr : ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | PACK LCURLY INT COMMA INT RCURLY -> ^( PACK INT INT ) | LPAREN expression RPAREN -> expression );
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID61 = None
        INT62 = None
        FLOAT63 = None
        PACK64 = None
        LCURLY65 = None
        INT66 = None
        COMMA67 = None
        INT68 = None
        RCURLY69 = None
        LPAREN70 = None
        RPAREN72 = None
        expression71 = None


        ID61_tree = None
        INT62_tree = None
        FLOAT63_tree = None
        PACK64_tree = None
        LCURLY65_tree = None
        INT66_tree = None
        COMMA67_tree = None
        INT68_tree = None
        RCURLY69_tree = None
        LPAREN70_tree = None
        RPAREN72_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_PACK = RewriteRuleTokenStream(self._adaptor, "token PACK")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:107:4: ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | PACK LCURLY INT COMMA INT RCURLY -> ^( PACK INT INT ) | LPAREN expression RPAREN -> expression )
                alt18 = 5
                LA18 = self.input.LA(1)
                if LA18 == ID:
                    alt18 = 1
                elif LA18 == INT:
                    alt18 = 2
                elif LA18 == FLOAT:
                    alt18 = 3
                elif LA18 == PACK:
                    alt18 = 4
                elif LA18 == LPAREN:
                    alt18 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammars/Core.g:107:6: ID
                    pass 
                    ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr1028) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID61)


                    # AST Rewrite
                    # elements: ID
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
                        # 108:6: -> ^( ID )
                        # grammars/Core.g:108:9: ^( ID )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IdentifierNode(stream_ID.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt18 == 2:
                    # grammars/Core.g:109:6: INT
                    pass 
                    INT62 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr1049) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT62)


                    # AST Rewrite
                    # elements: INT
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
                        # 110:4: -> ^( INT )
                        # grammars/Core.g:110:7: ^( INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IntNode(stream_INT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt18 == 3:
                    # grammars/Core.g:111:4: FLOAT
                    pass 
                    FLOAT63 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr1066) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT63)


                    # AST Rewrite
                    # elements: FLOAT
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
                        # 112:6: -> ^( FLOAT )
                        # grammars/Core.g:112:9: ^( FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        FloatNode(stream_FLOAT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt18 == 4:
                    # grammars/Core.g:113:6: PACK LCURLY INT COMMA INT RCURLY
                    pass 
                    PACK64 = self.match(self.input, PACK, self.FOLLOW_PACK_in_aexpr1087) 
                    if self._state.backtracking == 0:
                        stream_PACK.add(PACK64)


                    LCURLY65 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_aexpr1089) 
                    if self._state.backtracking == 0:
                        stream_LCURLY.add(LCURLY65)


                    INT66 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr1091) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT66)


                    COMMA67 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_aexpr1093) 
                    if self._state.backtracking == 0:
                        stream_COMMA.add(COMMA67)


                    INT68 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr1095) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT68)


                    RCURLY69 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_aexpr1097) 
                    if self._state.backtracking == 0:
                        stream_RCURLY.add(RCURLY69)


                    # AST Rewrite
                    # elements: PACK, INT, INT
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
                        # 114:6: -> ^( PACK INT INT )
                        # grammars/Core.g:114:9: ^( PACK INT INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        ConstructorNode(stream_PACK.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        IntNode(stream_INT.nextToken())
                        )

                        self._adaptor.addChild(root_1, 
                        IntNode(stream_INT.nextToken())
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt18 == 5:
                    # grammars/Core.g:115:6: LPAREN expression RPAREN
                    pass 
                    LPAREN70 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr1128) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN70)


                    self._state.following.append(self.FOLLOW_expression_in_aexpr1130)
                    expression71 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression71.tree)


                    RPAREN72 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr1132) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN72)


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
                        # 116:6: -> expression
                        self._adaptor.addChild(root_0, stream_expression.nextTree())




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
    # grammars/Core.g:119:1: relop : ( LT | LTE | EQ | NEQ | GTE | GT );
    def relop(self, ):
        retval = self.relop_return()
        retval.start = self.input.LT(1)

        relop_StartIndex = self.input.index()

        root_0 = None

        LT73 = None
        LTE74 = None
        EQ75 = None
        NEQ76 = None
        GTE77 = None
        GT78 = None

        LT73_tree = None
        LTE74_tree = None
        EQ75_tree = None
        NEQ76_tree = None
        GTE77_tree = None
        GT78_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Core.g:119:6: ( LT | LTE | EQ | NEQ | GTE | GT )
                alt19 = 6
                LA19 = self.input.LA(1)
                if LA19 == LT:
                    alt19 = 1
                elif LA19 == LTE:
                    alt19 = 2
                elif LA19 == EQ:
                    alt19 = 3
                elif LA19 == NEQ:
                    alt19 = 4
                elif LA19 == GTE:
                    alt19 = 5
                elif LA19 == GT:
                    alt19 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammars/Core.g:119:8: LT
                    pass 
                    root_0 = self._adaptor.nil()


                    LT73 = self.match(self.input, LT, self.FOLLOW_LT_in_relop1149)
                    if self._state.backtracking == 0:
                        LT73_tree = LessThanNode(LT73) 
                        self._adaptor.addChild(root_0, LT73_tree)




                elif alt19 == 2:
                    # grammars/Core.g:119:27: LTE
                    pass 
                    root_0 = self._adaptor.nil()


                    LTE74 = self.match(self.input, LTE, self.FOLLOW_LTE_in_relop1156)
                    if self._state.backtracking == 0:
                        LTE74_tree = LessThanEqualNode(LTE74) 
                        self._adaptor.addChild(root_0, LTE74_tree)




                elif alt19 == 3:
                    # grammars/Core.g:119:52: EQ
                    pass 
                    root_0 = self._adaptor.nil()


                    EQ75 = self.match(self.input, EQ, self.FOLLOW_EQ_in_relop1163)
                    if self._state.backtracking == 0:
                        EQ75_tree = EqualNode(EQ75) 
                        self._adaptor.addChild(root_0, EQ75_tree)




                elif alt19 == 4:
                    # grammars/Core.g:119:68: NEQ
                    pass 
                    root_0 = self._adaptor.nil()


                    NEQ76 = self.match(self.input, NEQ, self.FOLLOW_NEQ_in_relop1170)
                    if self._state.backtracking == 0:
                        NEQ76_tree = NotEqualNode(NEQ76) 
                        self._adaptor.addChild(root_0, NEQ76_tree)




                elif alt19 == 5:
                    # grammars/Core.g:119:88: GTE
                    pass 
                    root_0 = self._adaptor.nil()


                    GTE77 = self.match(self.input, GTE, self.FOLLOW_GTE_in_relop1177)
                    if self._state.backtracking == 0:
                        GTE77_tree = GreaterThanEqualNode(GTE77) 
                        self._adaptor.addChild(root_0, GTE77_tree)




                elif alt19 == 6:
                    # grammars/Core.g:119:116: GT
                    pass 
                    root_0 = self._adaptor.nil()


                    GT78 = self.match(self.input, GT, self.FOLLOW_GT_in_relop1184)
                    if self._state.backtracking == 0:
                        GT78_tree = GreaterThanNode(GT78) 
                        self._adaptor.addChild(root_0, GT78_tree)




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
        # grammars/Core.g:80:28: ( COMMA alternative )
        # grammars/Core.g:80:28: COMMA alternative
        pass 
        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred11_Core791)

        self._state.following.append(self.FOLLOW_alternative_in_synpred11_Core794)
        self.alternative()

        self._state.following.pop()



    # $ANTLR end "synpred11_Core"



    # $ANTLR start "synpred14_Core"
    def synpred14_Core_fragment(self, ):
        # grammars/Core.g:92:15: ( OR expression )
        # grammars/Core.g:92:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred14_Core908)

        self._state.following.append(self.FOLLOW_expression_in_synpred14_Core914)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred14_Core"



    # $ANTLR start "synpred15_Core"
    def synpred15_Core_fragment(self, ):
        # grammars/Core.g:94:15: ( AND expression )
        # grammars/Core.g:94:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred15_Core926)

        self._state.following.append(self.FOLLOW_expression_in_synpred15_Core932)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred15_Core"



    # $ANTLR start "synpred16_Core"
    def synpred16_Core_fragment(self, ):
        # grammars/Core.g:96:15: ( relop expression )
        # grammars/Core.g:96:15: relop expression
        pass 
        self._state.following.append(self.FOLLOW_relop_in_synpred16_Core944)
        self.relop()

        self._state.following.pop()

        self._state.following.append(self.FOLLOW_expression_in_synpred16_Core947)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred16_Core"




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

    def synpred15_Core(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_Core_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred16_Core(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred16_Core_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_COMMENT_in_program552 = frozenset([13, 42])
    FOLLOW_combinator_in_program556 = frozenset([13, 42])
    FOLLOW_SCOLON_in_program560 = frozenset([21])
    FOLLOW_combinator_in_program562 = frozenset([13, 42])
    FOLLOW_COMMENT_in_program566 = frozenset([13, 42])
    FOLLOW_SCOLON_in_program570 = frozenset([])
    FOLLOW_EOF_in_program573 = frozenset([1])
    FOLLOW_ID_in_combinator603 = frozenset([21, 24])
    FOLLOW_ID_in_combinator605 = frozenset([21, 24])
    FOLLOW_IS_in_combinator608 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_combinator610 = frozenset([1])
    FOLLOW_LET_in_expression651 = frozenset([21])
    FOLLOW_definitions_in_expression653 = frozenset([22])
    FOLLOW_IN_in_expression655 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_expression657 = frozenset([1])
    FOLLOW_LETREC_in_expression682 = frozenset([21])
    FOLLOW_definitions_in_expression684 = frozenset([22])
    FOLLOW_IN_in_expression686 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_expression688 = frozenset([1])
    FOLLOW_CASE_in_expression713 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_expression715 = frozenset([36])
    FOLLOW_OF_in_expression717 = frozenset([30])
    FOLLOW_alternatives_in_expression719 = frozenset([1])
    FOLLOW_LAMBDA_in_expression744 = frozenset([21])
    FOLLOW_ID_in_expression746 = frozenset([16, 21])
    FOLLOW_DOT_in_expression749 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_expression751 = frozenset([1])
    FOLLOW_expr1_in_expression780 = frozenset([1])
    FOLLOW_alternative_in_alternatives788 = frozenset([1, 12])
    FOLLOW_COMMA_in_alternatives791 = frozenset([30])
    FOLLOW_alternative_in_alternatives794 = frozenset([1, 12])
    FOLLOW_LT_in_alternative807 = frozenset([23])
    FOLLOW_INT_in_alternative809 = frozenset([19])
    FOLLOW_GT_in_alternative811 = frozenset([8, 21])
    FOLLOW_ID_in_alternative813 = frozenset([8, 21])
    FOLLOW_ARROW_in_alternative816 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_alternative818 = frozenset([1])
    FOLLOW_definition_in_definitions853 = frozenset([1, 12])
    FOLLOW_COMMA_in_definitions856 = frozenset([21])
    FOLLOW_definition_in_definitions859 = frozenset([1, 12])
    FOLLOW_ID_in_definition872 = frozenset([24])
    FOLLOW_IS_in_definition874 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_definition876 = frozenset([1])
    FOLLOW_expr2_in_expr1905 = frozenset([1, 37])
    FOLLOW_OR_in_expr1908 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_expr1914 = frozenset([1, 37])
    FOLLOW_expr3_in_expr2923 = frozenset([1, 6])
    FOLLOW_AND_in_expr2926 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_expr2932 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3941 = frozenset([1, 17, 19, 20, 30, 31, 34])
    FOLLOW_relop_in_expr3944 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_expr3947 = frozenset([1, 17, 19, 20, 30, 31, 34])
    FOLLOW_expr5_in_expr4956 = frozenset([1, 4, 32])
    FOLLOW_ADD_in_expr4960 = frozenset([18, 21, 23, 29, 38])
    FOLLOW_MIN_in_expr4966 = frozenset([18, 21, 23, 29, 38])
    FOLLOW_expr5_in_expr4973 = frozenset([1, 4, 32])
    FOLLOW_expr6_in_expr5982 = frozenset([1, 15, 33])
    FOLLOW_DIV_in_expr5986 = frozenset([18, 21, 23, 29, 38])
    FOLLOW_MUL_in_expr5992 = frozenset([18, 21, 23, 29, 38])
    FOLLOW_expr6_in_expr5999 = frozenset([1, 15, 33])
    FOLLOW_aexpr_in_expr61011 = frozenset([1, 18, 21, 23, 29, 38])
    FOLLOW_ID_in_aexpr1028 = frozenset([1])
    FOLLOW_INT_in_aexpr1049 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr1066 = frozenset([1])
    FOLLOW_PACK_in_aexpr1087 = frozenset([26])
    FOLLOW_LCURLY_in_aexpr1089 = frozenset([23])
    FOLLOW_INT_in_aexpr1091 = frozenset([12])
    FOLLOW_COMMA_in_aexpr1093 = frozenset([23])
    FOLLOW_INT_in_aexpr1095 = frozenset([40])
    FOLLOW_RCURLY_in_aexpr1097 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr1128 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_aexpr1130 = frozenset([41])
    FOLLOW_RPAREN_in_aexpr1132 = frozenset([1])
    FOLLOW_LT_in_relop1149 = frozenset([1])
    FOLLOW_LTE_in_relop1156 = frozenset([1])
    FOLLOW_EQ_in_relop1163 = frozenset([1])
    FOLLOW_NEQ_in_relop1170 = frozenset([1])
    FOLLOW_GTE_in_relop1177 = frozenset([1])
    FOLLOW_GT_in_relop1184 = frozenset([1])
    FOLLOW_COMMA_in_synpred11_Core791 = frozenset([30])
    FOLLOW_alternative_in_synpred11_Core794 = frozenset([1])
    FOLLOW_OR_in_synpred14_Core908 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_synpred14_Core914 = frozenset([1])
    FOLLOW_AND_in_synpred15_Core926 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_synpred15_Core932 = frozenset([1])
    FOLLOW_relop_in_synpred16_Core944 = frozenset([9, 18, 21, 23, 25, 27, 28, 29, 38])
    FOLLOW_expression_in_synpred16_Core947 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("CoreLexer", CoreParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
