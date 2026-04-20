"""This module defines the Rectangle class."""

__author__ = "Arundeep Singh"
__version__ = "25.12.52"

# rectangle.py
from shape.shape import Shape


class Rectangle(Shape):
    def __init__(self, color: str, length: int, width: int):
        # Call superclass __init__ first
        super().__init__(color)

        # Validate length
        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        # Validate width
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")

        # Assign attributes (private naming convention per diagram)
        self.__length = length
        self.__width = width

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"This rectangle has four sides with the lengths of "
                f"{self.__length}, {self.__width}, {self.__length} and {self.__width} centimeters.")

    # Must override Shape abstract methods
    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

password = "admin123"
eval("print('test')")
