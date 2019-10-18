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
            

class ListRand:
    
    def __init__(self, list_input):
        self.list_input= list_input
        self.i=0
         

    def rand(self):                
        while True:
            try:
                yield self.list_input[self.i]
            except Exception as e:
                print(e)
                return
            else:
                self.i += 1


if __name__== "__main__":
    c = LGCRand(6)
    gen = c.rand()
    for i in range(5):
        print (next(gen))
        
    array_list=[1,2,3]
    d= ListRand(array_list)
    gen1 = d.rand()
    for i in range(3):
        print(next(gen1))
        
    print(next(gen1))

   
