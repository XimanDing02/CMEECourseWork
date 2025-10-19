#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import sys
import re
from typing import Iterable

def _levenshtein_dist(a: str, b: str) -> int:
    la, lb = len(a), len(b)
    dp = list(range(lb + 1))
    for i in range(1, la + 1):
        prev, dp[0] = dp[0], i
        for j in range(1, lb + 1):
            cur = dp[j]
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[j] = min(
                dp[j] + 1,        # deletion
                dp[j - 1] + 1,    # insertion
                prev + cost       # substitution
            )
            prev = cur
    return dp[lb]

def _first_alpha_token(name: str) -> str:
    
    # Keep only letters and separators as spaces, then split
    cleaned = re.sub(r"[^A-Za-z]+", " ", name).strip()
    return cleaned.split()[0] if cleaned else ""

def is_an_oak(name: str) -> bool:
    """
    Return True if the input belongs to genus Quercus (oak).
    Robust to common typos such as 'Quercuss' (one extra 's') and to
    case/whitespace/punctuation noise.

    The logic:
      - Take the first alphabetic token as the genus candidate.
      - Exact match 'quercus' => True
      - Otherwise, allow Levenshtein distance <= 1 to 'quercus'.

    >>> is_an_oak('Quercus robur')
    True
    >>> is_an_oak('quercus petraea')
    True
    >>> is_an_oak(' Quercuss  cerris ')
    True
    >>> is_an_oak('Fagus sylvatica')
    False
    >>> is_an_oak('Pinus')
    False
    >>> is_an_oak('Quercus')
    True
    >>> is_an_oak("Q. robur")  # not strictly the full genus, should be False here
    False
    >>> is_an_oak("Quercu")    # missing 's' => distance 1 -> True by our tolerant rule
    True
    """
    token = _first_alpha_token(name).lower()
    if not token:
        return False
    if token == "quercus":
        return True
    # allow one edit away (handles 'quercuss', 'quercu', 'quer cus' etc.)
    return _levenshtein_dist(token, "quercus") <= 1

def filter_oaks(rows: Iterable[Iterable[str]]) -> Iterable[tuple[str, str]]:
 
    for row in rows:
        if not row:
            continue
        genus = row[0].strip()
        if genus.lower() == "genus":
            # header row
            continue
        species = row[1].strip() if len(row) > 1 else ""
        if is_an_oak(genus):
            yield (genus, species)

def main(argv):
    in_path = "../data/TestOaksData.csv"
    out_path = "../data/JustOaksData.csv"  

    with open(in_path, "r", newline="", encoding="utf-8") as f, \
         open(out_path, "w", newline="", encoding="utf-8") as g:
        reader = csv.reader(f)
        writer = csv.writer(g)

        for row in reader:
            # Optional: print for debugging
            # print(row)
            # print("The genus is:", row[0] if row else "")
            for genus, species in filter_oaks([row]):
                # Found an oak
                # print("FOUND AN OAK!")
                writer.writerow([genus, species])

    return 0

if __name__ == "__main__":
    # To run doctests:  python3 -m doctest -v oaks_debugme.py
    sys.exit(main(sys.argv))