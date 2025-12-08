#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: basic_io2.py
Des: Basic file output example using Python file I/O
Usage: python3 basic_io2.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

#############################
# FILE OUTPUT
#############################
# Save the elements of a list to a file
# Create a range object containing numbers from 0 to 99
list_to_save = range(100)

# Open a file for writing (this will overwrite the file if it already exists)
f = open('../sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n') # Add a new line at the end

f.close()