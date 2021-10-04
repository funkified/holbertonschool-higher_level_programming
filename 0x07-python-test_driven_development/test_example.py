#!/usr/bin/python3
import unittest
import uniq

class TestUniqList(unittest.TestCase):
    def test_list(self):
        self.assert(uniq(list), type)

    def test_type(self):
        self.assertRaises(TypeError, uniq, -2)
