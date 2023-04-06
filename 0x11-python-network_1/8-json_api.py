#!/usr/bin/python3
"""
Takes in a letter and sends a POST request with the letter as param
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    payload = {'q': arg}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
