#!/usr/bin/env python3
"""Convert a Claude style skill into a Muse ready skill folder.

A Claude style skill is a folder holding a SKILL.md that opens with YAML
frontmatter (name, description) followed by instructions. A Muse skill
keeps its instructions in a SKILL.md with no frontmatter, and keeps its
metadata in a skill.yaml beside it. This tool reads the first form and
writes the second.

Usage:
    python3 musekit_import.py path/to/skill
    python3 musekit_import.py path/to/skill/SKILL.md --output-dir ~/workspace/custom-skills

Zero dependencies. Python 3.10 or newer.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

KEBAB_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
KEPT_FIELDS = ("name", "description")


def parse_frontmatter(text):
    """Split a SKILL.md into (frontmatter dict, body). Returns (None, text)
    when the file does not open with a frontmatter block."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    end = None
    for index in range(1, len(lines)):
        if lines[index].strip() in ("---", "..."):
            end = index
            break
    if end is None:
        return None, text

    fields = {}
    current_key = None
    block_mode = None
    block_lines = []

    def flush_block():
        nonlocal block_lines, block_mode
        if current_key is not None and block_mode is not None:
            if block_mode == ">":
                fields[current_key] = " ".join(
                    line.strip() for line in block_lines
                ).strip()
            else:
                fields[current_key] = "\n".join(block_lines).strip()
        block_lines = []
        block_mode = None

    for raw in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if match and not raw.startswith((" ", "\t")):
            flush_block()
            current_key = match.group(1)
            value = match.group(2).strip()
            if value in ("|", "|-", "|+", ">", ">-", ">+"):
                block_mode = value[0]
                block_lines = []
            else:
                fields[current_key] = value
            continue
        if current_key is None:
            continue
        if block_mode is not None:
            block_lines.append(raw.strip())
        elif raw.strip():
            # A folded continuation of a plain scalar, or a nested block
            # such as metadata. Nested blocks are recorded as present and
            # dropped later, so only their first line matters here.
            existing = fields.get(current_key, "")
            fields[current_key] = (existing + " " + raw.strip()).strip()
    flush_block()

    body = "\n".join(lines[end + 1:]).lstrip("\n")
    return fields, body


def yaml_quote(value):
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return '"{}"'.format(escaped)


def find_title(body, fallback_name):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return " ".join(word.capitalize() for word in fallback_name.split("-"))


def collect_extra_files(source_dir, skill_md):
    extras = []
    for path in sorted(source_dir.rglob("*")):
        if not path.is_file():
            continue
        if path == skill_md:
            continue
        if any(part in (".git", "__pycache__") for part in path.parts):
            continue
        extras.append(path)
    return extras


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="musekit_import",
        description=(
            "Convert a Claude style skill (SKILL.md with YAML frontmatter) "
            "into a Muse ready skill folder (SKILL.md plus skill.yaml)."
        ),
    )
    parser.add_argument(
        "source",
        help="Folder holding a SKILL.md, or the path to a SKILL.md file.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="custom-skills",
        help="Folder the converted skill folder is written into. "
        "Default: ./custom-skills",
    )
    parser.add_argument(
        "--category",
        default="Work and knowledge",
        help="Category written into skill.yaml. Default: Work and knowledge",
    )
    parser.add_argument(
        "--include-in-prompt",
        action="store_true",
        help="List the skill in every conversation. By default an imported "
        "skill is left to skill search, which is the safer setting.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the target skill folder if it already exists.",
    )
    args = parser.parse_args(argv)

    source = Path(args.source).expanduser()
    if not source.exists():
        print("error: no such file or folder: {}".format(source), file=sys.stderr)
        return 2

    if source.is_dir():
        skill_md = source / "SKILL.md"
        source_dir = source
    else:
        skill_md = source
        source_dir = None
    if not skill_md.is_file():
        print("error: no SKILL.md found at {}".format(skill_md), file=sys.stderr)
        return 2

    text = skill_md.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    if fields is None:
        print(
            "error: {} does not start with a YAML frontmatter block, so it "
            "does not look like a Claude style skill.".format(skill_md),
            file=sys.stderr,
        )
        return 2

    name = (fields.get("name") or "").strip()
    description = (fields.get("description") or "").strip()
    if not name:
        print("error: the frontmatter has no name field.", file=sys.stderr)
        return 2
    if not KEBAB_NAME.match(name):
        print(
            "error: skill name {!r} is not kebab case. Use lowercase letters, "
            "digits and single hyphens, for example my-skill.".format(name),
            file=sys.stderr,
        )
        return 2
    if not description:
        print("error: the frontmatter has no description field.", file=sys.stderr)
        return 2
    if not body.strip():
        print("error: the SKILL.md has no instructions after the frontmatter.", file=sys.stderr)
        return 2

    muse_name = name.replace("-", "_")
    title = find_title(body, name)
    output_dir = Path(args.output_dir).expanduser()
    target = output_dir / muse_name
    if target.exists() and not args.force:
        print(
            "error: {} already exists. Pass --force to overwrite it.".format(target),
            file=sys.stderr,
        )
        return 2

    changes = []
    if muse_name != name:
        changes.append(
            "renamed the skill from {} to {} (Muse skill names use "
            "underscores)".format(name, muse_name)
        )
    dropped = [key for key in fields if key not in KEPT_FIELDS]
    if dropped:
        changes.append(
            "dropped frontmatter fields Muse does not use: {}".format(
                ", ".join(sorted(dropped))
            )
        )
    changes.append("moved name and description out of SKILL.md into skill.yaml")
    if not body.startswith("# "):
        body = "# {}\n\n{}".format(title, body)
        changes.append("added a title heading to SKILL.md")

    target.mkdir(parents=True, exist_ok=True)
    (target / "SKILL.md").write_text(body.rstrip("\n") + "\n", encoding="utf-8")

    skill_yaml = "\n".join(
        [
            "name: {}".format(muse_name),
            "title: {}".format(yaml_quote(title)),
            "description: {}".format(yaml_quote(description)),
            "category: {}".format(yaml_quote(args.category)),
            "include_in_prompt: {}".format(
                "true" if args.include_in_prompt else "false"
            ),
            "",
        ]
    )
    (target / "skill.yaml").write_text(skill_yaml, encoding="utf-8")
    changes.append("wrote skill.yaml with category {}".format(args.category))

    if source_dir is not None:
        extras = collect_extra_files(source_dir, skill_md)
        for extra in extras:
            relative = extra.relative_to(source_dir)
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(extra, destination)
        if extras:
            changes.append(
                "copied {} extra file{}: {}".format(
                    len(extras),
                    "s" if len(extras) != 1 else "",
                    ", ".join(str(path.relative_to(source_dir)) for path in extras),
                )
            )

    print("Imported {} into {}".format(name, target))
    for change in changes:
        print("  - {}".format(change))
    return 0


if __name__ == "__main__":
    sys.exit(main())
