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
        y = -5
        z = 3
        result = x + y + z
        self.assertTrue(result == func(x)(y)(z))
    

    def test_if_sum_4_result_of_the_function_is_the_sum_of_three_values(self):
        func = m.sum4
        w = 34
        x = 4
        y = -5
        z = 3
        result = w + x + y + z
        self.assertTrue(result == func(w)(x)(y)(z))
    
    
    def test_if_sum_5_result_of_the_function_is_the_sum_of_five_values(self):
        func = m.sum5
        v = 1000
        w = 0
        x = 4
        y = 5
        z = -3
        result = v + w + x + y + z
        self.assertTrue(result == func(v)(w)(x)(y)(z))


    def test_if_sum_6_result_of_the_function_is_the_sum_of_six_values(self):
        func = m.sum6
        u = 234
        v = 1000
        w = 0
        x = 4
        y = -5
        z = 3
        result = u + v + w + x + y + z
        self.assertTrue(result == func(u)(v)(w)(x)(y)(z))


    def test_if_sum_7_result_of_the_function_is_the_sum_of_seven_values(self):
        func = m.sum7
        t = -45
        u = 234
        v = 1000
        w = 0
        x = 4
        y = 5
        z = 3
        result = t + u + v + w + x + y + z
        self.assertTrue(result == func(t)(u)(v)(w)(x)(y)(z))
    
    def test_if_sum_8_result_of_the_function_is_the_sum_of_three_values(self):
        func = m.sum8
        s = 23
        t = 5
        u = 234
        v = 1000
        w = 0
        x = 4
        y = 5
        z = 3
        result = s + t + u + v + w + x + y + z
        self.assertTrue(result == func(s)(t)(u)(v)(w)(x)(y)(z))
    
    def test_if_the_power_of_2_by_2_is_4(self):
        self.assertEqual(m.power(2)(2), 4)
    
    def test_if_the_power_of_4_by_2_is_16(self):
        self.assertEqual(m.power(4)(2), 16)
    
    def test_if_the_power_of_1000_by_0_is_1(self):
        self.assertEqual(m.power(1000)(0), 1)
    
    def test_if_the_interger_division_of_100_by_40_is_20(self):
        self.assertEqual(m.int_div(10)(2), 5)

    def test_if_the_interger_division_of_100_by_40_is_20(self):
        self.assertEqual(m.int_div(100)(40), 2)

    def test_if_the_absolute_value_of_a_positive_number_is_equal_to_itself(self):
        x = 30
        self.assertEqual(m.absolute(x), x)
    
    def test_if_the_absolute_value_of_a_negative_number_is_equal_to_the_oposite_of_this_number(self):
        x = -30
        self.assertEqual(m.absolute(x), -x)
    
    def test_if_the_mod_of_10_by_5_is_0(self):
        self.assertTrue(m.mod(10)(5) == 0)
    
    def test_if_the_mod_of_100_by_40_is_20(self):
        self.assertTrue(m.mod(100)(40) == 20)