#!/usr/bin/env python3
"""Creates the next numbered task card and the asset ledger. Uses no tokens."""
import os
import re
import sys
import unicodedata

if len(sys.argv) < 2:
    sys.exit("usage: new-task.py <short name>")
TASKS = "docs/production/tasks"
LEDGER = "docs/production/asset-ledger.csv"
os.makedirs(TASKS, exist_ok=True)
name = " ".join(sys.argv[1:])
plain = name.replace("ı", "i").replace("İ", "i").lower()
plain = unicodedata.normalize("NFKD", plain).encode("ascii", "ignore").decode()
slug = re.sub(r"[^a-z0-9]+", "-", plain).strip("-") or "is"
numbers = [int(f[:3]) for f in os.listdir(TASKS) if f[:3].isdigit()]
path = f"{TASKS}/{max(numbers, default=0) + 1:03d}-{slug}.md"
sections = ["Hedef", "Kabul ölçütleri", "Bütçe", "Etkilenenler", "Görevler", "Sonuçlar"]
with open(path, "x", encoding="utf-8") as handle:
    handle.write(f"# {name}\n\nDurum: açık\n\n" + "\n".join(f"## {s}\n" for s in sections))
if not os.path.exists(LEDGER):
    with open(LEDGER, "w", encoding="utf-8") as handle:
        handle.write("path,source,tool,license,prompt_or_notes,approved_by\n")
print(path)
