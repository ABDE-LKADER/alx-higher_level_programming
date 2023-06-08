#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    list = 0
    for i in text:
        if list == 0:
            if i == ' ':
                continue
            else:
                list = 1
        if list == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                list = 0
            else:
                print(i, end="")
