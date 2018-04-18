#!/usr/bin/env python3

"""Functions for reading and working with VRPTW text input files.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Nathalie Friess last <first.last@edu.uni-graz.at>
"""

def read_string_list(filename='r101'):
    """
    Reads a .txt file into a list of strings.
    """
    #filename extension 'txt' must be added if not included
    if '.txt' not in filename:
        filename = filename + '.txt'
        
    #helping variable
    output = []
    
    #opening file and returnin list of strings
    with open (filename, encoding = 'utf-8') as f:
        count_line = 0
        for line in f:
            count_line += 1
            #headers should not be included in list
            if count_line > 1:
                output.append(line)
    return output
  
#solution_f1 = read_string_list()
#print(solution_f1)

#-----------------------------------------------------------------------------

def get_demand(string_list, cust_no):
    """Function that returns customer's demand as floating point number."""
    element = cust_no - 1
    rel_string = string_list[element]
    rel_string_spl = rel_string.split()
    demand = float(rel_string_spl[3])
    return demand

#string_list = read_string_list()
#solution_f2 = get_demand(string_list, 5)
#print(solution_f2)

#-----------------------------------------------------------------------------

def calc_distance(string_list, cust_no1, cust_no2):
    """Function that returns the euclidean distance between two customers."""
    rel_string1 = string_list[cust_no1 - 1]
    rel_string2 = string_list[cust_no2 - 1]
    rel_string1_spl = rel_string1.split()
    rel_string2_spl = rel_string2.split()
    x1 = float(rel_string1_spl[1])
    y1 = float(rel_string1_spl[2])
    x2 = float(rel_string2_spl[1])
    y2 = float(rel_string2_spl[2])
    #print(x1, x2, y1, y2)
    distance = ((y1 - y2)**2 + (x1 - x2)**2)**(1/2)
    return distance

#string_list = read_string_list()
#solution_f3 = calc_distance(string_list, 1, 2)
#print(solution_f3)
# test
