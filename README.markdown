FP is an educational functional language compiler/interpreter written in python. Based on Simon Peyton Jones' work, specifically: [Implementing functional languages: a tutorial](http://research.microsoft.com/en-us/um/people/simonpj/papers/pj-lester-book/). Inspired by Miranda and Amanda (A windows based clone created by D. Bruin, see [the Miranda wikipedia entry](http://en.wikipedia.org/wiki/Miranda_(programming_language) for more info generally and a download link).

It features:

- lazy evaluation
- a mark and sweep, stop the world garbage collector
- infinite precision arithmetic on ints and floats
- anonymous local function definitions
- structured datatypes (algebraic types)

Status
------
- Core
	* Functionally done. Everything works but isn't fully lazy yet (meaning some sub-expressions will be unnecessarily recalculated). The interpreter passes 91 high and low level unittests giving 91% code coverage (see --coverage for a report) and consists of 4985 lines of python code.
- High Level Language
	* 0%

Usage
-----
To compile (and evaluate) a Core program (extension assumed to be .core but isn't mandated), just supply it's name to the compiler:

	python fp.py core\examples\fac.core  

Core
----
      
The Core language is a minimal functional language carefully chosen so that it is possible to translate programs in a rich functional language (such as Miranda) into the Core language without losing expressiveness or efficiency. The Core language thus serves as a clean interface between the 'front end' of the compiler, which is concerned with high-level language constructs, and the 'back end', which is concerned with implementing the Core language in various different ways.

The basic types are: 

<table>
	<tr>
		<td>numbers</td>
		<td>both integer and real (ie. the integers: 1, 2, 4 or 1000 or the reals: 1.131, 2.31 etc)</td>
	</tr>
	<tr>
		<td>booleans</td>
		<td>with only values true, false </td>
	</tr>
	<tr>
		<td>characters</td>
		<td>intended to be the whole ASCII (and maybe even unicode set) but for now just '[a-zA-Z0-9]'</td>
	</tr>
</table>

Here is an example Core program, which evaluates to `42`:
   
	main = double 21;
	double x = x + x

A Core program consists of a set of supercombinator definitions, including a distinguished one: `main`. To execute the program, we evaluate `main`. Supercombinators can define functions, such as the definition of `double`. Supercombinators can have local definitions, using the `let` construct of the Core language:
   
	main = quadruple 20;
	quadruple x = let twice_x = x+x in twice_x + twice_x

Here `twice_x` is defined locally within the body of `quadruple` to be `x+x`, and `quadruple` returns `twice_x + twice_x`. A let expression is non-recursive. For recursive definitions, the Core language uses the `letrec` construct, which is exactly like `let` except that its definitions can be recursive. For example:
   
	infinite n = letrec ns = cons n ns in ns

The reason that we distinguish `let` from `letrec` in the Core language (rather than providing only `letrec`) is that `let` is a bit simpler to implement than `letrec`, and we may get slightly better code. The left-hand side of a `let` or `letrec` binding must always be a simple variable.

It is sometimes convenient to be able to denote functions using explicit lambda abstractions, and the Core language provides a construct to do so. For example, in the program

	double_list xs = map (\x. 2*x) xs

the lambda abstraction `(\x. 2*x)` denotes the function which doubles its argument.

A universal feature of all modern functional programming languages is the provision of structured types, often called algebraic data types. The Core language provides a single family of constructors:
   
	Pack{tag, arity}

Here, `tag` is an integer which uniquely identifies the constructor, and `arity` tells how many arguments it takes. So in the Core language one writes:

	Pack{2,2} (Pack{1,1} 3) (Pack{1,1} 4)

instead of:

	Branch (Leaf 3) (Leaf 4)

The `tag` is required so that objects built with different constructors can be distinguished from one another. In a well-typed program, objects of different type will never need to be distinguished at run-time, so `tag`'s only need to be unique within a data type. Hence, we can start the `tag` at 1 afresh for each new data type.

In general, the pattern matching allowed by modern functional programming languages can be rather complex, with multiple nested patterns, overlapping patterns, guards and so on. For the Core language, we eliminate these complications by outlawing all complex forms of pattern matching! We do this by providing only `case` expressions in the Core language.  

The important thing about case expressions is that each alternative consists only of a `tag` followed by a number of variables (which should be the same as the `arity` of the constructor). No nested patterns are allowed. Case 
expressions have a very simple operational interpretation, rather like a multi-way jump: evaluate the expression to be analysed, get the `tag` of the constructor it is built with and evaluate the appropriate alternative.

<table>
	<tr>
		<th>precedence</th>
		<th>associativity</th>
		<th>operator</th>
	</tr>
	<tr>
		<td>6</td>
		<td>left</td>
		<td>application</td>
	</tr>
	<tr>
		<td>5</td>
		<td>left</td>
		<td>/, *</td>
	</tr>
	<tr>
		<td>4</td>
		<td>left</td>
		<td>+, -</td>
	</tr>
	<tr>
		<td>3</td>
		<td>left</td>
		<td>&lt;, &lt;=, ==, !=, &gt;=, &gt;</td>
	</tr>
	<tr>
		<td>2</td>
		<td>left</td>
		<td>&amp;</td>
	</tr>
	<tr>
		<td>1</td>
		<td>left</td>
		<td>|</td>
	</tr>
</table>

Basic programs
--------------
The programs in this section require only integer constants and function application. The following and first program should return the value `3` rather quickly:
   
	main = I 3

The next program requires a couple more steps before returning `3`.
   
	id = S K K;
	main = id 3

This one makes quite a few applications of `id`.

	id = S K K;
	main = twice twice twice id 3

This program should show up the difference between a system which does updating and one which does not. If updating occurs, the evaluation of (`I I I`) should take place only once; without updating it will take place twice.

	main = twice (I I I) 3

This example uses a functional representation of lists to build an infinite list of `4`'s, and then takes its second element. The functions for head and tail (`hd` and `tl`) return abort if their argument is an empty list. The `abort` supercombinator just generates an infinite loop.

	cons a b cc cn = cc a b;
	nil cc cn = cn;
	hd list = list K abort;
	tl list = list K1 abort;
	abort = abort;
	
	infinite x = cons x (infinite x);
	main = hd (tl (infinite 4))

If updating is implemented, then this program will execute in fewer steps than if not, because the evaluation of `id1` is shared.
   
	main = let id1 = I I I in id1 id1 3

We should test nested `let` expressions too:

	oct g x = let h = twice g in let k = twice h in k (k x);
	main = oct I 4

The next program tests `letrec`'s, using 'functional lists' based on the earlier definitions of `cons`, `nil`, etc.
   
	infinite x = letrec xs = cons x xs in xs;
	main = hd (tl (tl (infinite 4)))

We begin with simple tests which do not require the conditional.
   
	main = 4*5+(2-5)

This next program needs function calls to work properly. Try replacing `twice twice` with `twice twice twice` or `twice twice twice twice`. 
   
	inc x = x+1;
	main = twice twice inc 4

Using functional lists again, we can write a `length` function:

	length xs = xs length1 0;
	length1 x xs = 1 + (length xs);
	main = length (cons 3 (cons 3 (cons 3 nil)))

Once we have conditionals we can at last write 'interesting' programs. For example, `factorial`:
   
	fac n = if (n==0) 1 (n * fac (n-1)) ;
	main = fac 5

The next program computes the greatest common divisor of two integers, using Euclid's algorithm:
   
	gcd a b = if (a==b) a if (a<b) (gcd b a) (gcd b (a-b));
	main = gcd 6 10

The nfib function is interesting because its result (an integer) gives a count of how many function calls were made during its execution. So the result divided by the execution time gives a performance measure in function calls per second. As a result, nfib is quite widely used as a benchmark. The 'nfib-number' for a particular implementation needs to be taken with an enormous dose of salt, however, because it is critically dependent on various rather specialised optimisations.
   
	nfib n = if (n <= 0) 1 (1 + nfib (n-1) + nfib (n-2));
	main = nfib 4

This program returns a list of descending integers. The evaluator should be expecting a list as the result of the program. `Cons` and `nil` are now expected to be implemented in the prelude as `Pack{3,2}` and `Pack{4,0}` respectively.
   
	downfrom n = if (n == 0) nil (cons n (downfrom (n-1)));
	main = hd (downfrom 4)

The next program implements the sieve of eratosthenes to generate the infinite list of primes, and `take`'s the first few elements of the result list.
   
	from n = cons n (from (n + 1));

	sieve xs = case xs of
		<4> -> nil,
		<3> p ps -> cons p (sieve (filter (nonMultiple p) ps));

	filter predicate xs = case xs of
			<4> -> nil,
			<3> p ps -> let rest = filter predicate ps in if (predicate p) (cons p rest) rest;

	nonMultiple p n = ((n/p)*p) != n;

	take n xs = if (n==0) nil (case xs of
		<4> -> nil,
		<3> p ps -> cons p (take (n-1) ps));

	main = (sieve (take 15 (from 2)))

* Adapted from: Implementing Functional Languages: a tutorial by Simon L. Peyton Jones & David R. Lester

Command Line Parameters
-----------------------
	usage: fp.py [-h] [--include INCLUDE] [-v] [--stats] [--test] [--coverage]
					 [--show-missing] [--no-includes] [--print-code PRINTCODE]
					 [--show-transformations]
					 [file [file ...]]

	Compiler for the miranda-style functional language FP.

	positional arguments:
	  file                  .core file to compile and evaluate

	optional arguments:
	  -h, --help            show this help message and exit
	  --include INCLUDE     include .core files in these directories (default:
									core/runtime/*.core)
	  --print-code PRINTCODE
									print gmachine instructions for the supplied
									combinators
	  --show-transformations
									prettyprint the program before, during and after the
									transformation step

	debug:
	  commandline options used during development on FPJS itself

	  -v, --verbose         output a lot of information on the internals of the
									systems
	  --stats               output stats for the execution of the program (nr. of
									steps, heap space used, pop/push/peeks, etc)
	  --test                run testsuite and report results
	  --coverage            run test, record code coverage and report results
	  --show-missing        show line numbers that were not covered by the
									testsuite in the --coverage report
	  --no-includes         do not include any external files (--include) except
									those supplied as positional arguments

Structure
---------

FP consists of 4 parts: 

- an ANTLR 3 based parser
- several program transformations
- a treewalker that compiles the AST down to a almost linear list of instructions
- a virtual machine that can interpret the list of instructions

- /fp.py
	- main entry point, defines command line options and implements unittest/coverage
- /common.py
   - contains shared misc code.
- /ast.py
	- contains the definition of the AST nodes (composite) and a utility function that constructs application spines
- /transforms.py
   - contains all the program transformations
- /visitors.py
   - contains all visitors including the compiler
- /CoreLexer.py
- /CoreParser.py
	- generated by ANTL from grammar/core.g

- /compile.bat
   - compile the grammer using ANTLR
- /tests/
	- module containing all the unittests
- /core/examples
	- some example programs
- /core/runtime
   - contains the std prelude
- /core/tests
   - misc core code used in the unittests

- /etc/
	- misc supporting stuff
- /etc/vb-antlr*
	- UTwente compiler construction lecture notes 
- /etc/Implementing Functional Languages.pdf
	- Book/Tutorial by Simon Peyton Jones about several machine models that can evaluate lazy functional languages and their implementations.
- /etc/antlr-3.4.jar 
	- the excellent antlr tool
- /etc/cloc-1.55.exe
- /etc/cloc.bat
	- line counts tooling