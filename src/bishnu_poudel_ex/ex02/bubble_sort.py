""" Bubble sort for Assignment 2"""
__author__ = "Bishnu Poudel"
__email__ = "bishnu.poudel@nmbu.no"


def bubble_sort(data1):
    data2 = list(data1)
    end = len(data2)
    if len(data2) <= 1:
        return data2
    else:
        for j in range(len(data2)):
            end = end - 1
            for i in range(end):
                if data2[i + 1] < data2[i]:
                    temp = data2[i + 1]
                    data2[i + 1] = data2[i]
                    data2[i] = temp
    return data2


if __name__ == "__main__":
    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
