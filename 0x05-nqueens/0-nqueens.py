#!/usr/bin/python3
"""
    Module that solves the N Queens problem
"""
import sys


def print_solution(solution):
    """ Prints the solution in the required format """
    print([[i, solution[i]] for i in range(len(solution))])


def is_safe(solution, row, col):
    """ Checks if placing a queen at (row, col) is safe """
    for i in range(row):
        if solution[i] == col or abs(solution[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, row, solution):
    """ Solves the N Queens problem using backtracking """
    if row == n:
        print_solution(solution)
    else:
        for col in range(n):
            if is_safe(solution, row, col):
                solution[row] = col
                solve_nqueens(n, row + 1, solution)
                solution[row] = -1  # backtrack


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution = [-1] * N
    solve_nqueens(N, 0, solution)


if __name__ == "__main__":
    main()
