"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""

from tools import run_euler, fibonacci


def is_even(n):
    return n % 2 == 0


def get_fibonacci_terms_below(limit):
    terms = []
    fib = fibonacci(1000, starters=[1, 2])

    while True:
        n_term = next(fib)
        if n_term < limit:
            terms.append(n_term)
        else:
            break

    return terms


@run_euler
def sum_even_fibs_below(n):
    terms = get_fibonacci_terms_below(n)
    even_terms = [i for i in terms if is_even(i)]
    return sum(even_terms)


sum_even_fibs_below(4000000)