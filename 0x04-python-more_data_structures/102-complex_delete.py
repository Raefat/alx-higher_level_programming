#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d_keys = list(a_dictionary.keys())
    for k in d_keys:
        if value == a_dictionary[k]:
            del a_dictionary[k]
    return a_dictionary
