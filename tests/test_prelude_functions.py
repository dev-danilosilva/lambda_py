import unittest
import lambda_py.prelude as prelude
import lambda_py.lazy_pair as p
import lambda_py.math as m


class TestPreludeFunctions(unittest.TestCase):

    def test_if_identity_function_returns_the_same_value_passed_as_argument(self):
        value = 3
        self.assertTrue(prelude.identity(value) == value)

    
    def test_if_the_apply_function_applies_correctly_a_given_function(self):
        f = m.double
        x = 3
        fx = f(x)
        self.assertTrue(prelude.apply(f)(x) == fx)
    

    def test_if_self_applying_the_second_function_results_in_the_identity_function(self):
        '''
        Tests the following function applications

        self_apply = λs.(s s)
        second = λx.λy.y
        identity = λx.x

        identity ==
            (self_apply second) => (second second) => (λx.λy.y λx'.λy'.y') => λy.y

        '''
        value = 29
        self.assertTrue(prelude.self_apply(p.second)(value) == value)
    

    def test_if_conditinal_is_works_as_expeted(self):
        self.assertTrue(prelude.cond_(True)(False)(prelude.true_))
        self.assertFalse(prelude.cond_(True)(False)(prelude.false_))
    
    def test_if_not_function_works_as_expected(self):
        self.assertFalse(prelude.cond_(True)(False)(prelude.not_(prelude.true_)))
        self.assertTrue(prelude.cond_(True)(False)(prelude.not_(prelude.false_)))

    def test_if_and_function_works_as_expected(self):
        self.assertTrue(prelude.cond_(True)(False)(prelude.and_(prelude.true_)(prelude.true_)))
        self.assertFalse(prelude.cond_(True)(False)(prelude.and_(prelude.false_)(prelude.true_)))
        self.assertFalse(prelude.cond_(True)(False)(prelude.and_(prelude.true_)(prelude.false_)))
        self.assertFalse(prelude.cond_(True)(False)(prelude.and_(prelude.false_)(prelude.false_)))

    
