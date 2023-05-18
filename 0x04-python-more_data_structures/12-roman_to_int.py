#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    sum_all = 0
    digits_roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for r in reversed(roman_string):
        digits_10 = digits_roman[r]
        sum_all += digits_10 if sum_all < digits_10 * 5 else -digits_10
    return sum_all
