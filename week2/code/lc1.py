#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: lc1.py
Des: Practice of list comprehensions and conventional loops using a tuple
     of bird species and their mean body masses.
Usage: python3 lc1.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

# Data: a tuple containing bird species information
# (Latin name, common name, mean body mass)
birds = (
    ('Passerculus sandwichensis', 'Savannah sparrow', 18.7),
    ('Delichon urbica', 'House martin', 19),
    ('Junco phaeonotus', 'Yellow-eyed junco', 19.5),
    ('Junco hyemalis', 'Dark-eyed junco', 19.6),
    ('Tachycineata bicolor', 'Tree swallow', 20.2),
)

# (1) List comprehensions
# Extract each component of the tuple into its own list
latin_names = [bird[0] for bird in birds] # Extract all Latin names using a list comprehension
common_names = [bird[1] for bird in birds] # Extract all common names using a list comprehension
mean_body_masses = [bird[2] for bird in birds] # Extract all mean body masses using a list comprehension

print("Step #1: Using list comprehensions")
print("Latin names:")
print(latin_names)
print("Common names:")
print(common_names)
print("Mean body masses:")
print(mean_body_masses)

# (2) Conventional for-loops
# Create empty lists and fill them using iteration
latin_names_loop = []
common_names_loop = []
mean_body_masses_loop = []

# Loop through each bird record and extract values manually
for bird in birds:
    latin_names_loop.append(bird[0])
    common_names_loop.append(bird[1])
    mean_body_masses_loop.append(bird[2])

print("\nStep #2: Using traditional for-loops")
print("Latin names:")
print(latin_names_loop)
print("Common names:")
print(common_names_loop)
print("Mean body masses:")
print(mean_body_masses_loop)