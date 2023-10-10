#!/usr/bin/python3
"""Module for MYlist class."""


class Mylist(list):
    """custom Mylist"""
    def print_sorted(self):
        """Methid for printing sprted list"""
        print(sorted(self))
