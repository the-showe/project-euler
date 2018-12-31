"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from tools import run_euler


def collatz(n):
    """
    Generator for the Collatz sequence beginning with n.

    This isn't used here, but may be useful in a later problem.
    """

    a = n
    for i in range(n):
        yield a
        if a == 1:
            break
        elif a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1


def get_collatz_lengths_below(n):
    """
    Efficient function to generate all Collatz lengths below n.

    Args:
        n (int): The upper limit.

    Returns:
        list of tuple: [(starter, Collatz length)]

    """

    # Initiate map to save lengths of each starter
    length_map = {}

    for starter in range(1, n + 1):
        number_steps = 0
        term_value = starter

        while True:
            if term_value == 1:
                # Save the number of steps in the map
                length_map[starter] = number_steps
                break

            number_steps += 1

            # Look in the map to see if the term value has already
            # been sequenced to completion
            if term_value in length_map:
                # Stop the loop and add the current number of steps
                # to the previously found number of steps
                length_map[starter] = number_steps + length_map[term_value] - 1
                break

            # Otherwise continue the sequence as normal
            elif term_value % 2 == 0:
                term_value = term_value // 2
            else:
                term_value = 3 * term_value + 1

    return list(length_map.items())


@run_euler
def get_longest_collatz_sequence_starting_below(n):
    lengths = get_collatz_lengths_below(n)
    longest = sorted(lengths, key=lambda tup: tup[1], reverse=True)[0]

    return longest[0]


get_longest_collatz_sequence_starting_below(1000000)
