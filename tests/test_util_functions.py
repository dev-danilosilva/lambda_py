import unittest
import lambda_py.util as util
import lambda_py.lazy_pair as p
import lambda_py.math as m


class TestutilFunctions(unittest.TestCase):

    def test_if_identity_function_returns_the_same_value_passed_as_argument(self):
        value = 3
        self.assertTrue(util.identity(value) == value)

    
    def test_if_the_apply_function_applies_correctly_a_given_function(self):
        f = m.double
        x = 3
        fx = f(x)
        self.assertTrue(util.apply(f)(x) == fx)
    

    def test_if_self_applying_the_se_condfunction_results_in_the_identity_function(self):
        '''
        Tests the following function applications

        self_apply = λs.(s s)
        second = λx.λy.y
        identity = λx.x

        identity ==
            (self_apply second) => (second second) => (λx.λy.y λx'.λy'.y') => λy.y

        '''
        value = 29
        self.assertTrue(util.self_apply(p.second)(value) == value)
    

    def test_if_conditinal_is_works_as_expeted(self):
        self.assertTrue(util._cond(True)(False)(util._true))
        self.assertFalse(util._cond(True)(False)(util._false))
    
    def test_if_not_function_works_as_expected(self):
        self.assertFalse(util._cond(True)(False)(util._not(util._true)))
        self.assertTrue(util._cond(True)(False)(util._not(util._false)))

    def test_if_and_function_works_as_expected(self):
        self.assertTrue(util._cond(True)(False)(util._and(util._true)(util._true)))
        self.assertFalse(util._cond(True)(False)(util._and(util._false)(util._true)))
        self.assertFalse(util._cond(True)(False)(util._and(util._true)(util._false)))
        self.assertFalse(util._cond(True)(False)(util._and(util._false)(util._false)))

    
