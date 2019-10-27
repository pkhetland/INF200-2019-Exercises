# -*- coding: utf-8 -*-

__author__ = 'Bishnu Poudel'
__email__ = 'bishnu.poudel@nmbu.no'

import random


class Walker:
    steps_taken = 0

    def __init__(self, initial_position, final_position):
        self.initial_position = initial_position
        self.final_position = final_position

    def move(self):
        if random.randint(0, 1) == 0:
            self.initial_position -= 1
        else:
            self.initial_position += 1
        self.steps_taken += 1
        # return self.initial_position

    def is_at_home(self):
        if self.initial_position == self.final_position:
            return True
        return False

    def get_position(self):
        return self.initial_position

    def get_steps(self):
        return self.steps_taken


if __name__ == "__main__":
    for j in (1, 2, 5, 10, 20, 50, 100):
        steps = []
        for i in range(5):
            walker = Walker(0, j)
            while not walker.is_at_home():
                walker.move()
            steps.append(walker.get_steps())
        print(" Distance: ", j, " -> Paths length: ", steps)
