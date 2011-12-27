||This script generates a solution to the well known `Towers of Hanoi'
||problem.  To see the moves (for a game with 8 discs) say
||	soln

soln = title++hanoi 8 "A" "B" "C"
title = "SOLUTION TO TOWERS OF HANOI WITH 8 DISCS\n\n"
hanoi 0 a b c = [] 
hanoi (n+1) a b c = hanoi n a c b
	            ++ move a b ++
	            hanoi n c b a
move a b = "move the top disc from "++a++" to "++b++"\n"
