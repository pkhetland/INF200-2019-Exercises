# -*- coding: utf-8 -*-

__author__ = 'Bishnu Poudel'
__email__ = 'bishnu.poudel@nmbu.no'

import random


def lcg(modulus, a, c, seed):
  while True:
    seed = (a * seed + c) % modulus
    yield seed

#class LGCRand:
#    a = 16807
#    m = 2 ** 31 - 1
#
#    def __init__(self, input_seed):
#        self.input_seed = input_seed
#        pass
#
#    def rand(self):
#        return (self.a * self.input_seed) % self.m

# class ListRand:
#     def __init__(self):
#         pass
#
#     def rand(self):
#         pass
#     pass

if __name__== "__main__":
    c= lcg(5,2,3,1)
    print(c)
#    l=LGCRand(6);
#    print( l.rand())
