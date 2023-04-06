#!/usr/bin/python3
"""
Given username and pat as param, get user id from Github api
usage: ./10-my_github.py github_username pat
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
