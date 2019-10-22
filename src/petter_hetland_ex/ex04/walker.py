# -*- coding: utf-8 -*-

__author__ = 'Petter Hetland'
__email__ = 'pehe@nmbu.no'

import random as r


class Walker:
    def __init__(self, x_0, h):
        self.x = x_0
        self.h = h
        self.num_steps = 0

    def move(self):
        if r.randint(0, 1) > 0.5:
            self.x += 1
        else:
            self.x -= 1

        self.num_steps += 1
        return self.x, self.num_steps

    def get_position(self):
        return self.x

    def is_at_home(self):
        if self.x == self.h:
            return True
        return False

    def get_steps(self):
        return self.num_steps


def walk_home(initial_position, distance):
    """Runs a full simulation of getting from the initial position
    to home, with a given distance beetween.
    """
    w = Walker(initial_position, distance)
    while not w.is_at_home():
        w.move()
    return w.get_steps()
