import unittest
from math import pi
import circle_Area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #test radius when radius >= 0
        self.assertAlmostEqual(circle_Area(1), pi)
        self.assertAlmostEqual(circle_Area(0), 0)



if __name__ == '__main__':
    app.run(debug = True)