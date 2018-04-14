#!/usr/bin/env python3

"""
This module provides a function to sum all numbers from 0 up to a given integer.

.. moduleauthor: 
"""


def sum_to(num):
    """
    Sum all numbers from 0 up to a given integer.

    Assert that no negative numbers are entered.
    """
    assert num >= 0, "Input was negative!"
    count = 0
    sum = 0
    while count <= num:
        sum += count
        count += 1
    return sum