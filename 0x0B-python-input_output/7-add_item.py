#!/usr/bin/python3
"""
this script adds all arguments to a Python list, and then\
        save them to a file:
"""
import sys
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
my_list = sys.argv[1:]
data = []
for arg in my_list:
    data.append(arg)
save_to_json_file(data, "add_item.json")
