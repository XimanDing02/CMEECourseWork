#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: basic_io3.py
Des: Store and load Python objects using the pickle module
Usage: python3 basic_io3.py (in terminal)
Date: Nov, 2025
"""

# docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

#############################
# STORING OBJECTS
#############################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle

f = open('../sandbox/testp.p','wb') # note the b: accept binary files
pickle.dump(my_dictionary, f)
# Close the file after writing
f.close()

## Load the data again
f = open('../sandbox/testp.p','rb')
# Load (deserialize) the dictionary from the file
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary) ## Print the loaded object to verify it was read correctly
