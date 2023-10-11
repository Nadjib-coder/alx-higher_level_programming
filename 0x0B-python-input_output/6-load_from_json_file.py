#!/usr/bin/python3
"""creat load_from_json_file function"""


import json


def load_from_json_file(filename):
    """create an object from json file"""
    with open(filename) as file:
        return json.load(file)
