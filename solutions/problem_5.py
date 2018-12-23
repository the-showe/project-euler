"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

from tools import run_euler


@run_euler
def smallest_number_divisible_by_all_numbers_up_to(n):
    divisors = list(range(1, n + 1))

    # As returned value must divide by all numbers
    # loop should step by the highest number to be efficient.
    step = max(divisors)

    i = 0
    while True:
        if i != 0 and all(i % divisor == 0 for divisor in divisors):
            return i
        i += step


smallest_number_divisible_by_all_numbers_up_to(20)
