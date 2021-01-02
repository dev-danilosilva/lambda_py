import unittest
import lambda_py.lazy_triple as t
import lambda_py.math as m


class TestTripleFunctions(unittest.TestCase):
    def test_if_triple_first_returns_the_first_element(self):
        x = 2
        y = 4
        z = 9
        triple = t.triple(x)(y)(z)
        self.assertTrue(triple(t.first) == x)
    
    def test_if_triple_second_function_returns_the_second_element(self):
        x = 2
        y = 3
        z = 9
        triple = t.triple(x)(y)(z)
        self.assertTrue( triple(t.second) == y )
    
    def test_if_map_function_transforms_the_triple_elements_correctly(self):
        func = m.double
        
        x0 = 2
        y0 = 3
        z0 = 4

        p0 = t.triple(x0)(y0)(z0)

        x1 = func(x0)
        y1 = func(y0)
        z1 = func(z0)

        p1 = p0(t.map_(func))

        x2 = p1(t.first)
        y2 = p1(t.second)
        z2 = p1(t.third)

        self.assertTrue(x1 == x2 and y1 == y2 and z1 == z2)