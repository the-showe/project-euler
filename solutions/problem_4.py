"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from tools import run_euler, DigitalString


def is_palindrome(digital_string):
    return digital_string == digital_string[::-1]


def get_all_n_digit_numbers(n):
    lower_bound = int('1' + '0' * (n -1))
    upper_bound = int('1' + '0' * (n))
    return range(lower_bound, upper_bound)


@run_euler
def get_largest_palindrome_product_of_n_digit_numbers(n):
    all_n_digit_numbers = get_all_n_digit_numbers(n)
    all_products = []

    for i in all_n_digit_numbers:
        for j in all_n_digit_numbers:
            all_products.append(i * j)

    palindromes = [k for k in all_products if is_palindrome(DigitalString(k))]
    return max(palindromes)


get_largest_palindrome_product_of_n_digit_numbers(3)
