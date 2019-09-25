""" count character frequencies -for Assignment 2"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"

import io


def char_counts(text_file_name):
    with io.open(text_file_name, 'r', encoding='utf8') as f:
        text = f.read()
    # print(text)
    utf_code_list = [0] * 256
    for i in range(len(text)):
        utf_code = ord(text[i])
        utf_code_list[utf_code] = utf_code_list[utf_code]+1
    return utf_code_list


if __name__ == '__main__':

    filename = 'message_entropy.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
