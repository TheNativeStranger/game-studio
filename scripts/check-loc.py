#!/usr/bin/env python3
"""Checks a translation CSV (first column key, second the source language). Uses no tokens."""
import csv
import re
import sys

MAX_GROWTH = 1.4
SLOTS = re.compile(r"\{[^{}]*\}|%[sd]|\[[A-Za-z_]+\]")
if len(sys.argv) != 2:
    sys.exit("usage: check-loc.py <table.csv>")
with open(sys.argv[1], encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.reader(handle))
if len(rows) < 2 or len(rows[0]) < 3:
    print("NO_TRANSLATIONS: need key, source and at least one language column")
    sys.exit(2)
header, problems, seen = rows[0], 0, set()


def report(kind, key, language=""):
    global problems
    problems += 1
    if problems <= 60:
        print(f"{kind}: {key} {language}".strip())


for row in rows[1:]:
    key, source = row[0], row[1] if len(row) > 1 else ""
    if key in seen:
        report("DUPLICATE_KEY", key)
    seen.add(key)
    for index, language in enumerate(header[2:], start=2):
        target = row[index].strip() if len(row) > index else ""
        if not target:
            report("MISSING", key, language)
            continue
        if sorted(SLOTS.findall(source)) != sorted(SLOTS.findall(target)):
            report("BROKEN_SLOT", key, language)
        if len(source) >= 12 and len(target) > len(source) * MAX_GROWTH:
            report("TOO_LONG", key, language)
print(f"SUMMARY: {len(rows) - 1} keys, {len(header) - 2} languages, {problems} problems")
sys.exit(1 if problems else 0)
