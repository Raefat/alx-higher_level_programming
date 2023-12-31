#!/usr/bin/python3

""" Sqaure Module """


class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize new Square
            Args:
                size (int): the size of the new square.
                position (tuple): the position of Square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the size of the square"""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0
                or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates the area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
