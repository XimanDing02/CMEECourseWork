#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: profileme2.py
Des: Optimised version of profiling example using list comprehension
     and faster string concatenation for performance comparison.
Usage: python3 profileme2.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

import sys

#functions 
def my_squares(iters: int):
    """
    Build and return a list of squares using a list comprehension
    (faster than repeated append in a loop).
    """
    return [i ** 2 for i in range(iters)]


def my_join(iters: int, string: str):
    """
    Build and return a long string by repeated concatenation.
    """
    out = ''
    for i in range(iters):
        out += ", " + string
    return out


def run_my_funcs(x: int, y: str) -> int:
    """
    Run the two example functions for profiling.
    """
    print(x, y)
    my_squares(x)
    my_join(x, y)
    return 0


def main(argv):
    """
    Main entry point of the script.
    """
    # Default test values (as in the teaching example)
    x = 10000000
    y = "My string"

    return run_my_funcs(x, y)


if __name__ == "__main__":
    """
    Ensures main() runs only when the script is executed directly.
    """
    status = main(sys.argv)
    sys.exit(status)