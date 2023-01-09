#!/usr/bin/python3
"""Implements a Square class.
Square class inherits from Rectangle.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A Square class."""

    def __init__(self, size):
        super().__init__(self.__size, self.__size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
