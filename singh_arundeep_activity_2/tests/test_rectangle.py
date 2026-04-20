"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Arundeep Singh"
__version__ = "25.12.52"

import unittest
from shape.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Common precondition: create a valid rectangle"""
        self.rectangle = Rectangle("red", 5, 6)

    def test_valid_rectangle_creation(self):
        self.assertIsInstance(self.rectangle, Rectangle)

    def test_length_not_numeric(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("blue", "a", 6)
        self.assertEqual(str(context.exception), "Length must be numeric.")

    def test_width_not_numeric(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("green", 5, "b")
        self.assertEqual(str(context.exception), "Width must be numeric.")

    def test_perimeter(self):
        self.assertEqual(self.rectangle.perimeter(), 22)  # 2*5 + 2*6

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 30)  # 5*6

    def test_str_output(self):
        expected_str = ("The shape color is red.\n"
                        "This rectangle has four sides with the lengths of "
                        "5, 6, 5 and 6 centimeters.")
        self.assertEqual(str(self.rectangle), expected_str)


if __name__ == '__main__':
    unittest.main()

