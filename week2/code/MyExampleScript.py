#!/usr/bin/env python3
#MyExampleScript.py

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: MyExampleScript.py
Des: First script for python
Usage: python3 MyExampleScript.py (in terminal)
Date: Nov, 2025
"""
def foo(x):
    """Print x squared (side effect)."""
    x *= x  # same as x = x * x
    print(x)

foo(2)
