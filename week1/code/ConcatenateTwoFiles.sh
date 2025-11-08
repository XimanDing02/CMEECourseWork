#!/bin/bash
# Author: Ximan Ding
# Script: ConcatenateTwoFiles.sh
# Desc: Concatenate two files into a third file
# Usage: bash ConcatenateTwoFiles.sh <file1> <file2> <output_file>
# Date: Nov 2025

# Check number of arguments
if [ $# -ne 3 ]; then
    echo "Usage: bash $0 <file1> <file2> <output_file>"
    exit 1
fi

# Check that both input files exist
if [ ! -f "$1" ]; then
    echo "Error: Input file '$1' not found!"
    exit 1
fi

if [ ! -f "$2" ]; then
    echo "Error: Input file '$2' not found!"
    exit 1
fi

# Avoid overwriting existing file accidentally
if [ -e "$3" ]; then
    echo "Warning: Output file '$3' already exists. Overwriting..."
fi

# Merge the files
cat "$1" > "$3"
cat "$2" >> "$3"

echo "Merged File is:"
cat "$3"

exit 0