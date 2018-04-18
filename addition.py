#!/usr/bin/env python3

"""
This module provides a function to sum all numbers from 0 up to a given integer.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Nathalie Friess last <first.last@edu.uni-graz.at>
"""

def sum_to(num):
    """
    Sum all numbers from 0 up to a given integer.

    Assert that no negative numbers are entered.
    """

    assert num >= 0, "Input was negative!"
    count = 0
    addition = 0
    while count <= num:
        addition += count
        count += 1
    return addition
