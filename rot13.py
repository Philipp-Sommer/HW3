#!/usr/bin/env python3

"""Functions to en-/decode a string using the rot13 algorithm."""

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
        
#text = "Arire gehfg n cebtenz lbh qba'g unir fbheprf sbe."
#solution = decode(text)
#print(solution)

def encode(text):
    """Function to encode a string using the rot13 algorithm."""
    
    #import for getting alphabet
    import string

    #helping variables
    alphabet = string.ascii_uppercase
    alphabet = list(alphabet)
    encoder = []
    output = []

    #calculations
    for i, c in enumerate(alphabet):
        if i <= 12:
            encoder.append(alphabet[i+13])
        else:
            encoder.append(alphabet[i-13])
    
    text = list(text.upper())
    for i, c in enumerate(text):
        count = 0 #counting for each character whether its in the alphabet
        for character in alphabet:
            if c == character:
                count = 1 #character is in the alphabet
                index_alphabet = (alphabet.index(character))
                output.append(encoder[index_alphabet])
        if count == 0: #if character is not in the alphabet
            output.append(c)

    #output
    output = ''.join(output) #change list to str
    return output

#text = "Never trust a program you don't have sources for."
#solution = encode(text)
#print(solution)
