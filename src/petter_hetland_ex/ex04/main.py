# -*- coding: utf-8 -*-

__author__ = 'Petter Hetland'
__email__ = 'pehe@nmbu.no'

from myrand import LCGRand, ListRand
from walker import Walker, walk_home


# Test walk_home() function from walker.py with different distances
print('\nTesting walk_home function:')
for distance in [1, 2, 5, 10, 20, 50, 100]:
    moves_count = [walk_home(0, distance) for _ in range(5)]
    print("Distance: {:5} -> Path lengths: {}"
          .format(distance, moves_count))

# Instantiate and test LCGRand:
print('\nTesting LCGRand:')
lcg_rand = LCGRand(346)
for i in range(5):
    print(f'Random number {i+1}: {lcg_rand.rand()}')

# Instantiate and print ListRand class
print('\nTesting ListRand:')
list_rand = ListRand([1, 6, 0, 4, 3, 8])
for i in range(5):
    print(f'Random number {i+1}: {list_rand.rand()}')
