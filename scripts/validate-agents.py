#!/usr/bin/env python3
"""Validates the frontmatter of every agent in claude/agents/.

Checks that:
- each file starts with a valid --- ... --- block;
- it has `name` and `description`, and `name` matches the file name;
- `model`, if present, is opus, sonnet, haiku or inherit;
- every agent mentioned as "<name> agent" in any agent file exists.
"""
import pathlib
import re
import sys

AGENTS_DIR = pathlib.Path(__file__).resolve().parent.parent / "claude" / "agents"
MODELS = {"opus", "sonnet", "haiku", "inherit"}
MENTION = re.compile(r"\b([a-z]+(?:-[a-z]+)+) agent\b")


def read_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def main():
    errors = []
    agents = sorted(AGENTS_DIR.glob("*.md"))
    names = {a.stem for a in agents}
    if not agents:
        errors.append(f"No agents found in {AGENTS_DIR}")

    for path in agents:
        text = path.read_text(encoding="utf-8")
        fields = read_frontmatter(text)
        if fields is None:
            errors.append(f"{path.name}: missing frontmatter (--- ... ---)")
            continue
        for field in ("name", "description"):
            if not fields.get(field):
                errors.append(f"{path.name}: missing `{field}`")
        if fields.get("name") and fields["name"] != path.stem:
            errors.append(f"{path.name}: `name` is '{fields['name']}', expected '{path.stem}'")
        model = fields.get("model")
        if model and model not in MODELS:
            errors.append(f"{path.name}: `model: {model}` is not valid")
        for mentioned in sorted(set(MENTION.findall(text))):
            if mentioned not in names:
                errors.append(f"{path.name}: mentions the '{mentioned}' agent, which does not exist")

    if errors:
        print("Errors found:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"OK: {len(agents)} valid agents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
