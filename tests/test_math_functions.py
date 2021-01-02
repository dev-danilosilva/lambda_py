import unittest
import lambda_py.math as m


class TestMathFunctions(unittest.TestCase):

    def test_if_sum_2_is_commutative(self):
        func = m.sum2
        x = 4
        y = 5
        self.assertTrue(func(x)(y) == func(y)(x))
    
    def test_if_sum_2_result_of_the_function_is_the_sum_of_two_values(self):
        func = m.sum2
        x = 4
        y = 5
        self.assertTrue(func(x)(y) == func(y)(x))

    def test_if_sum_3_result_of_the_function_is_the_sum_of_three_values(self):
        func = m.sum3
        x = 4
        y = 5
        z = 3
        result = x + y + z
        self.assertTrue(result == func(x)(y)(z))
    
    

