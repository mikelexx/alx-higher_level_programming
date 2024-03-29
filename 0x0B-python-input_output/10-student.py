#!/usr/bin/python3
"""
contains a class that defines a student.
"""


class Student():
    """
    defines a studenti by names and age.
    Args:
        first_name : first name of student
        second_name : second name of student.
        age: his or her age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a \
        Student instance (same as 8-class_to_json.py).
        Args:
            args: attribute names
        Returns: the object __dict__ values as a dictionary
        """
        description = {}
        for key, val in self.__dict__.items():
            if key in dir(self):
                if type(attrs) is not list:
                    description[key] = val
                    continue
                elif key in attrs:
                    description[key] = val
        return description
