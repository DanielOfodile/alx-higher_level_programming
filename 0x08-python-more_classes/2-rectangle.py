#!/usr/bin/python3
# 2-rectangle.py
"""
A module that returns the area and perimeter of a rectangle
"""
class Rectangle:
    """A Rectangle class that returns its area and perimeter"""

    def __init__(self, width=0, height=0):
        """initialises and sets some parameters"""
        
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """gets the  height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
    
    def area(self):
        """returns area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the circle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
