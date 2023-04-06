#!/usr/bin/python3
"""
Takes URL as params display the value of X-Request-Id in the repsonse header
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
