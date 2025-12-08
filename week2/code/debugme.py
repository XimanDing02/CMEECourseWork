#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: debugme.py
Des: Example script for debugging and demonstrating a ZeroDivisionError
Usage: python3 debugme.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

def buggyfunc(x):
    """
    Demonstrates try/except/else blocks with specific error handling.
    """
    y = x
    # Decrease y by 1 for x iterations
    for i in range(x):
        try: 
            y = y - 1
            z = x / y
        except ZeroDivisionError:
            print(f"The result of dividing a number by zero is undefined")
        except:
            print(f"This didn't work; x = {x}; y = {y}")
        else:
            print(f"OK; x = {x}; y = {y}, z = {z};")
    return z

buggyfunc(20)