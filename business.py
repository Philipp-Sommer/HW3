#!/usr/bin/env python3

"""This module offers simple functions for interest calculation."""

def interest(capital, rate, years=1, tax=0):
    assert rate <= 1 and rate >= 0, 'Wrong rate!'
    assert tax <= 1 and tax >= 0, 'Wrong tax!'
    interest = capital * (1 + rate * (1 - tax)) ** years - capital
    return interest

def terminal_value(capital, rate, years=1, tax=0):
    assert rate <= 1 and rate >= 0, 'Wrong rate!'
    assert tax <= 1 and tax >= 0, 'Wrong tax!'
    terminal_value = capital + interest(capital, rate, years, tax)
    return terminal_value