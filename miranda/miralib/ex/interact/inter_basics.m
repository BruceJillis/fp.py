
||----------------------------------------------------------------------||
||									||
||	inter_basics.m							||
||									||
||	Contains various auxilliary functions and definitions for	||
||	input/output							||
||									||
||	Version 1.0		18 September 1989			||
||									||
||	Simon Thompson, Computing Lab., Univ. of Kent.			||
||	sjt@ukc.ac.uk							||
||									||
||	This file is used by the interaction primitives in		||
||		interaction.m						||
||									||
||----------------------------------------------------------------------||

string     == [char]
input      == [string]
output     == [string]
raw_input  == [char]
raw_output == [char]

||----------------------------------------------------------------------||
||									||
||	The fundamental type definitions				||
||									||
||	Note that we have chosen to consider input and output as	||
||	consisting of streams of strings rather than streams of		||
||	char. Conversion to and from the ``raw'' versions is trivial:	||
||	raw_input is split at newlines, and raw_output is the result	||
||	of concatenating the string forming the output stream. (Note	||
||	that this means that we are explicit about the placing of	||
||	newlines etc.							||
||									||
||----------------------------------------------------------------------||

newline = '\n'
space   = ' '
tab	= '\t'

stdin = "/dev/tty"	

||----------------------------------------------------------------------||
||	Some sensible names. Note that stdin names standard input	||
||	as a file.							||
||----------------------------------------------------------------------||

split     :: raw_input -> input
gen_split :: char -> raw_input -> input

||----------------------------------------------------------------------||
||									||
||	split splits raw_input into lines. Defined in terms of the	||
||	more general gen_split which splits input at occurrences of 	||
||	its first argument, a character.				||
||									||
||	Following these definitions we have two more general ones, 	||
||	developed in the course of writing a text processing		||
||	system. They are more general in that they allow 		||
||		1. splitting on more than one character			||
||		2. multiple occurrences of the splitting characters	||
||		to be treated in a similar way to single occurrences.	||
||----------------------------------------------------------------------||

split = gen_split newline

gen_split ch l
      = aux_split ch [] l
	where
	aux_split ch sofar (a:rest)
		= reverse sofar : gen_split ch rest,  if a=ch
		= aux_split ch (a:sofar) rest,        otherwise
	aux_split ch sofar []
		= [ reverse sofar ]

||----------------------------------------------------------------------||
||	Splitting lists into lists of lists according to membership	||
||	of a `split_set'						||
||	Lists can be split into sublists in two slightly different	||
||	ways, depending on how we treat repeated occurrences of		||
||	members of the split_set. We can either treat a repetition	||
||	as delimiting an empty list, as we do in `cut', or we 		||
||	can treat repetitions as single instances, which we do in	||
||	`simple_cut'.							||
||	Both flavours have their uses.					||
||----------------------------------------------------------------------||

cut :: [*] -> [*] -> [[*]]

cut split_set [] = []
cut split_set (a:x) 
      = cut_aux [] (a:x)
	where
	cut_aux l []    = [l], if l ~= []
			= [],  otherwise
	cut_aux l (a:x) = cut_aux (l++[a]) x, if ~ member split_set a
		        = l : (cut_aux [] x), otherwise
			  
		      
simple_cut :: [*] -> [*] -> [[*]]

simple_cut split_set [] = []
simple_cut split_set (a:x) 
      = cut_aux [] (a:x)
	where
	cut_aux l []    = [l], if l~=[]
			= [],  otherwise
	cut_aux l (a:x) = cut_aux (l++[a]) x, if ~ member split_set a
		        = l : (cut_aux [] x), if l ~= []
			= cut_aux [] x, otherwise
		      
join      :: output -> raw_output

||----------------------------------------------------------------------||
||	join joins lines, and is an alias for concat.			||
||----------------------------------------------------------------------||

join = concat				||	from the standard envt.

||----------------------------------------------------------------------|| 
||									||
||	Dealing with basic types, of numbers and characters.		||
||									||
||----------------------------------------------------------------------|| 

numeric      :: char -> bool		||	To test for particular
alpha        :: char -> bool		||	kinds of character.
alphanumeric :: char -> bool

numeric = digit				||	from the standard envt.
alpha   = letter			||	ditto.
alphanumeric ch = alpha ch \/ numeric ch 

||----------------------------------------------------------------------||
||									||
||	Testing for strings consisting of particular kinds of		||
||	character							||
||	Note that the empty string is classed as being in the 		||
||	respective classes.						||
||									||
||----------------------------------------------------------------------||

numeric_string      :: string -> bool
alpha_string        :: string -> bool
alphanumeric_string :: string -> bool
integer_string      :: string -> bool

numeric_string      = foldr (&) True . map numeric
alpha_string        = foldr (&) True . map alpha
alphanumeric_string = foldr (&) True . map alphanumeric
integer_string x    = numeric_string x \/ ( hd x = '-' & numeric_string (tl x) )

||----------------------------------------------------------------------||
||									||
||	Converting strings to numbers and vice versa.			||
||	The empty numeric string is translated as zero.			||
||									||
||----------------------------------------------------------------------||

string_posint :: string -> num
string_int    :: string -> num

string_posint
      = conv_aux . reverse
	where
	conv_aux (a:x) = (code a - code '0') + 10 * conv_aux x, if numeric a
		       = error "string_posint found non-numeric character",
				otherwise
	conv_aux []    = 0

string_int (a:x)
      = string_posint (a:x), if numeric a
      = - (string_posint x), if a = '-'
      = error "unexpected first character to string_int"
				, otherwise
string_int [] = 0

num_string :: num -> string

num_string = show		||	A standard function
