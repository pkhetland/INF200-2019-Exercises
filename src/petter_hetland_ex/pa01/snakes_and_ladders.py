# -*- coding: utf-8 -*-

__author__ = "Eirik Helland, Petter Hetland"
__email__ = "eihelland@nmbu.no, pehe@nmbu.no"


import random


def add_players(n):
    player_position_list = [[0] for _ in range(n)]
    return player_position_list


"""
add_players(n) makes a list of lists containing 0. Each list of 0 represents a
 player and n is the number of players in the game. This will be used to store
 where the players are on the board and track their history using append.
"""


def snake_and_ladders():
    snake_and_ladders_dict = {
        1: 40,
        8: 10,
        36: 52,
        43: 62,
        49: 79,
        65: 82,
        68: 85,
        24: 5,
        33: 3,
        42: 30,
        56: 37,
        64: 27,
        74: 12,
        87: 70
    }
    return snake_and_ladders_dict


"""
snake_and_ladders() makes a dictionary which contains all the positions on the
board with ladders or snakes. This will be used to promote or relegate a 
player to the intended position. 
"""


def dice_value():
    dice = random.randint(1, 6)
    return dice


"""
dice_value() tosses a 6-sided dice and returns the value. 
"""


def win_checker(positions, num_of_players):
    for x in range(num_of_players):
        for y in range(len(positions[0])):
            if positions[x][y] >= 90:
                return 1
            else:
                pass
    return 0


"""
NOT USED
win_checker() checks if the game is won, so it can end the game if somebody
wins.
"""


def single_game(num_of_players):
    positions = add_players(num_of_players)
    snake_ladders = snake_and_ladders()
    winner = []
    has_won = False
    while has_won is not True:
        for player in range(num_of_players):
            dice = dice_value()
            positions[player].append(positions[player][-1] + dice)
            if positions[player][-1] in snake_ladders.keys():
                positions[player][-1] = snake_ladders[positions[player][-1]]
            else:
                pass
            if positions[player][-1] >= 90:
                winner = positions[player]
                has_won = True
            else:
                pass
    return len(winner) - 1


"""
single_game(num_of_players) runs a single game and stops when one of the player
has won. The input is how many players you want to play. The function returns
how many turns the winner used to win.
"""


def multiple_games(num_games, num_players):
    """Returns durations of a number of games.
    """
    game_lengths = []
    for _ in range(num_games):
        game_lengths.append(single_game(num_players))
    return game_lengths


def multi_game_experiment(num_games, num_players, seed):
    random.seed(seed)
    game_lengths = []
    for _ in range(num_games):
        game_lengths.append(single_game(num_players))
    return game_lengths

print(multi_game_experiment(100, 4, 2))

