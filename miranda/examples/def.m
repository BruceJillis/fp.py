foo a b 
	= foo (b-a) a, if b > a
	= foo a (a-b), if a > b
	= 1, otherwise
foo 10 20