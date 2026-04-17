#!/usr/bin/env python3
"""Enterprise Validator for the plantuml-skill repository (v1.0.0)"""

import argparse
import json
import re
import sys
from pathlib import Path

class Reporter:
    def __init__(self):
        self.failures = 0
        self.warnings = 0

    def ok(self, msg): print(f"PASS | {msg}")
    def warn(self, msg): self.warnings += 1; print(f"WARN | {msg}")
    def fail(self, msg): self.failures += 1; print(f"FAIL | {msg}")

def validate_structure(root: Path, reporter: Reporter):
    required_paths = [
        "SKILL.md",
        "README.md",
        "CHANGELOG.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "scripts/render.py",
        "scripts/evaluate_skill.py",
        "docs/syntax-guide.md",
        "docs/troubleshooting.md",
        "assets/premium-theme.puml",
        "evals/evals.json"
    ]
    for p in required_paths:
        if (root / p).exists():
            reporter.ok(f"Found {p}")
        else:
            reporter.fail(f"Missing mandatory file: {p}")

def validate_skill_md(root: Path, reporter: Reporter):
    path = root / "SKILL.md"
    if not path.exists(): return
    
    content = path.read_text(encoding="utf-8")
    
    # Check for version 2.x.x (allow optional quotes)
    version_match = re.search(r'version:\s*["\']?(2\.\d+\.\d+)["\']?', content)
    if version_match:
        reporter.ok(f"SKILL.md is v2.x compliant (found {version_match.group(1)})")
    else:
        reporter.fail("SKILL.md is missing a valid v2.x version string")

    required_headers = ["## Mission", "## 🧠 Cognitive Process", "## 📋 Input Contract", "## 🛡 Safeguards"]
    for h in required_headers:
        if h in content:
            # We use .encode().decode() trick or just avoid printing the emoji if needed, 
            # but better to just handle the reporter output or skip printing the exact header if it contains emojis
            reporter.ok(f"SKILL.md includes mandatory header: {h.split(' ')[0]} {h.split(' ')[-1]}")
        else:
            reporter.fail(f"SKILL.md missing critical header: {h}")

def main():
    # Force UTF-8 for stdout if possible
    if sys.stdout.encoding != 'utf-8':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    reporter = Reporter()

    print(f"--- Validating {root.name} ---")
    validate_structure(root, reporter)
    validate_skill_md(root, reporter)
    
    print(f"\nSummary: {reporter.failures} Failures, {reporter.warnings} Warnings")
    sys.exit(1 if reporter.failures else 0)

if __name__ == "__main__":
    main()
