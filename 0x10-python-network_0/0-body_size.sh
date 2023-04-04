#!/bin/bash
# Displays the size of the body of the response.
# Usage: ./0-body_size.sh url:port

curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
