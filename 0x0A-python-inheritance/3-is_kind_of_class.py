#!/usr/bin/python3
"""Checks if the object is an instance of, or if the object
   is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if the object
       is an instance of a class that inherited from, the specified class.
    Args:
       obj (any): The object to check.
       a_class (type): The class to match the type of obj to.
    Returns:
       True if the object is an instance of, or if the object
       is an instance of a class that inherited from, the specified class;
       otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
