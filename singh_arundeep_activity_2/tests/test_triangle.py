"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = ""
__version__ = ""

import unittest
from shape.triangle import Triangle


class TestTriangle(unittest.TestCase):

    def setUp(self):
        """Common precondition: create a valid triangle"""
        self.triangle = Triangle("red", 3, 4, 5)

    def test_valid_triangle_creation(self):
        self.assertIsInstance(self.triangle, Triangle)

    def test_side1_not_numeric(self):
        with self.assertRaises(ValueError) as context:
            Triangle("blue", "a", 4, 5)
        self.assertEqual(str(context.exception), "Side 1 must be numeric.")

    def test_side2_not_numeric(self):
        with self.assertRaises(ValueError) as context:
            Triangle("green", 3, "b", 5)
        self.assertEqual(str(context.exception), "Side 2 must be numeric.")

    def test_side3_not_numeric(self):
        with self.assertRaises(ValueError) as context:
            Triangle("yellow", 3, 4, "c")
        self.assertEqual(str(context.exception), "Side 3 must be numeric.")

    def test_triangle_inequality_violation(self):
        with self.assertRaises(ValueError) as context:
            Triangle("red", 1, 2, 3)
        self.assertEqual(str(context.exception), "The sides do not satisfy the Triangle Inequality Theorem.")

    def test_perimeter(self):
        self.assertEqual(self.triangle.perimeter(), 12)

    def test_area(self):
        self.assertAlmostEqual(self.triangle.area(), 6.0)

    def test_str_output(self):
        expected_str = ("The shape color is red\n"
                        "This triangle has three sides with lengths of 3, 4 and 5 centimeters.")
        self.assertEqual(str(self.triangle), expected_str)


if __name__ == '__main__':
    unittest.main()
