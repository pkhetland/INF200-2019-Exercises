def bubble_sort(data1):
    data=list(data1)
    end = len(data)
    if len(data) <= 1:
        return data
    else:
        for j in range(len(data)):
            end = end - 1
            for i in range(end):
                if data[i + 1] < data[i]:
                    temp = data[i + 1]
                    data[i + 1] = data[i]
                    data[i] = temp
    return data


# print( bubble_sort([1,2,4,2,1]) )


if __name__ == "__main__":
    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
