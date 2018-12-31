"""
Power digit sum
Problem 16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

from tools import run_euler, DigitalString


@run_euler
def get_sum_of_digits_of_power_result(n, power):
    result = n ** power
    result_str = DigitalString(result)
    result_list = result_str.to_ints()
    return sum(result_list)


get_sum_of_digits_of_power_result(2, 1000)
