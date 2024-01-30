"""
This class contains locked class
"""


class LockedClass:
    """"
    This class can't accept other attributes apart from first_name being\
            assigned on its objects.
    """

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError
        ("'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
