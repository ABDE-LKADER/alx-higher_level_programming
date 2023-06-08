#!/usr/bin/python3
"""Print text with 2 new lines"""


def text_indentation(text):
    """Print after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
  
    str = text[:]
    for i in ".?:":
        str = str.split(i)
        str = ""
        for j in str:
            str += j.strip()
            str += i
        str = str[:-1]
        print(str.strip())
