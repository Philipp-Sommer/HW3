#!/usr/bin/env python3

"""Main module of this homework.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Nathalie Friess last <first.last@edu.uni-graz.at>
"""

import sys
import equations
import addition
import conversion
import geometry
import business
import rot13
import vrptw_reader

def main():
    """A function that uses all the functions above."""
    try:
        equations.quadratic(1, 2, 3)
        addition.sum_to(5)
        conversion.celsius2fahrenheit(3)
        conversion.fahrenheit2celsius(3)
        geometry.perimeter_right_triangle(1, 2)
        geometry.area_right_triangle(1, 2)
        geometry.perimeter_circle(1)
        geometry.area_circle(1)
        geometry.surface_sphere(1)
        geometry.volume_sphere(1)
        geometry.surface_cylinder(1, 2)
        geometry.volume_cylinder(1, 2)
        geometry.surface_cone(1, 2)
        geometry.volume_cone(1, 2)
        business.interest(1000, 0.3)
        business.terminal_value(1000, 0.3)
        rot13.encode('abcd')
        rot13.decode('abcd')
        vrptw = vrptw_reader.read_string_list()
        vrptw_reader.get_demand(vrptw, 1)
        vrptw_reader.calc_distance(vrptw, 1, 2)
        return 0
    except:
        return 1

if __name__ == "__main__":
    sys.exit(main())
