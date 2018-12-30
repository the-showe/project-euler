import string
import time


def run_euler(func):
    def wrapper(*arg, **kwargs):
        t1 = time.time()
        answer = func(*arg, **kwargs)
        t2 = time.time()
        print('Answer: {answer}\nTime (s): {time:0.2f}'.format(
            answer=answer,
            time=t2 - t1
        ))
    return wrapper


class DigitalString(str):
    """
    Validates and returns a string consisting only of digits.
    """

    def __init__(self, n):
        super().__init__()
        self.number = n

        if not any(isinstance(self.number, test_type) for test_type in (int, str)):
            raise TypeError(
                'Input must be either int or str. '
                '{number_type} was passed.'.format(
                    number_type=type(self.number)
                )
            )

        self.digital_string = str(n)

        if not all(d in string.digits for d in self.digital_string):
            raise ValueError(
                'Input must be digital. {number} was passed.'.format(
                    number=self.number
                )
            )

    def __str__(self):
        return self.digital_string


def get_triangle_number(n):
    return int(n * (n + 1) / 2)


def get_factors(n):
    factors = []
    limit = int(n ** 0.5)

    for i in range(1, limit + 1):
        if n % i == 0:
            factors += [n // i, i]
    return set(factors)


def prime_numbers(limit=1000000):
    """
    Copied from https://stackoverflow.com/a/2901856

    Prime number generator. Yields the series
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
    using Sieve of Eratosthenes.
    """

    yield 2
    sub_limit = int(limit**0.5)
    flags = [True, True] + [False] * (limit - 2)
    # Step through all the odd numbers
    for i in range(3, limit, 2):
        if flags[i]:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i * i, limit, i << 1):
                flags[j] = True


def is_prime(n):
    return n in prime_numbers(limit=n + 1)


def fibonacci(n, starters=(1, 2)):
    a, b = starters
    for i in range(n):
        yield a
        a, b = b, a + b


def product(num_list):
    cumulative = num_list[0]
    for i in num_list[1:]:
        cumulative *= i
    return cumulative


def get_slices(iterable, length):
    slices = []
    for i in range(len(iterable) - length):
        slices.append(iterable[i: i + length])
    return slices
