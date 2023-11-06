#!/usr/bin/python3
""" Module for looking up objects"""


def lookup(obj):
    """ Looks up object methods and attributes.
        Args:
            obj (object): the object to look up.

        Returns:
            list: list of attributes.
    """
    return dir(obj)
