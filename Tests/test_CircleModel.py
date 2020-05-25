import unittest
from MyMathLib import CircleModel
from MyMathLib import Point
from typing import List, Set, Dict, Tuple, Optional
import math

class Test_CircleModel(unittest.TestCase):
    def test_When_Constructed_All_Properties_Must_Be_Initialized(self):
        c1= CircleModel(100.1,200.2,300.3)
        self.assertAlmostEquals(100.1,c1.X)
        self.assertAlmostEquals(200.2,c1.Y)
        self.assertAlmostEquals(300.3,c1.R)

    def test_String_Representation_Must_Have_Center_And_Radius(self):
        c1= CircleModel(100.1,200.2,300.3)
        display=str(c1)
        self.assertTrue(display.find("X=100.1") >= 0)
        self.assertTrue(display.find("Y=200.2") >= 0)
        self.assertTrue(display.find("R=300.3") >= 0)


if __name__ == '__main__':
    unittest.main()
