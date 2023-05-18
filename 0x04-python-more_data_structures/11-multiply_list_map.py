#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    all_val = list(map((lambda i: i * number), my_list))
    return (all_val)
