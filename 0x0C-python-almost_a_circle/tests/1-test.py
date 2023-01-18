#!/usr/bin/python3
"""
Module: 1-tests
tests the class contained in the module
"""


import unittest

class TestBaseClass(unittest.TestCase):
    """Class: test sub class derived from unittest.TestCase"""

    def test_import_class(self):
        from models.base import Base
        b1 = Base()
        self.assertEqual(b1.id, 1)
