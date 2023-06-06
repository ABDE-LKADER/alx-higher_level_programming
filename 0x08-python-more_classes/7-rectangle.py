#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle based on 6-rectangle.py"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.width = width
        self.height = height

    def __str__(self):
        """Prints a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """Sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
