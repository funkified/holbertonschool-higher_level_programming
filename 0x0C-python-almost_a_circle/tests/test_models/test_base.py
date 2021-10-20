#!/usr/bin/python3
"""
Module: Unittest for models
"""

from tests import *
import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """Testing for class Base"""

    @classmethod
    def setUpClass(self):
        self.a_base = Base()
        self.b_base = Base()
        self.c_base = Base(89)

    def test_init(self):
        self.assertEqual(self.a_base.id, 1)

    def test_assign_id(self):
        self.assertEqual(self.c_base.id, 89)

"""
    if __name__ == "__main__":
        unittest.main()
"""
