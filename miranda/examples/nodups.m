nodups []       = []
nodups [x]      = [x]
nodups (y:x:xs) = nodups (x:xs), if y = x
                = y : nodups (x:xs), otherwise
nodups [1,2,2,3]