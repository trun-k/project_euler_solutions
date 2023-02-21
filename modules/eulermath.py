import math


def sum_of_natural_numbers(n):
    """
    Return sum of natural numbers from 1 to n.
    """
    return int((n*(n+1))/2)


def sum_of_square_of_natural_numbers(n):
    """
    Return sum of squares of natural numbers from 1 to n.
    """
    return int((n*(n+1)*(2*n + 1))//6)


def get_primes(n):
    """
    Return list of prime numbers till n.
    """
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, math.ceil(math.sqrt(n))):
        for j in range(i*i, n, i):
            sieve[j] = False
    primes = []
    for i in range(n+1):
        if sieve[i] == True:
            primes.append(i)
    return primes


def check_prime(n):
    """
    Check if n is a prime number.
    """
    for i in range(2, math.ceil(math.sqrt(n))):
        if n%i==0:
            return False
    return True


def prime_factors(n):
    """
    Return a list of prime factors of n.
    """
    factors = []
    if n%2==0:
        n = n//2
        factors.append(2)
    for i in range(3, math.ceil(math.sqrt(n)), 2):
        if n%i==0:
            n = n//i
            factors.append(i)
    return factors


def check_palindrome(n):
    """
    Checks if a number n is palindrome 
    """
    s = str(n)
    for i in range(len(s)):
        if s[i]!=s[-i-1]:
            return False
    return True
