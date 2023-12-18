#!/usr/bin/python3

# A simple function that prints the first x elements of a list and only integers.

def safe_print_list_integers(my_list=[], x=0):

    count = printed_ints = 0
    while True:
        try:
            if count < x:
                print("{:d}".format(my_list[count]), end='')
                count += 1
                printed_ints += 1
            else:
                print()
                return printed_ints
        except (ValueError, TypeError):
            count += 1
