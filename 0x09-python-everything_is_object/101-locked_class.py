#!/usr/bin/python3
"""
This module contains locked class which can't allow assignment \
of any other attribure to its object except id the attribure is \
first_name.

"""


class LockedClass:
    """"
    This class can't accept other attributes apart from first_name being\
            assigned on its objects.
    """

    def __setattr__(self, name, value):
        """
        This function checks attribure before assigning it to object.
        Args:
            name: attribure to be assigned to object.
            value: value of that attribute.
        Raises:
            AttributeError: if attribure is not first_name.
        """

        if name != "first_name":
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
