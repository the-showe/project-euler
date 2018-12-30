"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from tools import run_euler, prime_numbers


@run_euler
def get_nth_prime(n):
    primes = list(prime_numbers())
    return primes[n - 1]


get_nth_prime(10001)
