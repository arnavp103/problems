module CalculatingWithFunctions (plus, minus, times, dividedBy, zero, one, two, three, four, five, six, seven, eight, nine) where

-- want to do things like five (times (seven)) = 35
-- or (four $ plus $ nine) = 13

-- that means seven (and therefore five) has to be a function that takes a function as an argument

plus, minus, times, dividedBy :: ((Int -> Int) -> Int) -> (Int -> Int)
plus num = (+) (num id)
minus num = flip (-) (num id)
times num = (*) (num id)
dividedBy num = flip div (num id)

zero, one, two, three, four, five, six, seven, eight, nine :: (Int -> Int) -> Int
zero f = f 0
one f = f 1
two f = f 2
three f = f 3
four f = f 4
five f = f 5
six f = f 6
seven f = f 7
eight f = f 8
nine f = f 9
