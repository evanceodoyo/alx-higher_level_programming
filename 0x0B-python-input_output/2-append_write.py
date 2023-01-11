#!/usr/bin/python3
"""function that appends a string at the
end of text file(utf8).
"""


def append_write(filename="", text=""):
    """Append text to file.
    Return number of characters added.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
