#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: basic_io1.py
Des: Basic file input example using Python file I/O
Usage: python3 basic_io1.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

#############################
# FILE INPUT
#############################
# Open a file for reading (relative path)
with open('../sandbox/test.txt', 'r') as f:

# Implicit loop over file object:
# Python automatically iterates over each line in the file
    for line in f:
        print(line)

# FILE INPUT (skip blank lines)
# Re-open the same file for reading
with open('../sandbox/test.txt', 'r') as f:

# Loop through each line and skip empty lines
    for line in f:
    # Remove leading/trailing whitespace and check line length
        if len(line.strip()) > 0:
            print(line)
