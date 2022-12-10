#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    targets = []
    for key, k_val in a_dictionary.items():
        if k_val is value:
            targets.append(key)
    for x in targets:
        del a_dictionary[x]
    return a_dictionary
