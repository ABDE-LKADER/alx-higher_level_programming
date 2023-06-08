#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
  
    str = text[:]
    for i in ".?:":
        list = str.split(" ")
        str = ""
        for j in list:
            j = j.strip(" ")
            if j != "":
                str = i + j
            else:
                str + "\n\n" + i + j
    print(str, end="")
