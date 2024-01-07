#!/usr/bin/python3

"""
script to list 10 most recent
commits of a GitHub repository.
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} <repository> <owner>".format(sys.argv[0]))
    sys.exit(1)

repository = sys.argv[1]
owner = sys.argv[2]
url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repository)

response = requests.get(url)

if response.status_code == 200:
    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
else:
    print("Error:", response.status_code)
