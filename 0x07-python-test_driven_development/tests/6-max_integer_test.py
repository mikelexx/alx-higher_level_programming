#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMatrix(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_max_int(self):
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([-1, 0]), 0)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1.0, 2.0]), 2.0)
        self.assertEqual(max_integer(["mike", "mike"]), "mike")
        self.assertEqual(max_integer([True, True]), True)
        self.assertEqual(max_integer([False, True]), True)
        self.assertEqual(max_integer([False, False]), False)
        self.assertEqual(max_integer([1, False]), 1)
        self.assertEqual(max_integer([1, True]), True)
        self.assertEqual(max_integer([1.0, 2]), 2)
        self.assertEqual(max_integer([1.0, 2.0]), 2.0)
        self.assertEqual(max_integer(["1", "3"]), "3")
        self.assertEqual(max_integer(["b", "B"]), "b")
