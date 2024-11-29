import unittest
import math
from circle import area, perimeter


class CircleTestArea(unittest.TestCase):
    def test_positive_values(self):
        for radius, expected in [(2, 4 * math.pi), (13, 169 * math.pi), (0.3, 0.09 * math.pi)]:
            with self.subTest(radius=radius):
                self.assertEqual(area(radius), expected)
    
    def test_zero_values(self):
        for radius, expected in [(0, 0 * math.pi)]:
            with self.subTest(radius=radius):
                self.assertEqual(area(radius), expected)


class CircleTestPerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(perimeter(2), 4 * math.pi)
        self.assertEqual(perimeter(13), 26 * math.pi)
        self.assertEqual(perimeter(0.3), 0.6 * math.pi)
        for radius, expected in [(2, 4 * math.pi), (13, 26 * math.pi), (0.3, 0.6 * math.pi)]:
            with self.subTest(radius=radius):
                self.assertEqual(perimeter(radius), expected)
    
    def test_zero_values(self):
        for radius, expected in [(0, 0 * math.pi)]:
            with self.subTest(radius=radius):
                self.assertEqual(perimeter(radius), expected)



if __name__ == '__main__':
    unittest.main()