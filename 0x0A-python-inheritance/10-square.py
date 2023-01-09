#!/usr/bin/python3
"""Implements a Square class.
Square class inherits from Rectangle.
"""


Rectangle = __import__("9-rectangle").Rectangle


"""Square class implementation"""


class Square:
    """A Square class."""

    def __init__(self, size):
        super().__init__(self.__size, self.__size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
