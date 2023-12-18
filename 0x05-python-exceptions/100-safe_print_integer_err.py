#!/usr/bin/python3

# A function that prints an integer.

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    except TypeError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
