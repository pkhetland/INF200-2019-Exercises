# -*- coding: utf-8 -*-

__author__ = 'Bishnu Poudel'
__email__ = 'bishnu.poudel@nmbu.no'



class LCGRand:
    a = 16807
    m = 2 ** 31 - 1

    def __init__(self, input_seed):
        self.input_seed = input_seed


    def rand(self):
        self.input_seed= (self.a * self.input_seed) % self.m
        return self.input_seed


class ListRand:

    def __init__(self, list_input):
        self.list_input= list_input
        self.i = -1


    def rand(self):
        self.i += 1
        return self.list_input[self.i]


if __name__== "__main__":
    c = LCGRand(346)
    print(c.rand())
    print(c.rand())


    array_list=[1,2,3]
    d= ListRand(array_list)
    print(  d.rand() )
    print( d.rand() )
    print(d.rand())
    print(d.rand())


   
