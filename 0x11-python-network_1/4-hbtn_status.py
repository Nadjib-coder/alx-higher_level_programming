#!/usr/bin/python3

"""
Script to fetch and display the status
of https://alx-intranet.hbtn.io using
the requests package.
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
