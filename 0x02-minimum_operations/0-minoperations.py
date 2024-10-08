#!/usr/bin/python3
"""0-minoperations.py"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed
    to achieve n H characters.

    Args:
        n (int): The number of H characters desired.

    Returns:
        int: The minimum number of operations required,
        or 0 if n is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
