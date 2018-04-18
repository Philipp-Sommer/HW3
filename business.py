#!/usr/bin/env python3

"""This module offers simple functions for interest calculation.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Nathalie Friess last <first.last@edu.uni-graz.at>
"""

def interest(capital, rate, years=1, tax=0):
    """
    Calculates interest of an investment.
    """
    assert rate <= 1 and rate >= 0, 'Wrong rate!'
    assert tax <= 1 and tax >= 0, 'Wrong tax!'
    result = capital * (1 + rate * (1 - tax)) ** years - capital
    return result

def terminal_value(capital, rate, years=1, tax=0):
    """
    Calculates terminal value of an investment.
    """
    assert rate <= 1 and rate >= 0, 'Wrong rate!'
    assert tax <= 1 and tax >= 0, 'Wrong tax!'
    result = capital + interest(capital, rate, years, tax)
    return result
