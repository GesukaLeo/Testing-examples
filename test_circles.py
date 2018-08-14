import unittest
from math import pi
from circle_Area import *

class TestCircleArea(unittest.TestCase):
    def test_circle_Area(self):
        #test radius when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)

