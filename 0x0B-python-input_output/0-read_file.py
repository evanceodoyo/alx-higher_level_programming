#!/usr/bin/python3
"""Function to read text from a file.
"""


def read_file(filename=""):
    """Read text file using UTF8 encoding
    and print it out to stdout.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
