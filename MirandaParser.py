# $ANTLR 3.4 grammars/Miranda.g 2011-12-25 23:51:09

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *


        
from ast import mk_ap_chain, IntNode, FloatNode, IdentifierNode, CharNode, AddNode, MinNode, MulNode, DivNode
from miranda_ast import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ADD=4
ALPHANUMERIC=5
AND=6
CHAR=7
COLON=8
COMMA=9
COMMENT=10
CONCAT=11
DEDENT=12
DEFINITION=13
DIV=14
DOT=15
DOUBLE_QUOTE=16
EQ=17
EXP=18
FALSE=19
FLOAT=20
GT=21
GTE=22
GUARD=23
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
WHERE=50
WHITESPACE=51

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ADD", "ALPHANUMERIC", "AND", "CHAR", "COLON", "COMMA", "COMMENT", "CONCAT", 
    "DEDENT", "DEFINITION", "DIV", "DOT", "DOUBLE_QUOTE", "EQ", "EXP", "FALSE", 
    "FLOAT", "GT", "GTE", "GUARD", "ID", "IDIV", "INT", "IS", "LBRACKET", 
    "LIST", "LPAREN", "LT", "LTE", "MIN", "MOD", "MUL", "NEQ", "NOT", "NUMERIC", 
    "OR", "OTHERWISE", "PROGRAM", "RBRACKET", "RPAREN", "SECTION", "SINGLE_QUOTE", 
    "STRING", "SUBTRACT", "TRUE", "TUPLE", "WHERE", "WHITESPACE"
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
    # grammars/Miranda.g:105:1: program : ( definition DEDENT )* expression EOF -> ^( PROGRAM ( definition )* expression ) ;
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


                # grammars/Miranda.g:105:8: ( ( definition DEDENT )* expression EOF -> ^( PROGRAM ( definition )* expression ) )
                # grammars/Miranda.g:106:3: ( definition DEDENT )* expression EOF
                pass 
                # grammars/Miranda.g:106:3: ( definition DEDENT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        LA1_1 = self.input.LA(2)

                        if (self.synpred1_Miranda()) :
                            alt1 = 1




                    if alt1 == 1:
                        # grammars/Miranda.g:106:4: definition DEDENT
                        pass 
                        self._state.following.append(self.FOLLOW_definition_in_program589)
                        definition1 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_definition.add(definition1.tree)


                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_program591) 
                        if self._state.backtracking == 0:
                            stream_DEDENT.add(DEDENT2)



                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_expression_in_program595)
                expression3 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression3.tree)


                EOF4 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program597) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)


                # AST Rewrite
                # elements: expression, definition
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
                    # 107:3: -> ^( PROGRAM ( definition )* expression )
                    # grammars/Miranda.g:107:6: ^( PROGRAM ( definition )* expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    ProgramNode(PROGRAM)
                    , root_1)

                    # grammars/Miranda.g:107:29: ( definition )*
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
    # grammars/Miranda.g:110:1: definition : ID ( parameter )* IS expression ( guard )? -> ^( DEFINITION ID ( parameter )* expression ( guard )? ) ;
    def definition(self, ):
        retval = self.definition_return()
        retval.start = self.input.LT(1)

        definition_StartIndex = self.input.index()

        root_0 = None

        ID5 = None
        IS7 = None
        parameter6 = None

        expression8 = None

        guard9 = None


        ID5_tree = None
        IS7_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_IS = RewriteRuleTokenStream(self._adaptor, "token IS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        stream_guard = RewriteRuleSubtreeStream(self._adaptor, "rule guard")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:110:11: ( ID ( parameter )* IS expression ( guard )? -> ^( DEFINITION ID ( parameter )* expression ( guard )? ) )
                # grammars/Miranda.g:111:3: ID ( parameter )* IS expression ( guard )?
                pass 
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_definition624) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID5)


                # grammars/Miranda.g:111:6: ( parameter )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((FALSE <= LA2_0 <= FLOAT) or LA2_0 == ID or LA2_0 == INT or LA2_0 == LBRACKET or LA2_0 == LPAREN or LA2_0 == TRUE) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammars/Miranda.g:111:6: parameter
                        pass 
                        self._state.following.append(self.FOLLOW_parameter_in_definition626)
                        parameter6 = self.parameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameter.add(parameter6.tree)



                    else:
                        break #loop2


                IS7 = self.match(self.input, IS, self.FOLLOW_IS_in_definition629) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS7)


                self._state.following.append(self.FOLLOW_expression_in_definition631)
                expression8 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression8.tree)


                # grammars/Miranda.g:111:31: ( guard )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == COMMA) :
                    alt3 = 1
                if alt3 == 1:
                    # grammars/Miranda.g:111:31: guard
                    pass 
                    self._state.following.append(self.FOLLOW_guard_in_definition633)
                    guard9 = self.guard()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_guard.add(guard9.tree)





                # AST Rewrite
                # elements: parameter, ID, guard, expression
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
                    # 112:3: -> ^( DEFINITION ID ( parameter )* expression ( guard )? )
                    # grammars/Miranda.g:112:6: ^( DEFINITION ID ( parameter )* expression ( guard )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    MirandaDefinitionNode(DEFINITION)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammars/Miranda.g:112:45: ( parameter )*
                    while stream_parameter.hasNext():
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())


                    stream_parameter.reset();

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    # grammars/Miranda.g:112:67: ( guard )?
                    if stream_guard.hasNext():
                        self._adaptor.addChild(root_1, stream_guard.nextTree())


                    stream_guard.reset();

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


    class guard_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.guard_return, self).__init__()

            self.tree = None





    # $ANTLR start "guard"
    # grammars/Miranda.g:115:1: guard : COMMA ( expression | OTHERWISE ) ;
    def guard(self, ):
        retval = self.guard_return()
        retval.start = self.input.LT(1)

        guard_StartIndex = self.input.index()

        root_0 = None

        COMMA10 = None
        OTHERWISE12 = None
        expression11 = None


        COMMA10_tree = None
        OTHERWISE12_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:115:6: ( COMMA ( expression | OTHERWISE ) )
                # grammars/Miranda.g:115:8: COMMA ( expression | OTHERWISE )
                pass 
                root_0 = self._adaptor.nil()


                COMMA10 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_guard664)
                if self._state.backtracking == 0:
                    COMMA10_tree = self._adaptor.createWithPayload(COMMA10)
                    self._adaptor.addChild(root_0, COMMA10_tree)



                # grammars/Miranda.g:115:14: ( expression | OTHERWISE )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == CHAR or (FALSE <= LA4_0 <= FLOAT) or LA4_0 == ID or LA4_0 == INT or LA4_0 == LBRACKET or LA4_0 == LPAREN or LA4_0 == NOT or LA4_0 == STRING or LA4_0 == TRUE) :
                    alt4 = 1
                elif (LA4_0 == OTHERWISE) :
                    alt4 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # grammars/Miranda.g:115:15: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_guard667)
                    expression11 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression11.tree)



                elif alt4 == 2:
                    # grammars/Miranda.g:115:26: OTHERWISE
                    pass 
                    OTHERWISE12 = self.match(self.input, OTHERWISE, self.FOLLOW_OTHERWISE_in_guard669)
                    if self._state.backtracking == 0:
                        OTHERWISE12_tree = self._adaptor.createWithPayload(OTHERWISE12)
                        self._adaptor.addChild(root_0, OTHERWISE12_tree)








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
                self.memoize(self.input, 3, guard_StartIndex, success)


            pass
        return retval

    # $ANTLR end "guard"


    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.parameter_return, self).__init__()

            self.tree = None





    # $ANTLR start "parameter"
    # grammars/Miranda.g:117:1: parameter : basic ( ( COLON | ADD ) ^ parameter )? ;
    def parameter(self, ):
        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        parameter_StartIndex = self.input.index()

        root_0 = None

        set14 = None
        basic13 = None

        parameter15 = None


        set14_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:118:3: ( basic ( ( COLON | ADD ) ^ parameter )? )
                # grammars/Miranda.g:118:5: basic ( ( COLON | ADD ) ^ parameter )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_basic_in_parameter680)
                basic13 = self.basic()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, basic13.tree)


                # grammars/Miranda.g:118:11: ( ( COLON | ADD ) ^ parameter )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == ADD or LA5_0 == COLON) :
                    alt5 = 1
                if alt5 == 1:
                    # grammars/Miranda.g:118:12: ( COLON | ADD ) ^ parameter
                    pass 
                    set14 = self.input.LT(1)

                    set14 = self.input.LT(1)

                    if self.input.LA(1) == ADD or self.input.LA(1) == COLON:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set14), root_0)

                        self._state.errorRecovery = False


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        raise mse



                    self._state.following.append(self.FOLLOW_parameter_in_parameter690)
                    parameter15 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter15.tree)







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
                self.memoize(self.input, 4, parameter_StartIndex, success)


            pass
        return retval

    # $ANTLR end "parameter"


    class basic_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.basic_return, self).__init__()

            self.tree = None





    # $ANTLR start "basic"
    # grammars/Miranda.g:121:1: basic : ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! parameter RPAREN !);
    def basic(self, ):
        retval = self.basic_return()
        retval.start = self.input.LT(1)

        basic_StartIndex = self.input.index()

        root_0 = None

        ID16 = None
        INT17 = None
        FLOAT18 = None
        LPAREN22 = None
        RPAREN24 = None
        boolean19 = None

        list20 = None

        tuple21 = None

        parameter23 = None


        ID16_tree = None
        INT17_tree = None
        FLOAT18_tree = None
        LPAREN22_tree = None
        RPAREN24_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:122:3: ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! parameter RPAREN !)
                alt6 = 7
                LA6 = self.input.LA(1)
                if LA6 == ID:
                    alt6 = 1
                elif LA6 == INT:
                    alt6 = 2
                elif LA6 == FLOAT:
                    alt6 = 3
                elif LA6 == FALSE or LA6 == TRUE:
                    alt6 = 4
                elif LA6 == LBRACKET:
                    alt6 = 5
                elif LA6 == LPAREN:
                    LA6_6 = self.input.LA(2)

                    if (self.synpred12_Miranda()) :
                        alt6 = 6
                    elif (True) :
                        alt6 = 7
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 6, 6, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammars/Miranda.g:122:5: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_basic705)
                    if self._state.backtracking == 0:
                        ID16_tree = self._adaptor.createWithPayload(ID16)
                        self._adaptor.addChild(root_0, ID16_tree)




                elif alt6 == 2:
                    # grammars/Miranda.g:123:5: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT17 = self.match(self.input, INT, self.FOLLOW_INT_in_basic711)
                    if self._state.backtracking == 0:
                        INT17_tree = self._adaptor.createWithPayload(INT17)
                        self._adaptor.addChild(root_0, INT17_tree)




                elif alt6 == 3:
                    # grammars/Miranda.g:124:5: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()


                    FLOAT18 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_basic717)
                    if self._state.backtracking == 0:
                        FLOAT18_tree = self._adaptor.createWithPayload(FLOAT18)
                        self._adaptor.addChild(root_0, FLOAT18_tree)




                elif alt6 == 4:
                    # grammars/Miranda.g:125:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_basic723)
                    boolean19 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean19.tree)



                elif alt6 == 5:
                    # grammars/Miranda.g:126:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_basic729)
                    list20 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list20.tree)



                elif alt6 == 6:
                    # grammars/Miranda.g:127:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_basic735)
                    tuple21 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple21.tree)



                elif alt6 == 7:
                    # grammars/Miranda.g:128:5: LPAREN ! parameter RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN22 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_basic741)

                    self._state.following.append(self.FOLLOW_parameter_in_basic744)
                    parameter23 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter23.tree)


                    RPAREN24 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_basic746)


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
                self.memoize(self.input, 5, basic_StartIndex, success)


            pass
        return retval

    # $ANTLR end "basic"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # grammars/Miranda.g:131:1: expression : expr0 ;
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        expr025 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:131:11: ( expr0 )
                # grammars/Miranda.g:131:13: expr0
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr0_in_expression755)
                expr025 = self.expr0()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr025.tree)




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
                self.memoize(self.input, 6, expression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expression"


    class expr0_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr0_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr0"
    # grammars/Miranda.g:133:1: expr0 : expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? ;
    def expr0(self, ):
        retval = self.expr0_return()
        retval.start = self.input.LT(1)

        expr0_StartIndex = self.input.index()

        root_0 = None

        CONCAT27 = None
        SUBTRACT28 = None
        COLON29 = None
        expr126 = None

        expr030 = None


        CONCAT27_tree = None
        SUBTRACT28_tree = None
        COLON29_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:133:6: ( expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? )
                # grammars/Miranda.g:133:8: expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr1_in_expr0762)
                expr126 = self.expr1()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr126.tree)


                # grammars/Miranda.g:133:14: ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                alt8 = 2
                LA8 = self.input.LA(1)
                if LA8 == CONCAT:
                    LA8_1 = self.input.LA(2)

                    if (self.synpred15_Miranda()) :
                        alt8 = 1
                elif LA8 == SUBTRACT:
                    LA8_2 = self.input.LA(2)

                    if (self.synpred15_Miranda()) :
                        alt8 = 1
                elif LA8 == COLON:
                    LA8_3 = self.input.LA(2)

                    if (self.synpred15_Miranda()) :
                        alt8 = 1
                if alt8 == 1:
                    # grammars/Miranda.g:133:15: ( CONCAT ^| SUBTRACT ^| COLON ^) expr0
                    pass 
                    # grammars/Miranda.g:133:15: ( CONCAT ^| SUBTRACT ^| COLON ^)
                    alt7 = 3
                    LA7 = self.input.LA(1)
                    if LA7 == CONCAT:
                        alt7 = 1
                    elif LA7 == SUBTRACT:
                        alt7 = 2
                    elif LA7 == COLON:
                        alt7 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 7, 0, self.input)

                        raise nvae


                    if alt7 == 1:
                        # grammars/Miranda.g:133:16: CONCAT ^
                        pass 
                        CONCAT27 = self.match(self.input, CONCAT, self.FOLLOW_CONCAT_in_expr0766)
                        if self._state.backtracking == 0:
                            CONCAT27_tree = self._adaptor.createWithPayload(CONCAT27)
                            root_0 = self._adaptor.becomeRoot(CONCAT27_tree, root_0)




                    elif alt7 == 2:
                        # grammars/Miranda.g:133:24: SUBTRACT ^
                        pass 
                        SUBTRACT28 = self.match(self.input, SUBTRACT, self.FOLLOW_SUBTRACT_in_expr0769)
                        if self._state.backtracking == 0:
                            SUBTRACT28_tree = self._adaptor.createWithPayload(SUBTRACT28)
                            root_0 = self._adaptor.becomeRoot(SUBTRACT28_tree, root_0)




                    elif alt7 == 3:
                        # grammars/Miranda.g:133:34: COLON ^
                        pass 
                        COLON29 = self.match(self.input, COLON, self.FOLLOW_COLON_in_expr0772)
                        if self._state.backtracking == 0:
                            COLON29_tree = self._adaptor.createWithPayload(COLON29)
                            root_0 = self._adaptor.becomeRoot(COLON29_tree, root_0)






                    self._state.following.append(self.FOLLOW_expr0_in_expr0776)
                    expr030 = self.expr0()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr030.tree)







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
                self.memoize(self.input, 7, expr0_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr0"


    class expr1_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr1_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr1"
    # grammars/Miranda.g:135:1: expr1 : expr2 ( OR ^ expression )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR32 = None
        expr231 = None

        expression33 = None


        OR32_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:135:6: ( expr2 ( OR ^ expression )* )
                # grammars/Miranda.g:135:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr1785)
                expr231 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr231.tree)


                # grammars/Miranda.g:135:14: ( OR ^ expression )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OR) :
                        LA9_2 = self.input.LA(2)

                        if (self.synpred16_Miranda()) :
                            alt9 = 1




                    if alt9 == 1:
                        # grammars/Miranda.g:135:15: OR ^ expression
                        pass 
                        OR32 = self.match(self.input, OR, self.FOLLOW_OR_in_expr1788)
                        if self._state.backtracking == 0:
                            OR32_tree = self._adaptor.createWithPayload(OR32)
                            root_0 = self._adaptor.becomeRoot(OR32_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr1791)
                        expression33 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression33.tree)



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
            super(MirandaParser.expr2_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr2"
    # grammars/Miranda.g:137:1: expr2 : expr3 ( AND ^ expression )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND35 = None
        expr334 = None

        expression36 = None


        AND35_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:137:6: ( expr3 ( AND ^ expression )* )
                # grammars/Miranda.g:137:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr2800)
                expr334 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr334.tree)


                # grammars/Miranda.g:137:14: ( AND ^ expression )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == AND) :
                        LA10_2 = self.input.LA(2)

                        if (self.synpred17_Miranda()) :
                            alt10 = 1




                    if alt10 == 1:
                        # grammars/Miranda.g:137:15: AND ^ expression
                        pass 
                        AND35 = self.match(self.input, AND, self.FOLLOW_AND_in_expr2803)
                        if self._state.backtracking == 0:
                            AND35_tree = self._adaptor.createWithPayload(AND35)
                            root_0 = self._adaptor.becomeRoot(AND35_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr2806)
                        expression36 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression36.tree)



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
            super(MirandaParser.expr3_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr3"
    # grammars/Miranda.g:139:1: expr3 : expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        set38 = None
        expr437 = None

        expression39 = None


        set38_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:139:6: ( expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* )
                # grammars/Miranda.g:139:8: expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr3815)
                expr437 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr437.tree)


                # grammars/Miranda.g:139:14: ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == EQ or (GT <= LA11_0 <= GTE) or (LT <= LA11_0 <= LTE) or LA11_0 == NEQ) :
                        LA11_2 = self.input.LA(2)

                        if (self.synpred23_Miranda()) :
                            alt11 = 1




                    if alt11 == 1:
                        # grammars/Miranda.g:139:15: ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression
                        pass 
                        set38 = self.input.LT(1)

                        set38 = self.input.LT(1)

                        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set38), root_0)

                            self._state.errorRecovery = False


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        self._state.following.append(self.FOLLOW_expression_in_expr3833)
                        expression39 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression39.tree)



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
            super(MirandaParser.expr4_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr4"
    # grammars/Miranda.g:141:1: expr4 : expr5 ( ( ADD ^| MIN ^) expr5 )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD41 = None
        MIN42 = None
        expr540 = None

        expr543 = None


        ADD41_tree = None
        MIN42_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:141:6: ( expr5 ( ( ADD ^| MIN ^) expr5 )* )
                # grammars/Miranda.g:141:8: expr5 ( ( ADD ^| MIN ^) expr5 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr4842)
                expr540 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr540.tree)


                # grammars/Miranda.g:141:14: ( ( ADD ^| MIN ^) expr5 )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == ADD) :
                        LA13_2 = self.input.LA(2)

                        if (self.synpred25_Miranda()) :
                            alt13 = 1


                    elif (LA13_0 == MIN) :
                        LA13_3 = self.input.LA(2)

                        if (self.synpred25_Miranda()) :
                            alt13 = 1




                    if alt13 == 1:
                        # grammars/Miranda.g:141:15: ( ADD ^| MIN ^) expr5
                        pass 
                        # grammars/Miranda.g:141:15: ( ADD ^| MIN ^)
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
                            # grammars/Miranda.g:141:16: ADD ^
                            pass 
                            ADD41 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr4846)
                            if self._state.backtracking == 0:
                                ADD41_tree = AddNode(ADD41) 
                                root_0 = self._adaptor.becomeRoot(ADD41_tree, root_0)




                        elif alt12 == 2:
                            # grammars/Miranda.g:141:30: MIN ^
                            pass 
                            MIN42 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr4852)
                            if self._state.backtracking == 0:
                                MIN42_tree = MinNode(MIN42) 
                                root_0 = self._adaptor.becomeRoot(MIN42_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr5_in_expr4859)
                        expr543 = self.expr5()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr543.tree)



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
            super(MirandaParser.expr5_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr5"
    # grammars/Miranda.g:143:1: expr5 : expr6 ( ( DIV ^| MUL ^) expr6 )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV45 = None
        MUL46 = None
        expr644 = None

        expr647 = None


        DIV45_tree = None
        MUL46_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:143:6: ( expr6 ( ( DIV ^| MUL ^) expr6 )* )
                # grammars/Miranda.g:143:8: expr6 ( ( DIV ^| MUL ^) expr6 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr5868)
                expr644 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr644.tree)


                # grammars/Miranda.g:143:14: ( ( DIV ^| MUL ^) expr6 )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == DIV) :
                        LA15_2 = self.input.LA(2)

                        if (self.synpred27_Miranda()) :
                            alt15 = 1


                    elif (LA15_0 == MUL) :
                        LA15_3 = self.input.LA(2)

                        if (self.synpred27_Miranda()) :
                            alt15 = 1




                    if alt15 == 1:
                        # grammars/Miranda.g:143:15: ( DIV ^| MUL ^) expr6
                        pass 
                        # grammars/Miranda.g:143:15: ( DIV ^| MUL ^)
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
                            # grammars/Miranda.g:143:16: DIV ^
                            pass 
                            DIV45 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr5872)
                            if self._state.backtracking == 0:
                                DIV45_tree = DivNode(DIV45) 
                                root_0 = self._adaptor.becomeRoot(DIV45_tree, root_0)




                        elif alt14 == 2:
                            # grammars/Miranda.g:143:30: MUL ^
                            pass 
                            MUL46 = self.match(self.input, MUL, self.FOLLOW_MUL_in_expr5878)
                            if self._state.backtracking == 0:
                                MUL46_tree = MulNode(MUL46) 
                                root_0 = self._adaptor.becomeRoot(MUL46_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr6_in_expr5885)
                        expr647 = self.expr6()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr647.tree)



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
            super(MirandaParser.expr6_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr6"
    # grammars/Miranda.g:145:1: expr6 : expr7 ( ( IDIV ^| MOD ^) expr7 )* ;
    def expr6(self, ):
        retval = self.expr6_return()
        retval.start = self.input.LT(1)

        expr6_StartIndex = self.input.index()

        root_0 = None

        IDIV49 = None
        MOD50 = None
        expr748 = None

        expr751 = None


        IDIV49_tree = None
        MOD50_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:145:6: ( expr7 ( ( IDIV ^| MOD ^) expr7 )* )
                # grammars/Miranda.g:145:8: expr7 ( ( IDIV ^| MOD ^) expr7 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr7_in_expr6894)
                expr748 = self.expr7()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr748.tree)


                # grammars/Miranda.g:145:14: ( ( IDIV ^| MOD ^) expr7 )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == IDIV) :
                        LA17_2 = self.input.LA(2)

                        if (self.synpred29_Miranda()) :
                            alt17 = 1


                    elif (LA17_0 == MOD) :
                        LA17_3 = self.input.LA(2)

                        if (self.synpred29_Miranda()) :
                            alt17 = 1




                    if alt17 == 1:
                        # grammars/Miranda.g:145:15: ( IDIV ^| MOD ^) expr7
                        pass 
                        # grammars/Miranda.g:145:15: ( IDIV ^| MOD ^)
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == IDIV) :
                            alt16 = 1
                        elif (LA16_0 == MOD) :
                            alt16 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 16, 0, self.input)

                            raise nvae


                        if alt16 == 1:
                            # grammars/Miranda.g:145:16: IDIV ^
                            pass 
                            IDIV49 = self.match(self.input, IDIV, self.FOLLOW_IDIV_in_expr6898)
                            if self._state.backtracking == 0:
                                IDIV49_tree = self._adaptor.createWithPayload(IDIV49)
                                root_0 = self._adaptor.becomeRoot(IDIV49_tree, root_0)




                        elif alt16 == 2:
                            # grammars/Miranda.g:145:22: MOD ^
                            pass 
                            MOD50 = self.match(self.input, MOD, self.FOLLOW_MOD_in_expr6901)
                            if self._state.backtracking == 0:
                                MOD50_tree = self._adaptor.createWithPayload(MOD50)
                                root_0 = self._adaptor.becomeRoot(MOD50_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr7_in_expr6905)
                        expr751 = self.expr7()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr751.tree)



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
                self.memoize(self.input, 13, expr6_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr6"


    class expr7_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr7_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr7"
    # grammars/Miranda.g:147:1: expr7 : expr8 ( ( EXP ^) expr8 )* ;
    def expr7(self, ):
        retval = self.expr7_return()
        retval.start = self.input.LT(1)

        expr7_StartIndex = self.input.index()

        root_0 = None

        EXP53 = None
        expr852 = None

        expr854 = None


        EXP53_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:147:6: ( expr8 ( ( EXP ^) expr8 )* )
                # grammars/Miranda.g:147:8: expr8 ( ( EXP ^) expr8 )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr8_in_expr7914)
                expr852 = self.expr8()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr852.tree)


                # grammars/Miranda.g:147:14: ( ( EXP ^) expr8 )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == EXP) :
                        LA18_2 = self.input.LA(2)

                        if (self.synpred30_Miranda()) :
                            alt18 = 1




                    if alt18 == 1:
                        # grammars/Miranda.g:147:15: ( EXP ^) expr8
                        pass 
                        # grammars/Miranda.g:147:15: ( EXP ^)
                        # grammars/Miranda.g:147:16: EXP ^
                        pass 
                        EXP53 = self.match(self.input, EXP, self.FOLLOW_EXP_in_expr7918)
                        if self._state.backtracking == 0:
                            EXP53_tree = self._adaptor.createWithPayload(EXP53)
                            root_0 = self._adaptor.becomeRoot(EXP53_tree, root_0)






                        self._state.following.append(self.FOLLOW_expr8_in_expr7922)
                        expr854 = self.expr8()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expr854.tree)



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
                self.memoize(self.input, 14, expr7_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr7"


    class expr8_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr8_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr8"
    # grammars/Miranda.g:149:1: expr8 : ( aexpr )+ ;
    def expr8(self, ):
        retval = self.expr8_return()
        retval.start = self.input.LT(1)

        expr8_StartIndex = self.input.index()

        root_0 = None

        aexpr55 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:149:6: ( ( aexpr )+ )
                # grammars/Miranda.g:149:8: ( aexpr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:149:8: ( aexpr )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19 = self.input.LA(1)
                    if LA19 == ID:
                        LA19_17 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == INT:
                        LA19_18 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == FLOAT:
                        LA19_19 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == CHAR:
                        LA19_20 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == STRING:
                        LA19_21 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == NOT:
                        LA19_22 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == FALSE or LA19 == TRUE:
                        LA19_23 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == LPAREN:
                        LA19_24 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1


                    elif LA19 == LBRACKET:
                        LA19_25 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt19 = 1



                    if alt19 == 1:
                        # grammars/Miranda.g:149:8: aexpr
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr8931)
                        aexpr55 = self.aexpr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, aexpr55.tree)



                    else:
                        if cnt19 >= 1:
                            break #loop19

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1


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
                self.memoize(self.input, 15, expr8_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr8"


    class aexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.aexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "aexpr"
    # grammars/Miranda.g:155:1: aexpr : ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !);
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID56 = None
        INT57 = None
        FLOAT58 = None
        CHAR59 = None
        STRING60 = None
        NOT61 = None
        LPAREN67 = None
        RPAREN69 = None
        expression62 = None

        boolean63 = None

        section64 = None

        tuple65 = None

        list66 = None

        expression68 = None


        ID56_tree = None
        INT57_tree = None
        FLOAT58_tree = None
        CHAR59_tree = None
        STRING60_tree = None
        NOT61_tree = None
        LPAREN67_tree = None
        RPAREN69_tree = None
        stream_CHAR = RewriteRuleTokenStream(self._adaptor, "token CHAR")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:156:3: ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !)
                alt20 = 11
                LA20 = self.input.LA(1)
                if LA20 == ID:
                    alt20 = 1
                elif LA20 == INT:
                    alt20 = 2
                elif LA20 == FLOAT:
                    alt20 = 3
                elif LA20 == CHAR:
                    alt20 = 4
                elif LA20 == STRING:
                    alt20 = 5
                elif LA20 == NOT:
                    alt20 = 6
                elif LA20 == FALSE or LA20 == TRUE:
                    alt20 = 7
                elif LA20 == LPAREN:
                    LA20_8 = self.input.LA(2)

                    if (self.synpred39_Miranda()) :
                        alt20 = 8
                    elif (self.synpred40_Miranda()) :
                        alt20 = 9
                    elif (True) :
                        alt20 = 11
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 20, 8, self.input)

                        raise nvae


                elif LA20 == LBRACKET:
                    alt20 = 10
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammars/Miranda.g:156:5: ID
                    pass 
                    ID56 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr944) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID56)


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
                        # 157:5: -> ^( ID )
                        # grammars/Miranda.g:157:8: ^( ID )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IdentifierNode(stream_ID.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 2:
                    # grammars/Miranda.g:158:5: INT
                    pass 
                    INT57 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr963) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT57)


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
                        # 159:5: -> ^( INT )
                        # grammars/Miranda.g:159:8: ^( INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IntNode(stream_INT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 3:
                    # grammars/Miranda.g:160:5: FLOAT
                    pass 
                    FLOAT58 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr982) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT58)


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
                        # 161:5: -> ^( FLOAT )
                        # grammars/Miranda.g:161:8: ^( FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        FloatNode(stream_FLOAT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 4:
                    # grammars/Miranda.g:162:5: CHAR
                    pass 
                    CHAR59 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_aexpr1001) 
                    if self._state.backtracking == 0:
                        stream_CHAR.add(CHAR59)


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
                        # 163:5: -> ^( CHAR )
                        # grammars/Miranda.g:163:8: ^( CHAR )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        CharNode(stream_CHAR.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 5:
                    # grammars/Miranda.g:164:5: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING60 = self.match(self.input, STRING, self.FOLLOW_STRING_in_aexpr1020)
                    if self._state.backtracking == 0:
                        STRING60_tree = self._adaptor.createWithPayload(STRING60)
                        self._adaptor.addChild(root_0, STRING60_tree)




                elif alt20 == 6:
                    # grammars/Miranda.g:165:5: NOT expression
                    pass 
                    root_0 = self._adaptor.nil()


                    NOT61 = self.match(self.input, NOT, self.FOLLOW_NOT_in_aexpr1026)
                    if self._state.backtracking == 0:
                        NOT61_tree = self._adaptor.createWithPayload(NOT61)
                        self._adaptor.addChild(root_0, NOT61_tree)



                    self._state.following.append(self.FOLLOW_expression_in_aexpr1028)
                    expression62 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression62.tree)



                elif alt20 == 7:
                    # grammars/Miranda.g:166:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_aexpr1034)
                    boolean63 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean63.tree)



                elif alt20 == 8:
                    # grammars/Miranda.g:167:5: section
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_section_in_aexpr1040)
                    section64 = self.section()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, section64.tree)



                elif alt20 == 9:
                    # grammars/Miranda.g:168:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_aexpr1046)
                    tuple65 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple65.tree)



                elif alt20 == 10:
                    # grammars/Miranda.g:169:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_aexpr1052)
                    list66 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list66.tree)



                elif alt20 == 11:
                    # grammars/Miranda.g:170:5: LPAREN ! expression RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN67 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr1058)

                    self._state.following.append(self.FOLLOW_expression_in_aexpr1061)
                    expression68 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression68.tree)


                    RPAREN69 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr1063)


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
                self.memoize(self.input, 16, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class tuple_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.tuple_return, self).__init__()

            self.tree = None





    # $ANTLR start "tuple"
    # grammars/Miranda.g:173:1: tuple : LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) ;
    def tuple(self, ):
        retval = self.tuple_return()
        retval.start = self.input.LT(1)

        tuple_StartIndex = self.input.index()

        root_0 = None

        LPAREN70 = None
        COMMA72 = None
        RPAREN74 = None
        expression71 = None

        expression73 = None


        LPAREN70_tree = None
        COMMA72_tree = None
        RPAREN74_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:173:6: ( LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) )
                # grammars/Miranda.g:173:8: LPAREN expression ( COMMA expression )+ RPAREN
                pass 
                LPAREN70 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_tuple1072) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN70)


                self._state.following.append(self.FOLLOW_expression_in_tuple1074)
                expression71 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression71.tree)


                # grammars/Miranda.g:173:26: ( COMMA expression )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == COMMA) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammars/Miranda.g:173:27: COMMA expression
                        pass 
                        COMMA72 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_tuple1077) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA72)


                        self._state.following.append(self.FOLLOW_expression_in_tuple1079)
                        expression73 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression73.tree)



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1


                RPAREN74 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_tuple1083) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN74)


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
                    # 174:8: -> ^( TUPLE ( expression )* )
                    # grammars/Miranda.g:174:11: ^( TUPLE ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TUPLE, "TUPLE")
                    , root_1)

                    # grammars/Miranda.g:174:19: ( expression )*
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
                self.memoize(self.input, 17, tuple_StartIndex, success)


            pass
        return retval

    # $ANTLR end "tuple"


    class list_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.list_return, self).__init__()

            self.tree = None





    # $ANTLR start "list"
    # grammars/Miranda.g:177:1: list : LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) ;
    def list(self, ):
        retval = self.list_return()
        retval.start = self.input.LT(1)

        list_StartIndex = self.input.index()

        root_0 = None

        LBRACKET75 = None
        COMMA77 = None
        RBRACKET79 = None
        expression76 = None

        expression78 = None


        LBRACKET75_tree = None
        COMMA77_tree = None
        RBRACKET79_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:177:5: ( LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) )
                # grammars/Miranda.g:177:7: LBRACKET ( expression )? ( COMMA expression )* RBRACKET
                pass 
                LBRACKET75 = self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_list1107) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET75)


                # grammars/Miranda.g:177:16: ( expression )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == CHAR or (FALSE <= LA22_0 <= FLOAT) or LA22_0 == ID or LA22_0 == INT or LA22_0 == LBRACKET or LA22_0 == LPAREN or LA22_0 == NOT or LA22_0 == STRING or LA22_0 == TRUE) :
                    alt22 = 1
                if alt22 == 1:
                    # grammars/Miranda.g:177:16: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_list1109)
                    expression76 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression76.tree)





                # grammars/Miranda.g:177:28: ( COMMA expression )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == COMMA) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammars/Miranda.g:177:29: COMMA expression
                        pass 
                        COMMA77 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_list1113) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA77)


                        self._state.following.append(self.FOLLOW_expression_in_list1115)
                        expression78 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression78.tree)



                    else:
                        break #loop23


                RBRACKET79 = self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_list1119) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET79)


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
                    # 178:7: -> ^( LIST ( expression )* )
                    # grammars/Miranda.g:178:10: ^( LIST ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # grammars/Miranda.g:178:17: ( expression )*
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
                self.memoize(self.input, 18, list_StartIndex, success)


            pass
        return retval

    # $ANTLR end "list"


    class section_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.section_return, self).__init__()

            self.tree = None





    # $ANTLR start "section"
    # grammars/Miranda.g:181:1: section : ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) );
    def section(self, ):
        retval = self.section_return()
        retval.start = self.input.LT(1)

        section_StartIndex = self.input.index()

        root_0 = None

        LPAREN80 = None
        RPAREN82 = None
        LPAREN83 = None
        RPAREN86 = None
        LPAREN87 = None
        RPAREN90 = None
        operator81 = None

        operator84 = None

        expression85 = None

        expression88 = None

        operator89 = None


        LPAREN80_tree = None
        RPAREN82_tree = None
        LPAREN83_tree = None
        RPAREN86_tree = None
        LPAREN87_tree = None
        RPAREN90_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_operator = RewriteRuleSubtreeStream(self._adaptor, "rule operator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:182:3: ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) )
                alt24 = 3
                LA24_0 = self.input.LA(1)

                if (LA24_0 == LPAREN) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == ADD or LA24_1 == AND or LA24_1 == CONCAT or LA24_1 == DIV or (EQ <= LA24_1 <= EXP) or (GT <= LA24_1 <= GTE) or LA24_1 == IDIV or (LT <= LA24_1 <= NEQ) or LA24_1 == OR or LA24_1 == SUBTRACT) :
                        LA24_2 = self.input.LA(3)

                        if (LA24_2 == RPAREN) :
                            alt24 = 1
                        elif (LA24_2 == CHAR or (FALSE <= LA24_2 <= FLOAT) or LA24_2 == ID or LA24_2 == INT or LA24_2 == LBRACKET or LA24_2 == LPAREN or LA24_2 == NOT or LA24_2 == STRING or LA24_2 == TRUE) :
                            alt24 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 24, 2, self.input)

                            raise nvae


                    elif (LA24_1 == CHAR or (FALSE <= LA24_1 <= FLOAT) or LA24_1 == ID or LA24_1 == INT or LA24_1 == LBRACKET or LA24_1 == LPAREN or LA24_1 == NOT or LA24_1 == STRING or LA24_1 == TRUE) :
                        alt24 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammars/Miranda.g:182:5: LPAREN operator RPAREN
                    pass 
                    LPAREN80 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1145) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN80)


                    self._state.following.append(self.FOLLOW_operator_in_section1147)
                    operator81 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator81.tree)


                    RPAREN82 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1149) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN82)


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
                        # 183:4: -> ^( SECTION operator )
                        # grammars/Miranda.g:183:7: ^( SECTION operator )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt24 == 2:
                    # grammars/Miranda.g:184:5: LPAREN operator expression RPAREN
                    pass 
                    LPAREN83 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1166) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN83)


                    self._state.following.append(self.FOLLOW_operator_in_section1168)
                    operator84 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator84.tree)


                    self._state.following.append(self.FOLLOW_expression_in_section1170)
                    expression85 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression85.tree)


                    RPAREN86 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1172) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN86)


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
                        # 185:4: -> ^( SECTION operator expression )
                        # grammars/Miranda.g:185:7: ^( SECTION operator expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt24 == 3:
                    # grammars/Miranda.g:186:5: LPAREN expression operator RPAREN
                    pass 
                    LPAREN87 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1191) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN87)


                    self._state.following.append(self.FOLLOW_expression_in_section1193)
                    expression88 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression88.tree)


                    self._state.following.append(self.FOLLOW_operator_in_section1195)
                    operator89 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator89.tree)


                    RPAREN90 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1197) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN90)


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
                        # 187:4: -> ^( SECTION expression operator )
                        # grammars/Miranda.g:187:7: ^( SECTION expression operator )
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
                self.memoize(self.input, 19, section_StartIndex, success)


            pass
        return retval

    # $ANTLR end "section"


    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.operator_return, self).__init__()

            self.tree = None





    # $ANTLR start "operator"
    # grammars/Miranda.g:189:10: fragment operator : ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP );
    def operator(self, ):
        retval = self.operator_return()
        retval.start = self.input.LT(1)

        operator_StartIndex = self.input.index()

        root_0 = None

        set91 = None

        set91_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:189:18: ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV | MUL | IDIV | MOD | EXP )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set91 = self.input.LT(1)

                if self.input.LA(1) == ADD or self.input.LA(1) == AND or self.input.LA(1) == CONCAT or self.input.LA(1) == DIV or (EQ <= self.input.LA(1) <= EXP) or (GT <= self.input.LA(1) <= GTE) or self.input.LA(1) == IDIV or (LT <= self.input.LA(1) <= NEQ) or self.input.LA(1) == OR or self.input.LA(1) == SUBTRACT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set91))

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
                self.memoize(self.input, 20, operator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "operator"


    class boolean_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.boolean_return, self).__init__()

            self.tree = None





    # $ANTLR start "boolean"
    # grammars/Miranda.g:191:1: boolean : ( TRUE | FALSE );
    def boolean(self, ):
        retval = self.boolean_return()
        retval.start = self.input.LT(1)

        boolean_StartIndex = self.input.index()

        root_0 = None

        set92 = None

        set92_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:191:8: ( TRUE | FALSE )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set92 = self.input.LT(1)

                if self.input.LA(1) == FALSE or self.input.LA(1) == TRUE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set92))

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
                self.memoize(self.input, 21, boolean_StartIndex, success)


            pass
        return retval

    # $ANTLR end "boolean"

    # $ANTLR start "synpred1_Miranda"
    def synpred1_Miranda_fragment(self, ):
        # grammars/Miranda.g:106:4: ( definition DEDENT )
        # grammars/Miranda.g:106:4: definition DEDENT
        pass 
        self._state.following.append(self.FOLLOW_definition_in_synpred1_Miranda589)
        self.definition()

        self._state.following.pop()

        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred1_Miranda591)



    # $ANTLR end "synpred1_Miranda"



    # $ANTLR start "synpred12_Miranda"
    def synpred12_Miranda_fragment(self, ):
        # grammars/Miranda.g:127:5: ( tuple )
        # grammars/Miranda.g:127:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred12_Miranda735)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred12_Miranda"



    # $ANTLR start "synpred15_Miranda"
    def synpred15_Miranda_fragment(self, ):
        # grammars/Miranda.g:133:15: ( ( CONCAT | SUBTRACT | COLON ) expr0 )
        # grammars/Miranda.g:133:15: ( CONCAT | SUBTRACT | COLON ) expr0
        pass 
        if self.input.LA(1) == COLON or self.input.LA(1) == CONCAT or self.input.LA(1) == SUBTRACT:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr0_in_synpred15_Miranda776)
        self.expr0()

        self._state.following.pop()



    # $ANTLR end "synpred15_Miranda"



    # $ANTLR start "synpred16_Miranda"
    def synpred16_Miranda_fragment(self, ):
        # grammars/Miranda.g:135:15: ( OR expression )
        # grammars/Miranda.g:135:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred16_Miranda788)

        self._state.following.append(self.FOLLOW_expression_in_synpred16_Miranda791)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred16_Miranda"



    # $ANTLR start "synpred17_Miranda"
    def synpred17_Miranda_fragment(self, ):
        # grammars/Miranda.g:137:15: ( AND expression )
        # grammars/Miranda.g:137:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred17_Miranda803)

        self._state.following.append(self.FOLLOW_expression_in_synpred17_Miranda806)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred17_Miranda"



    # $ANTLR start "synpred23_Miranda"
    def synpred23_Miranda_fragment(self, ):
        # grammars/Miranda.g:139:15: ( ( LT | LTE | EQ | NEQ | GTE | GT ) expression )
        # grammars/Miranda.g:139:15: ( LT | LTE | EQ | NEQ | GTE | GT ) expression
        pass 
        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred23_Miranda833)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred23_Miranda"



    # $ANTLR start "synpred25_Miranda"
    def synpred25_Miranda_fragment(self, ):
        # grammars/Miranda.g:141:15: ( ( ADD | MIN ) expr5 )
        # grammars/Miranda.g:141:15: ( ADD | MIN ) expr5
        pass 
        if self.input.LA(1) == ADD or self.input.LA(1) == MIN:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr5_in_synpred25_Miranda859)
        self.expr5()

        self._state.following.pop()



    # $ANTLR end "synpred25_Miranda"



    # $ANTLR start "synpred27_Miranda"
    def synpred27_Miranda_fragment(self, ):
        # grammars/Miranda.g:143:15: ( ( DIV | MUL ) expr6 )
        # grammars/Miranda.g:143:15: ( DIV | MUL ) expr6
        pass 
        if self.input.LA(1) == DIV or self.input.LA(1) == MUL:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr6_in_synpred27_Miranda885)
        self.expr6()

        self._state.following.pop()



    # $ANTLR end "synpred27_Miranda"



    # $ANTLR start "synpred29_Miranda"
    def synpred29_Miranda_fragment(self, ):
        # grammars/Miranda.g:145:15: ( ( IDIV | MOD ) expr7 )
        # grammars/Miranda.g:145:15: ( IDIV | MOD ) expr7
        pass 
        if self.input.LA(1) == IDIV or self.input.LA(1) == MOD:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr7_in_synpred29_Miranda905)
        self.expr7()

        self._state.following.pop()



    # $ANTLR end "synpred29_Miranda"



    # $ANTLR start "synpred30_Miranda"
    def synpred30_Miranda_fragment(self, ):
        # grammars/Miranda.g:147:15: ( ( EXP ) expr8 )
        # grammars/Miranda.g:147:15: ( EXP ) expr8
        pass 
        # grammars/Miranda.g:147:15: ( EXP )
        # grammars/Miranda.g:147:16: EXP
        pass 
        self.match(self.input, EXP, self.FOLLOW_EXP_in_synpred30_Miranda918)




        self._state.following.append(self.FOLLOW_expr8_in_synpred30_Miranda922)
        self.expr8()

        self._state.following.pop()



    # $ANTLR end "synpred30_Miranda"



    # $ANTLR start "synpred31_Miranda"
    def synpred31_Miranda_fragment(self, ):
        # grammars/Miranda.g:149:8: ( aexpr )
        # grammars/Miranda.g:149:8: aexpr
        pass 
        self._state.following.append(self.FOLLOW_aexpr_in_synpred31_Miranda931)
        self.aexpr()

        self._state.following.pop()



    # $ANTLR end "synpred31_Miranda"



    # $ANTLR start "synpred39_Miranda"
    def synpred39_Miranda_fragment(self, ):
        # grammars/Miranda.g:167:5: ( section )
        # grammars/Miranda.g:167:5: section
        pass 
        self._state.following.append(self.FOLLOW_section_in_synpred39_Miranda1040)
        self.section()

        self._state.following.pop()



    # $ANTLR end "synpred39_Miranda"



    # $ANTLR start "synpred40_Miranda"
    def synpred40_Miranda_fragment(self, ):
        # grammars/Miranda.g:168:5: ( tuple )
        # grammars/Miranda.g:168:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred40_Miranda1046)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred40_Miranda"




    def synpred39_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred39_Miranda_fragment()
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

    def synpred23_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred23_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred40_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred40_Miranda_fragment()
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

    def synpred17_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_Miranda_fragment()
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



 

    FOLLOW_definition_in_program589 = frozenset([12])
    FOLLOW_DEDENT_in_program591 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_program595 = frozenset([])
    FOLLOW_EOF_in_program597 = frozenset([1])
    FOLLOW_ID_in_definition624 = frozenset([19, 20, 24, 26, 27, 28, 30, 48])
    FOLLOW_parameter_in_definition626 = frozenset([19, 20, 24, 26, 27, 28, 30, 48])
    FOLLOW_IS_in_definition629 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_definition631 = frozenset([1, 9])
    FOLLOW_guard_in_definition633 = frozenset([1])
    FOLLOW_COMMA_in_guard664 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 40, 46, 48])
    FOLLOW_expression_in_guard667 = frozenset([1])
    FOLLOW_OTHERWISE_in_guard669 = frozenset([1])
    FOLLOW_basic_in_parameter680 = frozenset([1, 4, 8])
    FOLLOW_set_in_parameter683 = frozenset([19, 20, 24, 26, 28, 30, 48])
    FOLLOW_parameter_in_parameter690 = frozenset([1])
    FOLLOW_ID_in_basic705 = frozenset([1])
    FOLLOW_INT_in_basic711 = frozenset([1])
    FOLLOW_FLOAT_in_basic717 = frozenset([1])
    FOLLOW_boolean_in_basic723 = frozenset([1])
    FOLLOW_list_in_basic729 = frozenset([1])
    FOLLOW_tuple_in_basic735 = frozenset([1])
    FOLLOW_LPAREN_in_basic741 = frozenset([19, 20, 24, 26, 28, 30, 48])
    FOLLOW_parameter_in_basic744 = frozenset([43])
    FOLLOW_RPAREN_in_basic746 = frozenset([1])
    FOLLOW_expr0_in_expression755 = frozenset([1])
    FOLLOW_expr1_in_expr0762 = frozenset([1, 8, 11, 47])
    FOLLOW_CONCAT_in_expr0766 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_SUBTRACT_in_expr0769 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_COLON_in_expr0772 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr0_in_expr0776 = frozenset([1])
    FOLLOW_expr2_in_expr1785 = frozenset([1, 39])
    FOLLOW_OR_in_expr1788 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr1791 = frozenset([1, 39])
    FOLLOW_expr3_in_expr2800 = frozenset([1, 6])
    FOLLOW_AND_in_expr2803 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr2806 = frozenset([1, 6])
    FOLLOW_expr4_in_expr3815 = frozenset([1, 17, 21, 22, 31, 32, 36])
    FOLLOW_set_in_expr3818 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_expr3833 = frozenset([1, 17, 21, 22, 31, 32, 36])
    FOLLOW_expr5_in_expr4842 = frozenset([1, 4, 33])
    FOLLOW_ADD_in_expr4846 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_MIN_in_expr4852 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr5_in_expr4859 = frozenset([1, 4, 33])
    FOLLOW_expr6_in_expr5868 = frozenset([1, 14, 35])
    FOLLOW_DIV_in_expr5872 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_MUL_in_expr5878 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr6_in_expr5885 = frozenset([1, 14, 35])
    FOLLOW_expr7_in_expr6894 = frozenset([1, 25, 34])
    FOLLOW_IDIV_in_expr6898 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_MOD_in_expr6901 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr7_in_expr6905 = frozenset([1, 25, 34])
    FOLLOW_expr8_in_expr7914 = frozenset([1, 18])
    FOLLOW_EXP_in_expr7918 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr8_in_expr7922 = frozenset([1, 18])
    FOLLOW_aexpr_in_expr8931 = frozenset([1, 7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_ID_in_aexpr944 = frozenset([1])
    FOLLOW_INT_in_aexpr963 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr982 = frozenset([1])
    FOLLOW_CHAR_in_aexpr1001 = frozenset([1])
    FOLLOW_STRING_in_aexpr1020 = frozenset([1])
    FOLLOW_NOT_in_aexpr1026 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_aexpr1028 = frozenset([1])
    FOLLOW_boolean_in_aexpr1034 = frozenset([1])
    FOLLOW_section_in_aexpr1040 = frozenset([1])
    FOLLOW_tuple_in_aexpr1046 = frozenset([1])
    FOLLOW_list_in_aexpr1052 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr1058 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_aexpr1061 = frozenset([43])
    FOLLOW_RPAREN_in_aexpr1063 = frozenset([1])
    FOLLOW_LPAREN_in_tuple1072 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_tuple1074 = frozenset([9])
    FOLLOW_COMMA_in_tuple1077 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_tuple1079 = frozenset([9, 43])
    FOLLOW_RPAREN_in_tuple1083 = frozenset([1])
    FOLLOW_LBRACKET_in_list1107 = frozenset([7, 9, 19, 20, 24, 26, 28, 30, 37, 42, 46, 48])
    FOLLOW_expression_in_list1109 = frozenset([9, 42])
    FOLLOW_COMMA_in_list1113 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_list1115 = frozenset([9, 42])
    FOLLOW_RBRACKET_in_list1119 = frozenset([1])
    FOLLOW_LPAREN_in_section1145 = frozenset([4, 6, 11, 14, 17, 18, 21, 22, 25, 31, 32, 33, 34, 35, 36, 39, 47])
    FOLLOW_operator_in_section1147 = frozenset([43])
    FOLLOW_RPAREN_in_section1149 = frozenset([1])
    FOLLOW_LPAREN_in_section1166 = frozenset([4, 6, 11, 14, 17, 18, 21, 22, 25, 31, 32, 33, 34, 35, 36, 39, 47])
    FOLLOW_operator_in_section1168 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_section1170 = frozenset([43])
    FOLLOW_RPAREN_in_section1172 = frozenset([1])
    FOLLOW_LPAREN_in_section1191 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_section1193 = frozenset([4, 6, 11, 14, 17, 18, 21, 22, 25, 31, 32, 33, 34, 35, 36, 39, 47])
    FOLLOW_operator_in_section1195 = frozenset([43])
    FOLLOW_RPAREN_in_section1197 = frozenset([1])
    FOLLOW_definition_in_synpred1_Miranda589 = frozenset([12])
    FOLLOW_DEDENT_in_synpred1_Miranda591 = frozenset([1])
    FOLLOW_tuple_in_synpred12_Miranda735 = frozenset([1])
    FOLLOW_set_in_synpred15_Miranda765 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr0_in_synpred15_Miranda776 = frozenset([1])
    FOLLOW_OR_in_synpred16_Miranda788 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred16_Miranda791 = frozenset([1])
    FOLLOW_AND_in_synpred17_Miranda803 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred17_Miranda806 = frozenset([1])
    FOLLOW_set_in_synpred23_Miranda818 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expression_in_synpred23_Miranda833 = frozenset([1])
    FOLLOW_set_in_synpred25_Miranda845 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr5_in_synpred25_Miranda859 = frozenset([1])
    FOLLOW_set_in_synpred27_Miranda871 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr6_in_synpred27_Miranda885 = frozenset([1])
    FOLLOW_set_in_synpred29_Miranda897 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr7_in_synpred29_Miranda905 = frozenset([1])
    FOLLOW_EXP_in_synpred30_Miranda918 = frozenset([7, 19, 20, 24, 26, 28, 30, 37, 46, 48])
    FOLLOW_expr8_in_synpred30_Miranda922 = frozenset([1])
    FOLLOW_aexpr_in_synpred31_Miranda931 = frozenset([1])
    FOLLOW_section_in_synpred39_Miranda1040 = frozenset([1])
    FOLLOW_tuple_in_synpred40_Miranda1046 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MirandaLexer", MirandaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
