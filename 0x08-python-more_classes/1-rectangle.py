#!/usr/bin/python3
# 1-rectangle.py

"""

A Module with a simple Rectangle class.

"""
class Rectangle:
    """
    
    An empty Rectangle class

    """

    def __init__(self, width=0, height=0):
        """
        Checks the parameters and initializes some values
        Args:
            width (:obj:`int`, optional): The width of the Rectangle.
            height (:obj:`int`, optional): The height of the Rectangle.

        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """

            Returns the width of the rectangle.

            """
            return self.__width
        
        @width.setter
        def width(self, value):
            """

            Checks the parameters and set the size of the Rectangle
        
            Args:
            value (int): The width of the Rectangle.

            Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.

            """

            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        
        @property
        def height(self):
            """

            Returns the height of the Rectangle.

            """

            return self.__height
        
        @height.setter
        def height(self, value):
            """

            Checks the parameters and set the size of the Rectangle
    
            Args:
            value (int): The height of the Rectangle.

            Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`

            """
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            
            if value < 0:
                raise ValueError('heigtht must be >= 0')

            self.__height = value

my_rectangle = Rectangle(pie, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

