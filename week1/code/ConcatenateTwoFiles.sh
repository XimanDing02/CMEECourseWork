#!/bin/bash
# Author: Ximan Ding
# Script: ConcatenateTwoFiles.sh
# Desc: Concatenate two files into a third file
# Usage: bash ConcatenateTwoFiles.sh <file1> <file2> <output_file>
# Date: Nov 2025

# Check number of arguments
if [ $# -ne 3 ]; then
    echo "Usage: bash $0 <file1> <file2> <output_file>"
    return 0 2>/dev/null || exit 0
fi

# Check that both input files exist
if [ ! -f "$1" ]; then
    echo "Error: Input file '$1' not found!"
    return 0 2>/dev/null || exit 0
fi

if [ ! -f "$2" ]; then
    echo "Error: Input file '$2' not found!"
    return 0 2>/dev/null || exit 0
fi

# Avoid overwriting existing file accidentally
if [ -e "$3" ]; then
    echo "Warning: Output file '$3' already exists. Overwriting..."
fi

# Merge the files
cat "$1" > "$3"
cat "$2" >> "$3"
echo "Merged File is"
cat "$3"

# exit
return 0 2>/dev/null || exit 0