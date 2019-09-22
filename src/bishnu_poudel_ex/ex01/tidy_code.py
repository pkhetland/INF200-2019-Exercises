"""Cleaning the code for Exercises fro Assignment 1"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"

from random import randint


# compare two numbers
def compare(number_generated, number_guessed):
    return number_generated == number_guessed


# user input guess
def input_guess():
    return int(input('Your guess: '))


# random number between 2 and 12
def rand_int_between_1_12():
    return randint(1, 6) + randint(1, 6)


# main code
if __name__ == '__main__':
    state_now = False
    attempts_to_guess = 3
    rand_int = rand_int_between_1_12()
    # print('rand int is {} '.format(rand_int))
    while not state_now and attempts_to_guess > 0:
        guessed_number = input_guess()
        state_now = compare(rand_int, guessed_number)
        if not state_now:
            print('Wrong, try again!')
            attempts_to_guess -= 1

    if attempts_to_guess > 0:
        print('You won {} points.'.format(attempts_to_guess))
    else:
        print('You lost. Correct answer: {}.'.format(rand_int))
