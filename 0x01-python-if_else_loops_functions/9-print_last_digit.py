#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    if number < 0:
        last_digit = -1 (-1 * number % 10)
    print("{:d}".format(last_digit), end="")
    return last_digit
