#!/usr/bin/python3
"""
This module contains unitttest for Square class and methods
"""
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
from io import StringIO


class TestSquareMethods(unittest.TestCase):
    def setUp(self):
        """
        runs before each test method to reset number of objects created.
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        clears the stdout buffer after every test method.
        """
        sys.stdout = sys.__stdout__

    def test_invalid_initialization(self):
        """
        makes sure that all invalid initialization of square objects fail.
        """
        self.assertIsNotNone(id(Square(1)))
        self.assertIsInstance(Square(2), Square)
        self.assertTrue(issubclass(type(Square(2)), Rectangle))
        self.assertRaises(TypeError, Square, "3")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 0, ValueError)
        self.assertRaises(TypeError, Square, 1, "3")
        self.assertRaises(TypeError, Square, 1, True)

    def test_initializor(self):
        """
        tests that object attributes are properly configured
        during initializatoin.
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        captured_output = StringIO()
        sys.stdout = captured_output
        self.assertEqual(s1.area(), 25)
        s1.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "#####\n" * 5)
        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        sys.stdout = sys.__stdout__
        captured_output = StringIO()
        sys.stdout = captured_output
        s2.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, (" " * 2 + "##\n") * 2)
        sys.stdout = sys.__stdout__
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)
        sys.stdout = sys.__stdout__
        captured_output = StringIO()
        sys.stdout = captured_output
        s3.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\n\n\n" + (" " + "###\n") * 3)

    def test_square_properties(self):
        """
        Ensures proper modification fo square object properties.
        """
        s1 = Square(5)
        self.assertRaises(ValueError, setattr, s1, 'size', -2)
        self.assertRaises(ValueError, setattr, s1, 'size', 0)
        self.assertRaises(TypeError, setattr, s1, 'size', "2")
        self.assertRaises(TypeError, setattr, s1, 'size', True)
        s1.size = 4
        self.assertEqual(s1.size, 4)
        s1.width = 5
        self.assertEqual(s1.height, 4)

    def test_update(self):
        """
        tests succesful updation of square objects through args
        and kwargs passed to the update method.
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """
        tests that the produced square dictionary represantion is
        of correct form.
        """
        s1 = Square(10, 2, 1)
        s1_to_dictionary = s1.to_dictionary()
        self.assertEqual(s1_to_dictionary, {
            'id': 1, 'x': 2, 'size': 10, 'y': 1})


if __name__ == "__main__":
    unittest.main()
