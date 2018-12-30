"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from tools import run_euler, prime_numbers


@run_euler
def get_sum_of_primes_less_than(n):
    return sum(prime_numbers(n))


get_sum_of_primes_less_than(2000000)
