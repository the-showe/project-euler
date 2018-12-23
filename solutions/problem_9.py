"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from tools import run_euler


def find_pythagorean_triplet_equal_to(n):
    for b in range(1, n):
        for a in range(1, b):
            c = ((a ** 2) + (b ** 2)) ** 0.5
            if a + b + c == n:
                return a, b, c


@run_euler
def find_product_of_pythagorean_triplet_equal_to(n):
    a, b, c = find_pythagorean_triplet_equal_to(n)
    return a * b * c


find_product_of_pythagorean_triplet_equal_to(1000)
