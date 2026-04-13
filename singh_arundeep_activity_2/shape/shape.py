"""This module defines the Shape class."""

__author__ = "Arundeep Singh"
__version__ = "25.12.52"

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract class representing a generic shape.
    """
    def __init__(self, color: str):
        """
        Initializes the shape with the color.
        """
        if not color.strip():
            raise ValueError("colour cannot be blank.")
        self._color = color

    @property
    def color(self) -> str:
        """Get the color to shape."""
        return self._color
    
    @color.setter
    def color(self, value: str):
        """set the color to shape"""
        self._color = value

    @abstractmethod
    def area(self):
        """
        method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        to calculate perimeter of the shape.
        """
        pass

    def __str__(self):
        """
        String indicating the color of the shape
        """
        return f"The shape color is {self._color}"
