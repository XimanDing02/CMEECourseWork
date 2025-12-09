#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: profileme.py
Des: Simple functions used to practise profiling and performance analysis
     in Python by timing slow list-building and string-joining operations.
Usage: python3 profileme.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'


# imports
import sys


# functions

def my_squares(iters: int):
    """
    Build and return a list of squares from 0^2 up to (iters-1)^2.
    """
    out = []  # Empty list to store results
    for i in range(iters):
        out.append(i ** 2)
    return out


def my_join(iters: int, string: str):
    """
    Build and return a long string by repeatedly joining ', ' with `string`.
    """
    out = ''  # Start from empty string
    for i in range(iters):
        # Join ', ' with 'string' and append to the output in each iteration
        out += string.join(", ")
    return out


def run_my_funcs(x: int, y: str) -> int:
    """
    Run the two example functions with given arguments.
    """
    print(x, y)        # Print arguments so we know what is being run
    my_squares(x)      # Call the list-building function
    my_join(x, y)      # Call the string-joining function
    return 0


def main(argv):
    """
    Main entry point of the script.
    """
    # Default test values (same as in the teaching notes)
    x = 10000000
    y = "My string"

    return run_my_funcs(x, y)


if __name__ == "__main__":
    """
    Ensures main() runs only when the script is executed directly,
    and not when it is imported as a module.
    """
    status = main(sys.argv)
    sys.exit(status)