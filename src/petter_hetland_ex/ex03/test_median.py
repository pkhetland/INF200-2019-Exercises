# -*- coding: utf-8 -*-

__author__ = "Petter Hetland"
__email__ = "pehe@nmbu.no"


# Median function sourced from ex03.rst authored by Yngve Mardal Moe
def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (
        sdata[n // 2] if n % 2 == 1
        else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2])
    )

