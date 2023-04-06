#!/usr/bin/python3
"""
Takes in URL and email address as params
and sends POST request to the URL with the email as param.
"""

import sys
import requests

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
