#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v is highest:
            return k
