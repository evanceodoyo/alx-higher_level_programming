#!/usr/bin/python3
"""
Uses GitHub API to list 10 commits from a user.
"""

import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
           sys.argv[2], sys.argv[1])
    r = requests.get(url)
    for c in r.json()[:10]:
        print("{}: {}".format(c.get('sha'),
              c.get('commit').get('author').get('name')))
