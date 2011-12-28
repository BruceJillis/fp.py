mappairs f []     ys     = []
mappairs f (x:xs) []     = []
mappairs f (x:xs) (y:ys) = f x y : mappairs f xs ys
mappairs (+) [1,2] [3,4]