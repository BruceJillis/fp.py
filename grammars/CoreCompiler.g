tree grammar CoreCompiler;

options {
   language     = Python;
   ASTLabelType = CommonTree;
   tokenVocab   = Core;
   rewrite      = true;
}

@header {
   from common import Environment
}

start[info, code]
   : combinator[info, code]+ 
;

combinator[info, code]
   :  { env = Environment() }
      ^(COMBINATOR n=ID (i=ID { env.add($i.text) } )* expression[info, env, code]) {
      code.Update(env.count())
      code.Pop(env.count())
      code.Unwind()
      code.store($n.text, env)
   }
;

expression[info, env, code]
   : { 
      n = 0
      tmp = Environment()
   } 
      ^(LET 
            (definition[info, tmp, code] { n += 1; tmp = tmp.increment() })+ 
            { 
               n -= 1
               nn = n + 1
               env = env.increment(0)
               env.increment(n)
               for m in tmp.mapping:
                  env.addat(m, n)
                  n -= 1
               print env.mapping
            }
            expression[info, env, code]) {
      code.Slide(nn)
   }
   | ^(LETREC definition[info, env, code]+ expression[info, env, code])
   | ^(CASE expression[info, env, code] alternative+)
   | ^(LAMBDA ID+ expression[info, env, code])
   | ^(MUL expression[info, env, code] expression[info, env, code])
   | ^(DIV expression[info, env, code] expression[info, env, code])
   | ^(ADD expression[info, env, code] expression[info, env, code])
   | ^(MIN expression[info, env, code] expression[info, env, code])
   | ^(AND expression[info, env, code] expression[info, env, code])
   | ^(OR expression[info, env, code] expression[info, env, code])
   | ^(EQ expression[info, env, code] expression[info, env, code])
   | ^(NEQ expression[info, env, code] expression[info, env, code])
   | ^(LT expression[info, env, code] expression[info, env, code])
   | ^(LTE expression[info, env, code] expression[info, env, code])
   | ^(GT expression[info, env, code] expression[info, env, code])
   | ^(GTE expression[info, env, code] expression[info, env, code])
   | ^(APPLICATION expression[info, env, code] expression[info, env.increment(), code]) {
      code.Apply()
   }
   | basic[info, env, code]
;

basic[info, env, code]
   : ID {
      if $ID.text in info.combinators:
         $code.PushGlobal($ID.text)
      else:
         $code.Push(env.get($ID.text), $ID.text)
   }
   | NUMBER {
      $code.PushInt($NUMBER.text)
   }
   | ^(PACK NUMBER NUMBER)
;

alternative
   : ^(ARROW NUMBER expression[info, env, code])
;

definition[info, env, code]
   : ^(IS ID expression[info, env, code]) {
      env.add($ID.text)
   }
;