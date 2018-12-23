"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

from tools import run_euler


def get_sum_of_squares_up_to(n):
    squares = [i ** 2 for i in range(1, n + 1)]
    return sum(squares)


@run_euler
def sum_square_difference_up_to(n):
    sum_of_squares = get_sum_of_squares_up_to(n)
    square_of_sum = sum(range(1, n + 1)) ** 2
    difference = square_of_sum - sum_of_squares
    return difference


sum_square_difference_up_to(100)
