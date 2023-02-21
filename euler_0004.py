"""
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import eulermath


def solve(n):
    ans = 0
    for i in range((10**n)-1,(10**n)//2,-1):
        for j in range((10**n)-1,(10**n)//2,-1):
            if eulermath.check_palindrome(i*j)==True:
                ans = max(ans, i*j)
    return ans