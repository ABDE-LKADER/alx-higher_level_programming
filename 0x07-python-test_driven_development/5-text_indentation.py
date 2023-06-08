#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    str = 0
    for i in text:
        if str == 0:
            if i == ' ':
                continue
            else:
                str = 1
        if str == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                str = 0
            else:
                print(i, end="")
