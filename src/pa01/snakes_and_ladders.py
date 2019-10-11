# -*- coding: utf-8 -*-

__author__ = 'Nils Skadderenes, Bishnu Poudel'
__email__ = 'nils.skadderenes@nmbu.no,bishnu.poudel@nmbu.no'

from random import randint
def dice_throw():
    return randint(1, 6)

ladders_list= [(1,40),(8,10),(36,52),(43,62),(49,79),(65,82),(68,85)]
snakes_list= [(24,5),(33,3),(42,30),(56,37),(64,27),(74,12),(87,70)]

def check_for_snakes_and_ladders(position):
    for i in ladders_list:
        if position == i[0]:
            position= i[1]

    for i in snakes_list:
        if position == i[0]:
            position= i[1]
    return position


def play_one_dice_roll(position):
    dice_output = dice_throw()
    position = position + dice_output
    position = check_for_snakes_and_ladders(position)
    return position


def single_game(num_players):
    players_position = [0] * (num_players)
    players_steps = [0] * (num_players)

    while True:
        for i in range(num_players):
            players_position[i] = play_one_dice_roll(players_position[i])
            players_steps[i] += 1
            print(i, ' th player moved to ', players_position[i])
            if players_position[i] >= 90:
                return players_position, players_steps

def multiple_games(num_games,num_players):
    for i in range(num_games):
        p,s=single_game(num_players)
        print(p,s)

def multi_game_experiment(num_games, num_players, seed):
    random.seed(seed)
    for i in range(num_games):
        p,s=single_game(num_players)
        print(p,s)

if __name__ == '__main__':
    multi_game_experiment(3,1,1)
    multi_game_experiment(3,1,2)
    multi_game_experiment(3,1,3)