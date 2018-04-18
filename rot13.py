#!/usr/bin/env python3

"""
Functions to en-/decode a string using the rot13 algorithm.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Nathalie Friess last <first.last@edu.uni-graz.at>
"""

def decode(text):
    """Function to decode a string using the rot13 algorithm."""

    #import for getting alphabet
    import string

    #helping variables
    alphabet = string.ascii_uppercase
    alphabet = list(alphabet)
    decoder = []
    output = []

    #calculations
    for i, c in enumerate(alphabet):
        if i <= 12:
            decoder.append(alphabet[i+13])
        else:
            decoder.append(alphabet[i-13])

    text = list(text.upper())
    for i, c in enumerate(text):
        count = 0 #counting for each character whether its in the alphabet
        for character in alphabet:
            if c == character:
                count = 1 #character is in the alphabet
                index_alphabet = (alphabet.index(character))
                output.append(decoder[index_alphabet])
        if count == 0: #if character is not in the alphabet
            output.append(c)

    #output
    output = ''.join(output) #change list to str
    return output

def encode(text):
    """Function to encode a string using the rot13 algorithm."""
    output = decode(text)
    return output
