
triple = lambda x: lambda y: lambda z: lambda f: f(x)(y)(z)

first = lambda x: lambda y: lambda z: x

second = lambda x: lambda y: lambda z: y

third = lambda x: lambda y: lambda z: z

map_ = lambda func: lambda x: lambda y: lambda z: triple(func(x))(func(y))(func(z))
