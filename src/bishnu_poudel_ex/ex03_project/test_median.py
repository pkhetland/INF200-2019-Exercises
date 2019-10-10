# -*- coding: utf-8 -*-

__author__ = 'Bishnu Poudel'
__email__ = 'bishnu.poudel@nmbu.no'

# from hypothesis import given, strategies
import collections
# import math
import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_single():
    assert median([1]) == 1


def test_several_lists():
    odd_numbers = median([1, 3, 5, 7, 9])
    even_numbers = median([2, 4, 6, 8, 10])
    reverse_numbers = median([10, 9, 8, 7, 6, 5])
    unordered_floats = median([2.4, 3.6, 2.4, 1.2, 2.4, 3.6])
    unordered_ints = median([1, 2, 2, 3, 3, 2, 2, 1])
    assert (odd_numbers == 5 and
            even_numbers == 6 and
            reverse_numbers == 7.5 and
            unordered_floats == 2.4 and
            unordered_ints == 2)


def test_empty_returns_value_error():
    with pytest.raises(IndexError):
        median([])


def test_original_data_unchanged():
    data_before_median_calc = [2.4, 3.6, 2.4, 1.2, 2.4, 3.6]
    _ = median(data_before_median_calc)
    assert [2.4, 3.6, 2.4, 1.2, 2.4, 3.6] == data_before_median_calc


def test_tuple_or_list():
    tuple_example = (2.4, 3.6, 2.4, 1.2, 2.4, 3.6)
    list_example = [2.4, 3.6, 2.4, 1.2, 2.4, 3.6]
    assert(median(tuple_example) == median(list_example) == 2.4)
