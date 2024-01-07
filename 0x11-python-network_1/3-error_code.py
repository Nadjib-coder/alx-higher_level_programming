#!/usr/bin/python3

"""
script to send a request to a URL,
display the body of the response, and handle HTTP errors.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    fetches the URL and displays the body of the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The body of the response (decoded in utf-8).
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
        sys.exit(1)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    response_body = fetch_url(url)
    print(response_body)
