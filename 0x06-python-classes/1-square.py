#!/usr/bin/python3
"""Defines a square bassed on 0-square.py"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes the data"""
        if size.isdigit():
            print("size must be an integer")
        if size < 0:
            print("size must be >=0")
            self.__size = size
