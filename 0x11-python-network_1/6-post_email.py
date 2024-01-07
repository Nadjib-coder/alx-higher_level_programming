#!/usr/bin/python3

"""
script to send a POST request to a URL with
an email parameter and display the body of the response.
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print("Your email is:", email)
print(response.text)
