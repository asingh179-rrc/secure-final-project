"""This module defines the Triangle class."""

__author__ = "Arundeep Singh"
__version__ = "25.12.52"

# triangle.py
from shape.shape import Shape
import math


class Triangle(Shape):
    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        # Call superclass __init__ first
        super().__init__(color)

        # Validate side_1
        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")
        # Validate side_2
        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        # Validate side_3
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")

        # Triangle Inequality Theorem
        if not (side_1 + side_2 > side_3 and
                side_1 + side_3 > side_2 and
                side_2 + side_3 > side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")

        # Assign attributes
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"This triangle has three sides with lengths of "
                f"{self.__side_1}, {self.__side_2} and {self.__side_3} centimeters.")

    # Must override abstract methods area() and perimeter()
    def area(self):
        sp = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        return math.sqrt(sp * (sp - self.__side_1) * (sp - self.__side_2) * (sp - self.__side_3))

    def perimeter(self):
        return self.__side_1 + self.__side_2 + self.__side_3
