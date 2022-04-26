"""Compute values in the Collatz sequence using an iterative approach."""

from typing import Iterator


def compute_collatz_chain(number: int) -> Iterator[int]:
    """Compute the numbers in the Collatz sequence for the starting number."""
    # yield the original input number
    yield number
    # continue to iterate until the number is equal to 1
    while number != 1:
        # Add in all of the remaining functionality for this function
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        yield number
    # Reference:
    # https://projecteuler.net/problem=14
