#!/usr/bin/env python3
"""Structural checks: required skeleton paths and skill name == folder."""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = ["AGENTS.md", "README.md", "LICENSE", "rules/_global.md", "rules/software.md",
            "rules/data-dbt.md", "rules/docs.md", "workflows", "guardrails", "seats", "skills"]
errors = [f"missing: {p}" for p in REQUIRED if not (ROOT / p).exists()]
for skill in sorted((ROOT / "skills").glob("*/")):
    f = skill / "SKILL.md"
    if not f.exists():
        errors.append(f"{skill.name}: no SKILL.md"); continue
    m = re.match(r"---\n(.*?)\n---\n", f.read_text(), re.S)
    if not m:
        errors.append(f"{skill.name}: no frontmatter"); continue
    name = re.search(r"^name:\s*(\S+)", m.group(1), re.M)
    if not name or name.group(1) != skill.name:
        errors.append(f"{skill.name}: name != folder")
    if not re.search(r"^description:", m.group(1), re.M):
        errors.append(f"{skill.name}: no description")
for e in errors:
    print("ERROR", e)
print(f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
