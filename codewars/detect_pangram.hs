module Pangram where

import Data.Char

isPangram :: String -> Bool
isPangram str = all (`elem` lowers) ['a' .. 'z']
  where
    lowers = map toLower str