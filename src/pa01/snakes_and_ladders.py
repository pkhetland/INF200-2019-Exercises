# -*- coding: utf-8 -*-

__author__ = 'Nils Skadderenes, Bishnu Poudel'
__email__ = 'nils.skadderenes@nmbu.no,bishnu.poudel@nmbu.no'

'''Test'''
# test from Bish

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

 def define_players_and_play():
    num_players = int( input("Number of players:"))
    players_position= [0]* (num_players+1)
    print(players_position)

    for i in range( 1,  num_players+1):
        dice_output = dice_throw()
        print(dice_output)
        players_position[i] = players_position[i] + dice_output
        players_position[i] = check_for_snakes_and_ladders(players_position[i])
        
    return players_position

def win_check():
    pass
    
re=define_players_and_play()
print(re)
