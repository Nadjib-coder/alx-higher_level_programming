#!/usr/bin/python3

"""
script to send a request to a URL and display
the value of the X-Request-Id variable in the
response header.
"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

if 'X-Request-Id' in response.headers:
    print(response.headers['X-Request-Id'])
else:
    print("X-Request-Id not found in the response headers.")
