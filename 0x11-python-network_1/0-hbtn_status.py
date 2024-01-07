#!/usr/bin/env python3

"""
Module to fetch and display information about
the status of https://alx-intranet.hbtn.io
"""

import urllib.request


def fetch_status():
    """
    Fetches the status of https://alx-intranet.hbtn.io
    and displays relevant information.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        data = response.read()

    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data.decode('utf-8'))
    print("\t- utf8 content:", data.decode('utf-8'))


if __name__ == "__main__":
    fetch_status()
