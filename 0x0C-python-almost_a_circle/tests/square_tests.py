#!/bin/user/python3
"""Unittest for Square class"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def setUp(self):
        """Sets up the objects for testing"""
        Base._Base__nb_objects = 0
        self.s1 = Square(1)
        self.s2 = Square(2, 3)
        self.s3 = Square(3, 4, 5)
        self.s4 = Square(4, 5, 6, 7)

    def test_id(self):
        """Tests for id attribute"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 7)

    def test_size(self):
        """Tests for size attribute"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 3)
        self.assertEqual(self.s4.size, 4)

    def test_x(self):
        """Tests for x attribute"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 4)
        self.assertEqual(self.s4.x, 5)

    def test_y(self):
        """Tests for y attribute"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 5)
        self.assertEqual(self.s4.y, 6)

    def test_size_type(self):
        """Tests for size type"""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(True)
        with self.assertRaises(TypeError):
            Square(1.1)
        with self.assertRaises(TypeError):
            Square([1, 2, 3])

    def test_x_type(self):
        """Tests for x type"""
        with self.assertRaises(TypeError):
            Square(1, "1")
        with self.assertRaises(TypeError):
            Square(1, True)
        with self.assertRaises(TypeError):
            Square(1, 1.1)
        with self.assertRaises(TypeError):
            Square(1, [1, 2, 3])

    def test_y_type(self):
        """Tests for y type"""
        with self.assertRaises(TypeError):
            Square(1, 1, "1")
        with self.assertRaises(TypeError):
            Square(1, 1, True)
        with self.assertRaises(TypeError):
            Square(1, 1, 1.1)
        with self.assertRaises(TypeError):
            Square(1, 1, [1, 2, 3])

    def test_size_value(self):
        """Tests for size value"""
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_value(self):
        """Tests for x value"""
        with self.assertRaises(ValueError):
            Square(1, -1)
            
    def test_y_value(self):
        """Tests for y value"""
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_area(self):
        """Tests for area method"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 9)
        self.assertEqual(self.s4.area(), 16)

    def test_display(self):
        """Tests for display method"""
        self.assertEqual(self.s1.display(), None)
        self.assertEqual(self.s2.display(), None)
        self.assertEqual(self.s3.display(), None)
        self.assertEqual(self.s4.display(), None)

    def test_str(self):
        """Tests for __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (3) 4/5 - 3")
        self.assertEqual(str(self.s4), "[Square] (7) 5/6 - 4")

    def test_update_args(self):
        """Tests for update method with *args"""
        self.s1.update(89)
        self.assertEqual(str(self.s1), "[Square] (89) 0/0 - 1")
        self.s1.update(89, 2)
        self.assertEqual(str(self.s1), "[Square] (89) 0/0 - 2")
        self.s1.update(89, 2, 3)
        self.assertEqual(str(self.s1), "[Square] (89) 3/0 - 2")
        self.s1.update(89, 2, 3, 4)
        self.assertEqual(str(self.s1), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        """Tests for update method with **kwargs"""
        self.s1.update(size=10)
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 10")
        self.s1.update(size=11, x=2)
        self.assertEqual(str(self.s1), "[Square] (1) 2/0 - 11")
        self.s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(self.s1), "[Square] (89) 3/1 - 2")

    def test_update_args_kwargs(self):
        """Tests for update method with *args and **kwargs"""
        self.s1.update(89, 2, 3, 4, size=5, y=6)
        self.assertEqual(str(self.s1), "[Square] (89) 3/4 - 2")
