# $ANTLR 3.4 grammars/Miranda.g 2011-12-27 22:41:32

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *


        
from ast import mk_ap_chain, IntNode, FloatNode, IdentifierNode, CharNode, AddNode, MinNode, MulNode, DivNode, OrNode, AndNode
from miranda_ast import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ADD=4
ALPHANUMERIC=5
AND=6
BODY=7
CHAR=8
CHAR_TYPE=9
COLON=10
COMMA=11
COMMENT=12
CONCAT=13
DEDENT=14
DEFINITION=15
DIV=16
DOT=17
DOUBLE_QUOTE=18
EQ=19
EXP=20
FALSE=21
FLOAT=22
GENERIC=23
GT=24
GTE=25
ID=26
IDIV=27
INT=28
IS=29
LBRACKET=30
LIST=31
LPAREN=32
LT=33
LTE=34
MIN=35
MOD=36
MUL=37
NEQ=38
NOT=39
NUMERIC=40
NUM_TYPE=41
OR=42
OTHERWISE=43
PROGRAM=44
RBRACKET=45
RPAREN=46
SECTION=47
SINGLE_QUOTE=48
STARS=49
STRING=50
SUBTRACT=51
TRUE=52
TUPLE=53
TYPE=54
TYPE_IS=55
WHERE=56
WHITESPACE=57

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALPHANUMERIC", "AND", "BODY", "CHAR", "CHAR_TYPE", "COLON", 
    "COMMA", "COMMENT", "CONCAT", "DEDENT", "DEFINITION", "DIV", "DOT", 
    "DOUBLE_QUOTE", "EQ", "EXP", "FALSE", "FLOAT", "GENERIC", "GT", "GTE", 
    "ID", "IDIV", "INT", "IS", "LBRACKET", "LIST", "LPAREN", "LT", "LTE", 
    "MIN", "MOD", "MUL", "NEQ", "NOT", "NUMERIC", "NUM_TYPE", "OR", "OTHERWISE", 
    "PROGRAM", "RBRACKET", "RPAREN", "SECTION", "SINGLE_QUOTE", "STARS", 
    "STRING", "SUBTRACT", "TRUE", "TUPLE", "TYPE", "TYPE_IS", "WHERE", "WHITESPACE"
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
    # grammars/Miranda.g:111:1: program : ( ( typedef ) DEDENT )* expression EOF -> ^( PROGRAM ( typedef )* expression ) ;
    def program(self, ):
        retval = self.program_return()
        retval.start = self.input.LT(1)

        program_StartIndex = self.input.index()

        root_0 = None

        DEDENT2 = None
        EOF4 = None
        typedef1 = None

        expression3 = None


        DEDENT2_tree = None
        EOF4_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_typedef = RewriteRuleSubtreeStream(self._adaptor, "rule typedef")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:111:8: ( ( ( typedef ) DEDENT )* expression EOF -> ^( PROGRAM ( typedef )* expression ) )
                # grammars/Miranda.g:112:3: ( ( typedef ) DEDENT )* expression EOF
                pass 
                # grammars/Miranda.g:112:3: ( ( typedef ) DEDENT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        LA1_1 = self.input.LA(2)

                        if (LA1_1 == STARS) :
                            LA1_3 = self.input.LA(3)

                            if (LA1_3 == STARS or LA1_3 == TYPE_IS) :
                                alt1 = 1


                        elif (LA1_1 == TYPE_IS) :
                            alt1 = 1




                    if alt1 == 1:
                        # grammars/Miranda.g:112:4: ( typedef ) DEDENT
                        pass 
                        # grammars/Miranda.g:112:4: ( typedef )
                        # grammars/Miranda.g:112:5: typedef
                        pass 
                        self._state.following.append(self.FOLLOW_typedef_in_program651)
                        typedef1 = self.typedef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_typedef.add(typedef1.tree)





                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_program654) 
                        if self._state.backtracking == 0:
                            stream_DEDENT.add(DEDENT2)



                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_expression_in_program658)
                expression3 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression3.tree)


                EOF4 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program660) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)


                # AST Rewrite
                # elements: expression, typedef
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
                    # 113:3: -> ^( PROGRAM ( typedef )* expression )
                    # grammars/Miranda.g:113:6: ^( PROGRAM ( typedef )* expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    ProgramNode(PROGRAM)
                    , root_1)

                    # grammars/Miranda.g:113:29: ( typedef )*
                    while stream_typedef.hasNext():
                        self._adaptor.addChild(root_1, stream_typedef.nextTree())


                    stream_typedef.reset();

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
                self.memoize(self.input, 1, program_StartIndex, success)


            pass
        return retval

    # $ANTLR end "program"


    class definition_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.definition_return, self).__init__()

            self.tree = None





    # $ANTLR start "definition"
    # grammars/Miranda.g:116:1: definition : ID ( parameter )* ( body )* -> ^( DEFINITION ID ( parameter )* ( body )* ) ;
    def definition(self, ):
        retval = self.definition_return()
        retval.start = self.input.LT(1)

        definition_StartIndex = self.input.index()

        root_0 = None

        ID5 = None
        parameter6 = None

        body7 = None


        ID5_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_body = RewriteRuleSubtreeStream(self._adaptor, "rule body")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:118:3: ( ID ( parameter )* ( body )* -> ^( DEFINITION ID ( parameter )* ( body )* ) )
                # grammars/Miranda.g:118:5: ID ( parameter )* ( body )*
                pass 
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_definition690) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID5)


                # grammars/Miranda.g:118:8: ( parameter )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((FALSE <= LA2_0 <= FLOAT) or LA2_0 == ID or LA2_0 == INT or LA2_0 == LBRACKET or LA2_0 == LPAREN or LA2_0 == TRUE) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammars/Miranda.g:118:8: parameter
                        pass 
                        self._state.following.append(self.FOLLOW_parameter_in_definition692)
                        parameter6 = self.parameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameter.add(parameter6.tree)



                    else:
                        break #loop2


                # grammars/Miranda.g:118:19: ( body )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == IS) :
                        LA3_2 = self.input.LA(2)

                        if (self.synpred3_Miranda()) :
                            alt3 = 1




                    if alt3 == 1:
                        # grammars/Miranda.g:118:19: body
                        pass 
                        self._state.following.append(self.FOLLOW_body_in_definition695)
                        body7 = self.body()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_body.add(body7.tree)



                    else:
                        break #loop3


                # AST Rewrite
                # elements: ID, body, parameter
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
                    # 119:5: -> ^( DEFINITION ID ( parameter )* ( body )* )
                    # grammars/Miranda.g:119:8: ^( DEFINITION ID ( parameter )* ( body )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    MirandaDefinitionNode(DEFINITION)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammars/Miranda.g:119:47: ( parameter )*
                    while stream_parameter.hasNext():
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())


                    stream_parameter.reset();

                    # grammars/Miranda.g:119:58: ( body )*
                    while stream_body.hasNext():
                        self._adaptor.addChild(root_1, stream_body.nextTree())


                    stream_body.reset();

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


    class typedef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.typedef_return, self).__init__()

            self.tree = None





    # $ANTLR start "typedef"
    # grammars/Miranda.g:123:1: typedef : ID ( STARS )* TYPE_IS -> ^( TYPE ^( ID ( STARS )* ) ) ;
    def typedef(self, ):
        retval = self.typedef_return()
        retval.start = self.input.LT(1)

        typedef_StartIndex = self.input.index()

        root_0 = None

        ID8 = None
        STARS9 = None
        TYPE_IS10 = None

        ID8_tree = None
        STARS9_tree = None
        TYPE_IS10_tree = None
        stream_STARS = RewriteRuleTokenStream(self._adaptor, "token STARS")
        stream_TYPE_IS = RewriteRuleTokenStream(self._adaptor, "token TYPE_IS")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:124:3: ( ID ( STARS )* TYPE_IS -> ^( TYPE ^( ID ( STARS )* ) ) )
                # grammars/Miranda.g:124:5: ID ( STARS )* TYPE_IS
                pass 
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_typedef731) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID8)


                # grammars/Miranda.g:124:8: ( STARS )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == STARS) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammars/Miranda.g:124:8: STARS
                        pass 
                        STARS9 = self.match(self.input, STARS, self.FOLLOW_STARS_in_typedef733) 
                        if self._state.backtracking == 0:
                            stream_STARS.add(STARS9)



                    else:
                        break #loop4


                TYPE_IS10 = self.match(self.input, TYPE_IS, self.FOLLOW_TYPE_IS_in_typedef736) 
                if self._state.backtracking == 0:
                    stream_TYPE_IS.add(TYPE_IS10)


                # AST Rewrite
                # elements: STARS, ID
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
                    # 125:5: -> ^( TYPE ^( ID ( STARS )* ) )
                    # grammars/Miranda.g:125:8: ^( TYPE ^( ID ( STARS )* ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TYPE, "TYPE")
                    , root_1)

                    # grammars/Miranda.g:125:15: ^( ID ( STARS )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    stream_ID.nextNode()
                    , root_2)

                    # grammars/Miranda.g:125:20: ( STARS )*
                    while stream_STARS.hasNext():
                        self._adaptor.addChild(root_2, 
                        stream_STARS.nextNode()
                        )


                    stream_STARS.reset();

                    self._adaptor.addChild(root_1, root_2)

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
                self.memoize(self.input, 3, typedef_StartIndex, success)


            pass
        return retval

    # $ANTLR end "typedef"


    class body_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.body_return, self).__init__()

            self.tree = None





    # $ANTLR start "body"
    # grammars/Miranda.g:130:1: body : IS expression ( guard )? ( where )? -> ^( BODY expression ( guard )? ( where )? ) ;
    def body(self, ):
        retval = self.body_return()
        retval.start = self.input.LT(1)

        body_StartIndex = self.input.index()

        root_0 = None

        IS11 = None
        expression12 = None

        guard13 = None

        where14 = None


        IS11_tree = None
        stream_IS = RewriteRuleTokenStream(self._adaptor, "token IS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_guard = RewriteRuleSubtreeStream(self._adaptor, "rule guard")
        stream_where = RewriteRuleSubtreeStream(self._adaptor, "rule where")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:130:5: ( IS expression ( guard )? ( where )? -> ^( BODY expression ( guard )? ( where )? ) )
                # grammars/Miranda.g:130:7: IS expression ( guard )? ( where )?
                pass 
                IS11 = self.match(self.input, IS, self.FOLLOW_IS_in_body769) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS11)


                self._state.following.append(self.FOLLOW_expression_in_body771)
                expression12 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression12.tree)


                # grammars/Miranda.g:130:21: ( guard )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == COMMA) :
                    alt5 = 1
                if alt5 == 1:
                    # grammars/Miranda.g:130:21: guard
                    pass 
                    self._state.following.append(self.FOLLOW_guard_in_body773)
                    guard13 = self.guard()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_guard.add(guard13.tree)





                # grammars/Miranda.g:130:28: ( where )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == WHERE) :
                    alt6 = 1
                if alt6 == 1:
                    # grammars/Miranda.g:130:28: where
                    pass 
                    self._state.following.append(self.FOLLOW_where_in_body776)
                    where14 = self.where()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_where.add(where14.tree)





                # AST Rewrite
                # elements: where, expression, guard
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
                    # 131:7: -> ^( BODY expression ( guard )? ( where )? )
                    # grammars/Miranda.g:131:10: ^( BODY expression ( guard )? ( where )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(BODY, "BODY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    # grammars/Miranda.g:131:28: ( guard )?
                    if stream_guard.hasNext():
                        self._adaptor.addChild(root_1, stream_guard.nextTree())


                    stream_guard.reset();

                    # grammars/Miranda.g:131:35: ( where )?
                    if stream_where.hasNext():
                        self._adaptor.addChild(root_1, stream_where.nextTree())


                    stream_where.reset();

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
                self.memoize(self.input, 4, body_StartIndex, success)


            pass
        return retval

    # $ANTLR end "body"


    class guard_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.guard_return, self).__init__()

            self.tree = None





    # $ANTLR start "guard"
    # grammars/Miranda.g:134:1: guard : COMMA ( expression | OTHERWISE ) ;
    def guard(self, ):
        retval = self.guard_return()
        retval.start = self.input.LT(1)

        guard_StartIndex = self.input.index()

        root_0 = None

        COMMA15 = None
        OTHERWISE17 = None
        expression16 = None


        COMMA15_tree = None
        OTHERWISE17_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:134:6: ( COMMA ( expression | OTHERWISE ) )
                # grammars/Miranda.g:134:8: COMMA ( expression | OTHERWISE )
                pass 
                root_0 = self._adaptor.nil()


                COMMA15 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_guard805)
                if self._state.backtracking == 0:
                    COMMA15_tree = self._adaptor.createWithPayload(COMMA15)
                    self._adaptor.addChild(root_0, COMMA15_tree)



                # grammars/Miranda.g:134:14: ( expression | OTHERWISE )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == CHAR or (FALSE <= LA7_0 <= FLOAT) or LA7_0 == ID or LA7_0 == INT or LA7_0 == LBRACKET or LA7_0 == LPAREN or LA7_0 == NOT or LA7_0 == STRING or LA7_0 == TRUE) :
                    alt7 = 1
                elif (LA7_0 == OTHERWISE) :
                    alt7 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammars/Miranda.g:134:15: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_guard808)
                    expression16 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression16.tree)



                elif alt7 == 2:
                    # grammars/Miranda.g:134:26: OTHERWISE
                    pass 
                    OTHERWISE17 = self.match(self.input, OTHERWISE, self.FOLLOW_OTHERWISE_in_guard810)
                    if self._state.backtracking == 0:
                        OTHERWISE17_tree = self._adaptor.createWithPayload(OTHERWISE17)
                        self._adaptor.addChild(root_0, OTHERWISE17_tree)








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
                self.memoize(self.input, 5, guard_StartIndex, success)


            pass
        return retval

    # $ANTLR end "guard"


    class where_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.where_return, self).__init__()

            self.tree = None





    # $ANTLR start "where"
    # grammars/Miranda.g:136:1: where : WHERE definition ( DEDENT ! definition )* ;
    def where(self, ):
        retval = self.where_return()
        retval.start = self.input.LT(1)

        where_StartIndex = self.input.index()

        root_0 = None

        WHERE18 = None
        DEDENT20 = None
        definition19 = None

        definition21 = None


        WHERE18_tree = None
        DEDENT20_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:136:6: ( WHERE definition ( DEDENT ! definition )* )
                # grammars/Miranda.g:136:8: WHERE definition ( DEDENT ! definition )*
                pass 
                root_0 = self._adaptor.nil()


                WHERE18 = self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where818)
                if self._state.backtracking == 0:
                    WHERE18_tree = self._adaptor.createWithPayload(WHERE18)
                    self._adaptor.addChild(root_0, WHERE18_tree)



                self._state.following.append(self.FOLLOW_definition_in_where820)
                definition19 = self.definition()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, definition19.tree)


                # grammars/Miranda.g:136:25: ( DEDENT ! definition )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == DEDENT) :
                        LA8_1 = self.input.LA(2)

                        if (self.synpred8_Miranda()) :
                            alt8 = 1




                    if alt8 == 1:
                        # grammars/Miranda.g:136:26: DEDENT ! definition
                        pass 
                        DEDENT20 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_where823)

                        self._state.following.append(self.FOLLOW_definition_in_where826)
                        definition21 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition21.tree)



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
                self.memoize(self.input, 6, where_StartIndex, success)


            pass
        return retval

    # $ANTLR end "where"


    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.parameter_return, self).__init__()

            self.tree = None





    # $ANTLR start "parameter"
    # grammars/Miranda.g:138:1: parameter : basic ( ( COLON | ADD ) ^ parameter )? ;
    def parameter(self, ):
        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        parameter_StartIndex = self.input.index()

        root_0 = None

        set23 = None
        basic22 = None

        parameter24 = None


        set23_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:139:3: ( basic ( ( COLON | ADD ) ^ parameter )? )
                # grammars/Miranda.g:139:5: basic ( ( COLON | ADD ) ^ parameter )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_basic_in_parameter839)
                basic22 = self.basic()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, basic22.tree)


                # grammars/Miranda.g:139:11: ( ( COLON | ADD ) ^ parameter )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == ADD or LA9_0 == COLON) :
                    alt9 = 1
                if alt9 == 1:
                    # grammars/Miranda.g:139:12: ( COLON | ADD ) ^ parameter
                    pass 
                    set23 = self.input.LT(1)

                    set23 = self.input.LT(1)

                    if self.input.LA(1) == ADD or self.input.LA(1) == COLON:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set23), root_0)

                        self._state.errorRecovery = False


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        raise mse



                    self._state.following.append(self.FOLLOW_parameter_in_parameter849)
                    parameter24 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter24.tree)







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
                self.memoize(self.input, 7, parameter_StartIndex, success)


            pass
        return retval

    # $ANTLR end "parameter"


    class basic_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.basic_return, self).__init__()

            self.tree = None





    # $ANTLR start "basic"
    # grammars/Miranda.g:142:1: basic : ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! parameter RPAREN !);
    def basic(self, ):
        retval = self.basic_return()
        retval.start = self.input.LT(1)

        basic_StartIndex = self.input.index()

        root_0 = None

        ID25 = None
        INT26 = None
        FLOAT27 = None
        LPAREN31 = None
        RPAREN33 = None
        boolean28 = None

        list29 = None

        tuple30 = None

        parameter32 = None


        ID25_tree = None
        INT26_tree = None
        FLOAT27_tree = None
        LPAREN31_tree = None
        RPAREN33_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:143:3: ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! parameter RPAREN !)
                alt10 = 7
                LA10 = self.input.LA(1)
                if LA10 == ID:
                    alt10 = 1
                elif LA10 == INT:
                    alt10 = 2
                elif LA10 == FLOAT:
                    alt10 = 3
                elif LA10 == FALSE or LA10 == TRUE:
                    alt10 = 4
                elif LA10 == LBRACKET:
                    alt10 = 5
                elif LA10 == LPAREN:
                    LA10_6 = self.input.LA(2)

                    if (self.synpred16_Miranda()) :
                        alt10 = 6
                    elif (True) :
                        alt10 = 7
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 10, 6, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # grammars/Miranda.g:143:5: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_basic864)
                    if self._state.backtracking == 0:
                        ID25_tree = self._adaptor.createWithPayload(ID25)
                        self._adaptor.addChild(root_0, ID25_tree)




                elif alt10 == 2:
                    # grammars/Miranda.g:144:5: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT26 = self.match(self.input, INT, self.FOLLOW_INT_in_basic870)
                    if self._state.backtracking == 0:
                        INT26_tree = self._adaptor.createWithPayload(INT26)
                        self._adaptor.addChild(root_0, INT26_tree)




                elif alt10 == 3:
                    # grammars/Miranda.g:145:5: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()


                    FLOAT27 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_basic876)
                    if self._state.backtracking == 0:
                        FLOAT27_tree = self._adaptor.createWithPayload(FLOAT27)
                        self._adaptor.addChild(root_0, FLOAT27_tree)




                elif alt10 == 4:
                    # grammars/Miranda.g:146:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_basic882)
                    boolean28 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean28.tree)



                elif alt10 == 5:
                    # grammars/Miranda.g:147:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_basic888)
                    list29 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list29.tree)



                elif alt10 == 6:
                    # grammars/Miranda.g:148:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_basic894)
                    tuple30 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple30.tree)



                elif alt10 == 7:
                    # grammars/Miranda.g:149:5: LPAREN ! parameter RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN31 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_basic900)

                    self._state.following.append(self.FOLLOW_parameter_in_basic903)
                    parameter32 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter32.tree)


                    RPAREN33 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_basic905)


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
                self.memoize(self.input, 8, basic_StartIndex, success)


            pass
        return retval

    # $ANTLR end "basic"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # grammars/Miranda.g:152:1: expression : expr0 ;
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        expr034 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:152:11: ( expr0 )
                # grammars/Miranda.g:152:13: expr0
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr0_in_expression914)
                expr034 = self.expr0()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr034.tree)




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
                self.memoize(self.input, 9, expression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expression"


    class expr0_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr0_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr0"
    # grammars/Miranda.g:154:1: expr0 : expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? ;
    def expr0(self, ):
        retval = self.expr0_return()
        retval.start = self.input.LT(1)

        expr0_StartIndex = self.input.index()

        root_0 = None

        CONCAT36 = None
        SUBTRACT37 = None
        COLON38 = None
        expr135 = None

        expr039 = None


        CONCAT36_tree = None
        SUBTRACT37_tree = None
        COLON38_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:154:6: ( expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? )
                # grammars/Miranda.g:154:8: expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr1_in_expr0921)
                expr135 = self.expr1()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr135.tree)


                # grammars/Miranda.g:154:14: ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                alt12 = 2
                LA12 = self.input.LA(1)
                if LA12 == CONCAT:
                    LA12_1 = self.input.LA(2)

                    if (self.synpred19_Miranda()) :
                        alt12 = 1
                elif LA12 == SUBTRACT:
                    LA12_2 = self.input.LA(2)

                    if (self.synpred19_Miranda()) :
                        alt12 = 1
                elif LA12 == COLON:
                    LA12_3 = self.input.LA(2)

                    if (self.synpred19_Miranda()) :
                        alt12 = 1
                if alt12 == 1:
                    # grammars/Miranda.g:154:15: ( CONCAT ^| SUBTRACT ^| COLON ^) expr0
                    pass 
                    # grammars/Miranda.g:154:15: ( CONCAT ^| SUBTRACT ^| COLON ^)
                    alt11 = 3
                    LA11 = self.input.LA(1)
                    if LA11 == CONCAT:
                        alt11 = 1
                    elif LA11 == SUBTRACT:
                        alt11 = 2
                    elif LA11 == COLON:
                        alt11 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 11, 0, self.input)

                        raise nvae


                    if alt11 == 1:
                        # grammars/Miranda.g:154:16: CONCAT ^
                        pass 
                        CONCAT36 = self.match(self.input, CONCAT, self.FOLLOW_CONCAT_in_expr0925)
                        if self._state.backtracking == 0:
                            CONCAT36_tree = ConcatNode(CONCAT36) 
                            root_0 = self._adaptor.becomeRoot(CONCAT36_tree, root_0)




                    elif alt11 == 2:
                        # grammars/Miranda.g:154:36: SUBTRACT ^
                        pass 
                        SUBTRACT37 = self.match(self.input, SUBTRACT, self.FOLLOW_SUBTRACT_in_expr0931)
                        if self._state.backtracking == 0:
                            SUBTRACT37_tree = SubtractNode(SUBTRACT37) 
                            root_0 = self._adaptor.becomeRoot(SUBTRACT37_tree, root_0)




                    elif alt11 == 3:
                        # grammars/Miranda.g:154:60: COLON ^
                        pass 
                        COLON38 = self.match(self.input, COLON, self.FOLLOW_COLON_in_expr0937)
                        if self._state.backtracking == 0:
                            COLON38_tree = ColonNode(COLON38) 
                            root_0 = self._adaptor.becomeRoot(COLON38_tree, root_0)






                    self._state.following.append(self.FOLLOW_expr0_in_expr0944)
                    expr039 = self.expr0()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr039.tree)







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
                self.memoize(self.input, 10, expr0_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr0"


    class expr1_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr1_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr1"
    # grammars/Miranda.g:156:1: expr1 : expr2 ( OR ^ expression )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR41 = None
        expr240 = None

        expression42 = None


        OR41_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:156:6: ( expr2 ( OR ^ expression )* )
                # grammars/Miranda.g:156:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1953)
                expr240 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr240.tree)


                # grammars/Miranda.g:156:14: ( OR ^ expression )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == OR) :
                        LA13_2 = self.input.LA(2)

                        if (self.synpred20_Miranda()) :
                            alt13 = 1




                    if alt13 == 1:
                        # grammars/Miranda.g:156:15: OR ^ expression
                        pass 
                        OR41 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1956)
                        if self._state.backtracking == 0:
                            OR41_tree = OrNode(OR41) 
                            root_0 = self._adaptor.becomeRoot(OR41_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr1962)
                        expression42 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression42.tree)



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
                self.memoize(self.input, 11, expr1_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr1"


    class expr2_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr2_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr2"
    # grammars/Miranda.g:158:1: expr2 : expr3 ( AND ^ expression )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND44 = None
        expr343 = None

        expression45 = None


        AND44_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:158:6: ( expr3 ( AND ^ expression )* )
                # grammars/Miranda.g:158:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2971)
                expr343 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr343.tree)


                # grammars/Miranda.g:158:14: ( AND ^ expression )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == AND) :
                        LA14_2 = self.input.LA(2)

                        if (self.synpred21_Miranda()) :
                            alt14 = 1




                    if alt14 == 1:
                        # grammars/Miranda.g:158:15: AND ^ expression
                        pass 
                        AND44 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2974)
                        if self._state.backtracking == 0:
                            AND44_tree = AndNode(AND44) 
                            root_0 = self._adaptor.becomeRoot(AND44_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr2980)
                        expression45 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression45.tree)



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
                self.memoize(self.input, 12, expr2_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr2"


    class expr3_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr3_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr3"
    # grammars/Miranda.g:160:1: expr3 : expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        set47 = None
        expr446 = None

        expression48 = None


        set47_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:160:6: ( expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* )
                # grammars/Miranda.g:160:8: expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3989)
                expr446 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr446.tree)


                # grammars/Miranda.g:160:14: ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == EQ or (GT <= LA15_0 <= GTE) or (LT <= LA15_0 <= LTE) or LA15_0 == NEQ) :
                        LA15_2 = self.input.LA(2)

                        if (self.synpred27_Miranda()) :
                            alt15 = 1




                    if alt15 == 1:
                        # grammars/Miranda.g:160:15: ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression
                        pass 
                        set47 = self.input.LT(1)

                        set47 = self.input.LT(1)

                        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set47), root_0)

                            self._state.errorRecovery = False


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        self._state.following.append(self.FOLLOW_expression_in_expr31007)
                        expression48 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression48.tree)



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
                self.memoize(self.input, 13, expr3_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr3"


    class expr4_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr4_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr4"
    # grammars/Miranda.g:162:1: expr4 : expr5 ( ( ADD ^| MIN ^) expression )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD50 = None
        MIN51 = None
        expr549 = None

        expression52 = None


        ADD50_tree = None
        MIN51_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:162:6: ( expr5 ( ( ADD ^| MIN ^) expression )* )
                # grammars/Miranda.g:162:8: expr5 ( ( ADD ^| MIN ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr41016)
                expr549 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr549.tree)


                # grammars/Miranda.g:162:14: ( ( ADD ^| MIN ^) expression )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == ADD) :
                        LA17_2 = self.input.LA(2)

                        if (self.synpred29_Miranda()) :
                            alt17 = 1


                    elif (LA17_0 == MIN) :
                        LA17_3 = self.input.LA(2)

                        if (self.synpred29_Miranda()) :
                            alt17 = 1




                    if alt17 == 1:
                        # grammars/Miranda.g:162:15: ( ADD ^| MIN ^) expression
                        pass 
                        # grammars/Miranda.g:162:15: ( ADD ^| MIN ^)
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == ADD) :
                            alt16 = 1
                        elif (LA16_0 == MIN) :
                            alt16 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 16, 0, self.input)

                            raise nvae


                        if alt16 == 1:
                            # grammars/Miranda.g:162:16: ADD ^
                            pass 
                            ADD50 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr41020)
                            if self._state.backtracking == 0:
                                ADD50_tree = AddNode(ADD50) 
                                root_0 = self._adaptor.becomeRoot(ADD50_tree, root_0)




                        elif alt16 == 2:
                            # grammars/Miranda.g:162:30: MIN ^
                            pass 
                            MIN51 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr41026)
                            if self._state.backtracking == 0:
                                MIN51_tree = MinNode(MIN51) 
                                root_0 = self._adaptor.becomeRoot(MIN51_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr41033)
                        expression52 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression52.tree)



                    else:
                        break #loop17




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
                self.memoize(self.input, 14, expr4_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr4"


    class expr5_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr5_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr5"
    # grammars/Miranda.g:164:1: expr5 : expr6 ( ( DIV ^|{...}? STARS ^) expression )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV54 = None
        STARS55 = None
        expr653 = None

        expression56 = None


        DIV54_tree = None
        STARS55_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:164:6: ( expr6 ( ( DIV ^|{...}? STARS ^) expression )* )
                # grammars/Miranda.g:164:8: expr6 ( ( DIV ^|{...}? STARS ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr51042)
                expr653 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr653.tree)


                # grammars/Miranda.g:164:14: ( ( DIV ^|{...}? STARS ^) expression )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == DIV) :
                        LA19_2 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif (LA19_0 == STARS) :
                        LA19_3 = self.input.LA(2)

                        if ((((((len(self.input.LT(1).text) == 1)) and ((len(self.input.LT(1).text) == 1)))) and (self.synpred31_Miranda()))) :
                            alt19 = 1




                    if alt19 == 1:
                        # grammars/Miranda.g:164:15: ( DIV ^|{...}? STARS ^) expression
                        pass 
                        # grammars/Miranda.g:164:15: ( DIV ^|{...}? STARS ^)
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == DIV) :
                            alt18 = 1
                        elif (LA18_0 == STARS) :
                            alt18 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 18, 0, self.input)

                            raise nvae


                        if alt18 == 1:
                            # grammars/Miranda.g:164:16: DIV ^
                            pass 
                            DIV54 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr51046)
                            if self._state.backtracking == 0:
                                DIV54_tree = DivNode(DIV54) 
                                root_0 = self._adaptor.becomeRoot(DIV54_tree, root_0)




                        elif alt18 == 2:
                            # grammars/Miranda.g:164:31: {...}? STARS ^
                            pass 
                            if not ((len(self.input.LT(1).text) == 1)):
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                raise FailedPredicateException(self.input, "expr5", "len(self.input.LT(1).text) == 1")


                            STARS55 = self.match(self.input, STARS, self.FOLLOW_STARS_in_expr51055)
                            if self._state.backtracking == 0:
                                STARS55_tree = MulNode(STARS55) 
                                root_0 = self._adaptor.becomeRoot(STARS55_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr51062)
                        expression56 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression56.tree)



                    else:
                        break #loop19




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
                self.memoize(self.input, 15, expr5_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr5"


    class expr6_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr6_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr6"
    # grammars/Miranda.g:166:1: expr6 : expr7 ( ( IDIV ^| MOD ^) expression )* ;
    def expr6(self, ):
        retval = self.expr6_return()
        retval.start = self.input.LT(1)

        expr6_StartIndex = self.input.index()

        root_0 = None

        IDIV58 = None
        MOD59 = None
        expr757 = None

        expression60 = None


        IDIV58_tree = None
        MOD59_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:166:6: ( expr7 ( ( IDIV ^| MOD ^) expression )* )
                # grammars/Miranda.g:166:8: expr7 ( ( IDIV ^| MOD ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr7_in_expr61071)
                expr757 = self.expr7()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr757.tree)


                # grammars/Miranda.g:166:14: ( ( IDIV ^| MOD ^) expression )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == IDIV) :
                        LA21_2 = self.input.LA(2)

                        if (self.synpred33_Miranda()) :
                            alt21 = 1


                    elif (LA21_0 == MOD) :
                        LA21_3 = self.input.LA(2)

                        if (self.synpred33_Miranda()) :
                            alt21 = 1




                    if alt21 == 1:
                        # grammars/Miranda.g:166:15: ( IDIV ^| MOD ^) expression
                        pass 
                        # grammars/Miranda.g:166:15: ( IDIV ^| MOD ^)
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == IDIV) :
                            alt20 = 1
                        elif (LA20_0 == MOD) :
                            alt20 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 20, 0, self.input)

                            raise nvae


                        if alt20 == 1:
                            # grammars/Miranda.g:166:16: IDIV ^
                            pass 
                            IDIV58 = self.match(self.input, IDIV, self.FOLLOW_IDIV_in_expr61075)
                            if self._state.backtracking == 0:
                                IDIV58_tree = self._adaptor.createWithPayload(IDIV58)
                                root_0 = self._adaptor.becomeRoot(IDIV58_tree, root_0)




                        elif alt20 == 2:
                            # grammars/Miranda.g:166:22: MOD ^
                            pass 
                            MOD59 = self.match(self.input, MOD, self.FOLLOW_MOD_in_expr61078)
                            if self._state.backtracking == 0:
                                MOD59_tree = self._adaptor.createWithPayload(MOD59)
                                root_0 = self._adaptor.becomeRoot(MOD59_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr61082)
                        expression60 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression60.tree)



                    else:
                        break #loop21




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
                self.memoize(self.input, 16, expr6_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr6"


    class expr7_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr7_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr7"
    # grammars/Miranda.g:168:1: expr7 : expr8 ( ( EXP ^) expression )* ;
    def expr7(self, ):
        retval = self.expr7_return()
        retval.start = self.input.LT(1)

        expr7_StartIndex = self.input.index()

        root_0 = None

        EXP62 = None
        expr861 = None

        expression63 = None


        EXP62_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:168:6: ( expr8 ( ( EXP ^) expression )* )
                # grammars/Miranda.g:168:8: expr8 ( ( EXP ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr8_in_expr71091)
                expr861 = self.expr8()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr861.tree)


                # grammars/Miranda.g:168:14: ( ( EXP ^) expression )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == EXP) :
                        LA22_2 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1




                    if alt22 == 1:
                        # grammars/Miranda.g:168:15: ( EXP ^) expression
                        pass 
                        # grammars/Miranda.g:168:15: ( EXP ^)
                        # grammars/Miranda.g:168:16: EXP ^
                        pass 
                        EXP62 = self.match(self.input, EXP, self.FOLLOW_EXP_in_expr71095)
                        if self._state.backtracking == 0:
                            EXP62_tree = self._adaptor.createWithPayload(EXP62)
                            root_0 = self._adaptor.becomeRoot(EXP62_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr71099)
                        expression63 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression63.tree)



                    else:
                        break #loop22




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
                self.memoize(self.input, 17, expr7_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr7"


    class expr8_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr8_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr8"
    # grammars/Miranda.g:170:1: expr8 : ( aexpr )+ ;
    def expr8(self, ):
        retval = self.expr8_return()
        retval.start = self.input.LT(1)

        expr8_StartIndex = self.input.index()

        root_0 = None

        aexpr64 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:170:6: ( ( aexpr )+ )
                # grammars/Miranda.g:170:8: ( aexpr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:170:8: ( aexpr )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23 = self.input.LA(1)
                    if LA23 == ID:
                        LA23_19 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == INT:
                        LA23_20 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == FLOAT:
                        LA23_21 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == CHAR:
                        LA23_22 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == STRING:
                        LA23_23 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == NOT:
                        LA23_24 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == FALSE or LA23 == TRUE:
                        LA23_25 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == LPAREN:
                        LA23_26 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1


                    elif LA23 == LBRACKET:
                        LA23_27 = self.input.LA(2)

                        if (self.synpred35_Miranda()) :
                            alt23 = 1



                    if alt23 == 1:
                        # grammars/Miranda.g:170:8: aexpr
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr81108)
                        aexpr64 = self.aexpr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, aexpr64.tree)



                    else:
                        if cnt23 >= 1:
                            break #loop23

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(23, self.input)
                        raise eee

                    cnt23 += 1


                if self._state.backtracking == 0:
                    pass
                                  
                    chain = mk_ap_chain(root_0.children)
                    root_0.children = []
                    self._adaptor.addChild(root_0, chain)






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
                self.memoize(self.input, 18, expr8_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr8"


    class aexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.aexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "aexpr"
    # grammars/Miranda.g:176:1: aexpr : ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !);
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID65 = None
        INT66 = None
        FLOAT67 = None
        CHAR68 = None
        STRING69 = None
        NOT70 = None
        LPAREN76 = None
        RPAREN78 = None
        expression71 = None

        boolean72 = None

        section73 = None

        tuple74 = None

        list75 = None

        expression77 = None


        ID65_tree = None
        INT66_tree = None
        FLOAT67_tree = None
        CHAR68_tree = None
        STRING69_tree = None
        NOT70_tree = None
        LPAREN76_tree = None
        RPAREN78_tree = None
        stream_CHAR = RewriteRuleTokenStream(self._adaptor, "token CHAR")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:177:3: ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !)
                alt24 = 11
                LA24 = self.input.LA(1)
                if LA24 == ID:
                    alt24 = 1
                elif LA24 == INT:
                    alt24 = 2
                elif LA24 == FLOAT:
                    alt24 = 3
                elif LA24 == CHAR:
                    alt24 = 4
                elif LA24 == STRING:
                    alt24 = 5
                elif LA24 == NOT:
                    alt24 = 6
                elif LA24 == FALSE or LA24 == TRUE:
                    alt24 = 7
                elif LA24 == LPAREN:
                    LA24_8 = self.input.LA(2)

                    if (self.synpred43_Miranda()) :
                        alt24 = 8
                    elif (self.synpred44_Miranda()) :
                        alt24 = 9
                    elif (True) :
                        alt24 = 11
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 24, 8, self.input)

                        raise nvae


                elif LA24 == LBRACKET:
                    alt24 = 10
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammars/Miranda.g:177:5: ID
                    pass 
                    ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr1121) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID65)


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
                        # 178:5: -> ^( ID )
                        # grammars/Miranda.g:178:8: ^( ID )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IdentifierNode(stream_ID.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt24 == 2:
                    # grammars/Miranda.g:179:5: INT
                    pass 
                    INT66 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr1140) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT66)


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
                        # 180:5: -> ^( INT )
                        # grammars/Miranda.g:180:8: ^( INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IntNode(stream_INT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt24 == 3:
                    # grammars/Miranda.g:181:5: FLOAT
                    pass 
                    FLOAT67 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr1159) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT67)


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
                        # 182:5: -> ^( FLOAT )
                        # grammars/Miranda.g:182:8: ^( FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        FloatNode(stream_FLOAT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt24 == 4:
                    # grammars/Miranda.g:183:5: CHAR
                    pass 
                    CHAR68 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_aexpr1178) 
                    if self._state.backtracking == 0:
                        stream_CHAR.add(CHAR68)


                    # AST Rewrite
                    # elements: CHAR
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
                        # 184:5: -> ^( CHAR )
                        # grammars/Miranda.g:184:8: ^( CHAR )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        CharNode(stream_CHAR.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt24 == 5:
                    # grammars/Miranda.g:185:5: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING69 = self.match(self.input, STRING, self.FOLLOW_STRING_in_aexpr1197)
                    if self._state.backtracking == 0:
                        STRING69_tree = self._adaptor.createWithPayload(STRING69)
                        self._adaptor.addChild(root_0, STRING69_tree)




                elif alt24 == 6:
                    # grammars/Miranda.g:186:5: NOT expression
                    pass 
                    root_0 = self._adaptor.nil()


                    NOT70 = self.match(self.input, NOT, self.FOLLOW_NOT_in_aexpr1203)
                    if self._state.backtracking == 0:
                        NOT70_tree = self._adaptor.createWithPayload(NOT70)
                        self._adaptor.addChild(root_0, NOT70_tree)



                    self._state.following.append(self.FOLLOW_expression_in_aexpr1205)
                    expression71 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression71.tree)



                elif alt24 == 7:
                    # grammars/Miranda.g:187:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_aexpr1211)
                    boolean72 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean72.tree)



                elif alt24 == 8:
                    # grammars/Miranda.g:188:5: section
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_section_in_aexpr1217)
                    section73 = self.section()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, section73.tree)



                elif alt24 == 9:
                    # grammars/Miranda.g:189:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_aexpr1223)
                    tuple74 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple74.tree)



                elif alt24 == 10:
                    # grammars/Miranda.g:190:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_aexpr1229)
                    list75 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list75.tree)



                elif alt24 == 11:
                    # grammars/Miranda.g:191:5: LPAREN ! expression RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN76 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr1235)

                    self._state.following.append(self.FOLLOW_expression_in_aexpr1238)
                    expression77 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression77.tree)


                    RPAREN78 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr1240)


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
                self.memoize(self.input, 19, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class tuple_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.tuple_return, self).__init__()

            self.tree = None





    # $ANTLR start "tuple"
    # grammars/Miranda.g:194:1: tuple : LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) ;
    def tuple(self, ):
        retval = self.tuple_return()
        retval.start = self.input.LT(1)

        tuple_StartIndex = self.input.index()

        root_0 = None

        LPAREN79 = None
        COMMA81 = None
        RPAREN83 = None
        expression80 = None

        expression82 = None


        LPAREN79_tree = None
        COMMA81_tree = None
        RPAREN83_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:194:6: ( LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) )
                # grammars/Miranda.g:194:8: LPAREN expression ( COMMA expression )+ RPAREN
                pass 
                LPAREN79 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_tuple1249) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN79)


                self._state.following.append(self.FOLLOW_expression_in_tuple1251)
                expression80 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression80.tree)


                # grammars/Miranda.g:194:26: ( COMMA expression )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == COMMA) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammars/Miranda.g:194:27: COMMA expression
                        pass 
                        COMMA81 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_tuple1254) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA81)


                        self._state.following.append(self.FOLLOW_expression_in_tuple1256)
                        expression82 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression82.tree)



                    else:
                        if cnt25 >= 1:
                            break #loop25

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1


                RPAREN83 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_tuple1260) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN83)


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
                    # 195:8: -> ^( TUPLE ( expression )* )
                    # grammars/Miranda.g:195:11: ^( TUPLE ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TUPLE, "TUPLE")
                    , root_1)

                    # grammars/Miranda.g:195:19: ( expression )*
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
                self.memoize(self.input, 20, tuple_StartIndex, success)


            pass
        return retval

    # $ANTLR end "tuple"


    class list_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.list_return, self).__init__()

            self.tree = None





    # $ANTLR start "list"
    # grammars/Miranda.g:198:1: list : LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) ;
    def list(self, ):
        retval = self.list_return()
        retval.start = self.input.LT(1)

        list_StartIndex = self.input.index()

        root_0 = None

        LBRACKET84 = None
        COMMA86 = None
        RBRACKET88 = None
        expression85 = None

        expression87 = None


        LBRACKET84_tree = None
        COMMA86_tree = None
        RBRACKET88_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:198:5: ( LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) )
                # grammars/Miranda.g:198:7: LBRACKET ( expression )? ( COMMA expression )* RBRACKET
                pass 
                LBRACKET84 = self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_list1284) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET84)


                # grammars/Miranda.g:198:16: ( expression )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == CHAR or (FALSE <= LA26_0 <= FLOAT) or LA26_0 == ID or LA26_0 == INT or LA26_0 == LBRACKET or LA26_0 == LPAREN or LA26_0 == NOT or LA26_0 == STRING or LA26_0 == TRUE) :
                    alt26 = 1
                if alt26 == 1:
                    # grammars/Miranda.g:198:16: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_list1286)
                    expression85 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression85.tree)





                # grammars/Miranda.g:198:28: ( COMMA expression )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == COMMA) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammars/Miranda.g:198:29: COMMA expression
                        pass 
                        COMMA86 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_list1290) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA86)


                        self._state.following.append(self.FOLLOW_expression_in_list1292)
                        expression87 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression87.tree)



                    else:
                        break #loop27


                RBRACKET88 = self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_list1296) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET88)


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
                    # 199:7: -> ^( LIST ( expression )* )
                    # grammars/Miranda.g:199:10: ^( LIST ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # grammars/Miranda.g:199:17: ( expression )*
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
                self.memoize(self.input, 21, list_StartIndex, success)


            pass
        return retval

    # $ANTLR end "list"


    class section_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.section_return, self).__init__()

            self.tree = None





    # $ANTLR start "section"
    # grammars/Miranda.g:202:1: section : ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) );
    def section(self, ):
        retval = self.section_return()
        retval.start = self.input.LT(1)

        section_StartIndex = self.input.index()

        root_0 = None

        LPAREN89 = None
        RPAREN91 = None
        LPAREN92 = None
        RPAREN95 = None
        LPAREN96 = None
        RPAREN99 = None
        operator90 = None

        operator93 = None

        expression94 = None

        expression97 = None

        operator98 = None


        LPAREN89_tree = None
        RPAREN91_tree = None
        LPAREN92_tree = None
        RPAREN95_tree = None
        LPAREN96_tree = None
        RPAREN99_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_operator = RewriteRuleSubtreeStream(self._adaptor, "rule operator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:203:3: ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) )
                alt28 = 3
                LA28_0 = self.input.LA(1)

                if (LA28_0 == LPAREN) :
                    LA28_1 = self.input.LA(2)

                    if (LA28_1 == ADD or LA28_1 == AND or LA28_1 == CONCAT or LA28_1 == DIV or (EQ <= LA28_1 <= EXP) or (GT <= LA28_1 <= GTE) or LA28_1 == IDIV or (LT <= LA28_1 <= NEQ) or LA28_1 == OR or LA28_1 == SUBTRACT) :
                        LA28_2 = self.input.LA(3)

                        if (LA28_2 == RPAREN) :
                            alt28 = 1
                        elif (LA28_2 == CHAR or (FALSE <= LA28_2 <= FLOAT) or LA28_2 == ID or LA28_2 == INT or LA28_2 == LBRACKET or LA28_2 == LPAREN or LA28_2 == NOT or LA28_2 == STRING or LA28_2 == TRUE) :
                            alt28 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 28, 2, self.input)

                            raise nvae


                    elif (LA28_1 == CHAR or (FALSE <= LA28_1 <= FLOAT) or LA28_1 == ID or LA28_1 == INT or LA28_1 == LBRACKET or LA28_1 == LPAREN or LA28_1 == NOT or LA28_1 == STRING or LA28_1 == TRUE) :
                        alt28 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 28, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # grammars/Miranda.g:203:5: LPAREN operator RPAREN
                    pass 
                    LPAREN89 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1322) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN89)


                    self._state.following.append(self.FOLLOW_operator_in_section1324)
                    operator90 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator90.tree)


                    RPAREN91 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1326) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN91)


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
                        # 204:4: -> ^( SECTION operator )
                        # grammars/Miranda.g:204:7: ^( SECTION operator )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt28 == 2:
                    # grammars/Miranda.g:205:5: LPAREN operator expression RPAREN
                    pass 
                    LPAREN92 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1343) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN92)


                    self._state.following.append(self.FOLLOW_operator_in_section1345)
                    operator93 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator93.tree)


                    self._state.following.append(self.FOLLOW_expression_in_section1347)
                    expression94 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression94.tree)


                    RPAREN95 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1349) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN95)


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
                        # 206:4: -> ^( SECTION operator expression )
                        # grammars/Miranda.g:206:7: ^( SECTION operator expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt28 == 3:
                    # grammars/Miranda.g:207:5: LPAREN expression operator RPAREN
                    pass 
                    LPAREN96 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1368) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN96)


                    self._state.following.append(self.FOLLOW_expression_in_section1370)
                    expression97 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression97.tree)


                    self._state.following.append(self.FOLLOW_operator_in_section1372)
                    operator98 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator98.tree)


                    RPAREN99 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1374) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN99)


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
                        # 208:4: -> ^( SECTION expression operator )
                        # grammars/Miranda.g:208:7: ^( SECTION expression operator )
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
                self.memoize(self.input, 22, section_StartIndex, success)


            pass
        return retval

    # $ANTLR end "section"


    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.operator_return, self).__init__()

            self.tree = None





    # $ANTLR start "operator"
    # grammars/Miranda.g:210:10: fragment operator : ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP );
    def operator(self, ):
        retval = self.operator_return()
        retval.start = self.input.LT(1)

        operator_StartIndex = self.input.index()

        root_0 = None

        set100 = None

        set100_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:210:18: ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set100 = self.input.LT(1)

                if self.input.LA(1) == ADD or self.input.LA(1) == AND or self.input.LA(1) == CONCAT or self.input.LA(1) == DIV or (EQ <= self.input.LA(1) <= EXP) or (GT <= self.input.LA(1) <= GTE) or self.input.LA(1) == IDIV or (LT <= self.input.LA(1) <= NEQ) or self.input.LA(1) == OR or self.input.LA(1) == SUBTRACT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set100))

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
                self.memoize(self.input, 23, operator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "operator"


    class boolean_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.boolean_return, self).__init__()

            self.tree = None





    # $ANTLR start "boolean"
    # grammars/Miranda.g:212:1: boolean : ( TRUE | FALSE );
    def boolean(self, ):
        retval = self.boolean_return()
        retval.start = self.input.LT(1)

        boolean_StartIndex = self.input.index()

        root_0 = None

        set101 = None

        set101_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:212:8: ( TRUE | FALSE )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set101 = self.input.LT(1)

                if self.input.LA(1) == FALSE or self.input.LA(1) == TRUE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set101))

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
                self.memoize(self.input, 24, boolean_StartIndex, success)


            pass
        return retval

    # $ANTLR end "boolean"

    # $ANTLR start "synpred3_Miranda"
    def synpred3_Miranda_fragment(self, ):
        # grammars/Miranda.g:118:19: ( body )
        # grammars/Miranda.g:118:19: body
        pass 
        self._state.following.append(self.FOLLOW_body_in_synpred3_Miranda695)
        self.body()

        self._state.following.pop()



    # $ANTLR end "synpred3_Miranda"



    # $ANTLR start "synpred8_Miranda"
    def synpred8_Miranda_fragment(self, ):
        # grammars/Miranda.g:136:26: ( DEDENT definition )
        # grammars/Miranda.g:136:26: DEDENT definition
        pass 
        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred8_Miranda823)

        self._state.following.append(self.FOLLOW_definition_in_synpred8_Miranda826)
        self.definition()

        self._state.following.pop()



    # $ANTLR end "synpred8_Miranda"



    # $ANTLR start "synpred16_Miranda"
    def synpred16_Miranda_fragment(self, ):
        # grammars/Miranda.g:148:5: ( tuple )
        # grammars/Miranda.g:148:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred16_Miranda894)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred16_Miranda"



    # $ANTLR start "synpred19_Miranda"
    def synpred19_Miranda_fragment(self, ):
        # grammars/Miranda.g:154:15: ( ( CONCAT | SUBTRACT | COLON ) expr0 )
        # grammars/Miranda.g:154:15: ( CONCAT | SUBTRACT | COLON ) expr0
        pass 
        if self.input.LA(1) == COLON or self.input.LA(1) == CONCAT or self.input.LA(1) == SUBTRACT:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr0_in_synpred19_Miranda944)
        self.expr0()

        self._state.following.pop()



    # $ANTLR end "synpred19_Miranda"



    # $ANTLR start "synpred20_Miranda"
    def synpred20_Miranda_fragment(self, ):
        # grammars/Miranda.g:156:15: ( OR expression )
        # grammars/Miranda.g:156:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred20_Miranda956)

        self._state.following.append(self.FOLLOW_expression_in_synpred20_Miranda962)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred20_Miranda"



    # $ANTLR start "synpred21_Miranda"
    def synpred21_Miranda_fragment(self, ):
        # grammars/Miranda.g:158:15: ( AND expression )
        # grammars/Miranda.g:158:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred21_Miranda974)

        self._state.following.append(self.FOLLOW_expression_in_synpred21_Miranda980)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred21_Miranda"



    # $ANTLR start "synpred27_Miranda"
    def synpred27_Miranda_fragment(self, ):
        # grammars/Miranda.g:160:15: ( ( LT | LTE | EQ | NEQ | GTE | GT ) expression )
        # grammars/Miranda.g:160:15: ( LT | LTE | EQ | NEQ | GTE | GT ) expression
        pass 
        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred27_Miranda1007)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred27_Miranda"



    # $ANTLR start "synpred29_Miranda"
    def synpred29_Miranda_fragment(self, ):
        # grammars/Miranda.g:162:15: ( ( ADD | MIN ) expression )
        # grammars/Miranda.g:162:15: ( ADD | MIN ) expression
        pass 
        if self.input.LA(1) == ADD or self.input.LA(1) == MIN:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred29_Miranda1033)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred29_Miranda"



    # $ANTLR start "synpred31_Miranda"
    def synpred31_Miranda_fragment(self, ):
        # grammars/Miranda.g:164:15: ( ( DIV |{...}? STARS ) expression )
        # grammars/Miranda.g:164:15: ( DIV |{...}? STARS ) expression
        pass 
        # grammars/Miranda.g:164:15: ( DIV |{...}? STARS )
        alt29 = 2
        LA29_0 = self.input.LA(1)

        if (LA29_0 == DIV) :
            alt29 = 1
        elif (LA29_0 == STARS) :
            alt29 = 2
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 29, 0, self.input)

            raise nvae


        if alt29 == 1:
            # grammars/Miranda.g:164:16: DIV
            pass 
            self.match(self.input, DIV, self.FOLLOW_DIV_in_synpred31_Miranda1046)


        elif alt29 == 2:
            # grammars/Miranda.g:164:31: {...}? STARS
            pass 
            if not ((len(self.input.LT(1).text) == 1)):
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                raise FailedPredicateException(self.input, "synpred31_Miranda", "len(self.input.LT(1).text) == 1")


            self.match(self.input, STARS, self.FOLLOW_STARS_in_synpred31_Miranda1055)




        self._state.following.append(self.FOLLOW_expression_in_synpred31_Miranda1062)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred31_Miranda"



    # $ANTLR start "synpred33_Miranda"
    def synpred33_Miranda_fragment(self, ):
        # grammars/Miranda.g:166:15: ( ( IDIV | MOD ) expression )
        # grammars/Miranda.g:166:15: ( IDIV | MOD ) expression
        pass 
        if self.input.LA(1) == IDIV or self.input.LA(1) == MOD:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred33_Miranda1082)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred33_Miranda"



    # $ANTLR start "synpred34_Miranda"
    def synpred34_Miranda_fragment(self, ):
        # grammars/Miranda.g:168:15: ( ( EXP ) expression )
        # grammars/Miranda.g:168:15: ( EXP ) expression
        pass 
        # grammars/Miranda.g:168:15: ( EXP )
        # grammars/Miranda.g:168:16: EXP
        pass 
        self.match(self.input, EXP, self.FOLLOW_EXP_in_synpred34_Miranda1095)




        self._state.following.append(self.FOLLOW_expression_in_synpred34_Miranda1099)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred34_Miranda"



    # $ANTLR start "synpred35_Miranda"
    def synpred35_Miranda_fragment(self, ):
        # grammars/Miranda.g:170:8: ( aexpr )
        # grammars/Miranda.g:170:8: aexpr
        pass 
        self._state.following.append(self.FOLLOW_aexpr_in_synpred35_Miranda1108)
        self.aexpr()

        self._state.following.pop()



    # $ANTLR end "synpred35_Miranda"



    # $ANTLR start "synpred43_Miranda"
    def synpred43_Miranda_fragment(self, ):
        # grammars/Miranda.g:188:5: ( section )
        # grammars/Miranda.g:188:5: section
        pass 
        self._state.following.append(self.FOLLOW_section_in_synpred43_Miranda1217)
        self.section()

        self._state.following.pop()



    # $ANTLR end "synpred43_Miranda"



    # $ANTLR start "synpred44_Miranda"
    def synpred44_Miranda_fragment(self, ):
        # grammars/Miranda.g:189:5: ( tuple )
        # grammars/Miranda.g:189:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred44_Miranda1223)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred44_Miranda"




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

    def synpred16_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred16_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred43_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred43_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred33_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred33_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred29_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred29_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred19_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred19_Miranda_fragment()
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

    def synpred31_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred31_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred34_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred34_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred21_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred21_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred35_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred35_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred44_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred44_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred27_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred27_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred20_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred20_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_typedef_in_program651 = frozenset([14])
    FOLLOW_DEDENT_in_program654 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_program658 = frozenset([])
    FOLLOW_EOF_in_program660 = frozenset([1])
    FOLLOW_ID_in_definition690 = frozenset([1, 21, 22, 26, 28, 29, 30, 32, 52])
    FOLLOW_parameter_in_definition692 = frozenset([1, 21, 22, 26, 28, 29, 30, 32, 52])
    FOLLOW_body_in_definition695 = frozenset([1, 29])
    FOLLOW_ID_in_typedef731 = frozenset([49, 55])
    FOLLOW_STARS_in_typedef733 = frozenset([49, 55])
    FOLLOW_TYPE_IS_in_typedef736 = frozenset([1])
    FOLLOW_IS_in_body769 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_body771 = frozenset([1, 11, 56])
    FOLLOW_guard_in_body773 = frozenset([1, 56])
    FOLLOW_where_in_body776 = frozenset([1])
    FOLLOW_COMMA_in_guard805 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 43, 50, 52])
    FOLLOW_expression_in_guard808 = frozenset([1])
    FOLLOW_OTHERWISE_in_guard810 = frozenset([1])
    FOLLOW_WHERE_in_where818 = frozenset([26])
    FOLLOW_definition_in_where820 = frozenset([1, 14])
    FOLLOW_DEDENT_in_where823 = frozenset([26])
    FOLLOW_definition_in_where826 = frozenset([1, 14])
    FOLLOW_basic_in_parameter839 = frozenset([1, 4, 10])
    FOLLOW_set_in_parameter842 = frozenset([21, 22, 26, 28, 30, 32, 52])
    FOLLOW_parameter_in_parameter849 = frozenset([1])
    FOLLOW_ID_in_basic864 = frozenset([1])
    FOLLOW_INT_in_basic870 = frozenset([1])
    FOLLOW_FLOAT_in_basic876 = frozenset([1])
    FOLLOW_boolean_in_basic882 = frozenset([1])
    FOLLOW_list_in_basic888 = frozenset([1])
    FOLLOW_tuple_in_basic894 = frozenset([1])
    FOLLOW_LPAREN_in_basic900 = frozenset([21, 22, 26, 28, 30, 32, 52])
    FOLLOW_parameter_in_basic903 = frozenset([46])
    FOLLOW_RPAREN_in_basic905 = frozenset([1])
    FOLLOW_expr0_in_expression914 = frozenset([1])
    FOLLOW_expr1_in_expr0921 = frozenset([1, 10, 13, 51])
    FOLLOW_CONCAT_in_expr0925 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_SUBTRACT_in_expr0931 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_COLON_in_expr0937 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expr0_in_expr0944 = frozenset([1])
    FOLLOW_expr2_in_expr1953 = frozenset([1, 42])
    FOLLOW_OR_in_expr1956 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_expr1962 = frozenset([1, 42])
    FOLLOW_expr3_in_expr2971 = frozenset([1, 6])
    FOLLOW_AND_in_expr2974 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_expr2980 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3989 = frozenset([1, 19, 24, 25, 33, 34, 38])
    FOLLOW_set_in_expr3992 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_expr31007 = frozenset([1, 19, 24, 25, 33, 34, 38])
    FOLLOW_expr5_in_expr41016 = frozenset([1, 4, 35])
    FOLLOW_ADD_in_expr41020 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_MIN_in_expr41026 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_expr41033 = frozenset([1, 4, 35])
    FOLLOW_expr6_in_expr51042 = frozenset([1, 16, 49])
    FOLLOW_DIV_in_expr51046 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_STARS_in_expr51055 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_expr51062 = frozenset([1, 16, 49])
    FOLLOW_expr7_in_expr61071 = frozenset([1, 27, 36])
    FOLLOW_IDIV_in_expr61075 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_MOD_in_expr61078 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_expr61082 = frozenset([1, 27, 36])
    FOLLOW_expr8_in_expr71091 = frozenset([1, 20])
    FOLLOW_EXP_in_expr71095 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_expr71099 = frozenset([1, 20])
    FOLLOW_aexpr_in_expr81108 = frozenset([1, 8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_ID_in_aexpr1121 = frozenset([1])
    FOLLOW_INT_in_aexpr1140 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr1159 = frozenset([1])
    FOLLOW_CHAR_in_aexpr1178 = frozenset([1])
    FOLLOW_STRING_in_aexpr1197 = frozenset([1])
    FOLLOW_NOT_in_aexpr1203 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_aexpr1205 = frozenset([1])
    FOLLOW_boolean_in_aexpr1211 = frozenset([1])
    FOLLOW_section_in_aexpr1217 = frozenset([1])
    FOLLOW_tuple_in_aexpr1223 = frozenset([1])
    FOLLOW_list_in_aexpr1229 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr1235 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_aexpr1238 = frozenset([46])
    FOLLOW_RPAREN_in_aexpr1240 = frozenset([1])
    FOLLOW_LPAREN_in_tuple1249 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_tuple1251 = frozenset([11])
    FOLLOW_COMMA_in_tuple1254 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_tuple1256 = frozenset([11, 46])
    FOLLOW_RPAREN_in_tuple1260 = frozenset([1])
    FOLLOW_LBRACKET_in_list1284 = frozenset([8, 11, 21, 22, 26, 28, 30, 32, 39, 45, 50, 52])
    FOLLOW_expression_in_list1286 = frozenset([11, 45])
    FOLLOW_COMMA_in_list1290 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_list1292 = frozenset([11, 45])
    FOLLOW_RBRACKET_in_list1296 = frozenset([1])
    FOLLOW_LPAREN_in_section1322 = frozenset([4, 6, 13, 16, 19, 20, 24, 25, 27, 33, 34, 35, 36, 37, 38, 42, 51])
    FOLLOW_operator_in_section1324 = frozenset([46])
    FOLLOW_RPAREN_in_section1326 = frozenset([1])
    FOLLOW_LPAREN_in_section1343 = frozenset([4, 6, 13, 16, 19, 20, 24, 25, 27, 33, 34, 35, 36, 37, 38, 42, 51])
    FOLLOW_operator_in_section1345 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_section1347 = frozenset([46])
    FOLLOW_RPAREN_in_section1349 = frozenset([1])
    FOLLOW_LPAREN_in_section1368 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_section1370 = frozenset([4, 6, 13, 16, 19, 20, 24, 25, 27, 33, 34, 35, 36, 37, 38, 42, 51])
    FOLLOW_operator_in_section1372 = frozenset([46])
    FOLLOW_RPAREN_in_section1374 = frozenset([1])
    FOLLOW_body_in_synpred3_Miranda695 = frozenset([1])
    FOLLOW_DEDENT_in_synpred8_Miranda823 = frozenset([26])
    FOLLOW_definition_in_synpred8_Miranda826 = frozenset([1])
    FOLLOW_tuple_in_synpred16_Miranda894 = frozenset([1])
    FOLLOW_set_in_synpred19_Miranda924 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expr0_in_synpred19_Miranda944 = frozenset([1])
    FOLLOW_OR_in_synpred20_Miranda956 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_synpred20_Miranda962 = frozenset([1])
    FOLLOW_AND_in_synpred21_Miranda974 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_synpred21_Miranda980 = frozenset([1])
    FOLLOW_set_in_synpred27_Miranda992 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_synpred27_Miranda1007 = frozenset([1])
    FOLLOW_set_in_synpred29_Miranda1019 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_synpred29_Miranda1033 = frozenset([1])
    FOLLOW_DIV_in_synpred31_Miranda1046 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_STARS_in_synpred31_Miranda1055 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_synpred31_Miranda1062 = frozenset([1])
    FOLLOW_set_in_synpred33_Miranda1074 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_synpred33_Miranda1082 = frozenset([1])
    FOLLOW_EXP_in_synpred34_Miranda1095 = frozenset([8, 21, 22, 26, 28, 30, 32, 39, 50, 52])
    FOLLOW_expression_in_synpred34_Miranda1099 = frozenset([1])
    FOLLOW_aexpr_in_synpred35_Miranda1108 = frozenset([1])
    FOLLOW_section_in_synpred43_Miranda1217 = frozenset([1])
    FOLLOW_tuple_in_synpred44_Miranda1223 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MirandaLexer", MirandaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
