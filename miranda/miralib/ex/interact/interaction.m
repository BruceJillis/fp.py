||----------------------------------------------------------------------||
||	interact.m							||
||									||
||	A model of interactions based on the type interact.		||
||									||
||	Version 1.0		18 September 1989			||
||									||
||	Uses 	inter_basics.m						||
||									||
||	Simon Thompson, Computing Laboratory, Univ. of Kent, U.K.	||
||	sjt@ukc.ac.uk							||
||									||
||	For further details of the model, and for a formal semantics	||
||	of it see							||
||									||
||		Interactive Functional Programs; A Method and		||
||		A Formal Semantics					||
||									||
||		Simon Thompson 						||
||									||
||		in "Research Topics in Functional Programming"          ||
||              D. A. Turner (ed.) Addison-Wesley, 1990                 ||
||              (and also a University of Kent                          ||
||              Computing Laboratory Technical Report, 1988)            ||
||----------------------------------------------------------------------||

%include "inter_basics.m"
%export "inter_basics.m" +

||----------------------------------------------------------------------|| 
||	For details of types such as input, output etc., see the file	||
||	inter_basics.m							||
||----------------------------------------------------------------------|| 

interact * ** == (input,*) -> (input,**,output)

||----------------------------------------------------------------------||
||									||
||	A general interaction will consume some input, and produce	||
||	some output. The remainder of the input is returned too.	||
||									||
||	What about * **? These represent information about the state	||
||	of the machine before and after the interaction has taken	||
||	place. In a previous version					||
||	the state-info type was taken to be the same before and 	||
||	after the interaction - this results in some inelegancies:	||
||	Often an interaction can be used to ``pick up'' information	||
||	of a particular type - if this is to be modelled by an		||
||	interaction of the old kind, a dummy value has to be passed	||
||	inwards. We replace this with the unique value, (), of the one-	||
||	element type ().						||
||									||
||----------------------------------------------------------------------||

write :: string -> interact * *

write outstring (in,st) 
      = (in,st,[outstring])

writeln :: string -> interact * *

writeln outstring (in,st) 
      = (in,st,[outstring++"\n"])

||----------------------------------------------------------------------||
||	write and writeln push a string onto the output stream,		||
||	without modifying input or state				||
||----------------------------------------------------------------------||

readin :: interact () string

readin (in,())
      = (tl in,hd in,[])

||----------------------------------------------------------------------||
||	readin extracts the first string from the input stream,		||
||	and returns it using the state place in its output.		||
||----------------------------------------------------------------------||

||----------------------------------------------------------------------||
||									||
||	make_output 	is the function which puts its first		||
||	argument, a piece of output, at the front of the output		||
||	stream.								||
||									||
||	It is used in the rept function so that the piece of		||
||	output will appear on the output stream BEFORE the condition	||
||			~ cond next					||
||	is evaluated							||
||									||
||----------------------------------------------------------------------||

make_output :: output -> (input,*,output) -> (input,*,output)

make_output piece (in,st,out) = (in,st,piece++out)

||----------------------------------------------------------------------||
||									||
||	Some traditional control structures:				||
||									||
||	A condition is seen as a boolean function taking TWO 		||
||	arguments, the current input stream together with		||
||	the state. Hence the following type definition:			||
||									||
||----------------------------------------------------------------------||

condition * == (input,*) -> bool

||----------------------------------------------------------------------|| 
||	alt is an alternative command, which preforms the first of the	||
||	second of its interaction arguments depending upon the		||
||	(boolean) value of the condition.				||
||----------------------------------------------------------------------|| 

alt :: condition * -> interact * ** -> interact * ** -> interact * **

alt cond inter1 inter2 x
	= inter1 x , if cond x
	= inter2 x , otherwise

||----------------------------------------------------------------------|| 
||	The following sequencing functions perform a number of inter-	||
||	actions in sequence. sq takes two, seq3 and seq4 take three 	||
||	four respectively. seqlist will combine a list, but note that	||
||	as lists are homogeneous, all the interactions in the list need	||
||	to be of the same type, i.e. have the same state type 		||
||	on initiation and termination.					||
||	Pascal's infix operator `;' is given by the infix $sq.		||
||----------------------------------------------------------------------|| 

sq :: interact * ** -> interact ** *** -> interact * ***

sq inter1 inter2 x
      = make_output out1 (inter2 (rest,st))
	where (rest,st,out1) = inter1 x

seq3 :: interact * ** -> interact ** *** -> interact *** **** -> interact * ****

seq3 inter1 inter2 inter3
      = sq inter1
	    (sq inter2 inter3)

seq4 :: interact * ** -> interact ** ***
	-> interact *** **** -> interact **** *****
	-> interact * *****

seq4 inter1 inter2 inter3 inter4
      = sq inter1
	    (seq3 inter2 inter3 inter4)

seqlist :: [interact * *] -> interact * *

seqlist = foldr sq null

||----------------------------------------------------------------------|| 
||	while and repeat take an interaction and iterate it in the 	||
||	usual way:							||
||	with while, the condition is first evaluated, and if true the	||
||	interaction is performed, and the loop re-invoked. For repeat	||
||	the interaction is performed, and only if the condition fails	||
||	is the loop re-entered.						||
||									||
||	Note how higher-order definitions can be given: given alt and	||
||	sq we simply need to use recursion to give the iterators.	||
||----------------------------------------------------------------------|| 

while ::  condition * -> interact * * -> interact * *

while cond inter 
      = whi
	where
	whi = alt cond (inter $sq whi) null

rept  ::  condition * -> interact * * -> interact * *

rept cond inter
      = inter $sq (while ((~).cond) inter)

||----------------------------------------------------------------------||
||									||
||	We can build a state by the parallel application of 		||
||	a number of interactions.					||
||	We have parallelism in the sense that the second (and		||
||	subsequent) interactions					||
||	are performed in the initial state.				||
||									||
||----------------------------------------------------------------------||

par :: interact * ** -> interact * *** -> interact * (**,***)

par inter1 inter2 (in,st)
      = (rest2,(st1,st2),out1++out2)
	where
	(rest1,st1,out1) = inter1 (in,st)
	(rest2,st2,out2) = inter2 (rest1,st)

par3 :: interact * ** -> interact * *** ->
	interact * **** -> interact * (**,***,****)

par3 inter1 inter2 inter3 (in,st)
      = (rest3,(st1,st2,st3),out1++out2++out3)
	where
	(rest1,st1,out1) = inter1 (in,st)
	(rest2,st2,out2) = inter2 (rest1,st)
	(rest3,st3,out3) = inter3 (rest2,st)

||----------------------------------------------------------------------||
||									||
||	Function application as an interaction				||
||									||
||----------------------------------------------------------------------||

apply :: (* -> **) -> interact * **

apply f (in,st) = (in, f st , [])

||----------------------------------------------------------------------||
||									||
||	The null interaction is not simply the identity transformation,	||
||	since we must register the fact that it produces no output;	||
||	that is done by the next definition.				||
||									||
||----------------------------------------------------------------------||

null :: interact * *

null (in,st) = (in,st,[])

||----------------------------------------------------------------------||
||									||
||	Almost the same as the null interaction, except that we		||
||	forget the state information.					||
||									||
||----------------------------------------------------------------------||

forget :: interact * ()

forget (in,st)
      = (in,(),[])

||----------------------------------------------------------------------||
||									||
||	The ``inverse'' of the forget operation: gives the state a	||
||	starting value.							||
||									||
||----------------------------------------------------------------------||

start :: * -> interact () *

start v (in,()) = (in,v,[])

||----------------------------------------------------------------------||
||									||
||	changing :- putting forgetting and starting together:		||
||									||
||----------------------------------------------------------------------||

change :: ** -> interact * **

change n = sq forget (start n)

||----------------------------------------------------------------------||
||									||
||	This interaction checks its input state, so that it forces	||
||	evaluation of what precedes it. In the situation of		||
||		seq3 write read (write "Thanks")			||
||	we want the second write					||
||	to act only AFTER the read has been performed - this can be	||
||	achieved by prefacing it by a wait.				||
||	Thanks are due to Steve Hill for the example above		||
|| 	which stimulated this definition.				||
||									||
||----------------------------------------------------------------------||

wait :: interact * *
 
wait (in,x) = seq x (in,x,[])

||----------------------------------------------------------------------||
||									||
||	adding values to the state					||
||									||
||----------------------------------------------------------------------||

add_val_right v = add_val_r v null

add_val_r :: * -> interact ** *** -> interact ** (***,*)

add_val_r v inter 
      = (add_r v) . inter
	where
	add_r v (a,b,c) = (a,(b,v),c)

add_val_left v = add_val_l v null

add_val_l :: * -> interact ** *** -> interact ** (*,***)

add_val_l v inter 
      = (add_l v) . inter
	where
	add_l v (a,b,c) = (a,(v,b),c)

||----------------------------------------------------------------------||
||									||
||	functions which will pass state information around		||
||									||
||----------------------------------------------------------------------|| 

pass_on :: interact * ** -> interact (*,***) (**,***)
pass_on_l :: interact * ** -> interact (***,*) (***,**)
pass_on_r :: interact * ** -> interact (*,***) (**,***)


pass_on = pass_on_r

pass_on_l inter (in,(st3,st1))
      = (rest,(st3,st2),out)
	where
	(rest,st2,out) = inter (in,st1)

pass_on_r inter (in,(st1,st3))
      = (rest,(st2,st3),out)
	where
	(rest,st2,out) = inter (in,st1)


||----------------------------------------------------------------------||
||									||
||	The first interaction gathers a value, st1, of type **. 	||
||	We then	perform the interaction delivered by applying the	||
||	second argument, a function, to st1.				||
||									||
||----------------------------------------------------------------------||

pass_param :: interact * ** ->
	      ( ** -> interact () **** ) ->
	      interact * ****

pass_param int f (in,st)
      = (rest,final,out1++out)
	where
	(inter1,st1,out1) = int (in,st)
	(rest,final,out) = (f st1) (inter1,())

||----------------------------------------------------------------------||
||									||
||	In order to get these interactions to run on the Miranda	||
||	system, we have to evaluate an expression which gives		||
||	rise to the stream of output required. 				||
||									||
||	run will run an interaction from a starting state to 		||
||	termination, if that happens, printing the final state		||
||	if termination occurs.				 		||
||	run accepts input from stdin and must be supplied with a	||
||	`show' function for the final state. This is its third		||
||	parameter.							||
||									||
||----------------------------------------------------------------------||

run :: interact * ** -> * -> (** -> raw_output) -> raw_output

run inter st g
      = join out ++ g final
	where
	(rest,final,out) = inter (split (read stdin),st)

||----------------------------------------------------------------------|| 
||	dumprun causes the final state to be dumped in the file		||
||	which is passed as the third parameter.				||
||----------------------------------------------------------------------|| 

dumprun :: interact * ** -> * -> [char] -> (** -> raw_output) -> [sys_message]

dumprun inter st fil g
      = [ Stdout (join out) , Tofile fil (g final) ]
	where
	(rest,final,out) = inter (split (read stdin),st)
||----------------------------------------------------------------------|| 
||	SOME EXAMPLES							||
||----------------------------------------------------------------------|| 

||----------------------------------------------------------------------||
||									||
||	Interactions to try to get positive integers or integers.	||
||	The user is prompted once. If a correct input is produced,	||
||	it is returned, together with a flag value True. If not		||
||	the flag is set to False, (and a dummy value of 0 is returned)	||
||									||
||----------------------------------------------------------------------||

getposint :: interact () (num,bool)

getposint 
      = seq3 (write "Please enter a positive integer: ")
	     readin
	     (alt (numeric_string.snd)
		    (sq (apply string_posint)
			 (add_val_right True))
		    (seq3 (write "Not a positive integer, try again.\n")
			  forget
			  (start (0,False))))

getint :: interact () (num,bool)

getint 
      = seq3 (write "Please enter an integer: ")
	     readin
	     (alt (integer_string.snd)
		    (sq (apply string_int)
			 (add_val_right True))
		    (seq3 (write "Not an integer, try again.\n")
			  forget
			  (start (0,False))))

||----------------------------------------------------------------------||
||									||
||	newgetint is a new version of getint, which is parametrised	||
||	on its prompt, error message and checking function. It is	||
||	defined much as getstring, except that it caters for two 	||
||	kinds of error							||
||		not typing (a string representing an) integer		||
||	and								||
||		not typing an integer in the appropriate set		||
||									||
||	newgetposint acts similarly					||
||									||
||----------------------------------------------------------------------||

newgetint :: string -> string -> (num -> bool) -> interact () (num,bool)

newgetint prompt err_mess checkfun (in,())
      = make_output [prompt] aux
	where
	aux = (rest,outst,out)
	(outst,out) = ((0,False),["Not integer string; try again\n"])
					, if ~ integer_string a
	            = ((0,False),[err_mess++"\n"]) , if ~ checkfun num_a
		    = ((num_a ,True),[]) , otherwise
	a = hd in
	rest = tl in
	num_a = string_int a

newgetposint :: string -> string -> (num -> bool) -> interact () (num,bool)

newgetposint prompt err_mess checkfun (in,())
      = make_output [prompt] aux
	where
	aux = (rest,outst,out)
	(outst,out) = ((0,False),["Not positive integer string; try again\n"])
					, if ~ numeric_string a
	            = ((0,False),[err_mess++"\n"]) , if ~ checkfun num_a
		    = ((num_a ,True),[]) , otherwise
	a = hd in
	rest = tl in
	num_a = string_posint a

||----------------------------------------------------------------------||
||									||
||	getstring tries once to get a string. It prompts with its	||
||	first string argument, and outputs an error message if the	||
||	string doesn't meet the requirement of checkfun. It returns	||
||	the value of checkfun on the input, together with the input	||
||	itself.								||
||									||
||----------------------------------------------------------------------||

getstring :: string -> string -> (string -> bool) 
	     -> interact () (string,bool)

getstring prompt error_mess checkfun (x,())
      = make_output [prompt] aux
	where
	aux = (y,(a,ok),out)
	ok  = checkfun a
	out = [],                    if ok
	    = [ error_mess++"\n" ] , otherwise
	a   = hd x		||	Delayed pattern matching
	y   = tl x

||----------------------------------------------------------------------||
||									||
||	Often want to try repeatedly to get an integer - iterate 	||
||	a trial until it is successful - this can be performed using	||
||	control structures given in the file control.m			||
||									||
||	inputposint,inputint apply the functions getposint and getint	||
||	repeatedly until a valid input is found.			||
||									||
||	in_posint in_int do the same, but also perform a validity	||
||	check on their input accordint to the boolean function		||
||			checkfun					||
||	the prompt and the error message corresponding to checkfun	||
||	are also passed as parameters.					||
||									||
||----------------------------------------------------------------------||

inputposint :: interact () num

inputposint
      = seq3 (start (0,False)) 
	     (rept is_ok fetchposint) 
	     (apply num_part)
	where
	is_ok (in,(a,b)) = b
	fetchposint      = sq forget getposint
	num_part (a,b)   = a

