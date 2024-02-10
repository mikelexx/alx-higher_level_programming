#!/usr/bin/python3
"""
This module contains unittests for Rectangle class.
"""

from io import StringIO

import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys


class TestRectangleMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        sys.stdout = sys.__stdout__
    

    def test_proper_instantiation(self):
        """tests the initialization function"""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, 10, 2, {})
        self.assertRaises(TypeError, Rectangle, 10, 2, "1")
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, "10", "2")
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(TypeError, Rectangle, 1, True)
        self.assertRaises(TypeError, Rectangle, False, -1)
        self.assertRaises(TypeError, Rectangle, 1, False)
        self.assertTrue(issubclass(type(Rectangle(10, 2)), Base))
        self.assertIsInstance(Rectangle(10, 2), Rectangle)

    def test_proper_attributes_via_property(self):
        """tests that proper attributes are set. i.e tests property methods"""
        r = Rectangle(10, 2)
        self.assertRaises(ValueError, setattr, r, 'x', -1)
        self.assertRaises(ValueError, setattr, r, 'y', -1)
        self.assertRaises(ValueError, setattr, r, 'width', -1)
        self.assertRaises(ValueError, setattr, r, 'height', -1)
        self.assertRaises(TypeError, setattr, r, 'y', {})
        self.assertRaises(TypeError, setattr, r, 'x', {})
        self.assertRaises(TypeError, setattr, r, 'width', "10")
        self.assertRaises(TypeError, setattr, r, 'height', "10")

    def test_display(self):
        """ tests the display function only width and height attributes"""
        captured_output = StringIO()
        sys.stdout = captured_output
        r = Rectangle(4, 6)
        r.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "####\n" * 6)

    def test_display_improved(self):
        """ tests the display function considering x and y locations\
                inaddition to width and height attributes"""
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        printed_output = captured_output.getvalue()
        expected_output = "\n\n" + (" " * 2 + "##\n") * 3
        self.assertEqual(printed_output, expected_output)
        sys.stdout = sys.__stdout__
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(3, 2, 1, 0)
        r1.display()
        printed_output = captured_output.getvalue()
        expected_output2 = (" " + "###\n") * 2
        self.assertEqual(printed_output, expected_output2)

    def test_string_representation(self):
        """ tests the __str__ method"""
        self.assertEqual(str(Rectangle(
            4, 6, 2, 1, 12)), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)), "[Rectangle] (1) 1/0 - 5/5")

    def test_area(self):
        """ tests the area method"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_update(self):
        """ tests the update function considering only args"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_improved(self):
        """tests the update function considering args and kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """
        tests that the rectangle object dictionary representation is
        of correct form
        """
        r1 = Rectangle(10, 2, 1, 9)
        r1_to_dictionary = r1.to_dictionary()
        self.assertEqual(r1_to_dictionary, {
            'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})


if __name__ == "__main__":
    unittest.main()
