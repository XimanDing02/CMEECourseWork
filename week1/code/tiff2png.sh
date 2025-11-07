#!/bin/bash
# Author: Ximan Ding
# Script: tiff2png.sh
# Desc: Converts all .tif files in the current directory to .png
# Usage: bash tiff2png.sh
# Date: Nov 2025

# Check if there are any .tif files
shopt -s nullglob
tif_files=(*.tif)

if [ ${#tif_files[@]} -eq 0 ]; then
    echo "No .tif files found in the current directory."
    return 0 2>/dev/null || exit 0
fi

# Loop through and convert
for f in "${tif_files[@]}"; do
    echo "Converting $f"
    convert "$f" "${f%.tif}.png" 2>/dev/null || echo "Warning: failed to convert $f"
done

echo "Conversion complete."
# exit
return 0 2>/dev/null || exit 0