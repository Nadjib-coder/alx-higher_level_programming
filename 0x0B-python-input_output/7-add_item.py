#!/usr/bin/python3
"""module"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

JSON_FILENAME = "add_item.json"

arglist = sys.argv[1:]

try:
    old_data = load_from_json_file(JSON_FILENAME)
except FileNotFoundError:
    old_data = []

old_data.extend(arglist)
save_to_json_file(old_data, JSON_FILENAME)
