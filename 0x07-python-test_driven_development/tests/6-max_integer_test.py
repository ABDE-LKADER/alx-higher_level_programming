#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittests"""

    def test_max(self):
        """Test for max"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty(self):
        """Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Test for one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_float(self):
        """Test for float"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_string(self):
        """Test for string"""
        self.assertEqual(max_integer("string"), "t")

    def test_tuple(self):
        """Test for tuple"""
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_dictionary(self):
        """Test for dictionary"""
        self.assertEqual(max_integer({1: 2, 2: 3, 3: 4, 4: 5}), 4)

    def test_none(self):
        """Test for None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list(self):
        """Test for list"""
        with self.assertRaises(TypeError):
            max_integer([[1, 2], [3, 4]])
