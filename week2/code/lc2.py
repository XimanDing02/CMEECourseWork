#!/usr/bin/env python3
"""
Script Name: rainfall_lc.py
Description: 
    This script demonstrates the use of list comprehensions and 
    traditional for-loops to process rainfall data for the UK in 1910. 
    It identifies:
        (1) Months with rainfall greater than 100 mm.
        (2) Months with rainfall less than 50 mm.
Author: Ximan Ding (x.ding25@imperial.ac.uk)
Version: 0.1
License: MIT
Date: Oct 2025
"""

# DATA: Average UK Rainfall (mm) for 1910 by month
# Source: http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (
    ('JAN', 111.4),
    ('FEB', 126.1),
    ('MAR', 49.9),
    ('APR', 95.3),
    ('MAY', 71.8),
    ('JUN', 70.2),
    ('JUL', 97.1),
    ('AUG', 140.2),
    ('SEP', 27.0),
    ('OCT', 89.4),
    ('NOV', 128.4),
    ('DEC', 142.2),
)

# (1) Using list comprehensions
rainfall_over_100 = [(month, mm) for (month, mm) in rainfall if mm > 100]
rainfall_under_50 = [month for (month, mm) in rainfall if mm < 50]

print("Step #1:")
print("Months and rainfall values when the amount of rain was greater than 100 mm:")
print(rainfall_over_100)
print("Months with rainfall less than 50 mm:")
print(rainfall_under_50)

# (2) Using traditional loops
rainfall_over_100_loop = []
rainfall_under_50_loop = []

for month, mm in rainfall:
    if mm > 100:
        rainfall_over_100_loop.append((month, mm))
    elif mm < 50:
        rainfall_under_50_loop.append(month)

print("\nStep #2:")
print("Months and rainfall values when the amount of rain was greater than 100 mm (loop version):")
print(rainfall_over_100_loop)
print("Months with rainfall less than 50 mm (loop version):")
print(rainfall_under_50_loop)