tree grammar CoreAnalyzer;

options {
	language     = Python;
	ASTLabelType = CommonTree;
	tokenVocab   = Core;
	rewrite      = true;
}

start[info]
	: combinator[info]+
;

combinator[info]
	: ^(COMBINATOR name=ID (params+=ID)* expression[info]) {
		info.combinator($name.text, $params)
	}
;

expression[info]
	: ^(LET definition[info]+ expression[info])
	| ^(LETREC definition[info]+ expression[info])
	| ^(CASE expression[info] alternative[info]+)
	| ^(LAMBDA ID+ expression[info])
	| ^(MUL expression[info] expression[info])
	| ^(DIV expression[info] expression[info])
	| ^(ADD expression[info] expression[info])
	| ^(MIN expression[info] expression[info])
	| ^(AND expression[info] expression[info])
	| ^(OR expression[info] expression[info])
	| ^(EQ expression[info] expression[info])
	| ^(NEQ expression[info] expression[info])
	| ^(LT expression[info] expression[info])
	| ^(LTE expression[info] expression[info])
	| ^(GT expression[info] expression[info])
	| ^(GTE expression[info] expression[info])
	| ^(APPLICATION expression[info] expression[info])
	| basic[info]
;

basic[info]
	: ID
	| NUMBER
	| ^(PACK NUMBER NUMBER)
;

alternative[info]
	: ^(ARROW NUMBER expression[info])
;

definition[info]
	: ^(IS ID expression[info])
;