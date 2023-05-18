#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    sum_all = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        digits = roman[roman]
        sum_all += digits if sum_all < digits * 5 else -digits
    return sum_all
