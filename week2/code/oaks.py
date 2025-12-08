#!/usr/bin/env python3
## Finds just those taxa that are oak trees from a list of species
"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: oaks.py
Des: Identify oak tree species from a list of taxa using loops and
     list comprehensions.
Usage: python3 oaks.py (in terminal)
Date: Nov, 2025
"""

# docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

# List of species
taxa = [ 'Quercus robur',
         'Fraxinus excelsior',
         'Pinus sylvestris',
         'Quercus cerris',
         'Quercus petraea',
       ]

def is_an_oak(name):
    """
    Check whether a given species name belongs to the oak genus (Quercus).
    """
    # Convert the name to lower case and check if it starts with 'quercus '
    return name.lower().startswith('quercus ')

# Find oak species using a for-loop
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species)

print("Oak species found using for-loops:")
print(oaks_loops)

# Using list comprehensions   
oaks_lc = set([species for species in taxa if is_an_oak(species)])
print("\nOak species found using list comprehension:")
print(oaks_lc)

# Convert oak species names to upper case using a for-loop
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species.upper())
print(oaks_loops)

# Convert oak species names to upper case using a list comprehension
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)])
print("\nOak species in upper case (using list comprehension):")
print(oaks_lc)