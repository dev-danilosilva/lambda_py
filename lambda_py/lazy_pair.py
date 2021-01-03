# a -> a -> (a -> a -> b) -> b
Pair = lambda x: lambda y: lambda f: f (x) (y)

# a -> a -> a
first = lambda x: lambda _: x

# a -> a -> a
second = lambda _: lambda x: x

# (a -> b) -> a -> a -> ((a -> a -> b) -> b)
map_ = lambda func: lambda x: lambda y: Pair (func(x)) (func(y))

# ((a -> a -> b) -> b) -> String
show = lambda x: lambda y: f'Lazy Pair ({x}, {y})'

