#!/usr/bin/python3
"""creat write_file function"""


def write_file(filename="", text=""):
    """reads filename"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
