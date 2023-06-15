#!/usr/bin/python3
"""Module returns dictionary description with simple data structure"""


def class_to_json(obj):
    """Function returns dictionary description with simple data structure"""

    return obj.__dict__
