import math

# Num a => a -> a -> a
sum2 = lambda x0: lambda x1: x0 + x1

# Num a => a -> a -> a -> a
sum3 = lambda x0: lambda x1: lambda x2: sum2(sum2(x0)(x1))(x2)

# Num a => a -> a -> a -> a -> a
sum4 = lambda x0: lambda x1: lambda x2: lambda x3: x0 + x1 + x2 + x3

# Num a => a -> a -> a -> a -> a -> a
sum5 = lambda x0: lambda x1: lambda x2: lambda x3: lambda x4: x0 + x1 + x2 + x3 + x4

# Num a => a -> a -> a -> a -> a -> a -> a
sum6 = lambda x0: lambda x1: lambda x2: lambda x3: lambda x4: lambda x5: x0 + x1 + x2 + x3 + x4 + x5

# Num a => a -> a -> a -> a -> a -> a -> a -> a
sum7 = lambda x0: lambda x1: lambda x2: lambda x3: lambda x4: lambda x5: lambda x6: x0 + x1 + x2 + x3 + x4 + x5 + x6

# Num a => a -> a -> a -> a -> a -> a -> a -> a -> a
sum8 = lambda x0: lambda x1: lambda x2: lambda x3: lambda x4: lambda x5: lambda x6: lambda x7: x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7

# Int -> Int -> Int
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Int -> Int -> Int
power = lambda x: lambda n: 1 if n == 0 else x * power(x)(n-1)

# Int -> Int -> Int
int_div = lambda numerator: lambda denominator: 1 + int_div(numerator - denominator)(denominator) if numerator >= denominator else 0

# Num a => a -> a
double = lambda x: x + x

# Num a => a -> a -> a
times = lambda x: lambda y: x * y

# Float a => a -> a -> a
div = lambda x: lambda y: x / y

minus = lambda x: lambda y: sum2(x)(-y)

cos = math.cos

sin = math.sin

tan = math.tan

floor = math.floor

ceil = math.ceil

absolute = lambda x: x if x >= 0 else -x

modulo = lambda x: lambda y: modulo(x - y)(y) if x >= y else x
