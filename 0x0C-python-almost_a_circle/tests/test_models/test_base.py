#!/usr/bin/python3
"""
Module: Unittest for models
"""

import unittest
import inspect
import pep8
from models import base
Base = base.Base

class testBase(unittest.TestCase):
    """Testing for class Base"""
    def test_args(self):
        """ test if there is too many arguments"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

