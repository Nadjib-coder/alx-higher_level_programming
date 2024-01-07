#!/usr/bin/python3

"""
Module to send a request to a URL and display
the value of the X-Request-Id variable in the
response header.
"""

import urllib.request
import sys


def get_x_request_id(url):
    """
    Retrieves the X-Request-Id value from
    the response header of a given URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable
        in the response header.
    """
    try:
        with urllib.request.urlopen(url) as response:
            header_value = response.getheader('X-Request-Id')
            return header_value
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    print(x_request_id)
