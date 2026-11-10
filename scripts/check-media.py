#!/usr/bin/env python3
"""Checks PNG size, WAV format and glTF triangle count without opening them in a tool. Uses no tokens."""
import argparse
import json
import os
import struct
import sys
import wave

parser = argparse.ArgumentParser()
parser.add_argument("--max-texture", type=int, default=2048)
parser.add_argument("--max-tris", type=int, default=50000)
parser.add_argument("--rate", type=int, default=48000)
parser.add_argument("roots", nargs="*", default=["art", "audio", "assets", "Assets", "Content"])
args = parser.parse_args()
problems, checked = [], 0


def gltf_tris(data):
    total = 0
    accessors = data.get("accessors", [])
    for mesh in data.get("meshes", []):
        for part in mesh.get("primitives", []):
            if part.get("mode", 4) != 4:
                continue
            source = part.get("indices", part.get("attributes", {}).get("POSITION"))
            if source is not None:
                total += accessors[source]["count"] // 3
    return total


def check(path):
    kind = os.path.splitext(path)[1].lower()
    if kind == ".png":
        with open(path, "rb") as handle:
            head = handle.read(24)
        if head[:8] != b"\x89PNG\r\n\x1a\n":
            return "NOT_PNG"
        width, height = struct.unpack(">II", head[16:24])
        return f"TEXTURE_TOO_BIG {width}x{height}" if max(width, height) > args.max_texture else None
    if kind == ".wav":
        with wave.open(path, "rb") as sound:
            rate = sound.getframerate()
        return f"WRONG_RATE {rate}" if rate != args.rate else None
    if kind == ".gltf":
        with open(path, encoding="utf-8") as handle:
            tris = gltf_tris(json.load(handle))
    elif kind == ".glb":
        with open(path, "rb") as handle:
            handle.seek(12)
            length, _ = struct.unpack("<II", handle.read(8))
            tris = gltf_tris(json.loads(handle.read(length)))
    else:
        return "SKIP"
    return f"TOO_MANY_TRIS {tris}" if tris > args.max_tris else None


for root in args.roots:
    for folder, _, names in os.walk(root):
        for name in names:
            path = os.path.join(folder, name)
            try:
                result = check(path)
            except (OSError, ValueError, KeyError, IndexError, struct.error, wave.Error, EOFError) as error:
                result = f"UNREADABLE {error}"
            if result == "SKIP":
                continue
            checked += 1
            if result:
                problems.append(f"{result}: {path}")
print("\n".join(problems[:60]) if problems else "", end="\n" if problems else "")
print(f"SUMMARY: {checked} files checked, {len(problems)} problems")
sys.exit(1 if problems else 2 if checked == 0 else 0)
