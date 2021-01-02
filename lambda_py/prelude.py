# a -> a
identity = lambda x: x


# (a -> b) -> a -> b
apply = lambda f: lambda x: f(x)


# It's impossible to define a type to this function,
# because it is not possible to say if the evaluation will ever terminate
self_apply = lambda expr: expr(expr)



# a -> b -> (a -> b -> c) -> c
cond_ = lambda expr1: lambda expr2: lambda cond_func: cond_func(expr1)(expr2)

# true == select_first
true_ = lambda x: lambda y: x

# false == select_second
false_ = lambda x: lambda y: y

not_ = lambda bool_expr: cond_(false_)(true_)(bool_expr) 

# simplified version => x(y)(false)
and_ = lambda x: lambda y: cond_(y)(false_)(x)

or_ = lambda x: lambda y: cond_(true_)(y)(x)


