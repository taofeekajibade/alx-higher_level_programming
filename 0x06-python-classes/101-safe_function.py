#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as error:
        print(f"Exception: {error}", file=sys.stderr)
        return None
