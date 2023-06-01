#!/usr/bin/python3
"""Defines a square bassed on 3 -square.py"""

class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def size(self):
        """Retrieves the size"""
        return self.__size
    
    def size(self, value):
        """Sets the size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
    
    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)