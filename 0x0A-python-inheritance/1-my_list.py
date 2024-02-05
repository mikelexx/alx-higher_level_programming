#!/usr/bin/python3
"""
contains class that inherits from list.
"""


class MyList(list):
    """
    contains method that prints a list in sorted form.
    """
    def print_sorted(self):
        """
        prints the list but sorted in asceding sort.
        """
        print(sorted(self))
