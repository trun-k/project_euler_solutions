"""
Python 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import eulermath

def solve(n):
    return 3*eulermath.sum_of_natural_numbers((n-1)//3) + 5*eulermath.sum_of_natural_numbers((n-1)//5)