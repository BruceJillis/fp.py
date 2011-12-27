# $ANTLR 3.4 grammars/Miranda.g 2011-12-27 08:51:46

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
COLON=9
COMMA=10
COMMENT=11
CONCAT=12
DEDENT=13
DEFINITION=14
DIV=15
DOT=16
DOUBLE_QUOTE=17
EQ=18
EXP=19
FALSE=20
FLOAT=21
GT=22
GTE=23
ID=24
IDIV=25
INT=26
IS=27
LBRACKET=28
LIST=29
LPAREN=30
LT=31
LTE=32
MIN=33
MOD=34
MUL=35
NEQ=36
NOT=37
NUMERIC=38
OR=39
OTHERWISE=40
PROGRAM=41
RBRACKET=42
RPAREN=43
SECTION=44
SINGLE_QUOTE=45
STRING=46
SUBTRACT=47
TRUE=48
TUPLE=49
TYPEDEF=50
WHERE=51
WHITESPACE=52

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALPHANUMERIC", "AND", "BODY", "CHAR", "COLON", "COMMA", "COMMENT", 
    "CONCAT", "DEDENT", "DEFINITION", "DIV", "DOT", "DOUBLE_QUOTE", "EQ", 
    "EXP", "FALSE", "FLOAT", "GT", "GTE", "ID", "IDIV", "INT", "IS", "LBRACKET", 
    "LIST", "LPAREN", "LT", "LTE", "MIN", "MOD", "MUL", "NEQ", "NOT", "NUMERIC", 
    "OR", "OTHERWISE", "PROGRAM", "RBRACKET", "RPAREN", "SECTION", "SINGLE_QUOTE", 
    "STRING", "SUBTRACT", "TRUE", "TUPLE", "TYPEDEF", "WHERE", "WHITESPACE"
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
    # grammars/Miranda.g:106:1: program : ( definition DEDENT )* expression EOF -> ^( PROGRAM ( definition )* expression ) ;
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
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_definition = RewriteRuleSubtreeStream(self._adaptor, "rule definition")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:106:8: ( ( definition DEDENT )* expression EOF -> ^( PROGRAM ( definition )* expression ) )
                # grammars/Miranda.g:107:3: ( definition DEDENT )* expression EOF
                pass 
                # grammars/Miranda.g:107:3: ( definition DEDENT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        LA1_1 = self.input.LA(2)

                        if (self.synpred1_Miranda()) :
                            alt1 = 1




                    if alt1 == 1:
                        # grammars/Miranda.g:107:4: definition DEDENT
                        pass 
                        self._state.following.append(self.FOLLOW_definition_in_program600)
                        definition1 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_definition.add(definition1.tree)


                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_program602) 
                        if self._state.backtracking == 0:
                            stream_DEDENT.add(DEDENT2)



                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_expression_in_program606)
                expression3 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression3.tree)


                EOF4 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program608) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)


                # AST Rewrite
                # elements: definition, expression
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
                    # 108:3: -> ^( PROGRAM ( definition )* expression )
                    # grammars/Miranda.g:108:6: ^( PROGRAM ( definition )* expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    ProgramNode(PROGRAM)
                    , root_1)

                    # grammars/Miranda.g:108:29: ( definition )*
                    while stream_definition.hasNext():
                        self._adaptor.addChild(root_1, stream_definition.nextTree())


                    stream_definition.reset();

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
    # grammars/Miranda.g:111:1: definition : ID ( parameter )* ( body )* -> ^( DEFINITION ID ( parameter )* ( body )* ) ;
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


                # grammars/Miranda.g:113:3: ( ID ( parameter )* ( body )* -> ^( DEFINITION ID ( parameter )* ( body )* ) )
                # grammars/Miranda.g:113:5: ID ( parameter )* ( body )*
                pass 
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_definition638) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID5)


                # grammars/Miranda.g:113:8: ( parameter )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((FALSE <= LA2_0 <= FLOAT) or LA2_0 == ID or LA2_0 == INT or LA2_0 == LBRACKET or LA2_0 == LPAREN or LA2_0 == TRUE) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammars/Miranda.g:113:8: parameter
                        pass 
                        self._state.following.append(self.FOLLOW_parameter_in_definition640)
                        parameter6 = self.parameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameter.add(parameter6.tree)



                    else:
                        break #loop2


                # grammars/Miranda.g:113:19: ( body )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == IS) :
                        LA3_2 = self.input.LA(2)

                        if (self.synpred3_Miranda()) :
                            alt3 = 1




                    if alt3 == 1:
                        # grammars/Miranda.g:113:19: body
                        pass 
                        self._state.following.append(self.FOLLOW_body_in_definition643)
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
                    # 114:5: -> ^( DEFINITION ID ( parameter )* ( body )* )
                    # grammars/Miranda.g:114:8: ^( DEFINITION ID ( parameter )* ( body )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    MirandaDefinitionNode(DEFINITION)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammars/Miranda.g:114:47: ( parameter )*
                    while stream_parameter.hasNext():
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())


                    stream_parameter.reset();

                    # grammars/Miranda.g:114:58: ( body )*
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


    class body_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.body_return, self).__init__()

            self.tree = None





    # $ANTLR start "body"
    # grammars/Miranda.g:118:1: body : IS expression ( guard )? ( where )? -> ^( BODY expression ( guard )? ( where )? ) ;
    def body(self, ):
        retval = self.body_return()
        retval.start = self.input.LT(1)

        body_StartIndex = self.input.index()

        root_0 = None

        IS8 = None
        expression9 = None

        guard10 = None

        where11 = None


        IS8_tree = None
        stream_IS = RewriteRuleTokenStream(self._adaptor, "token IS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_guard = RewriteRuleSubtreeStream(self._adaptor, "rule guard")
        stream_where = RewriteRuleSubtreeStream(self._adaptor, "rule where")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:118:5: ( IS expression ( guard )? ( where )? -> ^( BODY expression ( guard )? ( where )? ) )
                # grammars/Miranda.g:118:7: IS expression ( guard )? ( where )?
                pass 
                IS8 = self.match(self.input, IS, self.FOLLOW_IS_in_body676) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS8)


                self._state.following.append(self.FOLLOW_expression_in_body678)
                expression9 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression9.tree)


                # grammars/Miranda.g:118:21: ( guard )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == COMMA) :
                    alt4 = 1
                if alt4 == 1:
                    # grammars/Miranda.g:118:21: guard
                    pass 
                    self._state.following.append(self.FOLLOW_guard_in_body680)
                    guard10 = self.guard()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_guard.add(guard10.tree)





                # grammars/Miranda.g:118:28: ( where )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == WHERE) :
                    alt5 = 1
                if alt5 == 1:
                    # grammars/Miranda.g:118:28: where
                    pass 
                    self._state.following.append(self.FOLLOW_where_in_body683)
                    where11 = self.where()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_where.add(where11.tree)





                # AST Rewrite
                # elements: expression, where, guard
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
                    # 119:7: -> ^( BODY expression ( guard )? ( where )? )
                    # grammars/Miranda.g:119:10: ^( BODY expression ( guard )? ( where )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(BODY, "BODY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    # grammars/Miranda.g:119:28: ( guard )?
                    if stream_guard.hasNext():
                        self._adaptor.addChild(root_1, stream_guard.nextTree())


                    stream_guard.reset();

                    # grammars/Miranda.g:119:35: ( where )?
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
                self.memoize(self.input, 3, body_StartIndex, success)


            pass
        return retval

    # $ANTLR end "body"


    class guard_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.guard_return, self).__init__()

            self.tree = None





    # $ANTLR start "guard"
    # grammars/Miranda.g:122:1: guard : COMMA ( expression | OTHERWISE ) ;
    def guard(self, ):
        retval = self.guard_return()
        retval.start = self.input.LT(1)

        guard_StartIndex = self.input.index()

        root_0 = None

        COMMA12 = None
        OTHERWISE14 = None
        expression13 = None


        COMMA12_tree = None
        OTHERWISE14_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:122:6: ( COMMA ( expression | OTHERWISE ) )
                # grammars/Miranda.g:122:8: COMMA ( expression | OTHERWISE )
                pass 
                root_0 = self._adaptor.nil()


                COMMA12 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_guard712)
                if self._state.backtracking == 0:
                    COMMA12_tree = self._adaptor.createWithPayload(COMMA12)
                    self._adaptor.addChild(root_0, COMMA12_tree)



                # grammars/Miranda.g:122:14: ( expression | OTHERWISE )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == CHAR or (FALSE <= LA6_0 <= FLOAT) or LA6_0 == ID or LA6_0 == INT or LA6_0 == LBRACKET or LA6_0 == LPAREN or LA6_0 == NOT or LA6_0 == STRING or LA6_0 == TRUE) :
                    alt6 = 1
                elif (LA6_0 == OTHERWISE) :
                    alt6 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammars/Miranda.g:122:15: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_guard715)
                    expression13 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression13.tree)



                elif alt6 == 2:
                    # grammars/Miranda.g:122:26: OTHERWISE
                    pass 
                    OTHERWISE14 = self.match(self.input, OTHERWISE, self.FOLLOW_OTHERWISE_in_guard717)
                    if self._state.backtracking == 0:
                        OTHERWISE14_tree = self._adaptor.createWithPayload(OTHERWISE14)
                        self._adaptor.addChild(root_0, OTHERWISE14_tree)








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
                self.memoize(self.input, 4, guard_StartIndex, success)


            pass
        return retval

    # $ANTLR end "guard"


    class where_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.where_return, self).__init__()

            self.tree = None





    # $ANTLR start "where"
    # grammars/Miranda.g:124:1: where : WHERE definition ( DEDENT ! definition )* ;
    def where(self, ):
        retval = self.where_return()
        retval.start = self.input.LT(1)

        where_StartIndex = self.input.index()

        root_0 = None

        WHERE15 = None
        DEDENT17 = None
        definition16 = None

        definition18 = None


        WHERE15_tree = None
        DEDENT17_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:124:6: ( WHERE definition ( DEDENT ! definition )* )
                # grammars/Miranda.g:124:8: WHERE definition ( DEDENT ! definition )*
                pass 
                root_0 = self._adaptor.nil()


                WHERE15 = self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where725)
                if self._state.backtracking == 0:
                    WHERE15_tree = self._adaptor.createWithPayload(WHERE15)
                    self._adaptor.addChild(root_0, WHERE15_tree)



                self._state.following.append(self.FOLLOW_definition_in_where727)
                definition16 = self.definition()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, definition16.tree)


                # grammars/Miranda.g:124:25: ( DEDENT ! definition )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == DEDENT) :
                        LA7_1 = self.input.LA(2)

                        if (self.synpred7_Miranda()) :
                            alt7 = 1




                    if alt7 == 1:
                        # grammars/Miranda.g:124:26: DEDENT ! definition
                        pass 
                        DEDENT17 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_where730)

                        self._state.following.append(self.FOLLOW_definition_in_where733)
                        definition18 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition18.tree)



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
                self.memoize(self.input, 5, where_StartIndex, success)


            pass
        return retval

    # $ANTLR end "where"


    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.parameter_return, self).__init__()

            self.tree = None





    # $ANTLR start "parameter"
    # grammars/Miranda.g:126:1: parameter : basic ( ( COLON | ADD ) ^ parameter )? ;
    def parameter(self, ):
        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        parameter_StartIndex = self.input.index()

        root_0 = None

        set20 = None
        basic19 = None

        parameter21 = None


        set20_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:127:3: ( basic ( ( COLON | ADD ) ^ parameter )? )
                # grammars/Miranda.g:127:5: basic ( ( COLON | ADD ) ^ parameter )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_basic_in_parameter746)
                basic19 = self.basic()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, basic19.tree)


                # grammars/Miranda.g:127:11: ( ( COLON | ADD ) ^ parameter )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ADD or LA8_0 == COLON) :
                    alt8 = 1
                if alt8 == 1:
                    # grammars/Miranda.g:127:12: ( COLON | ADD ) ^ parameter
                    pass 
                    set20 = self.input.LT(1)

                    set20 = self.input.LT(1)

                    if self.input.LA(1) == ADD or self.input.LA(1) == COLON:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set20), root_0)

                        self._state.errorRecovery = False


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        raise mse



                    self._state.following.append(self.FOLLOW_parameter_in_parameter756)
                    parameter21 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter21.tree)







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
                self.memoize(self.input, 6, parameter_StartIndex, success)


            pass
        return retval

    # $ANTLR end "parameter"


    class basic_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.basic_return, self).__init__()

            self.tree = None





    # $ANTLR start "basic"
    # grammars/Miranda.g:130:1: basic : ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! parameter RPAREN !);
    def basic(self, ):
        retval = self.basic_return()
        retval.start = self.input.LT(1)

        basic_StartIndex = self.input.index()

        root_0 = None

        ID22 = None
        INT23 = None
        FLOAT24 = None
        LPAREN28 = None
        RPAREN30 = None
        boolean25 = None

        list26 = None

        tuple27 = None

        parameter29 = None


        ID22_tree = None
        INT23_tree = None
        FLOAT24_tree = None
        LPAREN28_tree = None
        RPAREN30_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:131:3: ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! parameter RPAREN !)
                alt9 = 7
                LA9 = self.input.LA(1)
                if LA9 == ID:
                    alt9 = 1
                elif LA9 == INT:
                    alt9 = 2
                elif LA9 == FLOAT:
                    alt9 = 3
                elif LA9 == FALSE or LA9 == TRUE:
                    alt9 = 4
                elif LA9 == LBRACKET:
                    alt9 = 5
                elif LA9 == LPAREN:
                    LA9_6 = self.input.LA(2)

                    if (self.synpred15_Miranda()) :
                        alt9 = 6
                    elif (True) :
                        alt9 = 7
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 9, 6, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammars/Miranda.g:131:5: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_basic771)
                    if self._state.backtracking == 0:
                        ID22_tree = self._adaptor.createWithPayload(ID22)
                        self._adaptor.addChild(root_0, ID22_tree)




                elif alt9 == 2:
                    # grammars/Miranda.g:132:5: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT23 = self.match(self.input, INT, self.FOLLOW_INT_in_basic777)
                    if self._state.backtracking == 0:
                        INT23_tree = self._adaptor.createWithPayload(INT23)
                        self._adaptor.addChild(root_0, INT23_tree)




                elif alt9 == 3:
                    # grammars/Miranda.g:133:5: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()


                    FLOAT24 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_basic783)
                    if self._state.backtracking == 0:
                        FLOAT24_tree = self._adaptor.createWithPayload(FLOAT24)
                        self._adaptor.addChild(root_0, FLOAT24_tree)




                elif alt9 == 4:
                    # grammars/Miranda.g:134:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_basic789)
                    boolean25 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean25.tree)



                elif alt9 == 5:
                    # grammars/Miranda.g:135:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_basic795)
                    list26 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list26.tree)



                elif alt9 == 6:
                    # grammars/Miranda.g:136:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_basic801)
                    tuple27 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple27.tree)



                elif alt9 == 7:
                    # grammars/Miranda.g:137:5: LPAREN ! parameter RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN28 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_basic807)

                    self._state.following.append(self.FOLLOW_parameter_in_basic810)
                    parameter29 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter29.tree)


                    RPAREN30 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_basic812)


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
                self.memoize(self.input, 7, basic_StartIndex, success)


            pass
        return retval

    # $ANTLR end "basic"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # grammars/Miranda.g:140:1: expression : expr0 ;
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        expr031 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:140:11: ( expr0 )
                # grammars/Miranda.g:140:13: expr0
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr0_in_expression821)
                expr031 = self.expr0()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr031.tree)




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
                self.memoize(self.input, 8, expression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expression"


    class expr0_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr0_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr0"
    # grammars/Miranda.g:142:1: expr0 : expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? ;
    def expr0(self, ):
        retval = self.expr0_return()
        retval.start = self.input.LT(1)

        expr0_StartIndex = self.input.index()

        root_0 = None

        CONCAT33 = None
        SUBTRACT34 = None
        COLON35 = None
        expr132 = None

        expr036 = None


        CONCAT33_tree = None
        SUBTRACT34_tree = None
        COLON35_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:142:6: ( expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? )
                # grammars/Miranda.g:142:8: expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr1_in_expr0828)
                expr132 = self.expr1()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr132.tree)


                # grammars/Miranda.g:142:14: ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                alt11 = 2
                LA11 = self.input.LA(1)
                if LA11 == CONCAT:
                    LA11_1 = self.input.LA(2)

                    if (self.synpred18_Miranda()) :
                        alt11 = 1
                elif LA11 == SUBTRACT:
                    LA11_2 = self.input.LA(2)

                    if (self.synpred18_Miranda()) :
                        alt11 = 1
                elif LA11 == COLON:
                    LA11_3 = self.input.LA(2)

                    if (self.synpred18_Miranda()) :
                        alt11 = 1
                if alt11 == 1:
                    # grammars/Miranda.g:142:15: ( CONCAT ^| SUBTRACT ^| COLON ^) expr0
                    pass 
                    # grammars/Miranda.g:142:15: ( CONCAT ^| SUBTRACT ^| COLON ^)
                    alt10 = 3
                    LA10 = self.input.LA(1)
                    if LA10 == CONCAT:
                        alt10 = 1
                    elif LA10 == SUBTRACT:
                        alt10 = 2
                    elif LA10 == COLON:
                        alt10 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 10, 0, self.input)

                        raise nvae


                    if alt10 == 1:
                        # grammars/Miranda.g:142:16: CONCAT ^
                        pass 
                        CONCAT33 = self.match(self.input, CONCAT, self.FOLLOW_CONCAT_in_expr0832)
                        if self._state.backtracking == 0:
                            CONCAT33_tree = ConcatNode(CONCAT33) 
                            root_0 = self._adaptor.becomeRoot(CONCAT33_tree, root_0)




                    elif alt10 == 2:
                        # grammars/Miranda.g:142:36: SUBTRACT ^
                        pass 
                        SUBTRACT34 = self.match(self.input, SUBTRACT, self.FOLLOW_SUBTRACT_in_expr0838)
                        if self._state.backtracking == 0:
                            SUBTRACT34_tree = SubtractNode(SUBTRACT34) 
                            root_0 = self._adaptor.becomeRoot(SUBTRACT34_tree, root_0)




                    elif alt10 == 3:
                        # grammars/Miranda.g:142:60: COLON ^
                        pass 
                        COLON35 = self.match(self.input, COLON, self.FOLLOW_COLON_in_expr0844)
                        if self._state.backtracking == 0:
                            COLON35_tree = ColonNode(COLON35) 
                            root_0 = self._adaptor.becomeRoot(COLON35_tree, root_0)






                    self._state.following.append(self.FOLLOW_expr0_in_expr0851)
                    expr036 = self.expr0()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr036.tree)







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
                self.memoize(self.input, 9, expr0_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr0"


    class expr1_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr1_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr1"
    # grammars/Miranda.g:144:1: expr1 : expr2 ( OR ^ expression )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR38 = None
        expr237 = None

        expression39 = None


        OR38_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:144:6: ( expr2 ( OR ^ expression )* )
                # grammars/Miranda.g:144:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1860)
                expr237 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr237.tree)


                # grammars/Miranda.g:144:14: ( OR ^ expression )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == OR) :
                        LA12_2 = self.input.LA(2)

                        if (self.synpred19_Miranda()) :
                            alt12 = 1




                    if alt12 == 1:
                        # grammars/Miranda.g:144:15: OR ^ expression
                        pass 
                        OR38 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1863)
                        if self._state.backtracking == 0:
                            OR38_tree = OrNode(OR38) 
                            root_0 = self._adaptor.becomeRoot(OR38_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr1869)
                        expression39 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression39.tree)



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
                self.memoize(self.input, 10, expr1_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr1"


    class expr2_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr2_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr2"
    # grammars/Miranda.g:146:1: expr2 : expr3 ( AND ^ expression )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND41 = None
        expr340 = None

        expression42 = None


        AND41_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:146:6: ( expr3 ( AND ^ expression )* )
                # grammars/Miranda.g:146:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2878)
                expr340 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr340.tree)


                # grammars/Miranda.g:146:14: ( AND ^ expression )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == AND) :
                        LA13_2 = self.input.LA(2)

                        if (self.synpred20_Miranda()) :
                            alt13 = 1




                    if alt13 == 1:
                        # grammars/Miranda.g:146:15: AND ^ expression
                        pass 
                        AND41 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2881)
                        if self._state.backtracking == 0:
                            AND41_tree = AndNode(AND41) 
                            root_0 = self._adaptor.becomeRoot(AND41_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr2887)
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
                self.memoize(self.input, 11, expr2_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr2"


    class expr3_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr3_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr3"
    # grammars/Miranda.g:148:1: expr3 : expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        set44 = None
        expr443 = None

        expression45 = None


        set44_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:148:6: ( expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* )
                # grammars/Miranda.g:148:8: expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3896)
                expr443 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr443.tree)


                # grammars/Miranda.g:148:14: ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == EQ or (GT <= LA14_0 <= GTE) or (LT <= LA14_0 <= LTE) or LA14_0 == NEQ) :
                        LA14_2 = self.input.LA(2)

                        if (self.synpred26_Miranda()) :
                            alt14 = 1




                    if alt14 == 1:
                        # grammars/Miranda.g:148:15: ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression
                        pass 
                        set44 = self.input.LT(1)

                        set44 = self.input.LT(1)

                        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set44), root_0)

                            self._state.errorRecovery = False


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        self._state.following.append(self.FOLLOW_expression_in_expr3914)
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
                self.memoize(self.input, 12, expr3_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr3"


    class expr4_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr4_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr4"
    # grammars/Miranda.g:150:1: expr4 : expr5 ( ( ADD ^| MIN ^) expression )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD47 = None
        MIN48 = None
        expr546 = None

        expression49 = None


        ADD47_tree = None
        MIN48_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:150:6: ( expr5 ( ( ADD ^| MIN ^) expression )* )
                # grammars/Miranda.g:150:8: expr5 ( ( ADD ^| MIN ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4923)
                expr546 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr546.tree)


                # grammars/Miranda.g:150:14: ( ( ADD ^| MIN ^) expression )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ADD) :
                        LA16_2 = self.input.LA(2)

                        if (self.synpred28_Miranda()) :
                            alt16 = 1


                    elif (LA16_0 == MIN) :
                        LA16_3 = self.input.LA(2)

                        if (self.synpred28_Miranda()) :
                            alt16 = 1




                    if alt16 == 1:
                        # grammars/Miranda.g:150:15: ( ADD ^| MIN ^) expression
                        pass 
                        # grammars/Miranda.g:150:15: ( ADD ^| MIN ^)
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == ADD) :
                            alt15 = 1
                        elif (LA15_0 == MIN) :
                            alt15 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 15, 0, self.input)

                            raise nvae


                        if alt15 == 1:
                            # grammars/Miranda.g:150:16: ADD ^
                            pass 
                            ADD47 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4927)
                            if self._state.backtracking == 0:
                                ADD47_tree = AddNode(ADD47) 
                                root_0 = self._adaptor.becomeRoot(ADD47_tree, root_0)




                        elif alt15 == 2:
                            # grammars/Miranda.g:150:30: MIN ^
                            pass 
                            MIN48 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4933)
                            if self._state.backtracking == 0:
                                MIN48_tree = MinNode(MIN48) 
                                root_0 = self._adaptor.becomeRoot(MIN48_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr4940)
                        expression49 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression49.tree)



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
                self.memoize(self.input, 13, expr4_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr4"


    class expr5_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr5_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr5"
    # grammars/Miranda.g:152:1: expr5 : expr6 ( ( DIV ^| MUL ^) expression )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV51 = None
        MUL52 = None
        expr650 = None

        expression53 = None


        DIV51_tree = None
        MUL52_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:152:6: ( expr6 ( ( DIV ^| MUL ^) expression )* )
                # grammars/Miranda.g:152:8: expr6 ( ( DIV ^| MUL ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr5949)
                expr650 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr650.tree)


                # grammars/Miranda.g:152:14: ( ( DIV ^| MUL ^) expression )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == DIV) :
                        LA18_2 = self.input.LA(2)

                        if (self.synpred30_Miranda()) :
                            alt18 = 1


                    elif (LA18_0 == MUL) :
                        LA18_3 = self.input.LA(2)

                        if (self.synpred30_Miranda()) :
                            alt18 = 1




                    if alt18 == 1:
                        # grammars/Miranda.g:152:15: ( DIV ^| MUL ^) expression
                        pass 
                        # grammars/Miranda.g:152:15: ( DIV ^| MUL ^)
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == DIV) :
                            alt17 = 1
                        elif (LA17_0 == MUL) :
                            alt17 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 17, 0, self.input)

                            raise nvae


                        if alt17 == 1:
                            # grammars/Miranda.g:152:16: DIV ^
                            pass 
                            DIV51 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5953)
                            if self._state.backtracking == 0:
                                DIV51_tree = DivNode(DIV51) 
                                root_0 = self._adaptor.becomeRoot(DIV51_tree, root_0)




                        elif alt17 == 2:
                            # grammars/Miranda.g:152:30: MUL ^
                            pass 
                            MUL52 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5959)
                            if self._state.backtracking == 0:
                                MUL52_tree = MulNode(MUL52) 
                                root_0 = self._adaptor.becomeRoot(MUL52_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr5966)
                        expression53 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression53.tree)



                    else:
                        break #loop18




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
                self.memoize(self.input, 14, expr5_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr5"


    class expr6_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr6_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr6"
    # grammars/Miranda.g:154:1: expr6 : expr7 ( ( IDIV ^| MOD ^) expression )* ;
    def expr6(self, ):
        retval = self.expr6_return()
        retval.start = self.input.LT(1)

        expr6_StartIndex = self.input.index()

        root_0 = None

        IDIV55 = None
        MOD56 = None
        expr754 = None

        expression57 = None


        IDIV55_tree = None
        MOD56_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:154:6: ( expr7 ( ( IDIV ^| MOD ^) expression )* )
                # grammars/Miranda.g:154:8: expr7 ( ( IDIV ^| MOD ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr7_in_expr6975)
                expr754 = self.expr7()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr754.tree)


                # grammars/Miranda.g:154:14: ( ( IDIV ^| MOD ^) expression )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == IDIV) :
                        LA20_2 = self.input.LA(2)

                        if (self.synpred32_Miranda()) :
                            alt20 = 1


                    elif (LA20_0 == MOD) :
                        LA20_3 = self.input.LA(2)

                        if (self.synpred32_Miranda()) :
                            alt20 = 1




                    if alt20 == 1:
                        # grammars/Miranda.g:154:15: ( IDIV ^| MOD ^) expression
                        pass 
                        # grammars/Miranda.g:154:15: ( IDIV ^| MOD ^)
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == IDIV) :
                            alt19 = 1
                        elif (LA19_0 == MOD) :
                            alt19 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 19, 0, self.input)

                            raise nvae


                        if alt19 == 1:
                            # grammars/Miranda.g:154:16: IDIV ^
                            pass 
                            IDIV55 = self.match(self.input, IDIV, self.FOLLOW_IDIV_in_expr6979)
                            if self._state.backtracking == 0:
                                IDIV55_tree = self._adaptor.createWithPayload(IDIV55)
                                root_0 = self._adaptor.becomeRoot(IDIV55_tree, root_0)




                        elif alt19 == 2:
                            # grammars/Miranda.g:154:22: MOD ^
                            pass 
                            MOD56 = self.match(self.input, MOD, self.FOLLOW_MOD_in_expr6982)
                            if self._state.backtracking == 0:
                                MOD56_tree = self._adaptor.createWithPayload(MOD56)
                                root_0 = self._adaptor.becomeRoot(MOD56_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr6986)
                        expression57 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression57.tree)



                    else:
                        break #loop20




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
                self.memoize(self.input, 15, expr6_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr6"


    class expr7_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr7_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr7"
    # grammars/Miranda.g:156:1: expr7 : expr8 ( ( EXP ^) expression )* ;
    def expr7(self, ):
        retval = self.expr7_return()
        retval.start = self.input.LT(1)

        expr7_StartIndex = self.input.index()

        root_0 = None

        EXP59 = None
        expr858 = None

        expression60 = None


        EXP59_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:156:6: ( expr8 ( ( EXP ^) expression )* )
                # grammars/Miranda.g:156:8: expr8 ( ( EXP ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr8_in_expr7995)
                expr858 = self.expr8()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr858.tree)


                # grammars/Miranda.g:156:14: ( ( EXP ^) expression )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == EXP) :
                        LA21_2 = self.input.LA(2)

                        if (self.synpred33_Miranda()) :
                            alt21 = 1




                    if alt21 == 1:
                        # grammars/Miranda.g:156:15: ( EXP ^) expression
                        pass 
                        # grammars/Miranda.g:156:15: ( EXP ^)
                        # grammars/Miranda.g:156:16: EXP ^
                        pass 
                        EXP59 = self.match(self.input, EXP, self.FOLLOW_EXP_in_expr7999)
                        if self._state.backtracking == 0:
                            EXP59_tree = self._adaptor.createWithPayload(EXP59)
                            root_0 = self._adaptor.becomeRoot(EXP59_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr71003)
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
                self.memoize(self.input, 16, expr7_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr7"


    class expr8_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr8_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr8"
    # grammars/Miranda.g:158:1: expr8 : ( aexpr )+ ;
    def expr8(self, ):
        retval = self.expr8_return()
        retval.start = self.input.LT(1)

        expr8_StartIndex = self.input.index()

        root_0 = None

        aexpr61 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:158:6: ( ( aexpr )+ )
                # grammars/Miranda.g:158:8: ( aexpr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:158:8: ( aexpr )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22 = self.input.LA(1)
                    if LA22 == ID:
                        LA22_19 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == INT:
                        LA22_20 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == FLOAT:
                        LA22_21 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == CHAR:
                        LA22_22 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == STRING:
                        LA22_23 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == NOT:
                        LA22_24 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == FALSE or LA22 == TRUE:
                        LA22_25 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == LPAREN:
                        LA22_26 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1


                    elif LA22 == LBRACKET:
                        LA22_27 = self.input.LA(2)

                        if (self.synpred34_Miranda()) :
                            alt22 = 1



                    if alt22 == 1:
                        # grammars/Miranda.g:158:8: aexpr
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr81012)
                        aexpr61 = self.aexpr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, aexpr61.tree)



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1


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
                self.memoize(self.input, 17, expr8_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr8"


    class aexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.aexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "aexpr"
    # grammars/Miranda.g:164:1: aexpr : ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !);
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID62 = None
        INT63 = None
        FLOAT64 = None
        CHAR65 = None
        STRING66 = None
        NOT67 = None
        LPAREN73 = None
        RPAREN75 = None
        expression68 = None

        boolean69 = None

        section70 = None

        tuple71 = None

        list72 = None

        expression74 = None


        ID62_tree = None
        INT63_tree = None
        FLOAT64_tree = None
        CHAR65_tree = None
        STRING66_tree = None
        NOT67_tree = None
        LPAREN73_tree = None
        RPAREN75_tree = None
        stream_CHAR = RewriteRuleTokenStream(self._adaptor, "token CHAR")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:165:3: ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !)
                alt23 = 11
                LA23 = self.input.LA(1)
                if LA23 == ID:
                    alt23 = 1
                elif LA23 == INT:
                    alt23 = 2
                elif LA23 == FLOAT:
                    alt23 = 3
                elif LA23 == CHAR:
                    alt23 = 4
                elif LA23 == STRING:
                    alt23 = 5
                elif LA23 == NOT:
                    alt23 = 6
                elif LA23 == FALSE or LA23 == TRUE:
                    alt23 = 7
                elif LA23 == LPAREN:
                    LA23_8 = self.input.LA(2)

                    if (self.synpred42_Miranda()) :
                        alt23 = 8
                    elif (self.synpred43_Miranda()) :
                        alt23 = 9
                    elif (True) :
                        alt23 = 11
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 23, 8, self.input)

                        raise nvae


                elif LA23 == LBRACKET:
                    alt23 = 10
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammars/Miranda.g:165:5: ID
                    pass 
                    ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr1025) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID62)


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
                        # 166:5: -> ^( ID )
                        # grammars/Miranda.g:166:8: ^( ID )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IdentifierNode(stream_ID.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt23 == 2:
                    # grammars/Miranda.g:167:5: INT
                    pass 
                    INT63 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr1044) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT63)


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
                        # 168:5: -> ^( INT )
                        # grammars/Miranda.g:168:8: ^( INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IntNode(stream_INT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt23 == 3:
                    # grammars/Miranda.g:169:5: FLOAT
                    pass 
                    FLOAT64 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr1063) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT64)


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
                        # 170:5: -> ^( FLOAT )
                        # grammars/Miranda.g:170:8: ^( FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        FloatNode(stream_FLOAT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt23 == 4:
                    # grammars/Miranda.g:171:5: CHAR
                    pass 
                    CHAR65 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_aexpr1082) 
                    if self._state.backtracking == 0:
                        stream_CHAR.add(CHAR65)


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
                        # 172:5: -> ^( CHAR )
                        # grammars/Miranda.g:172:8: ^( CHAR )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        CharNode(stream_CHAR.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt23 == 5:
                    # grammars/Miranda.g:173:5: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING66 = self.match(self.input, STRING, self.FOLLOW_STRING_in_aexpr1101)
                    if self._state.backtracking == 0:
                        STRING66_tree = self._adaptor.createWithPayload(STRING66)
                        self._adaptor.addChild(root_0, STRING66_tree)




                elif alt23 == 6:
                    # grammars/Miranda.g:174:5: NOT expression
                    pass 
                    root_0 = self._adaptor.nil()


                    NOT67 = self.match(self.input, NOT, self.FOLLOW_NOT_in_aexpr1107)
                    if self._state.backtracking == 0:
                        NOT67_tree = self._adaptor.createWithPayload(NOT67)
                        self._adaptor.addChild(root_0, NOT67_tree)



                    self._state.following.append(self.FOLLOW_expression_in_aexpr1109)
                    expression68 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression68.tree)



                elif alt23 == 7:
                    # grammars/Miranda.g:175:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_aexpr1115)
                    boolean69 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean69.tree)



                elif alt23 == 8:
                    # grammars/Miranda.g:176:5: section
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_section_in_aexpr1121)
                    section70 = self.section()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, section70.tree)



                elif alt23 == 9:
                    # grammars/Miranda.g:177:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_aexpr1127)
                    tuple71 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple71.tree)



                elif alt23 == 10:
                    # grammars/Miranda.g:178:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_aexpr1133)
                    list72 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list72.tree)



                elif alt23 == 11:
                    # grammars/Miranda.g:179:5: LPAREN ! expression RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN73 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr1139)

                    self._state.following.append(self.FOLLOW_expression_in_aexpr1142)
                    expression74 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression74.tree)


                    RPAREN75 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr1144)


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
                self.memoize(self.input, 18, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class tuple_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.tuple_return, self).__init__()

            self.tree = None





    # $ANTLR start "tuple"
    # grammars/Miranda.g:182:1: tuple : LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) ;
    def tuple(self, ):
        retval = self.tuple_return()
        retval.start = self.input.LT(1)

        tuple_StartIndex = self.input.index()

        root_0 = None

        LPAREN76 = None
        COMMA78 = None
        RPAREN80 = None
        expression77 = None

        expression79 = None


        LPAREN76_tree = None
        COMMA78_tree = None
        RPAREN80_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:182:6: ( LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) )
                # grammars/Miranda.g:182:8: LPAREN expression ( COMMA expression )+ RPAREN
                pass 
                LPAREN76 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_tuple1153) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN76)


                self._state.following.append(self.FOLLOW_expression_in_tuple1155)
                expression77 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression77.tree)


                # grammars/Miranda.g:182:26: ( COMMA expression )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammars/Miranda.g:182:27: COMMA expression
                        pass 
                        COMMA78 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_tuple1158) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA78)


                        self._state.following.append(self.FOLLOW_expression_in_tuple1160)
                        expression79 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression79.tree)



                    else:
                        if cnt24 >= 1:
                            break #loop24

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1


                RPAREN80 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_tuple1164) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN80)


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
                    # 183:8: -> ^( TUPLE ( expression )* )
                    # grammars/Miranda.g:183:11: ^( TUPLE ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TUPLE, "TUPLE")
                    , root_1)

                    # grammars/Miranda.g:183:19: ( expression )*
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
                self.memoize(self.input, 19, tuple_StartIndex, success)


            pass
        return retval

    # $ANTLR end "tuple"


    class list_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.list_return, self).__init__()

            self.tree = None





    # $ANTLR start "list"
    # grammars/Miranda.g:186:1: list : LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) ;
    def list(self, ):
        retval = self.list_return()
        retval.start = self.input.LT(1)

        list_StartIndex = self.input.index()

        root_0 = None

        LBRACKET81 = None
        COMMA83 = None
        RBRACKET85 = None
        expression82 = None

        expression84 = None


        LBRACKET81_tree = None
        COMMA83_tree = None
        RBRACKET85_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:186:5: ( LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) )
                # grammars/Miranda.g:186:7: LBRACKET ( expression )? ( COMMA expression )* RBRACKET
                pass 
                LBRACKET81 = self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_list1188) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET81)


                # grammars/Miranda.g:186:16: ( expression )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == CHAR or (FALSE <= LA25_0 <= FLOAT) or LA25_0 == ID or LA25_0 == INT or LA25_0 == LBRACKET or LA25_0 == LPAREN or LA25_0 == NOT or LA25_0 == STRING or LA25_0 == TRUE) :
                    alt25 = 1
                if alt25 == 1:
                    # grammars/Miranda.g:186:16: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_list1190)
                    expression82 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression82.tree)





                # grammars/Miranda.g:186:28: ( COMMA expression )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == COMMA) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammars/Miranda.g:186:29: COMMA expression
                        pass 
                        COMMA83 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_list1194) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA83)


                        self._state.following.append(self.FOLLOW_expression_in_list1196)
                        expression84 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression84.tree)



                    else:
                        break #loop26


                RBRACKET85 = self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_list1200) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET85)


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
                    # 187:7: -> ^( LIST ( expression )* )
                    # grammars/Miranda.g:187:10: ^( LIST ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # grammars/Miranda.g:187:17: ( expression )*
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
                self.memoize(self.input, 20, list_StartIndex, success)


            pass
        return retval

    # $ANTLR end "list"


    class section_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.section_return, self).__init__()

            self.tree = None





    # $ANTLR start "section"
    # grammars/Miranda.g:190:1: section : ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) );
    def section(self, ):
        retval = self.section_return()
        retval.start = self.input.LT(1)

        section_StartIndex = self.input.index()

        root_0 = None

        LPAREN86 = None
        RPAREN88 = None
        LPAREN89 = None
        RPAREN92 = None
        LPAREN93 = None
        RPAREN96 = None
        operator87 = None

        operator90 = None

        expression91 = None

        expression94 = None

        operator95 = None


        LPAREN86_tree = None
        RPAREN88_tree = None
        LPAREN89_tree = None
        RPAREN92_tree = None
        LPAREN93_tree = None
        RPAREN96_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_operator = RewriteRuleSubtreeStream(self._adaptor, "rule operator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:191:3: ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) )
                alt27 = 3
                LA27_0 = self.input.LA(1)

                if (LA27_0 == LPAREN) :
                    LA27_1 = self.input.LA(2)

                    if (LA27_1 == ADD or LA27_1 == AND or LA27_1 == CONCAT or LA27_1 == DIV or (EQ <= LA27_1 <= EXP) or (GT <= LA27_1 <= GTE) or LA27_1 == IDIV or (LT <= LA27_1 <= NEQ) or LA27_1 == OR or LA27_1 == SUBTRACT) :
                        LA27_2 = self.input.LA(3)

                        if (LA27_2 == RPAREN) :
                            alt27 = 1
                        elif (LA27_2 == CHAR or (FALSE <= LA27_2 <= FLOAT) or LA27_2 == ID or LA27_2 == INT or LA27_2 == LBRACKET or LA27_2 == LPAREN or LA27_2 == NOT or LA27_2 == STRING or LA27_2 == TRUE) :
                            alt27 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 27, 2, self.input)

                            raise nvae


                    elif (LA27_1 == CHAR or (FALSE <= LA27_1 <= FLOAT) or LA27_1 == ID or LA27_1 == INT or LA27_1 == LBRACKET or LA27_1 == LPAREN or LA27_1 == NOT or LA27_1 == STRING or LA27_1 == TRUE) :
                        alt27 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 27, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammars/Miranda.g:191:5: LPAREN operator RPAREN
                    pass 
                    LPAREN86 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1226) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN86)


                    self._state.following.append(self.FOLLOW_operator_in_section1228)
                    operator87 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator87.tree)


                    RPAREN88 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1230) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN88)


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
                        # 192:4: -> ^( SECTION operator )
                        # grammars/Miranda.g:192:7: ^( SECTION operator )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt27 == 2:
                    # grammars/Miranda.g:193:5: LPAREN operator expression RPAREN
                    pass 
                    LPAREN89 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1247) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN89)


                    self._state.following.append(self.FOLLOW_operator_in_section1249)
                    operator90 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator90.tree)


                    self._state.following.append(self.FOLLOW_expression_in_section1251)
                    expression91 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression91.tree)


                    RPAREN92 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1253) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN92)


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
                        # 194:4: -> ^( SECTION operator expression )
                        # grammars/Miranda.g:194:7: ^( SECTION operator expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt27 == 3:
                    # grammars/Miranda.g:195:5: LPAREN expression operator RPAREN
                    pass 
                    LPAREN93 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1272) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN93)


                    self._state.following.append(self.FOLLOW_expression_in_section1274)
                    expression94 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression94.tree)


                    self._state.following.append(self.FOLLOW_operator_in_section1276)
                    operator95 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator95.tree)


                    RPAREN96 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1278) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN96)


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
                        # 196:4: -> ^( SECTION expression operator )
                        # grammars/Miranda.g:196:7: ^( SECTION expression operator )
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
                self.memoize(self.input, 21, section_StartIndex, success)


            pass
        return retval

    # $ANTLR end "section"


    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.operator_return, self).__init__()

            self.tree = None





    # $ANTLR start "operator"
    # grammars/Miranda.g:198:10: fragment operator : ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP );
    def operator(self, ):
        retval = self.operator_return()
        retval.start = self.input.LT(1)

        operator_StartIndex = self.input.index()

        root_0 = None

        set97 = None

        set97_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:198:18: ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set97 = self.input.LT(1)

                if self.input.LA(1) == ADD or self.input.LA(1) == AND or self.input.LA(1) == CONCAT or self.input.LA(1) == DIV or (EQ <= self.input.LA(1) <= EXP) or (GT <= self.input.LA(1) <= GTE) or self.input.LA(1) == IDIV or (LT <= self.input.LA(1) <= NEQ) or self.input.LA(1) == OR or self.input.LA(1) == SUBTRACT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set97))

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
                self.memoize(self.input, 22, operator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "operator"


    class boolean_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.boolean_return, self).__init__()

            self.tree = None





    # $ANTLR start "boolean"
    # grammars/Miranda.g:200:1: boolean : ( TRUE | FALSE );
    def boolean(self, ):
        retval = self.boolean_return()
        retval.start = self.input.LT(1)

        boolean_StartIndex = self.input.index()

        root_0 = None

        set98 = None

        set98_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:200:8: ( TRUE | FALSE )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set98 = self.input.LT(1)

                if self.input.LA(1) == FALSE or self.input.LA(1) == TRUE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set98))

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
                self.memoize(self.input, 23, boolean_StartIndex, success)


            pass
        return retval

    # $ANTLR end "boolean"

    # $ANTLR start "synpred1_Miranda"
    def synpred1_Miranda_fragment(self, ):
        # grammars/Miranda.g:107:4: ( definition DEDENT )
        # grammars/Miranda.g:107:4: definition DEDENT
        pass 
        self._state.following.append(self.FOLLOW_definition_in_synpred1_Miranda600)
        self.definition()

        self._state.following.pop()

        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred1_Miranda602)



    # $ANTLR end "synpred1_Miranda"



    # $ANTLR start "synpred3_Miranda"
    def synpred3_Miranda_fragment(self, ):
        # grammars/Miranda.g:113:19: ( body )
        # grammars/Miranda.g:113:19: body
        pass 
        self._state.following.append(self.FOLLOW_body_in_synpred3_Miranda643)
        self.body()

        self._state.following.pop()



    # $ANTLR end "synpred3_Miranda"



    # $ANTLR start "synpred7_Miranda"
    def synpred7_Miranda_fragment(self, ):
        # grammars/Miranda.g:124:26: ( DEDENT definition )
        # grammars/Miranda.g:124:26: DEDENT definition
        pass 
        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred7_Miranda730)

        self._state.following.append(self.FOLLOW_definition_in_synpred7_Miranda733)
        self.definition()

        self._state.following.pop()



    # $ANTLR end "synpred7_Miranda"



    # $ANTLR start "synpred15_Miranda"
    def synpred15_Miranda_fragment(self, ):
        # grammars/Miranda.g:136:5: ( tuple )
        # grammars/Miranda.g:136:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred15_Miranda801)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred15_Miranda"



    # $ANTLR start "synpred18_Miranda"
    def synpred18_Miranda_fragment(self, ):
        # grammars/Miranda.g:142:15: ( ( CONCAT | SUBTRACT | COLON ) expr0 )
        # grammars/Miranda.g:142:15: ( CONCAT | SUBTRACT | COLON ) expr0
        pass 
        if self.input.LA(1) == COLON or self.input.LA(1) == CONCAT or self.input.LA(1) == SUBTRACT:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr0_in_synpred18_Miranda851)
        self.expr0()

        self._state.following.pop()



    # $ANTLR end "synpred18_Miranda"



    # $ANTLR start "synpred19_Miranda"
    def synpred19_Miranda_fragment(self, ):
        # grammars/Miranda.g:144:15: ( OR expression )
        # grammars/Miranda.g:144:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred19_Miranda863)

        self._state.following.append(self.FOLLOW_expression_in_synpred19_Miranda869)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred19_Miranda"



    # $ANTLR start "synpred20_Miranda"
    def synpred20_Miranda_fragment(self, ):
        # grammars/Miranda.g:146:15: ( AND expression )
        # grammars/Miranda.g:146:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred20_Miranda881)

        self._state.following.append(self.FOLLOW_expression_in_synpred20_Miranda887)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred20_Miranda"



    # $ANTLR start "synpred26_Miranda"
    def synpred26_Miranda_fragment(self, ):
        # grammars/Miranda.g:148:15: ( ( LT | LTE | EQ | NEQ | GTE | GT ) expression )
        # grammars/Miranda.g:148:15: ( LT | LTE | EQ | NEQ | GTE | GT ) expression
        pass 
        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred26_Miranda914)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred26_Miranda"



    # $ANTLR start "synpred28_Miranda"
    def synpred28_Miranda_fragment(self, ):
        # grammars/Miranda.g:150:15: ( ( ADD | MIN ) expression )
        # grammars/Miranda.g:150:15: ( ADD | MIN ) expression
        pass 
        if self.input.LA(1) == ADD or self.input.LA(1) == MIN:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred28_Miranda940)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred28_Miranda"



    # $ANTLR start "synpred30_Miranda"
    def synpred30_Miranda_fragment(self, ):
        # grammars/Miranda.g:152:15: ( ( DIV | MUL ) expression )
        # grammars/Miranda.g:152:15: ( DIV | MUL ) expression
        pass 
        if self.input.LA(1) == DIV or self.input.LA(1) == MUL:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred30_Miranda966)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred30_Miranda"



    # $ANTLR start "synpred32_Miranda"
    def synpred32_Miranda_fragment(self, ):
        # grammars/Miranda.g:154:15: ( ( IDIV | MOD ) expression )
        # grammars/Miranda.g:154:15: ( IDIV | MOD ) expression
        pass 
        if self.input.LA(1) == IDIV or self.input.LA(1) == MOD:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred32_Miranda986)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred32_Miranda"



    # $ANTLR start "synpred33_Miranda"
    def synpred33_Miranda_fragment(self, ):
        # grammars/Miranda.g:156:15: ( ( EXP ) expression )
        # grammars/Miranda.g:156:15: ( EXP ) expression
        pass 
        # grammars/Miranda.g:156:15: ( EXP )
        # grammars/Miranda.g:156:16: EXP
        pass 
        self.match(self.input, EXP, self.FOLLOW_EXP_in_synpred33_Miranda999)




        self._state.following.append(self.FOLLOW_expression_in_synpred33_Miranda1003)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred33_Miranda"



    # $ANTLR start "synpred34_Miranda"
    def synpred34_Miranda_fragment(self, ):
        # grammars/Miranda.g:158:8: ( aexpr )
        # grammars/Miranda.g:158:8: aexpr
        pass 
        self._state.following.append(self.FOLLOW_aexpr_in_synpred34_Miranda1012)
        self.aexpr()

        self._state.following.pop()



    # $ANTLR end "synpred34_Miranda"



    # $ANTLR start "synpred42_Miranda"
    def synpred42_Miranda_fragment(self, ):
        # grammars/Miranda.g:176:5: ( section )
        # grammars/Miranda.g:176:5: section
        pass 
        self._state.following.append(self.FOLLOW_section_in_synpred42_Miranda1121)
        self.section()

        self._state.following.pop()



    # $ANTLR end "synpred42_Miranda"



    # $ANTLR start "synpred43_Miranda"
    def synpred43_Miranda_fragment(self, ):
        # grammars/Miranda.g:177:5: ( tuple )
        # grammars/Miranda.g:177:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred43_Miranda1127)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred43_Miranda"




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

    def synpred7_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred7_Miranda_fragment()
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

    def synpred18_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred18_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred26_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred26_Miranda_fragment()
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

    def synpred42_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred42_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred32_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred32_Miranda_fragment()
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

    def synpred28_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred28_Miranda_fragment()
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

    def synpred30_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred30_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_Miranda_fragment()
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



 

    FOLLOW_definition_in_program600 = frozenset([13])
    FOLLOW_DEDENT_in_program602 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_program606 = frozenset([])
    FOLLOW_EOF_in_program608 = frozenset([1])
    FOLLOW_ID_in_definition638 = frozenset([1, 20, 21, 24, 26, 27, 28, 30, 48])
    FOLLOW_parameter_in_definition640 = frozenset([1, 20, 21, 24, 26, 27, 28, 30, 48])
    FOLLOW_body_in_definition643 = frozenset([1, 27])
    FOLLOW_IS_in_body676 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_body678 = frozenset([1, 10, 51])
    FOLLOW_guard_in_body680 = frozenset([1, 51])
    FOLLOW_where_in_body683 = frozenset([1])
    FOLLOW_COMMA_in_guard712 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 40, 46, 48])
    FOLLOW_expression_in_guard715 = frozenset([1])
    FOLLOW_OTHERWISE_in_guard717 = frozenset([1])
    FOLLOW_WHERE_in_where725 = frozenset([24])
    FOLLOW_definition_in_where727 = frozenset([1, 13])
    FOLLOW_DEDENT_in_where730 = frozenset([24])
    FOLLOW_definition_in_where733 = frozenset([1, 13])
    FOLLOW_basic_in_parameter746 = frozenset([1, 4, 9])
    FOLLOW_set_in_parameter749 = frozenset([20, 21, 24, 26, 28, 30, 48])
    FOLLOW_parameter_in_parameter756 = frozenset([1])
    FOLLOW_ID_in_basic771 = frozenset([1])
    FOLLOW_INT_in_basic777 = frozenset([1])
    FOLLOW_FLOAT_in_basic783 = frozenset([1])
    FOLLOW_boolean_in_basic789 = frozenset([1])
    FOLLOW_list_in_basic795 = frozenset([1])
    FOLLOW_tuple_in_basic801 = frozenset([1])
    FOLLOW_LPAREN_in_basic807 = frozenset([20, 21, 24, 26, 28, 30, 48])
    FOLLOW_parameter_in_basic810 = frozenset([43])
    FOLLOW_RPAREN_in_basic812 = frozenset([1])
    FOLLOW_expr0_in_expression821 = frozenset([1])
    FOLLOW_expr1_in_expr0828 = frozenset([1, 9, 12, 47])
    FOLLOW_CONCAT_in_expr0832 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_SUBTRACT_in_expr0838 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_COLON_in_expr0844 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr0_in_expr0851 = frozenset([1])
    FOLLOW_expr2_in_expr1860 = frozenset([1, 39])
    FOLLOW_OR_in_expr1863 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr1869 = frozenset([1, 39])
    FOLLOW_expr3_in_expr2878 = frozenset([1, 6])
    FOLLOW_AND_in_expr2881 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr2887 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3896 = frozenset([1, 18, 22, 23, 31, 32, 36])
    FOLLOW_set_in_expr3899 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr3914 = frozenset([1, 18, 22, 23, 31, 32, 36])
    FOLLOW_expr5_in_expr4923 = frozenset([1, 4, 33])
    FOLLOW_ADD_in_expr4927 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_MIN_in_expr4933 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr4940 = frozenset([1, 4, 33])
    FOLLOW_expr6_in_expr5949 = frozenset([1, 15, 35])
    FOLLOW_DIV_in_expr5953 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_MUL_in_expr5959 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr5966 = frozenset([1, 15, 35])
    FOLLOW_expr7_in_expr6975 = frozenset([1, 25, 34])
    FOLLOW_IDIV_in_expr6979 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_MOD_in_expr6982 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr6986 = frozenset([1, 25, 34])
    FOLLOW_expr8_in_expr7995 = frozenset([1, 19])
    FOLLOW_EXP_in_expr7999 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr71003 = frozenset([1, 19])
    FOLLOW_aexpr_in_expr81012 = frozenset([1, 8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_ID_in_aexpr1025 = frozenset([1])
    FOLLOW_INT_in_aexpr1044 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr1063 = frozenset([1])
    FOLLOW_CHAR_in_aexpr1082 = frozenset([1])
    FOLLOW_STRING_in_aexpr1101 = frozenset([1])
    FOLLOW_NOT_in_aexpr1107 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_aexpr1109 = frozenset([1])
    FOLLOW_boolean_in_aexpr1115 = frozenset([1])
    FOLLOW_section_in_aexpr1121 = frozenset([1])
    FOLLOW_tuple_in_aexpr1127 = frozenset([1])
    FOLLOW_list_in_aexpr1133 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr1139 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_aexpr1142 = frozenset([43])
    FOLLOW_RPAREN_in_aexpr1144 = frozenset([1])
    FOLLOW_LPAREN_in_tuple1153 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_tuple1155 = frozenset([10])
    FOLLOW_COMMA_in_tuple1158 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_tuple1160 = frozenset([10, 43])
    FOLLOW_RPAREN_in_tuple1164 = frozenset([1])
    FOLLOW_LBRACKET_in_list1188 = frozenset([8, 10, 20, 21, 24, 26, 28, 30, 37, 42, 46, 48])
    FOLLOW_expression_in_list1190 = frozenset([10, 42])
    FOLLOW_COMMA_in_list1194 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_list1196 = frozenset([10, 42])
    FOLLOW_RBRACKET_in_list1200 = frozenset([1])
    FOLLOW_LPAREN_in_section1226 = frozenset([4, 6, 12, 15, 18, 19, 22, 23, 25, 31, 32, 33, 34, 35, 36, 39, 47])
    FOLLOW_operator_in_section1228 = frozenset([43])
    FOLLOW_RPAREN_in_section1230 = frozenset([1])
    FOLLOW_LPAREN_in_section1247 = frozenset([4, 6, 12, 15, 18, 19, 22, 23, 25, 31, 32, 33, 34, 35, 36, 39, 47])
    FOLLOW_operator_in_section1249 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_section1251 = frozenset([43])
    FOLLOW_RPAREN_in_section1253 = frozenset([1])
    FOLLOW_LPAREN_in_section1272 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_section1274 = frozenset([4, 6, 12, 15, 18, 19, 22, 23, 25, 31, 32, 33, 34, 35, 36, 39, 47])
    FOLLOW_operator_in_section1276 = frozenset([43])
    FOLLOW_RPAREN_in_section1278 = frozenset([1])
    FOLLOW_definition_in_synpred1_Miranda600 = frozenset([13])
    FOLLOW_DEDENT_in_synpred1_Miranda602 = frozenset([1])
    FOLLOW_body_in_synpred3_Miranda643 = frozenset([1])
    FOLLOW_DEDENT_in_synpred7_Miranda730 = frozenset([24])
    FOLLOW_definition_in_synpred7_Miranda733 = frozenset([1])
    FOLLOW_tuple_in_synpred15_Miranda801 = frozenset([1])
    FOLLOW_set_in_synpred18_Miranda831 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr0_in_synpred18_Miranda851 = frozenset([1])
    FOLLOW_OR_in_synpred19_Miranda863 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred19_Miranda869 = frozenset([1])
    FOLLOW_AND_in_synpred20_Miranda881 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred20_Miranda887 = frozenset([1])
    FOLLOW_set_in_synpred26_Miranda899 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred26_Miranda914 = frozenset([1])
    FOLLOW_set_in_synpred28_Miranda926 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred28_Miranda940 = frozenset([1])
    FOLLOW_set_in_synpred30_Miranda952 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred30_Miranda966 = frozenset([1])
    FOLLOW_set_in_synpred32_Miranda978 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred32_Miranda986 = frozenset([1])
    FOLLOW_EXP_in_synpred33_Miranda999 = frozenset([8, 20, 21, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred33_Miranda1003 = frozenset([1])
    FOLLOW_aexpr_in_synpred34_Miranda1012 = frozenset([1])
    FOLLOW_section_in_synpred42_Miranda1121 = frozenset([1])
    FOLLOW_tuple_in_synpred43_Miranda1127 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MirandaLexer", MirandaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
