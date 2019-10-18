# -*- coding: utf-8 -*-

__author__ = 'Bishnu Poudel'
__email__ = 'bishnu.poudel@nmbu.no'

import random


class LGCRand:
    a = 16807
    m = 2 ** 31 - 1

    def __init__(self, input_seed):
        self.input_seed = input_seed


# Using generator/yield concept    
    def rand(self):
        self.input_seed= (self.a * self.input_seed) % self.m
        while True:
            yield self.input_seed
            self.input_seed= (self.a * self.input_seed) % self.m
            

# class ListRand:
#     def __init__(self):
#         pass
#
#     def rand(self):
#         pass
#     pass

#if __name__== "__main__":
c = LGCRand(6)
gen = c.rand()
for i in range(5):
    print (next(gen))

   
