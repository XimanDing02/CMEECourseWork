
#!/bin/bash
# Author: Ximan Ding
# Script: CountLines.sh
# Desc: Counts the number of lines in a file
# Usage: bash CountLines.sh <filename>
# Date: Nov 2025

if [ $# -ne 1 ]; then
    echo "Usage: bash $0 <filename>" 
    return 0 2>/dev/null || exit 0
fi

if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found!"
    return 0 2>/dev/null || exit 0
fi

NumLines=$(wc -l < "$1")
echo "The file '$1' has $NumLines lines"
echo

return 0 2>/dev/null || exit 0