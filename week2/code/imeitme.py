#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: timeitme.py
Des: Compare the performance of loop-based vs. list-comprehension-based
     implementations, and different string-joining approaches, using timeit.
Usage: python3 timeitme.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are stripped). 
# Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'


# imports
import sys
import timeit

# Import the functions to be tested
from profileme import my_squares as my_squares_loops
from profileme2 import my_squares as my_squares_lc

from profileme import my_join as my_join_join
from profileme2 import my_join as my_join_concat

# SETTINGS

# Number of iterations for the test
iters = 1_000_000

# Test string for joining
mystring = "my string"

# TIMING TESTS

def main(argv):
    """
    Main entry point of the program.

    Uses the timeit module to compare:
    1. Loop-based vs. list-comprehension-based square computation.
    2. String join method vs. string concatenation in a loop.
    """
    print("Running timeit performance comparisons...\n")

    # Time loop-based square computation
    t1 = timeit.timeit(
        stmt="my_squares_loops(iters)",
        globals=globals(),
        number=5
    )

    # Time list-comprehension-based square computation
    t2 = timeit.timeit(
        stmt="my_squares_lc(iters)",
        globals=globals(),
        number=5
    )

    print("Squares computation:")
    print("Loop version time:", t1)
    print("List comprehension version time:", t2, "\n")

    # Time string join version
    t3 = timeit.timeit(
        stmt="my_join_join(iters, mystring)",
        globals=globals(),
        number=5
    )

    # Time string concatenation version
    t4 = timeit.timeit(
        stmt="my_join_concat(iters, mystring)",
        globals=globals(),
        number=5
    )

    print("String joining:")
    print("join() method time:", t3)
    print("concatenation version time:", t4)

    return 0


if __name__ == "__main__":
    """
    Ensures main() runs only when the script is executed directly.
    """
    status = main(sys.argv)
    sys.exit(status)