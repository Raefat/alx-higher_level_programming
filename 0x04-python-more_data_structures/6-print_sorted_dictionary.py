#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dict = dict(sorted(a_dictionary.items()))
    for key in a_dict:
        print("{}: {}".format(key, a_dict[key]))
