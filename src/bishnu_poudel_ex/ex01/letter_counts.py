"""Count distinct characters in a text- for Assignment 1"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"


def letter_freq(txt):
    new_dict = dict()
    for char in txt:
        char=char.lower()
        if char in new_dict.keys():
            new_dict[char] +=1
        else:
            new_dict[char] = 1
    return new_dict


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')
    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
