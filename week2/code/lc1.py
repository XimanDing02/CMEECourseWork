#!/usr/bin/env python3
"""
lc1.py
========
This script demonstrates the use of list comprehensions and conventional loops 
to extract specific elements from a tuple of bird data.

Each bird entry contains:
    (Latin name, Common name, Mean body mass)

Outputs:
    - Lists of Latin names
    - Lists of Common names
    - Lists of Mean body masses
"""

__appname__ = 'lc1'
__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "GNU General Public License"

# Data: a tuple containing bird species information
birds = (
    ('Passerculus sandwichensis', 'Savannah sparrow', 18.7),
    ('Delichon urbica', 'House martin', 19),
    ('Junco phaeonotus', 'Yellow-eyed junco', 19.5),
    ('Junco hyemalis', 'Dark-eyed junco', 19.6),
    ('Tachycineata bicolor', 'Tree swallow', 20.2),
)

# (1) List comprehensions
# Extract each component of the tuple into its own list
latin_names = [bird[0] for bird in birds]
common_names = [bird[1] for bird in birds]
mean_body_masses = [bird[2] for bird in birds]

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