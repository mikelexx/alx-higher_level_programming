#!/usr/bin/python3
"""
this module contains a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”:
    Args:
        filename: Json file containing JSON representation of object.
    Returns:
        object: object from its JSON representation.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        data = json.loads(f.read())
        return data
