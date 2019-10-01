""" Bubble sort for Assignment 2"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"


def bubble_sort(data1):
    data2 = list(data1)
    if len(data2) <= 1:
        return data2
    else:
        for j in range(len(data2)):
            for i in range(len(data2)-j-1):
                if data2[i + 1] < data2[i]:
                    data2[i + 1], data2[i] = data2[i],  data2[i + 1]
        return data2


if __name__ == "__main__":
    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
