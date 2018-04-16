#!/usr/bin/env python3


def quadratic(a, b, c):
    """Compute the solution to a quadratic equation."""
    import cmath
    
    q = cmath.sqrt(b**2-4*a*c)
    x1 = (-b+q)/(2*a)
    x2 = (-b-q)/(2*a)
    
    return (x1, x2)


