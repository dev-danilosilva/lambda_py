# lambda_py

Set of lazily evaluated python functions.


- The lazyness is achivied by curried functions.

- Because this functions are being written as I think and read about some lambda calculus ideas, you will see
  - functions written almost entirely using python lambda functions
  - no statements on function's body, only expressions
  - recursion as a tool for repetition
  - some simple data structures using just functions.

### The data structure thing:

- I've implemented an immutable pair by using functions.

Example:

```python
from lambda_py.lazy_pair import *
import lambda_py.math as m

# This is how you can create a pair

pair = Pair(3)(4)

# showing the evaluation lazyness building a pair in distinct moments 

partially_applied_pair_of_numbers = Pair(3)
pair = partially_applied_pair_of_numbers(4) # 'point' is a pair (3, 4)


# To get a string representation of the pair, you need send the 'show' function to the pair:

pair(show)

# You can get the first element of this pair by passing a function called 'first' to the pair:

pair(first) # -> 3

# or get the second similarly

pair(second) # -> 4

# the map_ function creates a new pair whose values is a transformation of the original pair:

pair2 = pair(map_(lambda x: x + 2)) # -> (5,6)

pair3 = pair(map_(m.double)) # -> (6,8)

times3 = m.times(3) # lazy times function

pair4 = pair(map_(lambda x: times3(x))) # -> (9, 12)

# chain of tranformations.
pair5 = pair (map_(lambda x: x + 2)) \
             (map_(lambda x: x * 2)) \
             (map_(times3))
```

A tuple of 3 elements was implemented with the same api
