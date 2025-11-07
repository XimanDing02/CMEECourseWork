#!/bin/sh
# Author: Ximan Ding
# Script: tabtocsv.sh
# Desc: Substitute tabs with commas in a file, saving as .csv
# Usage: bash tabtocsv.sh <tab_delimited_file>
# Date: Nov 2025

# check the parameters
if [ $# -ne 1 ]; then
    echo "Usage: bash $0 <tab_delimited_file>"
    return 0 2>/dev/null || exit 0
fi

in="$1"
if [ ! -f "$in" ]; then
    echo "Error: '$in' not found or not a regular file."
    return 0 2>/dev/null || exit 0
fi

out="${in%.*}.csv"
echo "Creating a comma-delimited version of $in ..."
tr -s "\t" "," < "$in" > "$out"
echo "Done: $out"