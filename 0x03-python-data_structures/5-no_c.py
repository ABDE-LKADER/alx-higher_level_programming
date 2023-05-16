#!/usr/bin/env python3
def no_c(my_string):
    translate  = {ord(i): None for i in 'cC'}
    new_string = my_string.translate(translate)
    return (new_string)
