#!/usr/bin/python3
"A module to add two numbers

This module performs the addition operation between two numbers,
these numbers can be integers or floats.

"""

def add_integer(a, b=98):
    """Adds two numbers

    Performs the addition between two numbers.
    
    Args:
        a (:obj:`int, float`): The first number.
        b (:obj:`int, float`, optional): The second number.
    
    Returns:
        int: The result of the addition.

    """

    if a is not type(int or float):
        raise TypeError('a must be an integer')
    
    if b is not type(int or float):
        raise TypeError('b must be an integer')
    
    if a is type(float):
        a = int(a)
    
    if b is type(float):
        b = int(b)

return  a + b
