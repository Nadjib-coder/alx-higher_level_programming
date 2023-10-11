#!/usr/bin/python3
"""module"""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        old_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []
    data.extend(sys.argv[1:])
    save_to_json_file(data, "add_item.json")
