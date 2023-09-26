#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializing the square class.
        Args:
            size: size of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculate area of the square.
        Returns: the current square area.
        """
        return (self.__size ** 2)
