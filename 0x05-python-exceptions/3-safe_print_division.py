#!/usr/bin/python3

# A function that divides 2 integers and prints the result.

def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.1f}".format(result))
    except:
        result = None
        print("Inside result: {}".format(result))
    finally:
        return result
