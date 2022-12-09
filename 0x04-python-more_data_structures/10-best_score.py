#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return 'None'
    return max(a_dictiionary, key=a_dictionary.get)
