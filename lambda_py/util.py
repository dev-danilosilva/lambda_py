# a -> a
identity = lambda x: x


# (a -> b) -> a -> b
apply = lambda f: lambda x: f(x)


# It's impossible to say if the evaluation will ever terminate
self_apply = lambda expr: expr(expr)


# a -> b -> (a -> b -> c) -> c
_cond = lambda expr1: lambda expr2: lambda _condfunc: _condfunc(expr1)(expr2)

# true == select_first
_true = lambda x: lambda y: x

# false == select_second
_false = lambda x: lambda y: y

_not = lambda bool_expr: _cond(_false)(_true)(bool_expr) 

# simplified version => x(y)(false)
_and = lambda x: lambda y: _cond(y)(_false)(x)

_or = lambda x: lambda y: _cond(_true)(y)(x)


