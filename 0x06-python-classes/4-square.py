#!/usr/bin/python3

""" Sqaure Module """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ Initialize new Square
            Args:
                size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a square """
        return self.__size ** 2
