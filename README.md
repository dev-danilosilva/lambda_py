# lambda_py

Set of lazily evaluated python functions.


- The lazyness is achivied by curried functions.

- Because this functions are being written as I think and read about some lambda calculus ideas, you will see
  - functions written almost entirely using python lambda functions
  - no statements on function's body, only expressions
  - recursion as a tool for repetition
  - some simple data structures using just functions.

### The data structure thing:

- I've implemented a pair by using functions.

Example:

```python
from lambda_py.lazy_pair import *

# This is how you can create a pair

point = pair(3)(4)

# showing the evaluation lazyness building a pair in distinct moments 

partially_applied_pair_of_numbers = pair(3)
point = partially_applied_pair_of_numbers(4) # 'point' is a pair (3, 4)


# To get a string representation of the pair, you need send the 'show' function to the pair:

point(show)

# You can get the first element of this pair by passing a function called 'first' to the pair:

point(first) # gets 3

# or get the second similarly

point(second)

# the map_ function creates a new pair whose values is a transformation of the original pair:

point2 = point(map_(lambda x: x + 2))

```
