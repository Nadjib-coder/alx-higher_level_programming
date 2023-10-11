#!/usr/bin/python3
"""creat save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to text file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
