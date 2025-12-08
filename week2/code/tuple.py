#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: tuple.py
Des: Print information about bird species stored in a tuple of tuples.
Usage: python3 tuple.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

# Birds is a tuple of tuples of length three:
# (Latin name, common name, mean body mass)
birds = (
    ('Passerculus sandwichensis', 'Savannah sparrow', 18.7),
    ('Delichon urbica', 'House martin', 19),
    ('Junco phaeonotus', 'Yellow-eyed junco', 19.5),
    ('Junco hyemalis', 'Dark-eyed junco', 19.6),
    ('Tachycineata bicolor', 'Tree swallow', 20.2),
)

## Functions ##
def print_bird_info(bird_data):
    """Print each bird's information (Latin name, common name, and mass)."""
    for latin_name, common_name, mass in bird_data:
        print(f"Latin name: {latin_name}\n"
              f"Common name: {common_name}\n"
              f"Mass: {mass}\n")


## Main ##
def main(argv):
    """Main entry point of the program."""
    print("Bird Information:\n")
    print_bird_info(birds)
    return 0


if __name__ == "__main__":
    import sys
    status = main(sys.argv)
    sys.exit(status)