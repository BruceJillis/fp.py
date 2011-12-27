# $ANTLR 3.4 grammars/Miranda.g 2011-12-27 23:24:25

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
NEQ=37
NOT=38
NUMERIC=39
NUM_TYPE=40
OR=41
OTHERWISE=42
PART=43
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
    "MIN", "MOD", "NEQ", "NOT", "NUMERIC", "NUM_TYPE", "OR", "OTHERWISE", 
    "PART", "PROGRAM", "RBRACKET", "RPAREN", "SECTION", "SINGLE_QUOTE", 
    "STARS", "STRING", "SUBTRACT", "TRUE", "TUPLE", "TYPE", "TYPE_IS", "WHERE", 
    "WHITESPACE"
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
    # grammars/Miranda.g:111:1: program : ( ( typedef | definition ) DEDENT )* expression EOF -> ^( PROGRAM ( typedef )* ( definition )* expression ) ;
    def program(self, ):
        retval = self.program_return()
        retval.start = self.input.LT(1)

        program_StartIndex = self.input.index()

        root_0 = None

        DEDENT3 = None
        EOF5 = None
        typedef1 = None

        definition2 = None

        expression4 = None


        DEDENT3_tree = None
        EOF5_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_definition = RewriteRuleSubtreeStream(self._adaptor, "rule definition")
        stream_typedef = RewriteRuleSubtreeStream(self._adaptor, "rule typedef")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:111:8: ( ( ( typedef | definition ) DEDENT )* expression EOF -> ^( PROGRAM ( typedef )* ( definition )* expression ) )
                # grammars/Miranda.g:112:3: ( ( typedef | definition ) DEDENT )* expression EOF
                pass 
                # grammars/Miranda.g:112:3: ( ( typedef | definition ) DEDENT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        LA2_1 = self.input.LA(2)

                        if (self.synpred2_Miranda()) :
                            alt2 = 1




                    if alt2 == 1:
                        # grammars/Miranda.g:112:4: ( typedef | definition ) DEDENT
                        pass 
                        # grammars/Miranda.g:112:4: ( typedef | definition )
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == ID) :
                            LA1_1 = self.input.LA(2)

                            if (LA1_1 == STARS or LA1_1 == TYPE_IS) :
                                alt1 = 1
                            elif (LA1_1 == DEDENT or (FALSE <= LA1_1 <= FLOAT) or LA1_1 == ID or (INT <= LA1_1 <= LBRACKET) or LA1_1 == LPAREN or LA1_1 == TRUE) :
                                alt1 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 1, 1, self.input)

                                raise nvae


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 1, 0, self.input)

                            raise nvae


                        if alt1 == 1:
                            # grammars/Miranda.g:112:5: typedef
                            pass 
                            self._state.following.append(self.FOLLOW_typedef_in_program650)
                            typedef1 = self.typedef()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_typedef.add(typedef1.tree)



                        elif alt1 == 2:
                            # grammars/Miranda.g:112:13: definition
                            pass 
                            self._state.following.append(self.FOLLOW_definition_in_program652)
                            definition2 = self.definition()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_definition.add(definition2.tree)





                        DEDENT3 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_program655) 
                        if self._state.backtracking == 0:
                            stream_DEDENT.add(DEDENT3)



                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_expression_in_program659)
                expression4 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression4.tree)


                EOF5 = self.match(self.input, EOF, self.FOLLOW_EOF_in_program661) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF5)


                # AST Rewrite
                # elements: typedef, expression, definition
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
                    # 113:3: -> ^( PROGRAM ( typedef )* ( definition )* expression )
                    # grammars/Miranda.g:113:6: ^( PROGRAM ( typedef )* ( definition )* expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    ProgramNode(PROGRAM)
                    , root_1)

                    # grammars/Miranda.g:113:29: ( typedef )*
                    while stream_typedef.hasNext():
                        self._adaptor.addChild(root_1, stream_typedef.nextTree())


                    stream_typedef.reset();

                    # grammars/Miranda.g:113:38: ( definition )*
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
    # grammars/Miranda.g:116:1: definition : ID ( pattern )* ( body )* -> ^( DEFINITION ID ( pattern )* ( body )* ) ;
    def definition(self, ):
        retval = self.definition_return()
        retval.start = self.input.LT(1)

        definition_StartIndex = self.input.index()

        root_0 = None

        ID6 = None
        pattern7 = None

        body8 = None


        ID6_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_body = RewriteRuleSubtreeStream(self._adaptor, "rule body")
        stream_pattern = RewriteRuleSubtreeStream(self._adaptor, "rule pattern")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:118:3: ( ID ( pattern )* ( body )* -> ^( DEFINITION ID ( pattern )* ( body )* ) )
                # grammars/Miranda.g:118:5: ID ( pattern )* ( body )*
                pass 
                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_definition694) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID6)


                # grammars/Miranda.g:118:8: ( pattern )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((FALSE <= LA3_0 <= FLOAT) or LA3_0 == ID or LA3_0 == INT or LA3_0 == LBRACKET or LA3_0 == LPAREN or LA3_0 == TRUE) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammars/Miranda.g:118:8: pattern
                        pass 
                        self._state.following.append(self.FOLLOW_pattern_in_definition696)
                        pattern7 = self.pattern()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_pattern.add(pattern7.tree)



                    else:
                        break #loop3


                # grammars/Miranda.g:118:17: ( body )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == IS) :
                        LA4_2 = self.input.LA(2)

                        if (self.synpred4_Miranda()) :
                            alt4 = 1




                    if alt4 == 1:
                        # grammars/Miranda.g:118:17: body
                        pass 
                        self._state.following.append(self.FOLLOW_body_in_definition699)
                        body8 = self.body()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_body.add(body8.tree)



                    else:
                        break #loop4


                # AST Rewrite
                # elements: ID, pattern, body
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
                    # 119:5: -> ^( DEFINITION ID ( pattern )* ( body )* )
                    # grammars/Miranda.g:119:8: ^( DEFINITION ID ( pattern )* ( body )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    MirandaDefinitionNode(DEFINITION)
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammars/Miranda.g:119:47: ( pattern )*
                    while stream_pattern.hasNext():
                        self._adaptor.addChild(root_1, stream_pattern.nextTree())


                    stream_pattern.reset();

                    # grammars/Miranda.g:119:56: ( body )*
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
    # grammars/Miranda.g:123:1: typedef : ID ( STARS )* TYPE_IS part ( OR part )* -> ^( TYPE ^( ID ( STARS )* ) ( part )* ) ;
    def typedef(self, ):
        retval = self.typedef_return()
        retval.start = self.input.LT(1)

        typedef_StartIndex = self.input.index()

        root_0 = None

        ID9 = None
        STARS10 = None
        TYPE_IS11 = None
        OR13 = None
        part12 = None

        part14 = None


        ID9_tree = None
        STARS10_tree = None
        TYPE_IS11_tree = None
        OR13_tree = None
        stream_STARS = RewriteRuleTokenStream(self._adaptor, "token STARS")
        stream_TYPE_IS = RewriteRuleTokenStream(self._adaptor, "token TYPE_IS")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_OR = RewriteRuleTokenStream(self._adaptor, "token OR")
        stream_part = RewriteRuleSubtreeStream(self._adaptor, "rule part")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:124:3: ( ID ( STARS )* TYPE_IS part ( OR part )* -> ^( TYPE ^( ID ( STARS )* ) ( part )* ) )
                # grammars/Miranda.g:124:5: ID ( STARS )* TYPE_IS part ( OR part )*
                pass 
                ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_typedef735) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID9)


                # grammars/Miranda.g:124:8: ( STARS )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == STARS) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammars/Miranda.g:124:8: STARS
                        pass 
                        STARS10 = self.match(self.input, STARS, self.FOLLOW_STARS_in_typedef737) 
                        if self._state.backtracking == 0:
                            stream_STARS.add(STARS10)



                    else:
                        break #loop5


                TYPE_IS11 = self.match(self.input, TYPE_IS, self.FOLLOW_TYPE_IS_in_typedef740) 
                if self._state.backtracking == 0:
                    stream_TYPE_IS.add(TYPE_IS11)


                self._state.following.append(self.FOLLOW_part_in_typedef742)
                part12 = self.part()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_part.add(part12.tree)


                # grammars/Miranda.g:124:28: ( OR part )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == OR) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammars/Miranda.g:124:29: OR part
                        pass 
                        OR13 = self.match(self.input, OR, self.FOLLOW_OR_in_typedef745) 
                        if self._state.backtracking == 0:
                            stream_OR.add(OR13)


                        self._state.following.append(self.FOLLOW_part_in_typedef747)
                        part14 = self.part()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_part.add(part14.tree)



                    else:
                        break #loop6


                # AST Rewrite
                # elements: part, STARS, ID
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
                    # 125:5: -> ^( TYPE ^( ID ( STARS )* ) ( part )* )
                    # grammars/Miranda.g:125:8: ^( TYPE ^( ID ( STARS )* ) ( part )* )
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

                    # grammars/Miranda.g:125:28: ( part )*
                    while stream_part.hasNext():
                        self._adaptor.addChild(root_1, stream_part.nextTree())


                    stream_part.reset();

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


    class part_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.part_return, self).__init__()

            self.tree = None





    # $ANTLR start "part"
    # grammars/Miranda.g:127:10: fragment part :{...}? ID ( typelist )? -> ^( PART ID ( typelist )? ) ;
    def part(self, ):
        retval = self.part_return()
        retval.start = self.input.LT(1)

        part_StartIndex = self.input.index()

        root_0 = None

        ID15 = None
        typelist16 = None


        ID15_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_typelist = RewriteRuleSubtreeStream(self._adaptor, "rule typelist")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:127:14: ({...}? ID ( typelist )? -> ^( PART ID ( typelist )? ) )
                # grammars/Miranda.g:127:16: {...}? ID ( typelist )?
                pass 
                if not ((self.input.LT(1).text[0].isupper())):
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    raise FailedPredicateException(self.input, "part", "self.input.LT(1).text[0].isupper()")


                ID15 = self.match(self.input, ID, self.FOLLOW_ID_in_part780) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID15)


                # grammars/Miranda.g:127:57: ( typelist )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == CHAR_TYPE or LA7_0 == ID or LA7_0 == LPAREN or LA7_0 == NUM_TYPE or LA7_0 == STARS) :
                    alt7 = 1
                if alt7 == 1:
                    # grammars/Miranda.g:127:57: typelist
                    pass 
                    self._state.following.append(self.FOLLOW_typelist_in_part782)
                    typelist16 = self.typelist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typelist.add(typelist16.tree)





                # AST Rewrite
                # elements: ID, typelist
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
                    # 127:67: -> ^( PART ID ( typelist )? )
                    # grammars/Miranda.g:127:70: ^( PART ID ( typelist )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(PART, "PART")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammars/Miranda.g:127:80: ( typelist )?
                    if stream_typelist.hasNext():
                        self._adaptor.addChild(root_1, stream_typelist.nextTree())


                    stream_typelist.reset();

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
                self.memoize(self.input, 4, part_StartIndex, success)


            pass
        return retval

    # $ANTLR end "part"


    class generic_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.generic_return, self).__init__()

            self.tree = None





    # $ANTLR start "generic"
    # grammars/Miranda.g:128:10: fragment generic : ( LPAREN !)? ID ( STARS )* ( RPAREN !)? ;
    def generic(self, ):
        retval = self.generic_return()
        retval.start = self.input.LT(1)

        generic_StartIndex = self.input.index()

        root_0 = None

        LPAREN17 = None
        ID18 = None
        STARS19 = None
        RPAREN20 = None

        LPAREN17_tree = None
        ID18_tree = None
        STARS19_tree = None
        RPAREN20_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:128:17: ( ( LPAREN !)? ID ( STARS )* ( RPAREN !)? )
                # grammars/Miranda.g:128:19: ( LPAREN !)? ID ( STARS )* ( RPAREN !)?
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:128:25: ( LPAREN !)?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == LPAREN) :
                    alt8 = 1
                if alt8 == 1:
                    # grammars/Miranda.g:128:25: LPAREN !
                    pass 
                    LPAREN17 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_generic802)




                ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_generic806)
                if self._state.backtracking == 0:
                    ID18_tree = self._adaptor.createWithPayload(ID18)
                    self._adaptor.addChild(root_0, ID18_tree)



                # grammars/Miranda.g:128:31: ( STARS )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == STARS) :
                        LA9_2 = self.input.LA(2)

                        if (self.synpred9_Miranda()) :
                            alt9 = 1




                    if alt9 == 1:
                        # grammars/Miranda.g:128:31: STARS
                        pass 
                        STARS19 = self.match(self.input, STARS, self.FOLLOW_STARS_in_generic808)
                        if self._state.backtracking == 0:
                            STARS19_tree = self._adaptor.createWithPayload(STARS19)
                            self._adaptor.addChild(root_0, STARS19_tree)




                    else:
                        break #loop9


                # grammars/Miranda.g:128:44: ( RPAREN !)?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == RPAREN) :
                    alt10 = 1
                if alt10 == 1:
                    # grammars/Miranda.g:128:44: RPAREN !
                    pass 
                    RPAREN20 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_generic811)






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
                self.memoize(self.input, 5, generic_StartIndex, success)


            pass
        return retval

    # $ANTLR end "generic"


    class typelist_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.typelist_return, self).__init__()

            self.tree = None





    # $ANTLR start "typelist"
    # grammars/Miranda.g:129:10: fragment typelist : ( NUM_TYPE | CHAR_TYPE | generic | STARS )+ ;
    def typelist(self, ):
        retval = self.typelist_return()
        retval.start = self.input.LT(1)

        typelist_StartIndex = self.input.index()

        root_0 = None

        NUM_TYPE21 = None
        CHAR_TYPE22 = None
        STARS24 = None
        generic23 = None


        NUM_TYPE21_tree = None
        CHAR_TYPE22_tree = None
        STARS24_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:129:18: ( ( NUM_TYPE | CHAR_TYPE | generic | STARS )+ )
                # grammars/Miranda.g:129:20: ( NUM_TYPE | CHAR_TYPE | generic | STARS )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:129:20: ( NUM_TYPE | CHAR_TYPE | generic | STARS )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 5
                    LA11 = self.input.LA(1)
                    if LA11 == NUM_TYPE:
                        alt11 = 1
                    elif LA11 == CHAR_TYPE:
                        alt11 = 2
                    elif LA11 == ID or LA11 == LPAREN:
                        alt11 = 3
                    elif LA11 == STARS:
                        alt11 = 4

                    if alt11 == 1:
                        # grammars/Miranda.g:129:21: NUM_TYPE
                        pass 
                        NUM_TYPE21 = self.match(self.input, NUM_TYPE, self.FOLLOW_NUM_TYPE_in_typelist822)
                        if self._state.backtracking == 0:
                            NUM_TYPE21_tree = self._adaptor.createWithPayload(NUM_TYPE21)
                            self._adaptor.addChild(root_0, NUM_TYPE21_tree)




                    elif alt11 == 2:
                        # grammars/Miranda.g:129:30: CHAR_TYPE
                        pass 
                        CHAR_TYPE22 = self.match(self.input, CHAR_TYPE, self.FOLLOW_CHAR_TYPE_in_typelist824)
                        if self._state.backtracking == 0:
                            CHAR_TYPE22_tree = self._adaptor.createWithPayload(CHAR_TYPE22)
                            self._adaptor.addChild(root_0, CHAR_TYPE22_tree)




                    elif alt11 == 3:
                        # grammars/Miranda.g:129:40: generic
                        pass 
                        self._state.following.append(self.FOLLOW_generic_in_typelist826)
                        generic23 = self.generic()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, generic23.tree)



                    elif alt11 == 4:
                        # grammars/Miranda.g:129:48: STARS
                        pass 
                        STARS24 = self.match(self.input, STARS, self.FOLLOW_STARS_in_typelist828)
                        if self._state.backtracking == 0:
                            STARS24_tree = self._adaptor.createWithPayload(STARS24)
                            self._adaptor.addChild(root_0, STARS24_tree)




                    else:
                        if cnt11 >= 1:
                            break #loop11

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1




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
                self.memoize(self.input, 6, typelist_StartIndex, success)


            pass
        return retval

    # $ANTLR end "typelist"


    class body_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.body_return, self).__init__()

            self.tree = None





    # $ANTLR start "body"
    # grammars/Miranda.g:133:1: body : IS expression ( guard )? ( where )? -> ^( BODY expression ( guard )? ( where )? ) ;
    def body(self, ):
        retval = self.body_return()
        retval.start = self.input.LT(1)

        body_StartIndex = self.input.index()

        root_0 = None

        IS25 = None
        expression26 = None

        guard27 = None

        where28 = None


        IS25_tree = None
        stream_IS = RewriteRuleTokenStream(self._adaptor, "token IS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_guard = RewriteRuleSubtreeStream(self._adaptor, "rule guard")
        stream_where = RewriteRuleSubtreeStream(self._adaptor, "rule where")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:133:5: ( IS expression ( guard )? ( where )? -> ^( BODY expression ( guard )? ( where )? ) )
                # grammars/Miranda.g:133:7: IS expression ( guard )? ( where )?
                pass 
                IS25 = self.match(self.input, IS, self.FOLLOW_IS_in_body845) 
                if self._state.backtracking == 0:
                    stream_IS.add(IS25)


                self._state.following.append(self.FOLLOW_expression_in_body847)
                expression26 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression26.tree)


                # grammars/Miranda.g:133:21: ( guard )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == COMMA) :
                    alt12 = 1
                if alt12 == 1:
                    # grammars/Miranda.g:133:21: guard
                    pass 
                    self._state.following.append(self.FOLLOW_guard_in_body849)
                    guard27 = self.guard()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_guard.add(guard27.tree)





                # grammars/Miranda.g:133:28: ( where )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == WHERE) :
                    alt13 = 1
                if alt13 == 1:
                    # grammars/Miranda.g:133:28: where
                    pass 
                    self._state.following.append(self.FOLLOW_where_in_body852)
                    where28 = self.where()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_where.add(where28.tree)





                # AST Rewrite
                # elements: guard, expression, where
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
                    # 134:7: -> ^( BODY expression ( guard )? ( where )? )
                    # grammars/Miranda.g:134:10: ^( BODY expression ( guard )? ( where )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(BODY, "BODY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    # grammars/Miranda.g:134:28: ( guard )?
                    if stream_guard.hasNext():
                        self._adaptor.addChild(root_1, stream_guard.nextTree())


                    stream_guard.reset();

                    # grammars/Miranda.g:134:35: ( where )?
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
                self.memoize(self.input, 7, body_StartIndex, success)


            pass
        return retval

    # $ANTLR end "body"


    class guard_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.guard_return, self).__init__()

            self.tree = None





    # $ANTLR start "guard"
    # grammars/Miranda.g:137:1: guard : COMMA ( expression | OTHERWISE ) ;
    def guard(self, ):
        retval = self.guard_return()
        retval.start = self.input.LT(1)

        guard_StartIndex = self.input.index()

        root_0 = None

        COMMA29 = None
        OTHERWISE31 = None
        expression30 = None


        COMMA29_tree = None
        OTHERWISE31_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:137:6: ( COMMA ( expression | OTHERWISE ) )
                # grammars/Miranda.g:137:8: COMMA ( expression | OTHERWISE )
                pass 
                root_0 = self._adaptor.nil()


                COMMA29 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_guard881)
                if self._state.backtracking == 0:
                    COMMA29_tree = self._adaptor.createWithPayload(COMMA29)
                    self._adaptor.addChild(root_0, COMMA29_tree)



                # grammars/Miranda.g:137:14: ( expression | OTHERWISE )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == CHAR or (FALSE <= LA14_0 <= FLOAT) or LA14_0 == ID or LA14_0 == INT or LA14_0 == LBRACKET or LA14_0 == LPAREN or LA14_0 == NOT or LA14_0 == STRING or LA14_0 == TRUE) :
                    alt14 = 1
                elif (LA14_0 == OTHERWISE) :
                    alt14 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammars/Miranda.g:137:15: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_guard884)
                    expression30 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression30.tree)



                elif alt14 == 2:
                    # grammars/Miranda.g:137:26: OTHERWISE
                    pass 
                    OTHERWISE31 = self.match(self.input, OTHERWISE, self.FOLLOW_OTHERWISE_in_guard886)
                    if self._state.backtracking == 0:
                        OTHERWISE31_tree = self._adaptor.createWithPayload(OTHERWISE31)
                        self._adaptor.addChild(root_0, OTHERWISE31_tree)








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
                self.memoize(self.input, 8, guard_StartIndex, success)


            pass
        return retval

    # $ANTLR end "guard"


    class where_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.where_return, self).__init__()

            self.tree = None





    # $ANTLR start "where"
    # grammars/Miranda.g:139:1: where : WHERE definition ( DEDENT ! definition )* ;
    def where(self, ):
        retval = self.where_return()
        retval.start = self.input.LT(1)

        where_StartIndex = self.input.index()

        root_0 = None

        WHERE32 = None
        DEDENT34 = None
        definition33 = None

        definition35 = None


        WHERE32_tree = None
        DEDENT34_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:139:6: ( WHERE definition ( DEDENT ! definition )* )
                # grammars/Miranda.g:139:8: WHERE definition ( DEDENT ! definition )*
                pass 
                root_0 = self._adaptor.nil()


                WHERE32 = self.match(self.input, WHERE, self.FOLLOW_WHERE_in_where894)
                if self._state.backtracking == 0:
                    WHERE32_tree = self._adaptor.createWithPayload(WHERE32)
                    self._adaptor.addChild(root_0, WHERE32_tree)



                self._state.following.append(self.FOLLOW_definition_in_where896)
                definition33 = self.definition()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, definition33.tree)


                # grammars/Miranda.g:139:25: ( DEDENT ! definition )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == DEDENT) :
                        LA15_1 = self.input.LA(2)

                        if (self.synpred18_Miranda()) :
                            alt15 = 1




                    if alt15 == 1:
                        # grammars/Miranda.g:139:26: DEDENT ! definition
                        pass 
                        DEDENT34 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_where899)

                        self._state.following.append(self.FOLLOW_definition_in_where902)
                        definition35 = self.definition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, definition35.tree)



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
                self.memoize(self.input, 9, where_StartIndex, success)


            pass
        return retval

    # $ANTLR end "where"


    class pattern_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.pattern_return, self).__init__()

            self.tree = None





    # $ANTLR start "pattern"
    # grammars/Miranda.g:141:1: pattern : basic ( ( COLON | ADD ) ^ pattern )? ;
    def pattern(self, ):
        retval = self.pattern_return()
        retval.start = self.input.LT(1)

        pattern_StartIndex = self.input.index()

        root_0 = None

        set37 = None
        basic36 = None

        pattern38 = None


        set37_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:142:3: ( basic ( ( COLON | ADD ) ^ pattern )? )
                # grammars/Miranda.g:142:5: basic ( ( COLON | ADD ) ^ pattern )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_basic_in_pattern915)
                basic36 = self.basic()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, basic36.tree)


                # grammars/Miranda.g:142:11: ( ( COLON | ADD ) ^ pattern )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == ADD or LA16_0 == COLON) :
                    alt16 = 1
                if alt16 == 1:
                    # grammars/Miranda.g:142:12: ( COLON | ADD ) ^ pattern
                    pass 
                    set37 = self.input.LT(1)

                    set37 = self.input.LT(1)

                    if self.input.LA(1) == ADD or self.input.LA(1) == COLON:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set37), root_0)

                        self._state.errorRecovery = False


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        raise mse



                    self._state.following.append(self.FOLLOW_pattern_in_pattern925)
                    pattern38 = self.pattern()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pattern38.tree)







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
                self.memoize(self.input, 10, pattern_StartIndex, success)


            pass
        return retval

    # $ANTLR end "pattern"


    class basic_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.basic_return, self).__init__()

            self.tree = None





    # $ANTLR start "basic"
    # grammars/Miranda.g:145:1: basic : ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! ( pattern )* RPAREN !);
    def basic(self, ):
        retval = self.basic_return()
        retval.start = self.input.LT(1)

        basic_StartIndex = self.input.index()

        root_0 = None

        ID39 = None
        INT40 = None
        FLOAT41 = None
        LPAREN45 = None
        RPAREN47 = None
        boolean42 = None

        list43 = None

        tuple44 = None

        pattern46 = None


        ID39_tree = None
        INT40_tree = None
        FLOAT41_tree = None
        LPAREN45_tree = None
        RPAREN47_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:146:3: ( ID | INT | FLOAT | boolean | list | tuple | LPAREN ! ( pattern )* RPAREN !)
                alt18 = 7
                LA18 = self.input.LA(1)
                if LA18 == ID:
                    alt18 = 1
                elif LA18 == INT:
                    alt18 = 2
                elif LA18 == FLOAT:
                    alt18 = 3
                elif LA18 == FALSE or LA18 == TRUE:
                    alt18 = 4
                elif LA18 == LBRACKET:
                    alt18 = 5
                elif LA18 == LPAREN:
                    LA18_6 = self.input.LA(2)

                    if (self.synpred26_Miranda()) :
                        alt18 = 6
                    elif (True) :
                        alt18 = 7
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 18, 6, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammars/Miranda.g:146:5: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_basic940)
                    if self._state.backtracking == 0:
                        ID39_tree = self._adaptor.createWithPayload(ID39)
                        self._adaptor.addChild(root_0, ID39_tree)




                elif alt18 == 2:
                    # grammars/Miranda.g:147:5: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT40 = self.match(self.input, INT, self.FOLLOW_INT_in_basic946)
                    if self._state.backtracking == 0:
                        INT40_tree = self._adaptor.createWithPayload(INT40)
                        self._adaptor.addChild(root_0, INT40_tree)




                elif alt18 == 3:
                    # grammars/Miranda.g:148:5: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()


                    FLOAT41 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_basic952)
                    if self._state.backtracking == 0:
                        FLOAT41_tree = self._adaptor.createWithPayload(FLOAT41)
                        self._adaptor.addChild(root_0, FLOAT41_tree)




                elif alt18 == 4:
                    # grammars/Miranda.g:149:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_basic958)
                    boolean42 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean42.tree)



                elif alt18 == 5:
                    # grammars/Miranda.g:150:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_basic964)
                    list43 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list43.tree)



                elif alt18 == 6:
                    # grammars/Miranda.g:151:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_basic970)
                    tuple44 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple44.tree)



                elif alt18 == 7:
                    # grammars/Miranda.g:152:5: LPAREN ! ( pattern )* RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN45 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_basic976)

                    # grammars/Miranda.g:152:13: ( pattern )*
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if ((FALSE <= LA17_0 <= FLOAT) or LA17_0 == ID or LA17_0 == INT or LA17_0 == LBRACKET or LA17_0 == LPAREN or LA17_0 == TRUE) :
                            alt17 = 1


                        if alt17 == 1:
                            # grammars/Miranda.g:152:13: pattern
                            pass 
                            self._state.following.append(self.FOLLOW_pattern_in_basic979)
                            pattern46 = self.pattern()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, pattern46.tree)



                        else:
                            break #loop17


                    RPAREN47 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_basic982)


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
                self.memoize(self.input, 11, basic_StartIndex, success)


            pass
        return retval

    # $ANTLR end "basic"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # grammars/Miranda.g:155:1: expression : expr0 ;
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        expr048 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:155:11: ( expr0 )
                # grammars/Miranda.g:155:13: expr0
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr0_in_expression991)
                expr048 = self.expr0()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr048.tree)




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
                self.memoize(self.input, 12, expression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expression"


    class expr0_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr0_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr0"
    # grammars/Miranda.g:157:1: expr0 : expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? ;
    def expr0(self, ):
        retval = self.expr0_return()
        retval.start = self.input.LT(1)

        expr0_StartIndex = self.input.index()

        root_0 = None

        CONCAT50 = None
        SUBTRACT51 = None
        COLON52 = None
        expr149 = None

        expr053 = None


        CONCAT50_tree = None
        SUBTRACT51_tree = None
        COLON52_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:157:6: ( expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )? )
                # grammars/Miranda.g:157:8: expr1 ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr1_in_expr0998)
                expr149 = self.expr1()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr149.tree)


                # grammars/Miranda.g:157:14: ( ( CONCAT ^| SUBTRACT ^| COLON ^) expr0 )?
                alt20 = 2
                LA20 = self.input.LA(1)
                if LA20 == CONCAT:
                    LA20_1 = self.input.LA(2)

                    if (self.synpred30_Miranda()) :
                        alt20 = 1
                elif LA20 == SUBTRACT:
                    LA20_2 = self.input.LA(2)

                    if (self.synpred30_Miranda()) :
                        alt20 = 1
                elif LA20 == COLON:
                    LA20_3 = self.input.LA(2)

                    if (self.synpred30_Miranda()) :
                        alt20 = 1
                if alt20 == 1:
                    # grammars/Miranda.g:157:15: ( CONCAT ^| SUBTRACT ^| COLON ^) expr0
                    pass 
                    # grammars/Miranda.g:157:15: ( CONCAT ^| SUBTRACT ^| COLON ^)
                    alt19 = 3
                    LA19 = self.input.LA(1)
                    if LA19 == CONCAT:
                        alt19 = 1
                    elif LA19 == SUBTRACT:
                        alt19 = 2
                    elif LA19 == COLON:
                        alt19 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 19, 0, self.input)

                        raise nvae


                    if alt19 == 1:
                        # grammars/Miranda.g:157:16: CONCAT ^
                        pass 
                        CONCAT50 = self.match(self.input, CONCAT, self.FOLLOW_CONCAT_in_expr01002)
                        if self._state.backtracking == 0:
                            CONCAT50_tree = ConcatNode(CONCAT50) 
                            root_0 = self._adaptor.becomeRoot(CONCAT50_tree, root_0)




                    elif alt19 == 2:
                        # grammars/Miranda.g:157:36: SUBTRACT ^
                        pass 
                        SUBTRACT51 = self.match(self.input, SUBTRACT, self.FOLLOW_SUBTRACT_in_expr01008)
                        if self._state.backtracking == 0:
                            SUBTRACT51_tree = SubtractNode(SUBTRACT51) 
                            root_0 = self._adaptor.becomeRoot(SUBTRACT51_tree, root_0)




                    elif alt19 == 3:
                        # grammars/Miranda.g:157:60: COLON ^
                        pass 
                        COLON52 = self.match(self.input, COLON, self.FOLLOW_COLON_in_expr01014)
                        if self._state.backtracking == 0:
                            COLON52_tree = ColonNode(COLON52) 
                            root_0 = self._adaptor.becomeRoot(COLON52_tree, root_0)






                    self._state.following.append(self.FOLLOW_expr0_in_expr01021)
                    expr053 = self.expr0()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr053.tree)







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
                self.memoize(self.input, 13, expr0_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr0"


    class expr1_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr1_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr1"
    # grammars/Miranda.g:159:1: expr1 : expr2 ( OR ^ expression )* ;
    def expr1(self, ):
        retval = self.expr1_return()
        retval.start = self.input.LT(1)

        expr1_StartIndex = self.input.index()

        root_0 = None

        OR55 = None
        expr254 = None

        expression56 = None


        OR55_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:159:6: ( expr2 ( OR ^ expression )* )
                # grammars/Miranda.g:159:8: expr2 ( OR ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr2_in_expr11030)
                expr254 = self.expr2()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr254.tree)


                # grammars/Miranda.g:159:14: ( OR ^ expression )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == OR) :
                        LA21_2 = self.input.LA(2)

                        if (self.synpred31_Miranda()) :
                            alt21 = 1




                    if alt21 == 1:
                        # grammars/Miranda.g:159:15: OR ^ expression
                        pass 
                        OR55 = self.match(self.input, OR, self.FOLLOW_OR_in_expr11033)
                        if self._state.backtracking == 0:
                            OR55_tree = OrNode(OR55) 
                            root_0 = self._adaptor.becomeRoot(OR55_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr11039)
                        expression56 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression56.tree)



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
                self.memoize(self.input, 14, expr1_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr1"


    class expr2_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr2_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr2"
    # grammars/Miranda.g:161:1: expr2 : expr3 ( AND ^ expression )* ;
    def expr2(self, ):
        retval = self.expr2_return()
        retval.start = self.input.LT(1)

        expr2_StartIndex = self.input.index()

        root_0 = None

        AND58 = None
        expr357 = None

        expression59 = None


        AND58_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:161:6: ( expr3 ( AND ^ expression )* )
                # grammars/Miranda.g:161:8: expr3 ( AND ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr3_in_expr21048)
                expr357 = self.expr3()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr357.tree)


                # grammars/Miranda.g:161:14: ( AND ^ expression )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == AND) :
                        LA22_2 = self.input.LA(2)

                        if (self.synpred32_Miranda()) :
                            alt22 = 1




                    if alt22 == 1:
                        # grammars/Miranda.g:161:15: AND ^ expression
                        pass 
                        AND58 = self.match(self.input, AND, self.FOLLOW_AND_in_expr21051)
                        if self._state.backtracking == 0:
                            AND58_tree = AndNode(AND58) 
                            root_0 = self._adaptor.becomeRoot(AND58_tree, root_0)



                        self._state.following.append(self.FOLLOW_expression_in_expr21057)
                        expression59 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression59.tree)



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
                self.memoize(self.input, 15, expr2_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr2"


    class expr3_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr3_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr3"
    # grammars/Miranda.g:163:1: expr3 : expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* ;
    def expr3(self, ):
        retval = self.expr3_return()
        retval.start = self.input.LT(1)

        expr3_StartIndex = self.input.index()

        root_0 = None

        set61 = None
        expr460 = None

        expression62 = None


        set61_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:163:6: ( expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )* )
                # grammars/Miranda.g:163:8: expr4 ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr4_in_expr31066)
                expr460 = self.expr4()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr460.tree)


                # grammars/Miranda.g:163:14: ( ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression )*
                while True: #loop23
                    alt23 = 2
                    LA23 = self.input.LA(1)
                    if LA23 == LT:
                        LA23_2 = self.input.LA(2)

                        if (self.synpred38_Miranda()) :
                            alt23 = 1


                    elif LA23 == LTE:
                        LA23_3 = self.input.LA(2)

                        if (self.synpred38_Miranda()) :
                            alt23 = 1


                    elif LA23 == EQ:
                        LA23_4 = self.input.LA(2)

                        if (self.synpred38_Miranda()) :
                            alt23 = 1


                    elif LA23 == NEQ:
                        LA23_5 = self.input.LA(2)

                        if (self.synpred38_Miranda()) :
                            alt23 = 1


                    elif LA23 == GTE:
                        LA23_6 = self.input.LA(2)

                        if (self.synpred38_Miranda()) :
                            alt23 = 1


                    elif LA23 == GT:
                        LA23_7 = self.input.LA(2)

                        if (self.synpred38_Miranda()) :
                            alt23 = 1



                    if alt23 == 1:
                        # grammars/Miranda.g:163:15: ( LT | LTE | EQ | NEQ | GTE | GT ) ^ expression
                        pass 
                        set61 = self.input.LT(1)

                        set61 = self.input.LT(1)

                        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set61), root_0)

                            self._state.errorRecovery = False


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        self._state.following.append(self.FOLLOW_expression_in_expr31084)
                        expression62 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression62.tree)



                    else:
                        break #loop23




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
                self.memoize(self.input, 16, expr3_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr3"


    class expr4_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr4_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr4"
    # grammars/Miranda.g:165:1: expr4 : expr5 ( ( ADD ^| MIN ^) expression )* ;
    def expr4(self, ):
        retval = self.expr4_return()
        retval.start = self.input.LT(1)

        expr4_StartIndex = self.input.index()

        root_0 = None

        ADD64 = None
        MIN65 = None
        expr563 = None

        expression66 = None


        ADD64_tree = None
        MIN65_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:165:6: ( expr5 ( ( ADD ^| MIN ^) expression )* )
                # grammars/Miranda.g:165:8: expr5 ( ( ADD ^| MIN ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr5_in_expr41093)
                expr563 = self.expr5()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr563.tree)


                # grammars/Miranda.g:165:14: ( ( ADD ^| MIN ^) expression )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ADD) :
                        LA25_2 = self.input.LA(2)

                        if (self.synpred40_Miranda()) :
                            alt25 = 1


                    elif (LA25_0 == MIN) :
                        LA25_3 = self.input.LA(2)

                        if (self.synpred40_Miranda()) :
                            alt25 = 1




                    if alt25 == 1:
                        # grammars/Miranda.g:165:15: ( ADD ^| MIN ^) expression
                        pass 
                        # grammars/Miranda.g:165:15: ( ADD ^| MIN ^)
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == ADD) :
                            alt24 = 1
                        elif (LA24_0 == MIN) :
                            alt24 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 24, 0, self.input)

                            raise nvae


                        if alt24 == 1:
                            # grammars/Miranda.g:165:16: ADD ^
                            pass 
                            ADD64 = self.match(self.input, ADD, self.FOLLOW_ADD_in_expr41097)
                            if self._state.backtracking == 0:
                                ADD64_tree = AddNode(ADD64) 
                                root_0 = self._adaptor.becomeRoot(ADD64_tree, root_0)




                        elif alt24 == 2:
                            # grammars/Miranda.g:165:30: MIN ^
                            pass 
                            MIN65 = self.match(self.input, MIN, self.FOLLOW_MIN_in_expr41103)
                            if self._state.backtracking == 0:
                                MIN65_tree = MinNode(MIN65) 
                                root_0 = self._adaptor.becomeRoot(MIN65_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr41110)
                        expression66 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression66.tree)



                    else:
                        break #loop25




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
                self.memoize(self.input, 17, expr4_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr4"


    class expr5_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr5_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr5"
    # grammars/Miranda.g:167:1: expr5 : expr6 ( ( DIV ^|{...}? STARS ^) expression )* ;
    def expr5(self, ):
        retval = self.expr5_return()
        retval.start = self.input.LT(1)

        expr5_StartIndex = self.input.index()

        root_0 = None

        DIV68 = None
        STARS69 = None
        expr667 = None

        expression70 = None


        DIV68_tree = None
        STARS69_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:167:6: ( expr6 ( ( DIV ^|{...}? STARS ^) expression )* )
                # grammars/Miranda.g:167:8: expr6 ( ( DIV ^|{...}? STARS ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr6_in_expr51119)
                expr667 = self.expr6()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr667.tree)


                # grammars/Miranda.g:167:14: ( ( DIV ^|{...}? STARS ^) expression )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == DIV) :
                        LA27_2 = self.input.LA(2)

                        if (self.synpred42_Miranda()) :
                            alt27 = 1


                    elif (LA27_0 == STARS) :
                        LA27_3 = self.input.LA(2)

                        if ((((((len(self.input.LT(1).text) == 1)) and ((len(self.input.LT(1).text) == 1)))) and (self.synpred42_Miranda()))) :
                            alt27 = 1




                    if alt27 == 1:
                        # grammars/Miranda.g:167:15: ( DIV ^|{...}? STARS ^) expression
                        pass 
                        # grammars/Miranda.g:167:15: ( DIV ^|{...}? STARS ^)
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == DIV) :
                            alt26 = 1
                        elif (LA26_0 == STARS) :
                            alt26 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 26, 0, self.input)

                            raise nvae


                        if alt26 == 1:
                            # grammars/Miranda.g:167:16: DIV ^
                            pass 
                            DIV68 = self.match(self.input, DIV, self.FOLLOW_DIV_in_expr51123)
                            if self._state.backtracking == 0:
                                DIV68_tree = DivNode(DIV68) 
                                root_0 = self._adaptor.becomeRoot(DIV68_tree, root_0)




                        elif alt26 == 2:
                            # grammars/Miranda.g:167:31: {...}? STARS ^
                            pass 
                            if not ((len(self.input.LT(1).text) == 1)):
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                raise FailedPredicateException(self.input, "expr5", "len(self.input.LT(1).text) == 1")


                            STARS69 = self.match(self.input, STARS, self.FOLLOW_STARS_in_expr51132)
                            if self._state.backtracking == 0:
                                STARS69_tree = MulNode(STARS69) 
                                root_0 = self._adaptor.becomeRoot(STARS69_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr51139)
                        expression70 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression70.tree)



                    else:
                        break #loop27




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
                self.memoize(self.input, 18, expr5_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr5"


    class expr6_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr6_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr6"
    # grammars/Miranda.g:169:1: expr6 : expr7 ( ( IDIV ^| MOD ^) expression )* ;
    def expr6(self, ):
        retval = self.expr6_return()
        retval.start = self.input.LT(1)

        expr6_StartIndex = self.input.index()

        root_0 = None

        IDIV72 = None
        MOD73 = None
        expr771 = None

        expression74 = None


        IDIV72_tree = None
        MOD73_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:169:6: ( expr7 ( ( IDIV ^| MOD ^) expression )* )
                # grammars/Miranda.g:169:8: expr7 ( ( IDIV ^| MOD ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr7_in_expr61148)
                expr771 = self.expr7()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr771.tree)


                # grammars/Miranda.g:169:14: ( ( IDIV ^| MOD ^) expression )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == IDIV) :
                        LA29_2 = self.input.LA(2)

                        if (self.synpred44_Miranda()) :
                            alt29 = 1


                    elif (LA29_0 == MOD) :
                        LA29_3 = self.input.LA(2)

                        if (self.synpred44_Miranda()) :
                            alt29 = 1




                    if alt29 == 1:
                        # grammars/Miranda.g:169:15: ( IDIV ^| MOD ^) expression
                        pass 
                        # grammars/Miranda.g:169:15: ( IDIV ^| MOD ^)
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == IDIV) :
                            alt28 = 1
                        elif (LA28_0 == MOD) :
                            alt28 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 28, 0, self.input)

                            raise nvae


                        if alt28 == 1:
                            # grammars/Miranda.g:169:16: IDIV ^
                            pass 
                            IDIV72 = self.match(self.input, IDIV, self.FOLLOW_IDIV_in_expr61152)
                            if self._state.backtracking == 0:
                                IDIV72_tree = self._adaptor.createWithPayload(IDIV72)
                                root_0 = self._adaptor.becomeRoot(IDIV72_tree, root_0)




                        elif alt28 == 2:
                            # grammars/Miranda.g:169:22: MOD ^
                            pass 
                            MOD73 = self.match(self.input, MOD, self.FOLLOW_MOD_in_expr61155)
                            if self._state.backtracking == 0:
                                MOD73_tree = self._adaptor.createWithPayload(MOD73)
                                root_0 = self._adaptor.becomeRoot(MOD73_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr61159)
                        expression74 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression74.tree)



                    else:
                        break #loop29




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
                self.memoize(self.input, 19, expr6_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr6"


    class expr7_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr7_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr7"
    # grammars/Miranda.g:171:1: expr7 : expr8 ( ( EXP ^) expression )* ;
    def expr7(self, ):
        retval = self.expr7_return()
        retval.start = self.input.LT(1)

        expr7_StartIndex = self.input.index()

        root_0 = None

        EXP76 = None
        expr875 = None

        expression77 = None


        EXP76_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:171:6: ( expr8 ( ( EXP ^) expression )* )
                # grammars/Miranda.g:171:8: expr8 ( ( EXP ^) expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr8_in_expr71168)
                expr875 = self.expr8()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr875.tree)


                # grammars/Miranda.g:171:14: ( ( EXP ^) expression )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == EXP) :
                        LA30_2 = self.input.LA(2)

                        if (self.synpred45_Miranda()) :
                            alt30 = 1




                    if alt30 == 1:
                        # grammars/Miranda.g:171:15: ( EXP ^) expression
                        pass 
                        # grammars/Miranda.g:171:15: ( EXP ^)
                        # grammars/Miranda.g:171:16: EXP ^
                        pass 
                        EXP76 = self.match(self.input, EXP, self.FOLLOW_EXP_in_expr71172)
                        if self._state.backtracking == 0:
                            EXP76_tree = self._adaptor.createWithPayload(EXP76)
                            root_0 = self._adaptor.becomeRoot(EXP76_tree, root_0)






                        self._state.following.append(self.FOLLOW_expression_in_expr71176)
                        expression77 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression77.tree)



                    else:
                        break #loop30




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
                self.memoize(self.input, 20, expr7_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr7"


    class expr8_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.expr8_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr8"
    # grammars/Miranda.g:173:1: expr8 : ( aexpr )+ ;
    def expr8(self, ):
        retval = self.expr8_return()
        retval.start = self.input.LT(1)

        expr8_StartIndex = self.input.index()

        root_0 = None

        aexpr78 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:173:6: ( ( aexpr )+ )
                # grammars/Miranda.g:173:8: ( aexpr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammars/Miranda.g:173:8: ( aexpr )+
                cnt31 = 0
                while True: #loop31
                    alt31 = 2
                    LA31 = self.input.LA(1)
                    if LA31 == ID:
                        LA31_19 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == INT:
                        LA31_20 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == FLOAT:
                        LA31_21 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == CHAR:
                        LA31_22 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == STRING:
                        LA31_23 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == NOT:
                        LA31_24 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == FALSE or LA31 == TRUE:
                        LA31_25 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == LPAREN:
                        LA31_26 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1


                    elif LA31 == LBRACKET:
                        LA31_27 = self.input.LA(2)

                        if (self.synpred46_Miranda()) :
                            alt31 = 1



                    if alt31 == 1:
                        # grammars/Miranda.g:173:8: aexpr
                        pass 
                        self._state.following.append(self.FOLLOW_aexpr_in_expr81185)
                        aexpr78 = self.aexpr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, aexpr78.tree)



                    else:
                        if cnt31 >= 1:
                            break #loop31

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(31, self.input)
                        raise eee

                    cnt31 += 1


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
                self.memoize(self.input, 21, expr8_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expr8"


    class aexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.aexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "aexpr"
    # grammars/Miranda.g:179:1: aexpr : ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !);
    def aexpr(self, ):
        retval = self.aexpr_return()
        retval.start = self.input.LT(1)

        aexpr_StartIndex = self.input.index()

        root_0 = None

        ID79 = None
        INT80 = None
        FLOAT81 = None
        CHAR82 = None
        STRING83 = None
        NOT84 = None
        LPAREN90 = None
        RPAREN92 = None
        expression85 = None

        boolean86 = None

        section87 = None

        tuple88 = None

        list89 = None

        expression91 = None


        ID79_tree = None
        INT80_tree = None
        FLOAT81_tree = None
        CHAR82_tree = None
        STRING83_tree = None
        NOT84_tree = None
        LPAREN90_tree = None
        RPAREN92_tree = None
        stream_CHAR = RewriteRuleTokenStream(self._adaptor, "token CHAR")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:180:3: ( ID -> ^( ID ) | INT -> ^( INT ) | FLOAT -> ^( FLOAT ) | CHAR -> ^( CHAR ) | STRING | NOT expression | boolean | section | tuple | list | LPAREN ! expression RPAREN !)
                alt32 = 11
                LA32 = self.input.LA(1)
                if LA32 == ID:
                    alt32 = 1
                elif LA32 == INT:
                    alt32 = 2
                elif LA32 == FLOAT:
                    alt32 = 3
                elif LA32 == CHAR:
                    alt32 = 4
                elif LA32 == STRING:
                    alt32 = 5
                elif LA32 == NOT:
                    alt32 = 6
                elif LA32 == FALSE or LA32 == TRUE:
                    alt32 = 7
                elif LA32 == LPAREN:
                    LA32_8 = self.input.LA(2)

                    if (self.synpred54_Miranda()) :
                        alt32 = 8
                    elif (self.synpred55_Miranda()) :
                        alt32 = 9
                    elif (True) :
                        alt32 = 11
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 32, 8, self.input)

                        raise nvae


                elif LA32 == LBRACKET:
                    alt32 = 10
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # grammars/Miranda.g:180:5: ID
                    pass 
                    ID79 = self.match(self.input, ID, self.FOLLOW_ID_in_aexpr1198) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID79)


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
                        # 181:5: -> ^( ID )
                        # grammars/Miranda.g:181:8: ^( ID )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IdentifierNode(stream_ID.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt32 == 2:
                    # grammars/Miranda.g:182:5: INT
                    pass 
                    INT80 = self.match(self.input, INT, self.FOLLOW_INT_in_aexpr1217) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT80)


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
                        # 183:5: -> ^( INT )
                        # grammars/Miranda.g:183:8: ^( INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        IntNode(stream_INT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt32 == 3:
                    # grammars/Miranda.g:184:5: FLOAT
                    pass 
                    FLOAT81 = self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_aexpr1236) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT81)


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
                        # 185:5: -> ^( FLOAT )
                        # grammars/Miranda.g:185:8: ^( FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        FloatNode(stream_FLOAT.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt32 == 4:
                    # grammars/Miranda.g:186:5: CHAR
                    pass 
                    CHAR82 = self.match(self.input, CHAR, self.FOLLOW_CHAR_in_aexpr1255) 
                    if self._state.backtracking == 0:
                        stream_CHAR.add(CHAR82)


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
                        # 187:5: -> ^( CHAR )
                        # grammars/Miranda.g:187:8: ^( CHAR )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        CharNode(stream_CHAR.nextToken())
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt32 == 5:
                    # grammars/Miranda.g:188:5: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING83 = self.match(self.input, STRING, self.FOLLOW_STRING_in_aexpr1274)
                    if self._state.backtracking == 0:
                        STRING83_tree = self._adaptor.createWithPayload(STRING83)
                        self._adaptor.addChild(root_0, STRING83_tree)




                elif alt32 == 6:
                    # grammars/Miranda.g:189:5: NOT expression
                    pass 
                    root_0 = self._adaptor.nil()


                    NOT84 = self.match(self.input, NOT, self.FOLLOW_NOT_in_aexpr1280)
                    if self._state.backtracking == 0:
                        NOT84_tree = self._adaptor.createWithPayload(NOT84)
                        self._adaptor.addChild(root_0, NOT84_tree)



                    self._state.following.append(self.FOLLOW_expression_in_aexpr1282)
                    expression85 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression85.tree)



                elif alt32 == 7:
                    # grammars/Miranda.g:190:5: boolean
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_boolean_in_aexpr1288)
                    boolean86 = self.boolean()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean86.tree)



                elif alt32 == 8:
                    # grammars/Miranda.g:191:5: section
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_section_in_aexpr1294)
                    section87 = self.section()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, section87.tree)



                elif alt32 == 9:
                    # grammars/Miranda.g:192:5: tuple
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_tuple_in_aexpr1300)
                    tuple88 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple88.tree)



                elif alt32 == 10:
                    # grammars/Miranda.g:193:5: list
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_in_aexpr1306)
                    list89 = self.list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list89.tree)



                elif alt32 == 11:
                    # grammars/Miranda.g:194:5: LPAREN ! expression RPAREN !
                    pass 
                    root_0 = self._adaptor.nil()


                    LPAREN90 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_aexpr1312)

                    self._state.following.append(self.FOLLOW_expression_in_aexpr1315)
                    expression91 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression91.tree)


                    RPAREN92 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_aexpr1317)


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
                self.memoize(self.input, 22, aexpr_StartIndex, success)


            pass
        return retval

    # $ANTLR end "aexpr"


    class tuple_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.tuple_return, self).__init__()

            self.tree = None





    # $ANTLR start "tuple"
    # grammars/Miranda.g:197:1: tuple : LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) ;
    def tuple(self, ):
        retval = self.tuple_return()
        retval.start = self.input.LT(1)

        tuple_StartIndex = self.input.index()

        root_0 = None

        LPAREN93 = None
        COMMA95 = None
        RPAREN97 = None
        expression94 = None

        expression96 = None


        LPAREN93_tree = None
        COMMA95_tree = None
        RPAREN97_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:197:6: ( LPAREN expression ( COMMA expression )+ RPAREN -> ^( TUPLE ( expression )* ) )
                # grammars/Miranda.g:197:8: LPAREN expression ( COMMA expression )+ RPAREN
                pass 
                LPAREN93 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_tuple1326) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN93)


                self._state.following.append(self.FOLLOW_expression_in_tuple1328)
                expression94 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression94.tree)


                # grammars/Miranda.g:197:26: ( COMMA expression )+
                cnt33 = 0
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == COMMA) :
                        alt33 = 1


                    if alt33 == 1:
                        # grammars/Miranda.g:197:27: COMMA expression
                        pass 
                        COMMA95 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_tuple1331) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA95)


                        self._state.following.append(self.FOLLOW_expression_in_tuple1333)
                        expression96 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression96.tree)



                    else:
                        if cnt33 >= 1:
                            break #loop33

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(33, self.input)
                        raise eee

                    cnt33 += 1


                RPAREN97 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_tuple1337) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN97)


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
                    # 198:8: -> ^( TUPLE ( expression )* )
                    # grammars/Miranda.g:198:11: ^( TUPLE ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TUPLE, "TUPLE")
                    , root_1)

                    # grammars/Miranda.g:198:19: ( expression )*
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
                self.memoize(self.input, 23, tuple_StartIndex, success)


            pass
        return retval

    # $ANTLR end "tuple"


    class list_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.list_return, self).__init__()

            self.tree = None





    # $ANTLR start "list"
    # grammars/Miranda.g:201:1: list : LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) ;
    def list(self, ):
        retval = self.list_return()
        retval.start = self.input.LT(1)

        list_StartIndex = self.input.index()

        root_0 = None

        LBRACKET98 = None
        COMMA100 = None
        RBRACKET102 = None
        expression99 = None

        expression101 = None


        LBRACKET98_tree = None
        COMMA100_tree = None
        RBRACKET102_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:201:5: ( LBRACKET ( expression )? ( COMMA expression )* RBRACKET -> ^( LIST ( expression )* ) )
                # grammars/Miranda.g:201:7: LBRACKET ( expression )? ( COMMA expression )* RBRACKET
                pass 
                LBRACKET98 = self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_list1361) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET98)


                # grammars/Miranda.g:201:16: ( expression )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == CHAR or (FALSE <= LA34_0 <= FLOAT) or LA34_0 == ID or LA34_0 == INT or LA34_0 == LBRACKET or LA34_0 == LPAREN or LA34_0 == NOT or LA34_0 == STRING or LA34_0 == TRUE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammars/Miranda.g:201:16: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_list1363)
                    expression99 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression99.tree)





                # grammars/Miranda.g:201:28: ( COMMA expression )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == COMMA) :
                        alt35 = 1


                    if alt35 == 1:
                        # grammars/Miranda.g:201:29: COMMA expression
                        pass 
                        COMMA100 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_list1367) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA100)


                        self._state.following.append(self.FOLLOW_expression_in_list1369)
                        expression101 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression101.tree)



                    else:
                        break #loop35


                RBRACKET102 = self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_list1373) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET102)


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
                    # 202:7: -> ^( LIST ( expression )* )
                    # grammars/Miranda.g:202:10: ^( LIST ( expression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # grammars/Miranda.g:202:17: ( expression )*
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
                self.memoize(self.input, 24, list_StartIndex, success)


            pass
        return retval

    # $ANTLR end "list"


    class section_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.section_return, self).__init__()

            self.tree = None





    # $ANTLR start "section"
    # grammars/Miranda.g:205:1: section : ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) );
    def section(self, ):
        retval = self.section_return()
        retval.start = self.input.LT(1)

        section_StartIndex = self.input.index()

        root_0 = None

        LPAREN103 = None
        RPAREN105 = None
        LPAREN106 = None
        RPAREN109 = None
        LPAREN110 = None
        RPAREN113 = None
        operator104 = None

        operator107 = None

        expression108 = None

        expression111 = None

        operator112 = None


        LPAREN103_tree = None
        RPAREN105_tree = None
        LPAREN106_tree = None
        RPAREN109_tree = None
        LPAREN110_tree = None
        RPAREN113_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_operator = RewriteRuleSubtreeStream(self._adaptor, "rule operator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:206:3: ( LPAREN operator RPAREN -> ^( SECTION operator ) | LPAREN operator expression RPAREN -> ^( SECTION operator expression ) | LPAREN expression operator RPAREN -> ^( SECTION expression operator ) )
                alt36 = 3
                LA36_0 = self.input.LA(1)

                if (LA36_0 == LPAREN) :
                    LA36 = self.input.LA(2)
                    if LA36 == OR:
                        LA36_2 = self.input.LA(3)

                        if (LA36_2 == RPAREN) :
                            alt36 = 1
                        elif (LA36_2 == CHAR or (FALSE <= LA36_2 <= FLOAT) or LA36_2 == ID or LA36_2 == INT or LA36_2 == LBRACKET or LA36_2 == LPAREN or LA36_2 == NOT or LA36_2 == STRING or LA36_2 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 2, self.input)

                            raise nvae


                    elif LA36 == AND:
                        LA36_3 = self.input.LA(3)

                        if (LA36_3 == RPAREN) :
                            alt36 = 1
                        elif (LA36_3 == CHAR or (FALSE <= LA36_3 <= FLOAT) or LA36_3 == ID or LA36_3 == INT or LA36_3 == LBRACKET or LA36_3 == LPAREN or LA36_3 == NOT or LA36_3 == STRING or LA36_3 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 3, self.input)

                            raise nvae


                    elif LA36 == LT:
                        LA36_4 = self.input.LA(3)

                        if (LA36_4 == RPAREN) :
                            alt36 = 1
                        elif (LA36_4 == CHAR or (FALSE <= LA36_4 <= FLOAT) or LA36_4 == ID or LA36_4 == INT or LA36_4 == LBRACKET or LA36_4 == LPAREN or LA36_4 == NOT or LA36_4 == STRING or LA36_4 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 4, self.input)

                            raise nvae


                    elif LA36 == LTE:
                        LA36_5 = self.input.LA(3)

                        if (LA36_5 == RPAREN) :
                            alt36 = 1
                        elif (LA36_5 == CHAR or (FALSE <= LA36_5 <= FLOAT) or LA36_5 == ID or LA36_5 == INT or LA36_5 == LBRACKET or LA36_5 == LPAREN or LA36_5 == NOT or LA36_5 == STRING or LA36_5 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 5, self.input)

                            raise nvae


                    elif LA36 == EQ:
                        LA36_6 = self.input.LA(3)

                        if (LA36_6 == RPAREN) :
                            alt36 = 1
                        elif (LA36_6 == CHAR or (FALSE <= LA36_6 <= FLOAT) or LA36_6 == ID or LA36_6 == INT or LA36_6 == LBRACKET or LA36_6 == LPAREN or LA36_6 == NOT or LA36_6 == STRING or LA36_6 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 6, self.input)

                            raise nvae


                    elif LA36 == NEQ:
                        LA36_7 = self.input.LA(3)

                        if (LA36_7 == RPAREN) :
                            alt36 = 1
                        elif (LA36_7 == CHAR or (FALSE <= LA36_7 <= FLOAT) or LA36_7 == ID or LA36_7 == INT or LA36_7 == LBRACKET or LA36_7 == LPAREN or LA36_7 == NOT or LA36_7 == STRING or LA36_7 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 7, self.input)

                            raise nvae


                    elif LA36 == GTE:
                        LA36_8 = self.input.LA(3)

                        if (LA36_8 == RPAREN) :
                            alt36 = 1
                        elif (LA36_8 == CHAR or (FALSE <= LA36_8 <= FLOAT) or LA36_8 == ID or LA36_8 == INT or LA36_8 == LBRACKET or LA36_8 == LPAREN or LA36_8 == NOT or LA36_8 == STRING or LA36_8 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 8, self.input)

                            raise nvae


                    elif LA36 == GT:
                        LA36_9 = self.input.LA(3)

                        if (LA36_9 == RPAREN) :
                            alt36 = 1
                        elif (LA36_9 == CHAR or (FALSE <= LA36_9 <= FLOAT) or LA36_9 == ID or LA36_9 == INT or LA36_9 == LBRACKET or LA36_9 == LPAREN or LA36_9 == NOT or LA36_9 == STRING or LA36_9 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 9, self.input)

                            raise nvae


                    elif LA36 == ADD:
                        LA36_10 = self.input.LA(3)

                        if (LA36_10 == RPAREN) :
                            alt36 = 1
                        elif (LA36_10 == CHAR or (FALSE <= LA36_10 <= FLOAT) or LA36_10 == ID or LA36_10 == INT or LA36_10 == LBRACKET or LA36_10 == LPAREN or LA36_10 == NOT or LA36_10 == STRING or LA36_10 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 10, self.input)

                            raise nvae


                    elif LA36 == MIN:
                        LA36_11 = self.input.LA(3)

                        if (LA36_11 == RPAREN) :
                            alt36 = 1
                        elif (LA36_11 == CHAR or (FALSE <= LA36_11 <= FLOAT) or LA36_11 == ID or LA36_11 == INT or LA36_11 == LBRACKET or LA36_11 == LPAREN or LA36_11 == NOT or LA36_11 == STRING or LA36_11 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 11, self.input)

                            raise nvae


                    elif LA36 == CONCAT:
                        LA36_12 = self.input.LA(3)

                        if (LA36_12 == RPAREN) :
                            alt36 = 1
                        elif (LA36_12 == CHAR or (FALSE <= LA36_12 <= FLOAT) or LA36_12 == ID or LA36_12 == INT or LA36_12 == LBRACKET or LA36_12 == LPAREN or LA36_12 == NOT or LA36_12 == STRING or LA36_12 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 12, self.input)

                            raise nvae


                    elif LA36 == SUBTRACT:
                        LA36_13 = self.input.LA(3)

                        if (LA36_13 == RPAREN) :
                            alt36 = 1
                        elif (LA36_13 == CHAR or (FALSE <= LA36_13 <= FLOAT) or LA36_13 == ID or LA36_13 == INT or LA36_13 == LBRACKET or LA36_13 == LPAREN or LA36_13 == NOT or LA36_13 == STRING or LA36_13 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 13, self.input)

                            raise nvae


                    elif LA36 == DIV:
                        LA36_14 = self.input.LA(3)

                        if (LA36_14 == RPAREN) :
                            alt36 = 1
                        elif (LA36_14 == CHAR or (FALSE <= LA36_14 <= FLOAT) or LA36_14 == ID or LA36_14 == INT or LA36_14 == LBRACKET or LA36_14 == LPAREN or LA36_14 == NOT or LA36_14 == STRING or LA36_14 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 14, self.input)

                            raise nvae


                    elif LA36 == STARS:
                        LA36_15 = self.input.LA(3)

                        if (LA36_15 == RPAREN) :
                            alt36 = 1
                        elif (LA36_15 == CHAR or (FALSE <= LA36_15 <= FLOAT) or LA36_15 == ID or LA36_15 == INT or LA36_15 == LBRACKET or LA36_15 == LPAREN or LA36_15 == NOT or LA36_15 == STRING or LA36_15 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 15, self.input)

                            raise nvae


                    elif LA36 == IDIV:
                        LA36_16 = self.input.LA(3)

                        if (LA36_16 == RPAREN) :
                            alt36 = 1
                        elif (LA36_16 == CHAR or (FALSE <= LA36_16 <= FLOAT) or LA36_16 == ID or LA36_16 == INT or LA36_16 == LBRACKET or LA36_16 == LPAREN or LA36_16 == NOT or LA36_16 == STRING or LA36_16 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 16, self.input)

                            raise nvae


                    elif LA36 == MOD:
                        LA36_17 = self.input.LA(3)

                        if (LA36_17 == RPAREN) :
                            alt36 = 1
                        elif (LA36_17 == CHAR or (FALSE <= LA36_17 <= FLOAT) or LA36_17 == ID or LA36_17 == INT or LA36_17 == LBRACKET or LA36_17 == LPAREN or LA36_17 == NOT or LA36_17 == STRING or LA36_17 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 17, self.input)

                            raise nvae


                    elif LA36 == EXP:
                        LA36_18 = self.input.LA(3)

                        if (LA36_18 == RPAREN) :
                            alt36 = 1
                        elif (LA36_18 == CHAR or (FALSE <= LA36_18 <= FLOAT) or LA36_18 == ID or LA36_18 == INT or LA36_18 == LBRACKET or LA36_18 == LPAREN or LA36_18 == NOT or LA36_18 == STRING or LA36_18 == TRUE) :
                            alt36 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 36, 18, self.input)

                            raise nvae


                    elif LA36 == CHAR or LA36 == FALSE or LA36 == FLOAT or LA36 == ID or LA36 == INT or LA36 == LBRACKET or LA36 == LPAREN or LA36 == NOT or LA36 == STRING or LA36 == TRUE:
                        alt36 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # grammars/Miranda.g:206:5: LPAREN operator RPAREN
                    pass 
                    LPAREN103 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1399) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN103)


                    self._state.following.append(self.FOLLOW_operator_in_section1401)
                    operator104 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator104.tree)


                    RPAREN105 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1403) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN105)


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
                        # 207:4: -> ^( SECTION operator )
                        # grammars/Miranda.g:207:7: ^( SECTION operator )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt36 == 2:
                    # grammars/Miranda.g:208:5: LPAREN operator expression RPAREN
                    pass 
                    LPAREN106 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1420) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN106)


                    self._state.following.append(self.FOLLOW_operator_in_section1422)
                    operator107 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator107.tree)


                    self._state.following.append(self.FOLLOW_expression_in_section1424)
                    expression108 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression108.tree)


                    RPAREN109 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1426) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN109)


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
                        # 209:4: -> ^( SECTION operator expression )
                        # grammars/Miranda.g:209:7: ^( SECTION operator expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(SECTION, "SECTION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_operator.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt36 == 3:
                    # grammars/Miranda.g:210:5: LPAREN expression operator RPAREN
                    pass 
                    LPAREN110 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_section1445) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN110)


                    self._state.following.append(self.FOLLOW_expression_in_section1447)
                    expression111 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression111.tree)


                    self._state.following.append(self.FOLLOW_operator_in_section1449)
                    operator112 = self.operator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_operator.add(operator112.tree)


                    RPAREN113 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_section1451) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN113)


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
                        # 211:4: -> ^( SECTION expression operator )
                        # grammars/Miranda.g:211:7: ^( SECTION expression operator )
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
                self.memoize(self.input, 25, section_StartIndex, success)


            pass
        return retval

    # $ANTLR end "section"


    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.operator_return, self).__init__()

            self.tree = None





    # $ANTLR start "operator"
    # grammars/Miranda.g:213:10: fragment operator : ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV |{...}? STARS | IDIV | MOD | EXP );
    def operator(self, ):
        retval = self.operator_return()
        retval.start = self.input.LT(1)

        operator_StartIndex = self.input.index()

        root_0 = None

        OR114 = None
        AND115 = None
        LT116 = None
        LTE117 = None
        EQ118 = None
        NEQ119 = None
        GTE120 = None
        GT121 = None
        ADD122 = None
        MIN123 = None
        CONCAT124 = None
        SUBTRACT125 = None
        DIV126 = None
        STARS127 = None
        IDIV128 = None
        MOD129 = None
        EXP130 = None

        OR114_tree = None
        AND115_tree = None
        LT116_tree = None
        LTE117_tree = None
        EQ118_tree = None
        NEQ119_tree = None
        GTE120_tree = None
        GT121_tree = None
        ADD122_tree = None
        MIN123_tree = None
        CONCAT124_tree = None
        SUBTRACT125_tree = None
        DIV126_tree = None
        STARS127_tree = None
        IDIV128_tree = None
        MOD129_tree = None
        EXP130_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:213:18: ( OR | AND | LT | LTE | EQ | NEQ | GTE | GT | ADD | MIN | CONCAT | SUBTRACT | DIV |{...}? STARS | IDIV | MOD | EXP )
                alt37 = 17
                LA37 = self.input.LA(1)
                if LA37 == OR:
                    alt37 = 1
                elif LA37 == AND:
                    alt37 = 2
                elif LA37 == LT:
                    alt37 = 3
                elif LA37 == LTE:
                    alt37 = 4
                elif LA37 == EQ:
                    alt37 = 5
                elif LA37 == NEQ:
                    alt37 = 6
                elif LA37 == GTE:
                    alt37 = 7
                elif LA37 == GT:
                    alt37 = 8
                elif LA37 == ADD:
                    alt37 = 9
                elif LA37 == MIN:
                    alt37 = 10
                elif LA37 == CONCAT:
                    alt37 = 11
                elif LA37 == SUBTRACT:
                    alt37 = 12
                elif LA37 == DIV:
                    alt37 = 13
                elif LA37 == STARS:
                    alt37 = 14
                elif LA37 == IDIV:
                    alt37 = 15
                elif LA37 == MOD:
                    alt37 = 16
                elif LA37 == EXP:
                    alt37 = 17
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # grammars/Miranda.g:213:20: OR
                    pass 
                    root_0 = self._adaptor.nil()


                    OR114 = self.match(self.input, OR, self.FOLLOW_OR_in_operator1473)
                    if self._state.backtracking == 0:
                        OR114_tree = self._adaptor.createWithPayload(OR114)
                        self._adaptor.addChild(root_0, OR114_tree)




                elif alt37 == 2:
                    # grammars/Miranda.g:213:23: AND
                    pass 
                    root_0 = self._adaptor.nil()


                    AND115 = self.match(self.input, AND, self.FOLLOW_AND_in_operator1475)
                    if self._state.backtracking == 0:
                        AND115_tree = self._adaptor.createWithPayload(AND115)
                        self._adaptor.addChild(root_0, AND115_tree)




                elif alt37 == 3:
                    # grammars/Miranda.g:213:27: LT
                    pass 
                    root_0 = self._adaptor.nil()


                    LT116 = self.match(self.input, LT, self.FOLLOW_LT_in_operator1477)
                    if self._state.backtracking == 0:
                        LT116_tree = self._adaptor.createWithPayload(LT116)
                        self._adaptor.addChild(root_0, LT116_tree)




                elif alt37 == 4:
                    # grammars/Miranda.g:213:30: LTE
                    pass 
                    root_0 = self._adaptor.nil()


                    LTE117 = self.match(self.input, LTE, self.FOLLOW_LTE_in_operator1479)
                    if self._state.backtracking == 0:
                        LTE117_tree = self._adaptor.createWithPayload(LTE117)
                        self._adaptor.addChild(root_0, LTE117_tree)




                elif alt37 == 5:
                    # grammars/Miranda.g:213:34: EQ
                    pass 
                    root_0 = self._adaptor.nil()


                    EQ118 = self.match(self.input, EQ, self.FOLLOW_EQ_in_operator1481)
                    if self._state.backtracking == 0:
                        EQ118_tree = self._adaptor.createWithPayload(EQ118)
                        self._adaptor.addChild(root_0, EQ118_tree)




                elif alt37 == 6:
                    # grammars/Miranda.g:213:37: NEQ
                    pass 
                    root_0 = self._adaptor.nil()


                    NEQ119 = self.match(self.input, NEQ, self.FOLLOW_NEQ_in_operator1483)
                    if self._state.backtracking == 0:
                        NEQ119_tree = self._adaptor.createWithPayload(NEQ119)
                        self._adaptor.addChild(root_0, NEQ119_tree)




                elif alt37 == 7:
                    # grammars/Miranda.g:213:41: GTE
                    pass 
                    root_0 = self._adaptor.nil()


                    GTE120 = self.match(self.input, GTE, self.FOLLOW_GTE_in_operator1485)
                    if self._state.backtracking == 0:
                        GTE120_tree = self._adaptor.createWithPayload(GTE120)
                        self._adaptor.addChild(root_0, GTE120_tree)




                elif alt37 == 8:
                    # grammars/Miranda.g:213:45: GT
                    pass 
                    root_0 = self._adaptor.nil()


                    GT121 = self.match(self.input, GT, self.FOLLOW_GT_in_operator1487)
                    if self._state.backtracking == 0:
                        GT121_tree = self._adaptor.createWithPayload(GT121)
                        self._adaptor.addChild(root_0, GT121_tree)




                elif alt37 == 9:
                    # grammars/Miranda.g:213:48: ADD
                    pass 
                    root_0 = self._adaptor.nil()


                    ADD122 = self.match(self.input, ADD, self.FOLLOW_ADD_in_operator1489)
                    if self._state.backtracking == 0:
                        ADD122_tree = self._adaptor.createWithPayload(ADD122)
                        self._adaptor.addChild(root_0, ADD122_tree)




                elif alt37 == 10:
                    # grammars/Miranda.g:213:52: MIN
                    pass 
                    root_0 = self._adaptor.nil()


                    MIN123 = self.match(self.input, MIN, self.FOLLOW_MIN_in_operator1491)
                    if self._state.backtracking == 0:
                        MIN123_tree = self._adaptor.createWithPayload(MIN123)
                        self._adaptor.addChild(root_0, MIN123_tree)




                elif alt37 == 11:
                    # grammars/Miranda.g:213:56: CONCAT
                    pass 
                    root_0 = self._adaptor.nil()


                    CONCAT124 = self.match(self.input, CONCAT, self.FOLLOW_CONCAT_in_operator1493)
                    if self._state.backtracking == 0:
                        CONCAT124_tree = self._adaptor.createWithPayload(CONCAT124)
                        self._adaptor.addChild(root_0, CONCAT124_tree)




                elif alt37 == 12:
                    # grammars/Miranda.g:213:63: SUBTRACT
                    pass 
                    root_0 = self._adaptor.nil()


                    SUBTRACT125 = self.match(self.input, SUBTRACT, self.FOLLOW_SUBTRACT_in_operator1495)
                    if self._state.backtracking == 0:
                        SUBTRACT125_tree = self._adaptor.createWithPayload(SUBTRACT125)
                        self._adaptor.addChild(root_0, SUBTRACT125_tree)




                elif alt37 == 13:
                    # grammars/Miranda.g:213:72: DIV
                    pass 
                    root_0 = self._adaptor.nil()


                    DIV126 = self.match(self.input, DIV, self.FOLLOW_DIV_in_operator1497)
                    if self._state.backtracking == 0:
                        DIV126_tree = self._adaptor.createWithPayload(DIV126)
                        self._adaptor.addChild(root_0, DIV126_tree)




                elif alt37 == 14:
                    # grammars/Miranda.g:213:76: {...}? STARS
                    pass 
                    root_0 = self._adaptor.nil()


                    if not ((len(self.input.LT(1).text) == 1)):
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        raise FailedPredicateException(self.input, "operator", "len(self.input.LT(1).text) == 1")


                    STARS127 = self.match(self.input, STARS, self.FOLLOW_STARS_in_operator1501)
                    if self._state.backtracking == 0:
                        STARS127_tree = self._adaptor.createWithPayload(STARS127)
                        self._adaptor.addChild(root_0, STARS127_tree)




                elif alt37 == 15:
                    # grammars/Miranda.g:213:117: IDIV
                    pass 
                    root_0 = self._adaptor.nil()


                    IDIV128 = self.match(self.input, IDIV, self.FOLLOW_IDIV_in_operator1503)
                    if self._state.backtracking == 0:
                        IDIV128_tree = self._adaptor.createWithPayload(IDIV128)
                        self._adaptor.addChild(root_0, IDIV128_tree)




                elif alt37 == 16:
                    # grammars/Miranda.g:213:122: MOD
                    pass 
                    root_0 = self._adaptor.nil()


                    MOD129 = self.match(self.input, MOD, self.FOLLOW_MOD_in_operator1505)
                    if self._state.backtracking == 0:
                        MOD129_tree = self._adaptor.createWithPayload(MOD129)
                        self._adaptor.addChild(root_0, MOD129_tree)




                elif alt37 == 17:
                    # grammars/Miranda.g:213:126: EXP
                    pass 
                    root_0 = self._adaptor.nil()


                    EXP130 = self.match(self.input, EXP, self.FOLLOW_EXP_in_operator1507)
                    if self._state.backtracking == 0:
                        EXP130_tree = self._adaptor.createWithPayload(EXP130)
                        self._adaptor.addChild(root_0, EXP130_tree)




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
                self.memoize(self.input, 26, operator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "operator"


    class boolean_return(ParserRuleReturnScope):
        def __init__(self):
            super(MirandaParser.boolean_return, self).__init__()

            self.tree = None





    # $ANTLR start "boolean"
    # grammars/Miranda.g:215:1: boolean : ( TRUE | FALSE );
    def boolean(self, ):
        retval = self.boolean_return()
        retval.start = self.input.LT(1)

        boolean_StartIndex = self.input.index()

        root_0 = None

        set131 = None

        set131_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # grammars/Miranda.g:215:8: ( TRUE | FALSE )
                # grammars/Miranda.g:
                pass 
                root_0 = self._adaptor.nil()


                set131 = self.input.LT(1)

                if self.input.LA(1) == FALSE or self.input.LA(1) == TRUE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set131))

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
                self.memoize(self.input, 27, boolean_StartIndex, success)


            pass
        return retval

    # $ANTLR end "boolean"

    # $ANTLR start "synpred2_Miranda"
    def synpred2_Miranda_fragment(self, ):
        # grammars/Miranda.g:112:4: ( ( typedef | definition ) DEDENT )
        # grammars/Miranda.g:112:4: ( typedef | definition ) DEDENT
        pass 
        # grammars/Miranda.g:112:4: ( typedef | definition )
        alt38 = 2
        LA38_0 = self.input.LA(1)

        if (LA38_0 == ID) :
            LA38_1 = self.input.LA(2)

            if (LA38_1 == STARS or LA38_1 == TYPE_IS) :
                alt38 = 1
            elif (LA38_1 == DEDENT or (FALSE <= LA38_1 <= FLOAT) or LA38_1 == ID or (INT <= LA38_1 <= LBRACKET) or LA38_1 == LPAREN or LA38_1 == TRUE) :
                alt38 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 38, 1, self.input)

                raise nvae


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 38, 0, self.input)

            raise nvae


        if alt38 == 1:
            # grammars/Miranda.g:112:5: typedef
            pass 
            self._state.following.append(self.FOLLOW_typedef_in_synpred2_Miranda650)
            self.typedef()

            self._state.following.pop()


        elif alt38 == 2:
            # grammars/Miranda.g:112:13: definition
            pass 
            self._state.following.append(self.FOLLOW_definition_in_synpred2_Miranda652)
            self.definition()

            self._state.following.pop()




        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred2_Miranda655)



    # $ANTLR end "synpred2_Miranda"



    # $ANTLR start "synpred4_Miranda"
    def synpred4_Miranda_fragment(self, ):
        # grammars/Miranda.g:118:17: ( body )
        # grammars/Miranda.g:118:17: body
        pass 
        self._state.following.append(self.FOLLOW_body_in_synpred4_Miranda699)
        self.body()

        self._state.following.pop()



    # $ANTLR end "synpred4_Miranda"



    # $ANTLR start "synpred9_Miranda"
    def synpred9_Miranda_fragment(self, ):
        # grammars/Miranda.g:128:31: ( STARS )
        # grammars/Miranda.g:128:31: STARS
        pass 
        self.match(self.input, STARS, self.FOLLOW_STARS_in_synpred9_Miranda808)



    # $ANTLR end "synpred9_Miranda"



    # $ANTLR start "synpred18_Miranda"
    def synpred18_Miranda_fragment(self, ):
        # grammars/Miranda.g:139:26: ( DEDENT definition )
        # grammars/Miranda.g:139:26: DEDENT definition
        pass 
        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred18_Miranda899)

        self._state.following.append(self.FOLLOW_definition_in_synpred18_Miranda902)
        self.definition()

        self._state.following.pop()



    # $ANTLR end "synpred18_Miranda"



    # $ANTLR start "synpred26_Miranda"
    def synpred26_Miranda_fragment(self, ):
        # grammars/Miranda.g:151:5: ( tuple )
        # grammars/Miranda.g:151:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred26_Miranda970)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred26_Miranda"



    # $ANTLR start "synpred30_Miranda"
    def synpred30_Miranda_fragment(self, ):
        # grammars/Miranda.g:157:15: ( ( CONCAT | SUBTRACT | COLON ) expr0 )
        # grammars/Miranda.g:157:15: ( CONCAT | SUBTRACT | COLON ) expr0
        pass 
        if self.input.LA(1) == COLON or self.input.LA(1) == CONCAT or self.input.LA(1) == SUBTRACT:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expr0_in_synpred30_Miranda1021)
        self.expr0()

        self._state.following.pop()



    # $ANTLR end "synpred30_Miranda"



    # $ANTLR start "synpred31_Miranda"
    def synpred31_Miranda_fragment(self, ):
        # grammars/Miranda.g:159:15: ( OR expression )
        # grammars/Miranda.g:159:15: OR expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred31_Miranda1033)

        self._state.following.append(self.FOLLOW_expression_in_synpred31_Miranda1039)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred31_Miranda"



    # $ANTLR start "synpred32_Miranda"
    def synpred32_Miranda_fragment(self, ):
        # grammars/Miranda.g:161:15: ( AND expression )
        # grammars/Miranda.g:161:15: AND expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred32_Miranda1051)

        self._state.following.append(self.FOLLOW_expression_in_synpred32_Miranda1057)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred32_Miranda"



    # $ANTLR start "synpred38_Miranda"
    def synpred38_Miranda_fragment(self, ):
        # grammars/Miranda.g:163:15: ( ( LT | LTE | EQ | NEQ | GTE | GT ) expression )
        # grammars/Miranda.g:163:15: ( LT | LTE | EQ | NEQ | GTE | GT ) expression
        pass 
        if self.input.LA(1) == EQ or (GT <= self.input.LA(1) <= GTE) or (LT <= self.input.LA(1) <= LTE) or self.input.LA(1) == NEQ:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred38_Miranda1084)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred38_Miranda"



    # $ANTLR start "synpred40_Miranda"
    def synpred40_Miranda_fragment(self, ):
        # grammars/Miranda.g:165:15: ( ( ADD | MIN ) expression )
        # grammars/Miranda.g:165:15: ( ADD | MIN ) expression
        pass 
        if self.input.LA(1) == ADD or self.input.LA(1) == MIN:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred40_Miranda1110)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred40_Miranda"



    # $ANTLR start "synpred42_Miranda"
    def synpred42_Miranda_fragment(self, ):
        # grammars/Miranda.g:167:15: ( ( DIV |{...}? STARS ) expression )
        # grammars/Miranda.g:167:15: ( DIV |{...}? STARS ) expression
        pass 
        # grammars/Miranda.g:167:15: ( DIV |{...}? STARS )
        alt39 = 2
        LA39_0 = self.input.LA(1)

        if (LA39_0 == DIV) :
            alt39 = 1
        elif (LA39_0 == STARS) :
            alt39 = 2
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 39, 0, self.input)

            raise nvae


        if alt39 == 1:
            # grammars/Miranda.g:167:16: DIV
            pass 
            self.match(self.input, DIV, self.FOLLOW_DIV_in_synpred42_Miranda1123)


        elif alt39 == 2:
            # grammars/Miranda.g:167:31: {...}? STARS
            pass 
            if not ((len(self.input.LT(1).text) == 1)):
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                raise FailedPredicateException(self.input, "synpred42_Miranda", "len(self.input.LT(1).text) == 1")


            self.match(self.input, STARS, self.FOLLOW_STARS_in_synpred42_Miranda1132)




        self._state.following.append(self.FOLLOW_expression_in_synpred42_Miranda1139)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred42_Miranda"



    # $ANTLR start "synpred44_Miranda"
    def synpred44_Miranda_fragment(self, ):
        # grammars/Miranda.g:169:15: ( ( IDIV | MOD ) expression )
        # grammars/Miranda.g:169:15: ( IDIV | MOD ) expression
        pass 
        if self.input.LA(1) == IDIV or self.input.LA(1) == MOD:
            self.input.consume()
            self._state.errorRecovery = False


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            mse = MismatchedSetException(None, self.input)
            raise mse



        self._state.following.append(self.FOLLOW_expression_in_synpred44_Miranda1159)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred44_Miranda"



    # $ANTLR start "synpred45_Miranda"
    def synpred45_Miranda_fragment(self, ):
        # grammars/Miranda.g:171:15: ( ( EXP ) expression )
        # grammars/Miranda.g:171:15: ( EXP ) expression
        pass 
        # grammars/Miranda.g:171:15: ( EXP )
        # grammars/Miranda.g:171:16: EXP
        pass 
        self.match(self.input, EXP, self.FOLLOW_EXP_in_synpred45_Miranda1172)




        self._state.following.append(self.FOLLOW_expression_in_synpred45_Miranda1176)
        self.expression()

        self._state.following.pop()



    # $ANTLR end "synpred45_Miranda"



    # $ANTLR start "synpred46_Miranda"
    def synpred46_Miranda_fragment(self, ):
        # grammars/Miranda.g:173:8: ( aexpr )
        # grammars/Miranda.g:173:8: aexpr
        pass 
        self._state.following.append(self.FOLLOW_aexpr_in_synpred46_Miranda1185)
        self.aexpr()

        self._state.following.pop()



    # $ANTLR end "synpred46_Miranda"



    # $ANTLR start "synpred54_Miranda"
    def synpred54_Miranda_fragment(self, ):
        # grammars/Miranda.g:191:5: ( section )
        # grammars/Miranda.g:191:5: section
        pass 
        self._state.following.append(self.FOLLOW_section_in_synpred54_Miranda1294)
        self.section()

        self._state.following.pop()



    # $ANTLR end "synpred54_Miranda"



    # $ANTLR start "synpred55_Miranda"
    def synpred55_Miranda_fragment(self, ):
        # grammars/Miranda.g:192:5: ( tuple )
        # grammars/Miranda.g:192:5: tuple
        pass 
        self._state.following.append(self.FOLLOW_tuple_in_synpred55_Miranda1300)
        self.tuple()

        self._state.following.pop()



    # $ANTLR end "synpred55_Miranda"




    def synpred46_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred46_Miranda_fragment()
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

    def synpred9_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred9_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred38_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred38_Miranda_fragment()
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

    def synpred55_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred55_Miranda_fragment()
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

    def synpred45_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred45_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred54_Miranda(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred54_Miranda_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_typedef_in_program650 = frozenset([14])
    FOLLOW_definition_in_program652 = frozenset([14])
    FOLLOW_DEDENT_in_program655 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_program659 = frozenset([])
    FOLLOW_EOF_in_program661 = frozenset([1])
    FOLLOW_ID_in_definition694 = frozenset([1, 21, 22, 26, 28, 29, 30, 32, 52])
    FOLLOW_pattern_in_definition696 = frozenset([1, 21, 22, 26, 28, 29, 30, 32, 52])
    FOLLOW_body_in_definition699 = frozenset([1, 29])
    FOLLOW_ID_in_typedef735 = frozenset([49, 55])
    FOLLOW_STARS_in_typedef737 = frozenset([49, 55])
    FOLLOW_TYPE_IS_in_typedef740 = frozenset([26])
    FOLLOW_part_in_typedef742 = frozenset([1, 41])
    FOLLOW_OR_in_typedef745 = frozenset([26])
    FOLLOW_part_in_typedef747 = frozenset([1, 41])
    FOLLOW_ID_in_part780 = frozenset([1, 9, 26, 32, 40, 49])
    FOLLOW_typelist_in_part782 = frozenset([1])
    FOLLOW_LPAREN_in_generic802 = frozenset([26])
    FOLLOW_ID_in_generic806 = frozenset([1, 46, 49])
    FOLLOW_STARS_in_generic808 = frozenset([1, 46, 49])
    FOLLOW_RPAREN_in_generic811 = frozenset([1])
    FOLLOW_NUM_TYPE_in_typelist822 = frozenset([1, 9, 26, 32, 40, 49])
    FOLLOW_CHAR_TYPE_in_typelist824 = frozenset([1, 9, 26, 32, 40, 49])
    FOLLOW_generic_in_typelist826 = frozenset([1, 9, 26, 32, 40, 49])
    FOLLOW_STARS_in_typelist828 = frozenset([1, 9, 26, 32, 40, 49])
    FOLLOW_IS_in_body845 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_body847 = frozenset([1, 11, 56])
    FOLLOW_guard_in_body849 = frozenset([1, 56])
    FOLLOW_where_in_body852 = frozenset([1])
    FOLLOW_COMMA_in_guard881 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 42, 50, 52])
    FOLLOW_expression_in_guard884 = frozenset([1])
    FOLLOW_OTHERWISE_in_guard886 = frozenset([1])
    FOLLOW_WHERE_in_where894 = frozenset([26])
    FOLLOW_definition_in_where896 = frozenset([1, 14])
    FOLLOW_DEDENT_in_where899 = frozenset([26])
    FOLLOW_definition_in_where902 = frozenset([1, 14])
    FOLLOW_basic_in_pattern915 = frozenset([1, 4, 10])
    FOLLOW_set_in_pattern918 = frozenset([21, 22, 26, 28, 30, 32, 52])
    FOLLOW_pattern_in_pattern925 = frozenset([1])
    FOLLOW_ID_in_basic940 = frozenset([1])
    FOLLOW_INT_in_basic946 = frozenset([1])
    FOLLOW_FLOAT_in_basic952 = frozenset([1])
    FOLLOW_boolean_in_basic958 = frozenset([1])
    FOLLOW_list_in_basic964 = frozenset([1])
    FOLLOW_tuple_in_basic970 = frozenset([1])
    FOLLOW_LPAREN_in_basic976 = frozenset([21, 22, 26, 28, 30, 32, 46, 52])
    FOLLOW_pattern_in_basic979 = frozenset([21, 22, 26, 28, 30, 32, 46, 52])
    FOLLOW_RPAREN_in_basic982 = frozenset([1])
    FOLLOW_expr0_in_expression991 = frozenset([1])
    FOLLOW_expr1_in_expr0998 = frozenset([1, 10, 13, 51])
    FOLLOW_CONCAT_in_expr01002 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_SUBTRACT_in_expr01008 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_COLON_in_expr01014 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expr0_in_expr01021 = frozenset([1])
    FOLLOW_expr2_in_expr11030 = frozenset([1, 41])
    FOLLOW_OR_in_expr11033 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_expr11039 = frozenset([1, 41])
    FOLLOW_expr3_in_expr21048 = frozenset([1, 6])
    FOLLOW_AND_in_expr21051 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_expr21057 = frozenset([1, 6])
    FOLLOW_expr4_in_expr31066 = frozenset([1, 19, 24, 25, 33, 34, 37])
    FOLLOW_set_in_expr31069 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_expr31084 = frozenset([1, 19, 24, 25, 33, 34, 37])
    FOLLOW_expr5_in_expr41093 = frozenset([1, 4, 35])
    FOLLOW_ADD_in_expr41097 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_MIN_in_expr41103 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_expr41110 = frozenset([1, 4, 35])
    FOLLOW_expr6_in_expr51119 = frozenset([1, 16, 49])
    FOLLOW_DIV_in_expr51123 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_STARS_in_expr51132 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_expr51139 = frozenset([1, 16, 49])
    FOLLOW_expr7_in_expr61148 = frozenset([1, 27, 36])
    FOLLOW_IDIV_in_expr61152 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_MOD_in_expr61155 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_expr61159 = frozenset([1, 27, 36])
    FOLLOW_expr8_in_expr71168 = frozenset([1, 20])
    FOLLOW_EXP_in_expr71172 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_expr71176 = frozenset([1, 20])
    FOLLOW_aexpr_in_expr81185 = frozenset([1, 8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_ID_in_aexpr1198 = frozenset([1])
    FOLLOW_INT_in_aexpr1217 = frozenset([1])
    FOLLOW_FLOAT_in_aexpr1236 = frozenset([1])
    FOLLOW_CHAR_in_aexpr1255 = frozenset([1])
    FOLLOW_STRING_in_aexpr1274 = frozenset([1])
    FOLLOW_NOT_in_aexpr1280 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_aexpr1282 = frozenset([1])
    FOLLOW_boolean_in_aexpr1288 = frozenset([1])
    FOLLOW_section_in_aexpr1294 = frozenset([1])
    FOLLOW_tuple_in_aexpr1300 = frozenset([1])
    FOLLOW_list_in_aexpr1306 = frozenset([1])
    FOLLOW_LPAREN_in_aexpr1312 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_aexpr1315 = frozenset([46])
    FOLLOW_RPAREN_in_aexpr1317 = frozenset([1])
    FOLLOW_LPAREN_in_tuple1326 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_tuple1328 = frozenset([11])
    FOLLOW_COMMA_in_tuple1331 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_tuple1333 = frozenset([11, 46])
    FOLLOW_RPAREN_in_tuple1337 = frozenset([1])
    FOLLOW_LBRACKET_in_list1361 = frozenset([8, 11, 21, 22, 26, 28, 30, 32, 38, 45, 50, 52])
    FOLLOW_expression_in_list1363 = frozenset([11, 45])
    FOLLOW_COMMA_in_list1367 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_list1369 = frozenset([11, 45])
    FOLLOW_RBRACKET_in_list1373 = frozenset([1])
    FOLLOW_LPAREN_in_section1399 = frozenset([4, 6, 13, 16, 19, 20, 24, 25, 27, 33, 34, 35, 36, 37, 41, 49, 51])
    FOLLOW_operator_in_section1401 = frozenset([46])
    FOLLOW_RPAREN_in_section1403 = frozenset([1])
    FOLLOW_LPAREN_in_section1420 = frozenset([4, 6, 13, 16, 19, 20, 24, 25, 27, 33, 34, 35, 36, 37, 41, 49, 51])
    FOLLOW_operator_in_section1422 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_section1424 = frozenset([46])
    FOLLOW_RPAREN_in_section1426 = frozenset([1])
    FOLLOW_LPAREN_in_section1445 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_section1447 = frozenset([4, 6, 13, 16, 19, 20, 24, 25, 27, 33, 34, 35, 36, 37, 41, 49, 51])
    FOLLOW_operator_in_section1449 = frozenset([46])
    FOLLOW_RPAREN_in_section1451 = frozenset([1])
    FOLLOW_OR_in_operator1473 = frozenset([1])
    FOLLOW_AND_in_operator1475 = frozenset([1])
    FOLLOW_LT_in_operator1477 = frozenset([1])
    FOLLOW_LTE_in_operator1479 = frozenset([1])
    FOLLOW_EQ_in_operator1481 = frozenset([1])
    FOLLOW_NEQ_in_operator1483 = frozenset([1])
    FOLLOW_GTE_in_operator1485 = frozenset([1])
    FOLLOW_GT_in_operator1487 = frozenset([1])
    FOLLOW_ADD_in_operator1489 = frozenset([1])
    FOLLOW_MIN_in_operator1491 = frozenset([1])
    FOLLOW_CONCAT_in_operator1493 = frozenset([1])
    FOLLOW_SUBTRACT_in_operator1495 = frozenset([1])
    FOLLOW_DIV_in_operator1497 = frozenset([1])
    FOLLOW_STARS_in_operator1501 = frozenset([1])
    FOLLOW_IDIV_in_operator1503 = frozenset([1])
    FOLLOW_MOD_in_operator1505 = frozenset([1])
    FOLLOW_EXP_in_operator1507 = frozenset([1])
    FOLLOW_typedef_in_synpred2_Miranda650 = frozenset([14])
    FOLLOW_definition_in_synpred2_Miranda652 = frozenset([14])
    FOLLOW_DEDENT_in_synpred2_Miranda655 = frozenset([1])
    FOLLOW_body_in_synpred4_Miranda699 = frozenset([1])
    FOLLOW_STARS_in_synpred9_Miranda808 = frozenset([1])
    FOLLOW_DEDENT_in_synpred18_Miranda899 = frozenset([26])
    FOLLOW_definition_in_synpred18_Miranda902 = frozenset([1])
    FOLLOW_tuple_in_synpred26_Miranda970 = frozenset([1])
    FOLLOW_set_in_synpred30_Miranda1001 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expr0_in_synpred30_Miranda1021 = frozenset([1])
    FOLLOW_OR_in_synpred31_Miranda1033 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_synpred31_Miranda1039 = frozenset([1])
    FOLLOW_AND_in_synpred32_Miranda1051 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_synpred32_Miranda1057 = frozenset([1])
    FOLLOW_set_in_synpred38_Miranda1069 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_synpred38_Miranda1084 = frozenset([1])
    FOLLOW_set_in_synpred40_Miranda1096 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_synpred40_Miranda1110 = frozenset([1])
    FOLLOW_DIV_in_synpred42_Miranda1123 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_STARS_in_synpred42_Miranda1132 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_synpred42_Miranda1139 = frozenset([1])
    FOLLOW_set_in_synpred44_Miranda1151 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_synpred44_Miranda1159 = frozenset([1])
    FOLLOW_EXP_in_synpred45_Miranda1172 = frozenset([8, 21, 22, 26, 28, 30, 32, 38, 50, 52])
    FOLLOW_expression_in_synpred45_Miranda1176 = frozenset([1])
    FOLLOW_aexpr_in_synpred46_Miranda1185 = frozenset([1])
    FOLLOW_section_in_synpred54_Miranda1294 = frozenset([1])
    FOLLOW_tuple_in_synpred55_Miranda1300 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MirandaLexer", MirandaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
