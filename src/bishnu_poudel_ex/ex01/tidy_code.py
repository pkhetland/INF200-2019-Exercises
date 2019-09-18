"""Cleaning the code for Exercises fro Assignment 1"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"

from random import randint as a


# compare two numbers
def compare(f, g):
    return f == g


# user input guess
def input_guess():
    return int(input('Your guess: '))


# random number between 1 and 12
def rand_int_between_1_12():
    return a(1, 6) + a(1, 6)


# main code
if __name__ == '__main__':
    statenow = False
    attempts_to_guess = 3
    rand_int = rand_int_between_1_12()
    # print('rand int is {} '.format(rand_int))
    while not statenow and attempts_to_guess > 0:
        k = input_guess()
        statenow = compare(rand_int, k)
        if not statenow:
            print('Wrong, try again!')
            attempts_to_guess -= 1

    if attempts_to_guess > 0:
        print('You won {} points.'.format(attempts_to_guess))
    else:
        print('You lost. Correct answer: {}.'.format(rand_int))
