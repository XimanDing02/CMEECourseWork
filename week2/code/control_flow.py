#!/usr/bin/env python3
"""Some functions exemplifying the use of control statements"""

__appname__ = 'control_flow'
__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import sys

## functions ##

def even_or_odd(x):
    """Decides whether a number x is even or odd."""
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

def largest_divisor_five(x):
    """Finds the largest divisor of x among 2, 3, 4, 5."""
    largest = 0
    for i in range(2, 6):
        if x % i == 0:
            largest = i
    if largest > 0:
        return f"The largest divisor of {x} is {largest}"
    else:
        return f"No divisor found for {x} between 2 and 5!"

def main(argv):
    """Main entry point of the program"""
    print("Testing control flow functions...")
    print(even_or_odd(22))
    print(largest_divisor_five(120))
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)