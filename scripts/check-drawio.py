#!/usr/bin/env python3
"""Checks that .drawio files are valid, uncompressed draw.io XML. Uses no tokens."""
import sys
import xml.etree.ElementTree as ET

failed = False
for path in sys.argv[1:]:
    try:
        root = ET.parse(path).getroot()
        pages = root.findall("diagram")
        cells = list(root.iter("mxCell"))
        ids = [c.get("id") for c in cells]
        problems = []
        if root.tag != "mxfile" or not pages:
            problems.append("not an mxfile with pages")
        if not cells:
            problems.append("no mxCell found (compressed?)")
        if len(pages) == 1 and len(ids) != len(set(ids)):
            problems.append("duplicate cell ids")
        known = set(ids)
        for c in cells:
            for end in ("source", "target"):
                if c.get(end) and c.get(end) not in known:
                    problems.append(f"edge {c.get('id')} has unknown {end}")
        if problems:
            failed = True
            print(f"FAIL {path}: {'; '.join(problems)}")
        else:
            edges = sum(1 for c in cells if c.get("edge") == "1")
            print(f"OK {path}: {len(pages)} page(s), {len(cells)} cells, {edges} edges")
    except (ET.ParseError, OSError) as error:
        failed = True
        print(f"FAIL {path}: {error}")
sys.exit(1 if failed else 0)
