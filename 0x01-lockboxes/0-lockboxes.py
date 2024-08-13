#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.

    Args:
    - boxes: is a list of lists
        - A key with the same number as a box opens that box
        - Each box can contain keys to other boxes

    Returns:
    - True if all boxes can be opened, else return False
    """

    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is already unlocked
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        key = keys.pop()
        if key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)
