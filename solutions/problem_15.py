"""
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

from tools import run_euler
from math import factorial


def get_num_combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


@run_euler
def get_num_routes_across_grid(side_length):
    """
    Simple combinations problem. Any route has to contain side_length right
        steps plus side_length down steps. The 'r' paramter in the combination
        equation is simply the side length of the grid.

    Args:
        side_length (int)

    Returns:
        int: Number of possible routes across the grid from one corner
            to the opposite.
    """

    num_steps = side_length * 2

    return get_num_combinations(num_steps, side_length)


get_num_routes_across_grid(20)
