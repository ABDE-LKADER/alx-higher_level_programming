#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            print(text[i], end="")
