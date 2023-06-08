#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == " " and text[j] != " ":
                break
        if text[i] in ".?:":
            print(text[i])
            print()
        else:
            print(text[i], end="")

    print()
