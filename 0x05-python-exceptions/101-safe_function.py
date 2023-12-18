#!/usr/bin/python3

# A function that executes a function safely.

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
