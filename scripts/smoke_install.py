#!/usr/bin/env python3
"""Install smoke tests. Each target installs the repo into a fresh temp dir the
way its README quick start says, then checks the agent would find everything.

Usage: smoke_install.py {cursor,claude,codex,all}
"""
import json, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
RULES = sorted(p.stem for p in (ROOT / "rules").glob("*.md") if p.name != "README.md")
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


class Fail(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise Fail(msg)


def check_skills(dest):
    for s in SKILLS:
        f = dest / s / "SKILL.md"
        need(f.is_file(), f"skill not installed: {f}")
        m = FM.match(f.read_text())
        need(m and re.search(rf"^name:\s*{re.escape(s)}\s*$", m.group(1), re.M),
             f"{s}: frontmatter name missing or != folder")


def cursor(tmp):
    proj = tmp / "proj"
    proj.mkdir()
    # Fresh render into the temp project, as a user running the script would.
    subprocess.run([sys.executable, ROOT / "scripts/render_rules.py", "--out", proj],
                   check=True, stdout=subprocess.DEVNULL)
    shutil.copytree(ROOT / "skills", proj / ".cursor/skills")
    mdc = sorted(p.stem for p in (proj / ".cursor/rules").glob("*.mdc"))
    need(mdc == RULES, f"rules rendered {mdc} != rules/ {RULES}")
    for r in RULES:
        m = FM.match((proj / f".cursor/rules/{r}.mdc").read_text())
        need(m, f"{r}.mdc: no frontmatter")
        keys = dict(l.split(":", 1) for l in m.group(1).splitlines())
        need({"description", "globs", "alwaysApply"} <= keys.keys(), f"{r}.mdc: missing keys")
        need(keys["alwaysApply"].strip() in ("true", "false"), f"{r}.mdc: bad alwaysApply")
        need(keys["alwaysApply"].strip() == "true" or keys["globs"].strip(),
             f"{r}.mdc: neither alwaysApply nor globs, Cursor would never load it")
    check_skills(proj / ".cursor/skills")


def claude(tmp):
    mp = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    need(mp.get("name") and mp.get("owner", {}).get("name"), "marketplace: name/owner missing")
    listed = []
    for p in mp.get("plugins", []):
        need(p.get("name") and p.get("source"), "plugin: name/source missing")
        src = (ROOT / p["source"]).resolve()
        need(src.is_dir(), f"plugin source not found: {p['source']}")
        for s in p.get("skills", []):
            need((src / s / "SKILL.md").is_file(), f"marketplace skill path broken: {s}")
            listed.append(pathlib.PurePosixPath(s).name)
    need(sorted(listed) == SKILLS, f"marketplace lists {sorted(listed)} != skills/ {SKILLS}")
    # Personal install path: ~/.claude/skills under a temp HOME.
    home = tmp / "home"
    for s in listed:
        shutil.copytree(ROOT / "skills" / s, home / ".claude/skills" / s)
    check_skills(home / ".claude/skills")
    # Project install: CLAUDE.md imports must resolve.
    proj = tmp / "proj"
    subprocess.run([sys.executable, ROOT / "scripts/render_rules.py", "--out", proj],
                   check=True, stdout=subprocess.DEVNULL)
    shutil.copytree(ROOT / "rules", proj / "rules")
    imports = re.findall(r"^@(\S+)$", (proj / "CLAUDE.md").read_text(), re.M)
    need(sorted(pathlib.Path(i).stem for i in imports) == RULES, "CLAUDE.md does not import every rule")
    for i in imports:
        need((proj / i).is_file(), f"CLAUDE.md import does not resolve: {i}")


def codex(tmp):
    proj = tmp / "proj"
    proj.mkdir()
    agents = (ROOT / "AGENTS.md").read_bytes()
    need(len(agents) <= 32 * 1024, "AGENTS.md over Codex's 32 KiB project-doc limit")
    (proj / "AGENTS.md").write_bytes(agents)
    shutil.copytree(ROOT / "rules", proj / "rules")
    shutil.copytree(ROOT / "skills", proj / ".agents/skills")
    # Every repo path AGENTS.md points at must exist in the install.
    for ref in re.findall(r"`((?:rules|skills|workflows|guardrails|seats|scripts)/[^`<*]*)`", agents.decode()):
        need((ROOT / ref.rstrip("/")).exists(), f"AGENTS.md references missing path: {ref}")
    check_skills(proj / ".agents/skills")


TARGETS = {"cursor": cursor, "claude": claude, "codex": codex}


def main():
    want = sys.argv[1:] or ["all"]
    names = list(TARGETS) if want == ["all"] else want
    bad = 0
    for n in names:
        with tempfile.TemporaryDirectory(prefix=f"smoke-{n}-") as d:
            try:
                TARGETS[n](pathlib.Path(d))
                print(f"PASS {n}")
            except Fail as e:
                print(f"FAIL {n}: {e}")
                bad += 1
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
