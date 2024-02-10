#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBaseMethods(unittest.TestCase):
    def setUp(self):
        """
        runs before every test_method
        """
        Base._Base__nb_objects = 0

    def test_proper_instantiation(self):
        """
        This function tests if objects are instantiated properly.
        """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base(None).id, 5)

    def test_to_json_string(self):
        """
        tests if argumets are converted to their json string reprsentation.
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json.loads(json_dictionary), [
            {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}])

    def test_save_to_file(self):
        """
        tests for succesful storage of objects to file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [
                {"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {
                    "y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])

    def test_from_json_string(self):
        """
        tests for proper conversion of json string representation to
        actual objects.
        """
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,  [
            {'height': 4, 'width': 10, 'id': 89}, {
                'height': 7, 'width': 1, 'id': 7}])

    def test_create(self):
        """
        tests for proper creation of object from dictionary of attributes.
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_load_from_file(self):
        """
        tests if object lists are correctly loaded from file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for inst in list_rectangles_output:
            self.assertIsInstance(inst, Rectangle)
            self.assertTrue(type(inst) is Rectangle)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for inst in list_squares_output:
            self.assertIsInstance(inst, Square)


if __name__ == "__main__":
    unittest.main()
