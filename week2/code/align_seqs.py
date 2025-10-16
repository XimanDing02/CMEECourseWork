#align_seqs.py
#!/usr/bin/env python3

__author__  = "Ximan Ding (x.ding25@imperial.ac.uk)"
__version__ = "0.1.0"

import argparse
import csv
from pathlib import Path

def clean(seq: str) -> str:
    """Uppercase and keep only A/C/G/T (drop whitespace and other chars)."""
    seq = seq.upper()
    return "".join(ch for ch in seq if ch in {"A", "C", "G", "T"})

def calculate_score(longer: str, shorter: str, start: int) -> tuple[int, str]:
    """
    Score an alignment by sliding `shorter` so its index 0 sits at `start` on `longer`.
    Returns (score, match_line) where match_line has '*' for matches and '-' for mismatches.
    """
    score = 0
    marks = []
    for i, base in enumerate(shorter):
        j = start + i
        if j >= len(longer):
            break
        if base == longer[j]:
            score += 1
            marks.append("*")
        else:
            marks.append("-")
    return score, "".join(marks)

def best_alignment(seq1: str, seq2: str) -> dict:
    """
    Find the best alignment between seq1 and seq2.
    Always slides the shorter over the longer (0..len(longer)-1).
    Returns a dict with keys: start, score, longer, shorter, match_line, aligned_longer, aligned_shorter.
    """
    # Ensure we treat the longer one as the "reference"
    if len(seq1) >= len(seq2):
        longer, shorter = seq1, seq2
        swapped = False
    else:
        longer, shorter = seq2, seq1
        swapped = True

    best = {"start": 0, "score": -1, "match_line": ""}
    for start in range(len(longer)):  # positions where the shorter's 0th base could land
        score, marks = calculate_score(longer, shorter, start)
        if score > best["score"]:
            best.update({"start": start, "score": score, "match_line": marks})

    # Build pretty alignment strings with padding on the shorter and match line
    pad = " " * best["start"]
    aligned_shorter = pad + shorter
    aligned_longer = longer
    # match_line must be padded to align visually under the shorter’s first char
    match_line = pad + best["match_line"]

    result = {
        "start": best["start"],
        "score": best["score"],
        "longer": longer,
        "shorter": shorter,
        "aligned_longer": aligned_longer,
        "aligned_shorter": aligned_shorter,
        "match_line": match_line,
        "swapped": swapped,
    }
    return result


def read_two_seqs_from_csv(path: Path) -> tuple[str, str]:
    """
    Expect a CSV with header: seq1,seq2 (order can vary).
    The first non-empty row is used.
    """
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            s1 = clean(row.get("seq1", "")) if row.get("seq1") else ""
            s2 = clean(row.get("seq2", "")) if row.get("seq2") else ""
            if s1 and s2:
                return s1, s2
    raise ValueError("Input CSV must contain at least one row with both seq1 and seq2.")

def write_alignment_text(out_path: Path, info: dict) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        f.write("# Best alignment (slide shorter along longer)\n")
        f.write(f"# Start position on longer: {info['start']}\n")
        f.write(f"# Score (matches): {info['score']}\n")
        if info["swapped"]:
            f.write("# Note: input sequences were swapped internally so that 'longer' is the longer one.\n")
        f.write("\n")
        f.write(info["aligned_longer"] + "\n")
        f.write(info["match_line"] + "\n")
        f.write(info["aligned_shorter"] + "\n")
        f.write("\n")
        f.write(f"Longer length:  {len(info['longer'])}\n")
        f.write(f"Shorter length: {len(info['shorter'])}\n")

def parse_args():
    p = argparse.ArgumentParser(description="Align two DNA sequences from a single CSV and write best alignment.")
    p.add_argument("--input", "-i", default="data/align_seqs.csv",
                   help="CSV with columns seq1,seq2 (default: data/align_seqs.csv)")
    p.add_argument("--output", "-o", default="results/best_alignment.txt",
                   help="Text file to save best alignment (default: results/best_alignment.txt)")
    return p.parse_args()

def main():
    args = parse_args()
    in_path = Path(args.input)
    out_path = Path(args.output)

    s1, s2 = read_two_seqs_from_csv(in_path)
    info = best_alignment(s1, s2)
    write_alignment_text(out_path, info)

    # Console summary
    print(f"[OK] Best alignment written to {out_path}")
    print(f"Score: {info['score']}, start: {info['start']}")
    print(info["aligned_longer"])
    print(info["match_line"])
    print(info["aligned_shorter"])

if __name__ == "__main__":
    main()
