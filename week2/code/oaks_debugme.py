#!/usr/bin/env python3
"""
Filter oaks from a species list.

Reads:  data/TestOaksData.csv  （来自 TheMulQuaBio 仓库）
Writes: results/JustOaksData.csv

A species is considered an oak if its binomial starts with 'Quercus'
(case-insensitive, tolerant to a common typo 'Quercuss').

Run:
    python oaks_debugme.py
or:
    python -m doctest -v oaks_debugme.py  # run doctests
"""

__author__  = "Your Name (you@uni)"
__version__ = "0.1.0"

from pathlib import Path
import csv
import re


# ---------- Core predicate with doctests ----------

def is_an_oak(name: str) -> bool:
    """
    Return True if the species (binomial or full name) is an oak.

    Normal behaviour:
    >>> is_an_oak('Quercus robur')
    True
    >>> is_an_oak('Fagus sylvatica')
    False
    >>> is_an_oak('quercus petraea')
    True
    >>> is_an_oak('  QuErCuS  cerris ')
    True

    Tolerate a common typo: 'Quercuss' (double s)
    >>> is_an_oak('Quercuss petraea')
    True

    Edge cases:
    >>> is_an_oak('Quercus')    # genus only
    True
    >>> is_an_oak('Quercuss')   # genus only with typo
    True
    >>> is_an_oak('Querc')      # truncated; not acceptable
    False
    >>> is_an_oak('')           # empty
    False
    >>> is_an_oak(None)         # non-string
    False
    """
    if not isinstance(name, str):
        return False
    s = name.strip().lower()
    # 容错：接受 quercus 或 quercuss 开头，后面要么空白/结束，要么接种加词
    # ^\s* 已在 strip 后无意义；要求以 quercus 或 quercuss 开头，并在词边界结束
    # 例：quercus、quercus robur、quercuss petraea 均 True
    return bool(re.match(r'^quercus+s?\b', s))


# ---------- I/O and processing ----------

def read_species_strings(path: Path) -> list[str]:
    """Read species names from CSV. Accepts columns like 'Species', or 'Genus'+'species'. """
    records = []
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # 调试断点（需要时启用）
        # import ipdb; ipdb.set_trace()
        for row in reader:
            # 常见原始数据列名：'Species' 或 'Genus','species'
            if 'Species' in row and row['Species']:
                records.append(row['Species'])
            elif 'Genus' in row and 'species' in row and (row['Genus'] or row['species']):
                genus = (row['Genus'] or '').strip()
                sp    = (row['species'] or '').strip()
                if genus or sp:
                    records.append((genus + ' ' + sp).strip())
            else:
                # 兜底：拼接所有非空字段
                parts = [str(v).strip() for v in row.values() if str(v).strip()]
                if parts:
                    records.append(" ".join(parts))
    return records


def write_oaks(path_out: Path, oaks: list[str]) -> None:
    path_out.parent.mkdir(parents=True, exist_ok=True)
    with path_out.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Species'])
        for s in oaks:
            w.writerow([s])


def main():
    repo_root = Path(__file__).resolve().parent.parent  # 典型课程结构：weekN/code/ 脚本在两层内
    # 如果你的脚本已经在 TheMulQuaBio 的 code/ 目录下，这里也能工作：
    # repo_root = Path(__file__).resolve().parents[1]
    data_in   = repo_root / 'data' / 'TestOaksData.csv'
    out_path  = repo_root / 'results' / 'JustOaksData.csv'

    if not data_in.exists():
        # 兼容在仓库根目录直接运行
        data_in = Path('data/TestOaksData.csv')
        out_path = Path('results/JustOaksData.csv')

    species = read_species_strings(data_in)
    oaks = [s for s in species if is_an_oak(s)]

    write_oaks(out_path, oaks)

    print(f"[OK] Found {len(oaks)} oaks. Written to {out_path}")
    # 打印前几条以便人工目检
    for s in oaks[:5]:
        print("  -", s)


if __name__ == '__main__':
    main()
