"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from tools import run_euler, is_prime, get_factors


def get_prime_factors(n):
    factors = get_factors(n)
    prime_factors = [f for f in factors if is_prime(f)]
    return prime_factors


@run_euler
def get_largest_prime_factor(n):
    return max(get_prime_factors(n))


get_largest_prime_factor(600851475143)
