#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: basic_csv.py
Des: Basic CSV input and output examples using the csv module in Python
Usage: python3 basic_csv.py (in terminal)
Date: Nov, 2025
"""

# docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

import csv

# Read a file containing:
# 'Species','Infraorder','Family','Distribution','Body mass male (Kg)'
with open('../data/testcsv.csv','r') as f:

    csvread = csv.reader(f) # Create a CSV reader object
    temp = []
    # Iterate over each row in the CSV file
    for row in csvread:
        temp.append(tuple(row))
        print(row)
        print("The species is", row[0])

# Read the original CSV again and write a new CSV
# containing only the species name and body mass
with open('../data/testcsv.csv','r') as f:
    with open('../data/bodymass.csv','w') as g:

        csvread = csv.reader(f)
        csvwrite = csv.writer(g)
        for row in csvread:
            print(row)
            csvwrite.writerow([row[0], row[4]])
