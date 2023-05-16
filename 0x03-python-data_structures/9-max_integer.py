#!/usr/bin/python3
def max_integer(my_list=[]):
    num_max = my_list[0]
    if my_list != "":
        for i in range(len(my_list)):
            if my_list[i] > num_max:
                num_max = my_list[i]
    else:
        return "None"
    return num_max
