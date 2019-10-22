# -*- coding: utf-8 -*-

__author__ = 'Petter Hetland'
__email__ = 'pehe@nmbu.no'


class LCGRand:
    """
    This class is a linear congruential generator (LCG),
    which generates numbers according to the following equation


    r[n+1] = a * r[n] mod m

    where ``a = 7**5 = 16807`` and ``m = 2**31-1``.
    """
    def __init__(self, seed):
        self.init_number = seed

    def rand(self):
        self.next_number = (16807 * self.init_number) % (2**31-1)
        self.init_number = self.next_number
        return self.next_number


class ListRand:
    def __init__(self, list):
        self.list = list
        self.times_called = 0

    def rand(self):
        item = self.times_called
        self.times_called += 1
        try:
            return self.list[item]
        except IndexError:
            raise RuntimeError("We're out of numbers!")
