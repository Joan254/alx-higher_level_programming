#!/usr/bin/python3
"""Module that defines a class Base."""


class Base:
    """This class will be the “base” of all other classes
    in the project 0x0C. Python - Almost a circle.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
