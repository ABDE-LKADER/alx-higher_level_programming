#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    str = ""
    for i in text:
        str += i
        if i == '.' or i == '?' or i == ':':
            str += '\n\n'
    print(str.strip(), end="")
