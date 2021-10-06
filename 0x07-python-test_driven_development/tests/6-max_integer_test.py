#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class Test
    Args:
        unittest {[type]} [description]
        """
    def test_max(self):
        """ Test for max positive integers"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float(self):
        """ test for float type"""
        self.assertAlmostEqual(max_integer([3, 4, 10, 12.5]), 12.5)

    def test_negative(self):
        """ test for negative"""
        self.assertAlmostEqual(max_integer([-1, -2, 3, 4]), 4)

    def test_empty(self):
        """ test for empty list"""
        self.assertAlmostEqual(max_integer(()), None)

    def test_one_neg_int(self):
        """ test for just one negative number"""
        self.assertAlmostEqual(max_integer([-100]), -100)

    def test_one_int(self):
        """ test for just one postive number"""
        self.assertAlmostEqual(max_integer([100]), 100)
    def test_start(self):
        self.assertAlmostEqual(max_integer([7, 2, 3, 4, 5]), 7)
    def test_middle(self):
        self.assertAlmostEqual(max_integer([1, 2, 5, 2]), 5)
