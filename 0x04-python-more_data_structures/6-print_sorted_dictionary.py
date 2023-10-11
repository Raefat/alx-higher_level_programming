#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dict = sorted(a_dictionary.items())
    for key, val in enumerate(a_dict):
        print("{}: {}".format(key, value))
