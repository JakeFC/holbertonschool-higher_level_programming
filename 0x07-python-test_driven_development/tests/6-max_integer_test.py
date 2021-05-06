#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A test case for max_integer function tests"""
    def test_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_zero(self):
        self.assertEqual(max_integer([]), None)

    def test_beginning(self):
        self.assertEqual(max_integer([3, 1, 2]), 3)

    def test_middle(self):
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_one(self):
        self.assertEqual(max_integer([1]), 1)

    def test_neg(self):
        self.assertEqual(max_integer([0, -1]), 0)

    def test_all_neg(self):
        self.assertEqual(max_integer([-1, -4, -3]), -1)

if __name__ == "__main__":
    unittest.main()
