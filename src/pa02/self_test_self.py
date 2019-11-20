from copy import copy

from chutes_simulation import Board, Player, ResilientPlayer, Simulation, \
    LazyPlayer
s = Simulation([Player,ResilientPlayer,LazyPlayer],randomize_players=True)
a= s.single_game()
print(a)
