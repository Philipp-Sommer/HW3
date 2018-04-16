#!/usr/bin/env python3

"""Main module of this homework."""
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
            print(equations.quadratic(1, 2, 3))
            print(addition.sum_to(5))
            print(conversion.celsius2fahrenheit(3))
            print(conversion.fahrenheit2celsius(3))
            print(geometry.perimeter_right_triangle(1, 2))
            print(geometry.area_right_triangle(1, 2))
            print(geometry.perimeter_circle(1))
            print(geometry.area_circle(1))
            print(geometry.surface_sphere(1))
            print(geometry.volume_sphere(1))
            print(geometry.surface_cylinger(1, 2))
            print(geometry.volume_cylinder(1, 2))
            print(geometry.surface_cone(1, 2))
            print(geometry.volume_cone(1, 2))
            print(business.interest(1000, 0.3))
            print(business.terminal_value(1000, 0.3))
            print(rot13.encode('abcd'))
            print(rot13.decode('abcd'))
            print(vrptw = vrptw_reader.read_string_list())
            print(vrptw_reader.get_demand(vrptw, 1))
            print(vrptw_reader.calc_distance(vrptw, 1, 2))
            return 0
        except:
            return 1

if __name__ == "__main__":
    sys.exit(main())

