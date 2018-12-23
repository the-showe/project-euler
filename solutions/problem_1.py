"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from tools import run_euler


def is_multiple_of_3_of_5(n):
    return n % 3 == 0 or n % 5 == 0


@run_euler
def get_total_multiples_below(n):
    valid_multiples = [i for i in range(1, n) if is_multiple_of_3_of_5(i)]
    return sum(valid_multiples)


get_total_multiples_below(1000)
