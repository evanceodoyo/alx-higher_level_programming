#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exception as err:
        prints("Exception: {}".format(err), file=stderr)
        return None
