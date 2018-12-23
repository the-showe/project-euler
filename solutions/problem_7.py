"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from tools import run_euler, is_prime


@run_euler
def get_nth_prime(n):
    num_primes_found = 0
    i = 0

    while True:
        if is_prime(i):
            num_primes_found += 1

        if num_primes_found == n:
            return i

        i += 1


get_nth_prime(10001)
