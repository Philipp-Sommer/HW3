#!/usr/bin/env python3

"""Functions calculating characteristic numbers of common gemoetric shapes.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Nathalie Friess last <first.last@edu.uni-graz.at>
"""

import math

def perimeter_right_triangle(c1, c2):
    """
    Return the perimeter of a right triangle.

    `c1`, `c2`: catheti of the right triangle
    """
    hyp = math.sqrt(c1 ** 2 + c2 ** 2)
    perimeter = hyp + c1 + c2
    return perimeter


def area_right_triangle(c1, c2):
    """
    Return the area of a right triangle.

    `c1`, `c2`: catheti of the right triangle
    """
    area = (c1 * c2) / 2
    return area


def perimeter_circle(r):
    """Return the perimeter of a circle with radius r."""
    radius = 2 * r * math.pi
    return radius


def area_circle(r):
    """Return the area of a circle with radius r."""
    area = r ** 2 * math.pi
    return area


def surface_sphere(r):
    """Return the surface of a sphere with radius r."""
    surface = 4 * math.pi * r ** 2
    return surface


def volume_sphere(r):
    """Return the volume of a sphere with radius r."""
    volume = 4 / 3 * math.pi * r ** 3
    return volume

def surface_cylinder(r, h):
    """Return the surface of a cylinder with radius r and height h."""
    surface = 2 * math.pi * r ** 2 + 2 * math.pi * r * h
    return surface


def volume_cylinder(r, h):
    """Return the volume of a cylinder with radius r and height h."""
    volume = math.pi * r ** 2 * h
    return volume


def surface_cone(r, h):
    """Return the surface of a right circular cone."""
    s = math.sqrt(r ** 2 + h ** 2)
    surface = math.pi * (r * s + r ** 2)
    return surface


def volume_cone(r, h):
    """Return the volume of a right circular cone."""
    volume = (math.pi * r ** 2 * h) / 3
    return volume
