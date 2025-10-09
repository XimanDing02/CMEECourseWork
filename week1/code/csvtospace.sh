#!/bin/sh
# Author:  Ximan Ding<x.ding25@imperial.ac.uk>
# Script: csvtospace.sh
# Desc: Convert a comma-separated file to a space-separated file.
#       Does NOT modify the input; writes alongside it as <basename>.space
# Usage: bash csvtospace.sh <csv_file>
# Date: Oct 2025

set -u

usage() { echo "Usage: bash $0 <csv_file>"; exit 1; }

[ $# -eq 1 ] || usage

in="$1"
[ -f "$in" ] || { echo "Error: '$in' not found or not a regular file."; exit 2; }

dir=$(dirname "$in")
base=$(basename "$in")
name="${base%.*}"
out="$dir/$name.space"

if [ -e "$out" ]; then
  echo "Error: output '$out' already exists. Refusing to overwrite."
  exit 3
fi

echo "Converting commas to spaces: $in -> $out"
tr ',' ' ' < "$in" | tr -s ' ' > "$out" || { echo "Conversion failed."; exit 4; }

echo "Done: $out"
