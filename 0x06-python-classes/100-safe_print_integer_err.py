#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print(f"{value}")
        return True
    except ValueError as err:
        print(f"Exception: {err}", file=sys.stderr)
        return False
    except TypeError as err:
        print(f"Exception: {err}", file=sys.stderr)
        return False
