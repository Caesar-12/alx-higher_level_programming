#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """
    Test Class for max_integer([...])
    """

    def test_max(self):
        self.assertEqual(max_integer([2, 4, 7, 13, 5, 8]), 13)

    def test_emptyList(self):
        self.assertEqual(max_integer([]), None)

    def test_floatval(self):
        self.assertEqual(max_integer([1.1, 2.2, 4, 2, 5, 5.7]), 5.7)

if __name__ == '__main__':
    unittest.main()
