#!/bin/bash
# Author: Ximan Ding
# Script: CountLines.sh
# Desc: Counts the number of lines in a file
# Usage: bash CountLines.sh <filename>
# Date: Nov 2025

# Check argument count
if [ $# -ne 1 ]; then
    echo "Usage: bash $0 <filename>"
    exit 1
fi

# Check file existence
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found!"
    exit 1
fi

# Count lines
NumLines=$(wc -l < "$1")
echo "The file '$1' has $NumLines lines."
echo

exit 0