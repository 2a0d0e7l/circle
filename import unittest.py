import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res1 = area(1)
        res2 = area(2)
        self.assertAlmostEqual(res1, math.pi, places=5)
        self.assertAlmostEqual(res2, math.pi * 4, places=5)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res1 = perimeter(1)
        res2 = perimeter(2)
        self.assertAlmostEqual(res1, 2 * math.pi, places=5)
        self.assertAlmostEqual(res2, 4 * math.pi, places=5)

    def test_negative_radius(self):
        res1 = area(-2)
        res2 = area(2)
        res3 = perimeter(-2)
        res4 = perimeter(2)
        self.assertAlmostEqual(res1, res2, places=5)
        self.assertAlmostEqual(res3, res4, places=5)
