#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dict = a_dictionary.copy()
    for k in a_dict:
        a_dict[k] = a_dictionary[k] * 2
    return a_dict
