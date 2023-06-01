#!/usr/bin/python3
"""Defines a square bassed on 1-square.py"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes the data"""
        if not size.isdigit:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
        self.__size = size
