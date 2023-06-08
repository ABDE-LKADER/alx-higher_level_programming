#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in ".?:":
        text = text.replace(i, i + "\n\n")
    print("\n".join([i.strip() for i in text.split("\n")]), end="")
