#!/usr/bin/python3
"""Defines Student class
"""


class Student:
    """Represents a student
    """
    def __init__(self, first_name, last_name, age):
        """__init__ method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return json representaion of student instance
        """
        return self.__dict__
