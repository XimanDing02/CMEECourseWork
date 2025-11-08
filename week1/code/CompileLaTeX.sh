#!/bin/bash
# Author: Ximan Ding <x.ding25@imperial.ac.uk>
# Script: CompileLaTeX.sh
# Description: Compile a LaTeX file (and run bibtex if needed) to make a PDF.
# Usage: bash CompileLaTeX.sh <filename or filename.tex>
# Date: Oct 2025

set -euo pipefail  # stop if something goes wrong or a variable is undefined

# check if a filename was given
if [ $# -ne 1 ]; then
    echo "Usage: bash $0 <filename or filename.tex>"
    exit 1
fi

# remove the .tex extension if the user added it
file="${1%.tex}"

# make sure the main .tex file exists
if [ ! -f "$file.tex" ]; then
    echo "Error: $file.tex not found."
    exit 2
fi

echo "Compiling LaTeX document: $file.tex"

# first compile
if ! pdflatex -interaction=nonstopmode "$file.tex" >/dev/null 2>&1; then
    echo "Error: pdflatex failed."
    exit 3
fi

# run bibtex if there’s a .bib file
if [ -f "$file.bib" ]; then
    echo "Running bibtex..."
    if ! bibtex "$file" >/dev/null 2>&1; then
        echo "Warning: bibtex failed or maybe there are no citations."
    fi
fi

# compile twice more to update references
pdflatex -interaction=nonstopmode "$file.tex" >/dev/null 2>&1
pdflatex -interaction=nonstopmode "$file.tex" >/dev/null 2>&1

# clean up temporary files
for ext in aux log bbl blg; do
    [ -f "$file.$ext" ] && rm "$file.$ext"
done

echo "Done! PDF has been generated: $file.pdf"