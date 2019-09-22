"""Loop to list comprehension -for Assignment 1"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"

SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    return [(suit, val) for suit in SUITS for val in VALUES]
    

if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
    else:
        print('NO ERROR!')
