#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: oaks_debugme.py
Des: Read a CSV file of tree taxa, detect oaks (genus Quercus),
     and write only oak records to an output CSV. Includes doctests
     for the oak-detection function.
Usage: python3 oaks_debugme.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

import csv
import sys
import doctest

def is_an_oak(name: str) -> bool:
    """
    Return True if the taxon name belongs to genus 'Quercus'.

    The function should correctly identify oaks and reject non-oaks,
    including simple typos like 'Quercuss'.

    Examples
    --------
    >>> is_an_oak('Quercus')
    True
    >>> is_an_oak('Quercus robur')
    True
    >>> is_an_oak('quercus petraea')
    True
    >>> is_an_oak('Quercus, robur')
    True
    >>> is_an_oak('Quercuss robur')   # typo, should NOT be treated as oak
    False
    >>> is_an_oak('Fagus sylvatica')
    False
    >>> is_an_oak('Fraxinus')
    False
    """
    # Clean whitespace and split off any commas or extra species names
    cleaned = name.strip()
    if not cleaned:
        return False

    # Take first part before comma, then first word (genus)
    first_field = cleaned.split(",")[0]
    genus = first_field.split()[0]

    # Check whether the genus is exactly 'quercus' (case-insensitive)
    return genus.lower() == "quercus"


def main(argv):
    """
    Main entry point of the program.

    Reads taxa from '../data/TestOaksData.csv' and writes only
    the oak records to '../data/JustOaksData.csv'.
    """
    in_path = '../data/TestOaksData.csv'
    out_path = '../data/JustOaksData.csv'

    # Open input and output CSV files safely using 'with'
    with open(in_path, 'r', newline='') as f, open(out_path, 'w', newline='') as g:
        taxa = csv.reader(f)
        csvwrite = csv.writer(g)

        oaks = set()

        for i, row in enumerate(taxa):
            # Skip completely empty rows
            if not row:
                continue

            genus = row[0].strip()

            # Skip header row if present (e.g. "Genus, species")
            if i == 0 and genus.lower() == "genus":
                continue

            print(row)
            print("The genus is:")
            print(genus + '\n')

            if is_an_oak(genus):
                print('FOUND AN OAK!\n')
                oaks.add(genus)
                # Write genus + species (if species column exists)
                if len(row) > 1:
                    csvwrite.writerow([row[0], row[1]])
                else:
                    csvwrite.writerow(row)

    print(f"Finished. Number of unique oak genera found: {len(oaks)}")
    print("Oaks found:", oaks)

    return 0


if __name__ == "__main__":
    # Run doctests first to ensure is_an_oak behaves as expected
    doctest.testmod(verbose=False)

    status = main(sys.argv)
    sys.exit(status)