from copy import copy

from chutes_simulation import Board, Player, ResilientPlayer

# b= Board()
# print( b.position_adjustment(1))
# p= Player()

r = ResilientPlayer(extra_steps=6)
while r.position != 5:
    r.position = 23
    r.move()
# r.position += r.board.position_adjustment(r.position)
a = copy(r.position)
r.move()
print(a, r.position)
