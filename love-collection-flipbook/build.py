#!/usr/bin/env python3
"""Scan pages/ and write pages.json for the flipbook.

Add or remove images in pages/ (sorted by filename: 01-..., 02-...).
Story text and product code per image go in captions.json (keyed by filename).
WhatsApp number goes in config.json.
Cloudflare Pages build command:  python3 build.py
"""
import json
from pathlib import Path

root = Path(__file__).parent
exts = {".jpg", ".jpeg", ".png", ".webp"}
files = sorted(p for p in (root / "pages").iterdir() if p.suffix.lower() in exts)

caps_path = root / "captions.json"
caps = json.loads(caps_path.read_text(encoding="utf-8")) if caps_path.exists() else {}

pages = []
for p in files:
    c = caps.get(p.name, {})
    pages.append({"src": f"pages/{p.name}", "en": c.get("en", ""), "zh": c.get("zh", ""), "product": c.get("product")})

cfg = json.loads((root / "config.json").read_text(encoding="utf-8"))
cfg["pages"] = pages
cfg["products"] = [p["product"] | {"page": i} for i, p in enumerate(pages) if p["product"]]
(root / "pages.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"pages.json written: {len(pages)} pages")
