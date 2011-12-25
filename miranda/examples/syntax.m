remainder = 10 mod 4
# expressions
integer = 3 div 2
float = 3 / 2
byte = 2^8 + 2
negint = -1
negfloat = -1.2
cmp = 1 < 2 < 3
wrong = not true
not_wrong = (1,2) == (1,2)
list = [1] ++ [1,2,3] ++ [] -- [2,3]
a_tuple = (1 + 2, 2 * (2 + 3))
hours = 24 + (1 + 2)
days  = 2
# sections
a1 = a / b
a2 = (/) a b
a3 = (a /) b
a4 = (/ b) a
# -2 -> 0 - 2
# - 2 -> section (- 2)
a5 = (- 2) 1
testsec = apply (- 2) [1,2,3]
# arguments
twice x = x * x
toupper c = decode ((code c) - (code 'a') + (code 'A'))

# TODO: offside rule
# offside1 
# 	= 1
# offside2 a = message ++ 
# 			    " at " ++ (show time) ++ " oclock"
# cjustify n s = spaces lmargin++s++spaces rmargin
# 				   where
# 				   margin = n - # s
# 	            lmargin = margin div 2
# 		         rmargin = margin - lmargin

# pattern matching
match (1,2) = 1
match [] = 1
match [a,b] = 1
match a:b:[] = 1
match a:[b] = 0
match 0 = 1
match n = 1
match y-1 = y
match y+1 = y
factorial 0 = 1
factorial(n+1) = (n+1)*factorial n
reverse [] = []
reverse (a:x) = reverse x ++ [a]
last [a] = a
last (a:x) = last x, if x != []
last [] = error "last of empty list"
and = foldr (&) True
and true false = true
and false true = true
and false false = false
test x = x, if x != [1,2,3]
test 0 = 1
hours * days