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


def is_prime(n):
    # TODO research Robert William Hanks' is_prime solution
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def fibonacci(n, starters=(1, 2)):
    a, b = starters
    for i in range(n):
        yield a
        a, b = b, a + b


def product(num_list):
    cumulative = num_list[0]
    for i in num_list:
        cumulative *= i
    return cumulative
