#!/usr/bin/env python3
#!/usr/bin/env python3
from __future__ import annotations
"""
align_seqs.py

This program reads two DNA sequences from an input CSV file,
finds the best alignment (highest number of matching bases),
and writes the best alignment and score to a results text file.

Usage:
    python3 align_seqs.py
"""

__appname__ = "align_seqs"
__author__ = "Ximan Ding (x.ding25@imperial.ac.uk)"
__version__ = "1.0.0"
__license__ = "MIT"
from pathlib import Path
import csv
import re
import sys
from typing import Tuple, Optional

# Allowed DNA bases (A, C, G, T, case-insensitive)
_VALID_DNA = re.compile(r"^[ACGTacgt]+$")


def read_two_sequences(csv_path: Path) -> Tuple[str, str]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {csv_path}")

    raw = csv_path.read_text(encoding="utf-8", errors="ignore")
    raw = raw.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")

    tokens: list[str] = []

    # Try CSV parsing first
    from io import StringIO
    f = StringIO(raw)
    reader = csv.reader(f)
    for row in reader:
        for cell in row:
            cell = cell.strip().strip('"').strip("'")
            if cell:
                tokens.append(cell)

    # If nothing was found, split more loosely
    if not tokens:
        for line in raw.split("\n"):
            for cell in re.split(r"[,\t; ]+", line.strip()):
                if cell:
                    tokens.append(cell)

    def looks_like_dna(s: str) -> bool:
        return bool(re.fullmatch(r"[ACGTacgt]+", s))

    seqs = [t.upper() for t in tokens if looks_like_dna(t)]

    # Fallback: global regex extraction if still less than 2 sequences
    if len(seqs) < 2:
        seqs = re.findall(r"[ACGT]+", raw.upper())

    if len(seqs) < 2:
        raise ValueError("Could not find two valid DNA sequences in the input file.")

    return seqs[0], seqs[1]


def _looks_like_dna(s: str) -> bool:
    return bool(_VALID_DNA.match(s.replace(" ", "")))

def choose_long_short(a: str, b: str) -> Tuple[str, str]:
    # Return (longer, shorter)
    return (a, b) if len(a) >= len(b) else (b, a)


def calculate_score(s1: str, s2: str, start: int) -> Tuple[int, str]:
    l1, l2 = len(s1), len(s2)
    score = 0
    matched_marks = []

    # Uncomment for debugging:
    # import ipdb; ipdb.set_trace()

    for i in range(l2):
        j = i + start
        if j >= l1:
            break
        if s1[j] == s2[i]:
            score += 1
            matched_marks.append("*")
        else:
            matched_marks.append("-")

    return score, "".join(matched_marks)



def find_best_alignment(seq1: str, seq2: str) -> Tuple[str, str, int, int]:

    s1, s2 = choose_long_short(seq1, seq2)
    l1 = len(s1)

    best_score = -1
    best_align = ""
    best_start = 0

    for start in range(l1):
        score, _ = calculate_score(s1, s2, start)
        if score > best_score:
            best_score = score
            best_align = "." * start + s2
            best_start = start

    return best_align, s1, best_score, best_start


def write_report(out_path: Path, aligned_s2: str, s1: str, score: int, start: int) -> None:
    # Save the best alignment and score to a text file.
    out_path.parent.mkdir(parents=True, exist_ok=True)
    content = [
        "# Best overlap alignment\n",
        f"Start position: {start}\n",
        f"Score (matches): {score}\n",
        "\n",
        aligned_s2 + "\n",
        s1 + "\n",
        "\n",
        "# Legend: '.' = offset, '*' = match, '-' = mismatch (debug view)\n",
    ]
    out_path.write_text("".join(content), encoding="utf-8")



def main(in_file: Optional[str] = None, out_file: Optional[str] = None) -> int:
    here = Path(__file__).resolve().parent
    default_in = (here / "../data/align_seqs.csv").resolve()
    default_out = (here / "../results/best_alignment.txt").resolve()

    in_path = Path(in_file) if in_file else default_in
    out_path = Path(out_file) if out_file else default_out

    seq1, seq2 = read_two_sequences(in_path)
    aligned_s2, s1, best_score, best_start = find_best_alignment(seq1, seq2)
    write_report(out_path, aligned_s2, s1, best_score, best_start)

    # Print summary to terminal
    print(f"Input:  {in_path}")
    print(f"Output: {out_path}")
    print("Alignment:")
    print(aligned_s2)
    print(s1)
    print(f"Best score: {best_score} (start={best_start})")
    return 0


if __name__ == "__main__":

    args = sys.argv[1:]
    in_arg = args[0] if len(args) >= 1 else None
    out_arg = args[1] if len(args) >= 2 else None
    sys.exit(main(in_arg, out_arg))