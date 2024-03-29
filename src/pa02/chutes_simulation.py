# -*- coding: utf-8 -*-
'''Snakes and Ladders using OOP approach.'''
__author__ = 'Petter K. Hetland, Bishnu Poudel'
__email__ = 'pehe@nmbu.no, bishnu.poudel@nmbu.no'

import random as r
from random import randint, shuffle


class Board:
    """
    The Board class shall manage all information about ladders, snakes,
    and the goal.
    """
    default_ladders = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                       (65, 82), (68, 85)]
    default_chutes = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                      (74, 12), (87, 70)]

    def __init__(self,
                 ladders=default_ladders,
                 chutes=default_chutes,
                 goal=90):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        """Shall return true if it is passed a position at or beyond the goal
        """
        return position >= self.goal

    def position_adjustment(self, position):
        """
        Shall handle changes in position due to snakes and ladders.

        Arguments
        -------
        Position (Int)

        Returns
        -------
        Adjustment(Int) - The amount of steps the player has to move
        in either direction to get the correct position.
        """
        adjustment = 0
        for ladder in self.ladders:
            if position == ladder[0]:
                adjustment = ladder[1] - ladder[0]

        for chute in self.chutes:
            if position == chute[0]:
                adjustment = chute[1] - chute[0]

        return adjustment


class Player:
    """
    Manages information about player position, including information on which
    board a player “lives”.

    Arguments
    -------
    board (Class)
    """

    def __init__(self, board=Board()):
        self.board = board
        self.position = 0
        self.num_moves = 0

    def move(self):
        """Will move the player by implementing a die cast,
         and, if necessary, a move up a ladder or down a chute.
        """
        self.num_moves += 1
        dice_value = randint(1, 6)
        self.position += dice_value
        jump = self.board.position_adjustment(self.position)
        self.position += jump


class ResilientPlayer(Player):
    """
    When a resilient player slips down a chute, he will take extra steps in
    the next move, in addition to the roll of the die. The number of extra
    teps is provided as an argument to the constructor, default is 1.
    """

    def __init__(self,
                 board=Board(),
                 extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps
        self.got_chutes = False

    def move(self):
        """Modifies the "move"-method of the super() by adding the given
        number of extra steps. Extra steps added if the got_chutes variable is
        True.
        """
        self.num_moves += 1
        dice_value = randint(1, 6)
        self.position += dice_value
        jump = self.board.position_adjustment(self.position)

        if jump < 0:
            self.got_chutes = True

        self.position += jump
        if self.got_chutes:
            self.position += self.extra_steps


class LazyPlayer(Player):
    """After climbing a ladder, a lazy player drops a given number of steps.
    The number of dropped steps is an optional argument to the constructor,
    default is 1.
    """

    def __init__(self,
                 board=Board(),
                 dropped_steps=1):
        super().__init__(board)
        self.drop_steps = dropped_steps
        self.got_ladder = False

    def move(self):
        """Modifies the "move"-method of the super() by adding the given
        number of drop steps. Drop steps subtracted if the got_ladder variable
        is True and the number of drop steps is less than dice value.
        """
        self.num_moves += 1
        dice_value = randint(1, 6)
        self.position += dice_value
        if self.got_ladder and self.drop_steps <= dice_value:
            self.position -= self.drop_steps

        jump = self.board.position_adjustment(self.position)
        self.position += jump

        self.got_ladder = False
        if jump > 0:
            self.got_ladder = True


class Simulation:
    """Manages an entire simulation.
    """

    def __init__(self, player_field,
                 board=Board(),
                 seed=1,
                 randomize_players=True):
        self.player_field = player_field  # List of players
        self.board = board  # Class
        self.seed = seed  # Integer
        self.randomize_players = randomize_players  # Boolean value

        self.results = []  # Stores the results of simulations as a list
        self.players_dict = {}  # Maps num of players to each type
        self.winners_dict = {}  # Maps num of winners per type
        self.durations_dict = {}  # Maps duration of games per type

        # Fill in players_per_type_dict
        for player in player_field:
            self.players_dict[player.__name__] = \
                self.player_field.count(player)

        # Fill in winner_per_type_dict with zeros
        for player in player_field:
            self.winners_dict[player.__name__] = 0

        # Randomize player field if parameter is set to True
        if randomize_players:
            shuffle(self.player_field)

    def single_game(self):
        """Runs a single game
        Returns
        --------
        tuple - number of moves made and the type of the winner
        """

        pl = []

        for play in self.player_field:
            pl.append(play())

        while True:
            for player in pl:
                player.move()
                if player.position >= 90:
                    result = (player.num_moves, type(player).__name__)
                    return result

    def run_simulation(self, num_of_sims):
        """
        Runs a given number of simulations and stores the results in the
        Simulation class.

        Arguments
        -------
        num_of_sims = int
        """
        r.seed(self.seed)  # Applies the given seed for the simulation

        for _ in range(num_of_sims):
            self.results.append(self.single_game())

    def get_results(self):
        """
        Returns all results generated by run_simulation() calls so far as a
        list of result tuples, e.g., [(10, 'Player'), (6, 'ResilientPlayer')].
        """
        return self.results

    def winners_per_type(self):
        """
        Returns a dictionary mapping player types to the number of wins,
        e.g., {'Player': 4, 'LazyPlayer': 2, 'ResilientPlayer': 5}
        """
        for result in self.results:
            for player in set(self.player_field):
                if result[1] == player.__name__:
                    self.winners_dict[player.__name__] += 1
        return self.winners_dict

    def durations_per_type(self):
        """returns a dictionary mapping player types to lists of game
        durations for that type, e.g., {'Player': [11, 25, 13], 'LazyPlayer':
         [39], 'ResilientPlayer': [8, 7, 6, 11]}
         """
        for player in set(self.player_field):  # Set values to empty lists
            self.durations_dict[player.__name__] = []

        for result in self.results:  # Add durations to value lists
            for player in set(self.player_field):
                if result[1] == player.__name__:
                    self.durations_dict[player.__name__].append(result[0])

        return self.durations_dict

    def players_per_type(self):
        """returns a dictionary showing how many players of each type
        participate, e.g., {'Player': 3, 'LazyPlayer': 1, 'ResilientPlayer': 0}
        """
        for player in self.player_field:
            self.players_dict[player.__name__] = \
                self.player_field.count(player)
        return self.players_dict


if __name__ == "__main__":
    b = Board()
    sim = Simulation([Player,
                      Player,
                      LazyPlayer,
                      ResilientPlayer,
                      LazyPlayer],
                     randomize_players=True)
    sim.run_simulation(10)
    print('Results: ', sim.get_results())
    print('\nDurations per type: ', sim.durations_per_type())
    print('\nNum of wins per type: ', sim.winners_per_type())
    print('\nNum of players per type: ', sim.players_per_type())
