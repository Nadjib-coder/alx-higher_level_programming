#!/usr/bin/python3

"""
script to send a POST request to a
URL with an email parameter and display
the body of the response.
"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    sends a POST request to the specified URL
    with the provided email parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email parameter to
        include in the request.

    Returns:
        str: The body of the response (decoded in utf-8).
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    try:
        with urllib.request.urlopen(url, data=data) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = post_email(url, email)
    print("Your email is:", email)
    print(response_body)
