#!/usr/bin/env python3
"""Lists art and audio files missing from the asset ledger. Uses no tokens."""
import csv
import os
import sys

LEDGER = "docs/production/asset-ledger.csv"
ROOTS = ("art", "audio", "assets", "Assets", "Content")
TYPES = {".blend", ".fbx", ".glb", ".gltf", ".obj", ".png", ".jpg", ".jpeg", ".tga", ".psd", ".wav", ".mp3", ".ogg", ".flac"}
BAD_LICENSE = {"", "unknown", "belirsiz", "?"}

files = []
for root in ROOTS:
    for folder, _, names in os.walk(root):
        for name in names:
            if os.path.splitext(name)[1].lower() in TYPES:
                files.append(os.path.join(folder, name))

if not os.path.exists(LEDGER):
    print(f"NO_LEDGER: {LEDGER} not found, {len(files)} asset file(s) on disk")
    sys.exit(2 if not files else 1)

with open(LEDGER, encoding="utf-8", newline="") as handle:
    rows = {row["path"]: row for row in csv.DictReader(handle)}

missing = [f for f in files if f not in rows]
unlicensed = [p for p, r in rows.items() if (r.get("license") or "").strip().lower() in BAD_LICENSE]
gone = [p for p in rows if not os.path.exists(p)]
for label, items in (("NOT_IN_LEDGER", missing), ("NO_LICENSE", unlicensed), ("FILE_MISSING", gone)):
    for item in items[:40]:
        print(f"{label}: {item}")
print(f"SUMMARY: {len(files)} files, {len(rows)} ledger rows, {len(missing)} not in ledger, {len(unlicensed)} without licence, {len(gone)} missing")
sys.exit(1 if missing or unlicensed or gone else 0)
