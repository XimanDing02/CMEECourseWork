#!/usr/bin/env python3

"""Some functions exemplifying the use of control statements"""

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

import sys
import doctest  # Import the doctest module


def even_or_odd(x=0):
    """Find whether a number x is even or odd.
      
    >>> even_or_odd(10)
    '10 is Even!'
    
    >>> even_or_odd(5)
    '5 is Odd!'
        
    In case of negative numbers, the positive is taken:    
    >>> even_or_odd(-2)
    '-2 is Even!'
    """
    # Define function to be tested
    if x % 2 == 0:
        return f"{x} is Even!"
    return f"{x} is Odd!"


if __name__ == "__main__":
    # Run doctests
    doctest.testmod(verbose=True)

    # Optional: manual prints (not needed for doctest, just for demonstration)
    print(even_or_odd(22))
    print(even_or_odd(33))