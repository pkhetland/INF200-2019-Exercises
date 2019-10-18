# -*- coding: utf-8 -*-

__author__ = 'Nils Skadderenes, Bishnu Poudel'
__email__ = 'nils.skadderenes@nmbu.no,  bishnu.poudel@nmbu.no'

''' We implement the skeleton of Snakes and ladders games using a set of 
functions.
The rules are as follows:

1. Each player has one figure, which starts at the imaginary square 0 to the 
   left of square 1.
2. Each time it is a player’s turn, she throws a six-sided die and moves
   her figure the given number of fields forward.
3. If the figure stops on a field at the bottom of a ladder, 
   the figure moves immediately up the ladder.
4. If the figure stops on a field at the top of a chute, 
   the figure moves immediately down the chute.
5. The game ends when the first player reaches (or passes) field 90.
'''

from random import randint
import random
import statistics as st


# dice_throw gives integers from 1 to 6
def dice_throw():
    return randint(1, 6)


# Store the snakes and ladders as a list of lists
ladders_list = [[1, 40], [8, 10], [36, 52], [43, 62], [49, 79], [65, 82],
                [68, 85]]
snakes_list = [[24, 5], [33, 3], [42, 30], [56, 37], [64, 27], [74, 12],
               [87, 70]]


# After every dice roll, we call this function to check if the
# player has hit either a snake or a ladder
def check_for_snakes_and_ladders(position):
    for i in ladders_list:
        if position == i[0]:
            position = i[1]

    for i in snakes_list:
        if position == i[0]:
            position = i[1]
    return position


# Simulate the dice roll and also snake/ladder move. This functions returns a
# new position after every dice roll
def play_one_dice_roll(position):
    dice_output = dice_throw()
    position = position + dice_output
    position = check_for_snakes_and_ladders(position)
    return position


# Play single game, track the number of steps every player takes, and the
# position of every player. function returns only when one player gets to or
# crosses 90.
def single_game(num_players):
    players_positions = [0] * num_players
    players_steps = [0] * num_players

    while True:
        for i in range(num_players):
            players_positions[i] = play_one_dice_roll(players_positions[i])
            players_steps[i] += 1
            #            print(i, ' th player moved to ', players_position[i])
            if players_positions[i] >= 90:
                #                print('Game Over!')
                return players_positions[i], players_steps[i]


# simulate multiple games by calling single_game function
def multiple_games(num_games, num_players):
    players_positions = [None] * num_games
    players_steps = [None] * num_games
    for i in range(num_games):
        players_positions[i], players_steps[i] = single_game(num_players)
    return players_positions, players_steps


# simulate multiple games but with a seed, so that the results are
# reproducible
def multi_game_experiment(num_games, num_players, seed_passed):
    random.seed(seed_passed)
    players_positions, players_steps = multiple_games(num_games, num_players)
    return seed_passed, players_positions, players_steps


# Call the multi_game_experiment and print minimum, maximum and
# average number of steps for game completion
if __name__ == '__main__':
    p_seed, p_positions, p_steps = \
        multi_game_experiment(100, 4, randint(1, 999))  # 27 )
    #    print("The seed is ", p_seed)
    #    print(p)
    print("The shortest game duration is ", min(p_steps),
          " and Longest ", max(p_steps))
    print("The median game duration is ", st.median(p_steps))
    print("The mean game duration is ", st.mean(p_steps))
