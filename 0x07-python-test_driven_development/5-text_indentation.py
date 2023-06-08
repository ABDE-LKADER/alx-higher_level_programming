#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
  
    str = text.replace(". ", ".\n\n")
    str = str.replace("? ", "?\n\n")
    str = str.replace(": ", ":\n\n")
    print(str, end="")
