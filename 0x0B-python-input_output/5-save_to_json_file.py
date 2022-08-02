#!/usr/bin/python3
# 5-from_json_string.py
"""Defines a JSON-to-object function."""

from json import dumps


def save_to_json_file(my_obj, filename):
    """Return the Python object representation of a JSON string."""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
