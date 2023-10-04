#!/usr/bin/python3
"""defines locked class"""


class LockedClass:
    """
    prevent the user from instantiating new lockedclass attributes
    but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
