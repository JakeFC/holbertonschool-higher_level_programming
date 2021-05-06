#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A test case for max_integer function tests"""
    def normal_test(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def zero_test(self):
        self.assertEqual(max_integer([]), none)

if __name__ == "__main__":
    unittest.main()
