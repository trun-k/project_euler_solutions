"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math


def solve(n):
    ans = 1
    for i in range(1, n+1):
        ans = math.lcm(ans, i)
    return ans