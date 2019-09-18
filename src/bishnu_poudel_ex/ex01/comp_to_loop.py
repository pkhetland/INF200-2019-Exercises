""" list comprehension to loop -for Assignment 1"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"


def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    listk2 = []
    for k in range(n):
        if k % 3 == 1:
            listk2.append(k ** 2)
    return listk2


# Checking the output---
# a=squares_by_comp(10)
# print(a)
# print("-----------------------------------------------------------------------------")
# print("-----------------------------------------------------------------------------")
# print("-----------------------------------------------------------------------------")
# b=squares_by_loop(10)
# print(b)

if __name__ == '__main__':
    if squares_by_comp(10) != squares_by_loop(10):
        print('ERROR!')
    else:
        print('NO ERROR!')
