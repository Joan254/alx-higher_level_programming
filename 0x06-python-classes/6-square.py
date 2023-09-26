#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Create a Square.
        Args:
            size: size of the square.
            position: position of the square.
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """Retrieves size of square.
        Raises:
             TypeError: if size is not an integer
             ValueError: if size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieves position of the square.
        Raises:
             TypeError: if value is not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of the Square.
        Args:
           value: tuple of two positive integers.
        Raises:
           TypeError: if value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate area of the square.
        Returns: the current square area.
        """
        return (self.__size ** 2)

    def pos_print(self):
        """Returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            pos += "\n"
        for x in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Prints in position the square with the character #."""
        print(self.pos_print(), end="")
