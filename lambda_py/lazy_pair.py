# a -> a -> (a -> a -> b) -> b
pair = lambda x: lambda y: lambda f: f (x) (y)

# a -> a -> a
first = lambda x: lambda _: x

# a -> a -> a
second = lambda _: lambda x: x

# (a -> b) -> a -> a -> ((a -> a -> b) -> b)
map_ = lambda func: lambda x: lambda y: pair (func(x)) (func(y))

# ((a -> a -> b) -> b) -> String
show = lambda pair: f'Pair {pair(first)} {pair(second)}'

