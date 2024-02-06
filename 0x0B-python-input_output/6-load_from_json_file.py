#!/usr/bin/python3
"""
this module contains a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="UTF8") as f:
        data = json.loads(f.read())
        return data
