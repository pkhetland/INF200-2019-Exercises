# -*- coding: utf-8 -*-

__author__ = 'Bishnu Poudel'
__email__ = 'bishnu.poudel@nmbu.no'

# from hypothesis import given, strategies
import collections
import math


# Writing a compare function for use in one of the tests
def compare(first, second):
    return collections.Counter(first) == collections.Counter(second)


def bubble_sort(data1):
    data2 = list(data1)
    if len(data2) <= 1:
        return data2
    else:
        for j in range(len(data2)):
            for i in range(len(data2) - j - 1):
                if data2[i + 1] < data2[i]:
                    data2[i + 1], data2[i] = data2[i], data2[i + 1]
        return data2


def test_empty():
    assert bubble_sort([]) == []


# @given(strategies.lists(strategies.integers()))
def test_single():
    assert bubble_sort([0]) == [0]


def test_sorted_is_not_original():
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data is not sorted_data


def test_original_unchanged():
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert compare(data, sorted_data)


def test_sort_sorted():
    data = [1, 2, 3, 4, 5, 11, 19]
    sorted_data = bubble_sort(data)
    sorted_by_python = sorted(data)
    assert sorted_data == sorted_by_python


def test_sort_reversed():
    data = [19, 11, 5, 4, 3, 2, 1]
    sorted_data = bubble_sort(data)
    sorted_by_python = sorted(data)
    assert sorted_data == sorted_by_python


def test_sort_all_equal():
    data = [3, 3, 3, 3, 3, 3]
    sorted_data = bubble_sort(data)
    sorted_by_python = sorted(data)
    assert (compare(data, sorted_data) and sorted_by_python == sorted_data)


def test_sorting():
    int_example = bubble_sort([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
    sorted_int_example = sorted(int_example)
    float_example = bubble_sort(
        [1.098, 0.009, 3.45, math.log(10), math.log2(32), 4.99, 5.4, 1.1e3])
    sorted_float_example = sorted(float_example)
    string_example = bubble_sort(
        ['kangaroo', 'zebra', 'an', 'elephant', 'er', 'ikke'])
    sorted_string_example = sorted(string_example)
    characters_example = bubble_sort(
        ['1', '234', 'name', 'inf200', '?,.', '?', '&&*'])
    sorted_characters_example = sorted(characters_example)
    assert (int_example == sorted_int_example and
            float_example == sorted_float_example and
            string_example == sorted_string_example and
            characters_example == sorted_characters_example)
