__author__ = "petter hetland"
__email__ = "pehe@nmbu.no"

"""
Then write code for the ``char_counts()`` function that opens the file
with the given ``filename`` using encoding ``utf-8`` and reads the
entire file content into a single string. It shall then count how often
each character code (0–255) occurs in the string and return the result
as a list or tuple, where ``result[i]`` gives the number of occurrences
of character code ``i``."""


def char_counts(textfilename):
    with open(textfilename, "r") as f:
        string = f.read()
        result = [string.count(chr(i)) for i in range(256)]
        f.close()
        return result


if __name__ == "__main__":

    def entropy(message):
        pass


if __name__ == "__main__":
    for msg in "", "aaaa", "aaba", "abcd", "This is a short text.":
        print("{:25}: {:8.3f} bits".format(msg, entropy(msg)))
