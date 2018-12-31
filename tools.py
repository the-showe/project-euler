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

        if not any(isinstance(self.number, test_type)
                   for test_type in (int, str)):
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

    def to_list(self):
        return list(self.digital_string)

    def to_ints(self):
        return [int(d) for d in self.digital_string]


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


class NumberGrid(list):
    def __init__(self, ls):
        super().__init__()
        self.grid = ls
        self.validate()

    def validate(self):
        # Check grid is type list
        if not isinstance(self.grid, list):
            raise TypeError(
                'Input must be list of lists. '
                '{list_type} was passed.'.format(
                    list_type=type(self.grid)
                )
            )

        # Check all rows are lists
        for row in self.grid:
            if not isinstance(row, list):
                raise TypeError(
                    'Input must be list of lists. '
                    'Non-list types were detected in list:\n{row}'.format(
                        row=row
                    )
                )

        # Check all values are int or float
        for row in self.grid:
            for value in row:
                if not (isinstance(value, int) or isinstance(value, float)):
                    raise TypeError(
                        'Each value must be int or float. '
                        'Other types were detected in row:\n{value}'.format(
                            value=value
                        )
                    )

        # Check all row lengths are equal
        row_lengths = [len(row) for row in self.grid]
        if not len(set(row_lengths)) == 1:
            raise ValueError('All row lengths must be equal:\n'
                             '{row_lengths}'.format(row_lengths=row_lengths))

    def __str__(self):
        return '\n'.join([str(row) for row in self.grid])

    def rows(self):
        return self.grid

    def columns(self):
        columns = []
        row_length = len(self.grid[0])

        for col_number in range(row_length):
            column = [row[col_number] for row in self.grid]
            columns.append(column)

        return columns

    @property
    def num_rows(self):
        return len(self.rows())

    @property
    def num_columns(self):
        return len(self.columns())

    def _get_diagonal(self, start_row_num, start_column_num, direction='right'):
        if not (start_column_num == 0 or start_row_num == 0):
            raise ValueError(
                'Either start_row_num or start_column_num must be 0.')

        if direction == 'right':
            col_num = start_column_num
            col_increment = 1
        elif direction == 'left':
            col_num = self.num_columns - start_column_num - 1
            col_increment = -1
        else:
            raise ValueError("direction must be either 'left' or 'right'.")

        row_range = list(range(start_row_num, self.num_rows))

        diagonal_values = []
        for row_num in row_range:
            diagonal_values.append(self.grid[row_num][col_num])

            col_num += col_increment

            if col_num >= self.num_columns:
                break

        return diagonal_values

    def diagonals(self, direction='right'):
        row_starts = [(row_num, 0) for row_num in range(len(self.grid))[::-1]]
        col_starts = [(0, col_num) for col_num in range(len(self.grid[0]))
                      if col_num > 0]

        start_coords = row_starts + col_starts

        diagonals = [self._get_diagonal(coord[0], coord[1], direction)
                     for coord in start_coords]

        return diagonals