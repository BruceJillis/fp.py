test (Leaf a b)        = (test a) + (test b)
test (Nilt)            = 1
test (Branch a (Nilt)) = 1
test (Branch (Leaf a)) = 1
test 2