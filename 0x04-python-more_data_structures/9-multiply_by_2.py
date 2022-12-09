#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp_dict = a_dictionary.copy()
    for k in tmp_dict.keys():
        tmp_dict[k] *= 2
    return tmp_dict
