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
      ^(COMBINATOR n=ID {info.current = $n.text} (i=ID { env.add($i.text) } )* expression[info, env, code]) {
      code.Update(env.count())
      code.Pop(env.count())
      code.Unwind()
      code.store($n.text, env)
   }
;

expression[info, env, code]
   : { 
      n = 0
      tmp = env.increment(0)
   } 
      ^(LET 
            (definition[info, tmp, code, True] { n += 1; tmp = tmp.increment() })+ 
            { 
               n -= 1
               nn = n + 1
               env2 = env.increment(n + 1)
               for m in tmp.mapping:
                  if m in env.mapping:
                     continue;
                  env2.addat(m, n)
                  n -= 1
            }
            expression[info, env2, code]) {
      code.Slide(nn)
   }
   | {
      params = info.letrec(self.input.index())
      n = len(params)
      code.Alloc(n)
      env2 = env.increment(n)
      # bookkeeping for the environment
      n_param = n - 1
      for p in params:
         env2.addat(p, n_param)
         n_param -= 1
      # bookkeeping for the updates of the local variable of the letrec
      n_update = n - 1
   }
     ^(LETREC 
         (definition[info, env2, code, False] {code.Update(n_update); n_update -= 1} )+ 
         expression[info, env2, code]
      ) {
      code.Slide(n)
   }
   | ^(CASE expression[info, env, code] alternative+)
   | ^(LAMBDA ID+ expression[info, env, code])
   | ^(MUL expression[info, env, code] expression[info, env, code])
   | ^(DIV expression[info, env, code] expression[info, env, code])
   | ^(ADD expression[info, env, code] expression[info, env.increment(), code]) {
		$code.Add()
	}
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

definition[info, env, code, record]
   : ^(IS ID expression[info, env, code]) {
      if record:
         env.add($ID.text)
   }
;