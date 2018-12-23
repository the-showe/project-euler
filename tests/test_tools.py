import unittest
from tools import *
import os


class ToolsTest(unittest.TestCase):
    def test_is_prime(self):
        with open(os.path.join('lookups', 'first_1000_primes.txt'), 'r') as fp:
            first_1000_primes = [int(i) for i in fp.readlines()]

        if len(first_1000_primes) != 1000:
            raise ValueError('Length should equal 1000.')

        if first_1000_primes[0] != 2:
            raise ValueError('First value should be 2.')

        non_primes = [i for i in range(max(first_1000_primes))
                      if i not in first_1000_primes]

        for prime in first_1000_primes:
            self.assertTrue(is_prime(prime), prime)

        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime), non_prime)
