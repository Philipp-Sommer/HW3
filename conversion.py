"""
This module provides functions to convert between Celsius to Fahrenheit.
"""


def celsius2fahrenheit(celsius):
    """Convert a temperature given in Celsius to Fahrenheit."""
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

def fahrenheit2celsius(fahrenheit):
    """Convert a temperature given in Fahrenheit to Celsius."""
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

