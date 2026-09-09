#!/usr/bin/env python3
"""Portable package validation for CI; complements Codex's local validator."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


def validate(root: Path) -> list[str]:
    issues = []
    packages = sorted(path for path in (root / "skills").iterdir() if path.is_dir())
    if not packages:
        issues.append("No skill packages found")
    for package in packages:
        entry = package / "SKILL.md"
        if not entry.is_file():
            issues.append(f"{package.name}: missing SKILL.md")
            continue
        source = entry.read_text()
        match = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", source, re.S)
        try:
            data = yaml.safe_load(match[1]) if match else None
            if not isinstance(data, dict):
                raise ValueError("missing or invalid frontmatter")
            if data.get("name") != package.name or not re.fullmatch(r"[a-z0-9-]{1,64}", package.name):
                issues.append(f"{entry}: name must match the lowercase skill directory")
            if not isinstance(data.get("description"), str) or not data["description"].strip():
                issues.append(f"{entry}: missing description")
        except (ValueError, yaml.YAMLError) as error:
            issues.append(f"{entry}: {error}")

        metadata = package / "agents/openai.yaml"
        if metadata.exists():
            try:
                data = yaml.safe_load(metadata.read_text())
                interface = data["interface"]
                if not 25 <= len(interface["short_description"]) <= 64:
                    issues.append(f"{metadata}: short_description must be 25–64 characters")
                if f"${package.name}" not in interface["default_prompt"]:
                    issues.append(f"{metadata}: prompt must name the skill")
            except (KeyError, TypeError, yaml.YAMLError) as error:
                issues.append(f"{metadata}: invalid interface: {error}")

        referenced = set()
        for doc in package.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text()):
                target = target.strip("<>")
                url = urlsplit(target)
                if url.scheme or not url.path:
                    continue
                resolved = (doc.parent / unquote(url.path)).resolve()
                referenced.add(resolved)
                if not resolved.is_relative_to(package.resolve()):
                    issues.append(f"{doc}: local link leaves package: {target}")
                elif not resolved.exists():
                    issues.append(f"{doc}: missing link: {target}")
        for ref in (package / "references").glob("*.md"):
            if ref.resolve() not in referenced:
                issues.append(f"{ref}: reference is not linked")
        for script in package.rglob("*.py"):
            try:
                compile(script.read_text(), str(script), "exec")
            except SyntaxError as error:
                issues.append(f"{script}: {error}")
    return issues


if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(error, file=sys.stderr)
    print("Skill package validation failed" if errors else "Skill packages validated")
    sys.exit(bool(errors))
