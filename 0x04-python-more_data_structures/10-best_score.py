#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_sc = max(a_dictionary, key=a_dictionary.get)
    return best_sc
