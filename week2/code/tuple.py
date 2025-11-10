#!/usr/bin/env python3
"""
Description:
    This program prints information about a set of bird species.
    Each record includes the Latin name, common name, and average mass.
    The script demonstrates unpacking tuples and formatted printing.
"""

__appname__ = 'bird_info_printer'
__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '1.0.0'
__license__ = 'MIT'

## Constants ##
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