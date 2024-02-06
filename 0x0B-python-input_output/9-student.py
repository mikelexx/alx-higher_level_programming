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

    def to_json(self):
        """
        retrieves a dictionary representation of a \
        Student instance (same as 8-class_to_json.py).
        Returns: the object __dict__ values as a dictionary
        """
        description = {}
        for key, val in self.__dict__.items():
            description[key] = val
        return description
