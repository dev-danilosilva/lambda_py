import unittest
import lambda_py.lazy_pair as p
import lambda_py.math as m


class TestPairFunctions(unittest.TestCase):
    def test_if_pair_first_returns_the_first_element(self):
        x = 2
        y = 4
        pair = p.pair(x)(y)
        self.assertTrue(pair(p.first) == x)
    
    def test_if_pair_second_function_returns_the_second_element(self):
        x = 2
        y = 3
        pair = p.pair(x)(y)
        self.assertTrue( pair(p.second) == y )
    
    def test_if_map_function_transforms_the_pair_elements_correctly(self):
        func = m.double
        
        x0 = 2
        y0 = 3
        p0 = p.pair(x0)(y0)

        x1 = func(x0)
        y1 = func(y0)
        p1 = p0(p.map_(func)) # main test function

        x2 = p1(p.first)
        y2 = p1(p.second)

        self.assertTrue(x1 == x2 and y1 == y2)

        
