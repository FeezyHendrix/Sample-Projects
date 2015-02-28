"""
Title: An Introduction to Interactive Programming in Python -
Week 0b Practice Challenge

Author: Mandeep Bhutani
Date: 2/14/2015

Problem: Heron's Formula states that the area of a triangle is equal to
the square root of s(s-a)(s-b)(s-c) where a, b, and c are the lengths
of the sides of the triangle and s = 1/2(a + b + c) is the semi-perimeter
of the triangle. Given the variables x0, y0, x1, y1, x2, and y2, write
a Python program that computes a variable 'area' whose value is the area
of the triangle with vertices (x0, y0), (x1, y1), and (x2, y2).
"""

# In order to skip writing multiple formulas for the distance between two
# coordinates, a function to calculate the distance is defined.


def distance(x0, y0, x1, y1):
    dist = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
    return dist


def area(x0, y0, x1, y1, x2, y2):
    a = distance(x0, y0, x1, y1)
    b = distance(x1, y1, x2, y2)
    c = distance(x0, y0, x2, y2)
    s = (0.5 * (a + b + c))
    heron = (s * (s - a) * (s - b) * (s - c))**0.5
    return heron
print area(-2, 4, 1, 6, 2, 1)
