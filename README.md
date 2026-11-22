# MuseKit

**The starter kit for Muse power users.**

MuseKit is an unofficial community project. It is not made by Meta and it is not official documentation. It collects what a Muse user needs to start working with skills: a small importer, three starter skills, and a short guide to writing your own.

## What Muse is

Muse is Meta's personal AI agent. It lives in the messaging apps and surfaces you already use, remembers what matters to you, and can do real work on your behalf, from reading mail and calendars to running scheduled checks in the background. One of the ways it gets better at a kind of task is a skill: a folder of plain instructions that teaches it a method once, so every later conversation can follow it.

## Why this kit

Skills are the part of Muse most users never touch, because the format is not obvious from the outside. A Muse skill is not a single file with frontmatter, the way Claude skills are written. It is a folder holding an instructions file and a small metadata file beside it. MuseKit exists to make that format easy to adopt: convert the skills you already have, start from three that are written natively for Muse, and learn the rules well enough to write your own.

## What is inside

- `importer/`: one Python file that converts a Claude style skill into a Muse ready skill folder.
- `starter-skills/`: three original skills written for Muse, ready to copy into your workspace.
- `docs/writing-skills.md`: a short guide to the file layout, the metadata fields, and the rules that make a skill work.
- `tests/`: a small test suite for the importer, runnable with plain Python.

## Quick start

### Import a skill you already have

```bash
python3 importer/musekit_import.py path/to/your-skill --output-dir ~/workspace/custom-skills
```

Pass a folder holding a `SKILL.md`, or the path to a `SKILL.md` itself. The importer writes a converted folder into the output directory and prints everything it changed. Your own Muse skills live in the `custom-skills` folder of your Muse workspace, one folder per skill, so point the output there.

### Install the starter skills

Copy any of the folders under `starter-skills/` into the `custom-skills` folder of your Muse workspace. Each folder is complete as it stands, with its `SKILL.md` and its `skill.yaml` beside it.

### Write your own

Copy a starter skill, rename the folder, and edit both files. The folder name and the name in `skill.yaml` must match. Read `docs/writing-skills.md` first; it is short and it covers the mistakes that make a skill fail quietly.

## Starter skills

| Skill | What it does |
| --- | --- |
| `morning_brief` | Prepares a short morning briefing from your calendar, unread mail and scheduled tasks, shaped by your proactive preferences file. |
| `memory_keeper` | Captures durable facts, preferences and decisions into your memory files, with dates and sources, and reconciles corrections. |
| `watch_and_report` | Sets up a scheduled check on a topic you name, with clear rules for when to interrupt you and when to stay silent. |

## The importer

Claude skills carry their name and description in YAML frontmatter at the top of `SKILL.md`. Muse skills carry no frontmatter at all: the instructions live in `SKILL.md`, and the name, title, description, category and prompt setting live in `skill.yaml`. The importer bridges the two. It validates the skill name, converts it to the underscore form Muse uses, moves the metadata into `skill.yaml`, copies any extra files the skill ships with, and refuses to overwrite an existing skill unless you pass `--force`. It is a single file with zero dependencies, and it runs on Python 3.10 or newer.

```bash
python3 importer/musekit_import.py --help
```

## Contributing

Corrections and small, well tested improvements are welcome. Keep prose in plain English, keep the importer dependency free, and run the tests before opening a pull request:

```bash
python3 -m unittest discover -s tests
```

New starter skills should be original, safe to run, and useful to a stranger without any knowledge of your setup.

## License

MIT. See [LICENSE](LICENSE).
