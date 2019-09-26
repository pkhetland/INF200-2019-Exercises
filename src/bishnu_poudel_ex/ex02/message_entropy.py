""" Message entropy -for Assignment 2"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"

import math


def letter_freq(txt):
    new_dict = dict()
    for char in txt:
        char = char.lower()
        if char in new_dict.keys():
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict


def entropy(message):
    result_freq = letter_freq(message)  # The function above returns a dictionary
    sum_values = 0
    for i in result_freq.values():  # taking the sum of all the values. i.e. finding N- total characters in the text
        sum_values = sum_values + i
    entr = 0
    for i in result_freq.values():
        entr = entr + (i / sum_values) * math.log((i / sum_values),
                                                  2)  # multiplying probability with its log 2 value and summing up

    return -1 * entr


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
