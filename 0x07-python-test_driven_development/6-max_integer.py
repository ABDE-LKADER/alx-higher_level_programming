#!/usr/bin/python3
"""Defines a function that finds the biggest integer of a list"""


def max_integer(list=[]):
    """Finds the biggest integer of a list"""

    if len(list) == 0:
        return None
    m = list[0]
    i = 1
    while i < len(list):
        if list[i] > m:
            m = list[i]
        i += 1
    return m
