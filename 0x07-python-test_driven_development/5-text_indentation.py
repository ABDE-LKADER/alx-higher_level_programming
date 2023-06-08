#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    str = text[:]

    for i in ".?:":
        list_text = str.split(i)
        str = ""
        for j in list_text:
            j = j.strip(" ")
            str = j + i if str is "" else str + "\n\n" + j + i

    print(str[:-3], end="")
