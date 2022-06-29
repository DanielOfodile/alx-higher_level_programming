#!/usr/bin/python3
# Python function def magic_calculation(a, b, c)
# that does exactly the same as the python bytecode

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
