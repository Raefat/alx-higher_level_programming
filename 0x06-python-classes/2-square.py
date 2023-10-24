#!/usr/bin/python3

""" Sqaure Module """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ Initialize new Square
            Args:
                size (int): the size of the new square.
        """
        if not isinstance(size, str):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
