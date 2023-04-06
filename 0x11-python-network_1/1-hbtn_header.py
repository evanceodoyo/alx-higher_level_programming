#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and
display the value of X-Request-Id
Usage: ./1-hbtn_header.py URL
"""
import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
