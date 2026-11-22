![MuseKit](assets/masthead.png)

[![Release](https://img.shields.io/github/v/release/Dongdarealest/musekit)](https://github.com/Dongdarealest/musekit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-0064D1.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-0064D1.svg)
![Skills: 3 starter](https://img.shields.io/badge/Skills-3%20starter-0064D1.svg)

**Your Muse can do more than chat. MuseKit teaches it how.**

Muse is Meta's personal AI agent. It can learn new abilities, called skills: small folders of instructions you give it once, and it follows them in every chat after that. Almost nobody knows this exists, and there is no store to get skills from. MuseKit is the starting point: three ready-made skills you can install in a minute, a tool that converts skills you already have, and a short guide to writing your own.

## Start here: three skills, one minute, no tools

1. [Download the kit](https://github.com/Dongdarealest/musekit/releases/latest) and unzip it.
2. Open the `starter-skills` folder and pick a skill.
3. Copy that skill's folder into the `custom-skills` folder of your Muse workspace.
4. Start a new chat with your Muse. The skill is live.

## What you get

**A morning briefing that only speaks when something matters.** The `morning_brief` skill reads your calendar, unread mail and scheduled tasks, and gives you the short version. A sample:

```
Good morning. Two things need you today.
- Dentist at 09:30, then you are free until 14:00.
- One unread email from your landlord, about the contract.
Nothing else changed overnight.
```

**A memory that survives the chat.** The `memory_keeper` skill teaches your Muse to write down durable facts, preferences and decisions, with dates, and to replace an old fact when you correct it instead of letting both live on.

**A watcher that stays quiet until it should not.** The `watch_and_report` skill sets up a scheduled check on anything you name, a price, a page, a topic, with the cost agreed up front and clear rules: interrupt you only on a real change, stay silent otherwise.

## Already write Claude skills? Bring them with you

Claude skills and Muse skills look similar and are not the same file. The importer in this kit converts yours in one command:

```bash
python3 importer/musekit_import.py path/to/your-skill --output-dir ~/workspace/custom-skills
```

![A real run of the importer](assets/demo.png)

| | Claude | Muse |
| --- | --- | --- |
| Layout | One `SKILL.md` file | A folder with two files |
| Metadata | YAML frontmatter inside `SKILL.md` | A separate `skill.yaml` beside it |
| Name style | kebab-case, like `demo-skill` | snake_case, like `demo_skill` |
| Instructions | `SKILL.md` with frontmatter | `SKILL.md` with no frontmatter at all |

The importer validates the name, converts it to the underscore form, moves the metadata into `skill.yaml`, drops fields Muse does not use and tells you which ones, copies any extra files the skill ships with, and refuses to overwrite an existing skill unless you pass `--force`. One Python file, zero dependencies, Python 3.10 or newer.

## Write your own

Copy a starter skill, rename the folder, edit both files. The folder name and the name in `skill.yaml` must match. Read [docs/writing-skills.md](docs/writing-skills.md) first: it is short, and it covers the mistakes that make a skill fail quietly.

## What is inside

- `starter-skills/`: three original Muse native skills, ready to copy.
- `importer/`: the Claude to Muse converter, one Python file.
- `docs/writing-skills.md`: the format guide.
- `tests/`: the importer test suite, runnable with plain Python.

From the same workshop: [SkillPort](https://github.com/Dongdarealest/skillport), skill packs that run on every AI, and [SkillDoctor](https://github.com/Dongdarealest/skilldoctor), a checkup for the skills your AI runs.

## Support

MuseKit is free and MIT licensed. If it saves you time, you can support the workshop:

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Support-0A0D26?style=for-the-badge&logo=githubsponsors&logoColor=EA4AAA)](https://github.com/sponsors/Dongdarealest)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20a%20coffee-0A0D26?style=for-the-badge&logo=kofi&logoColor=FF5E5B)](https://ko-fi.com/dongdarealest)

## Contributing

Corrections and small, well tested improvements are welcome. Keep prose in plain English, keep the importer dependency free, and run the tests before opening a pull request:

```bash
python3 -m unittest discover -s tests
```

New starter skills should be original, safe to run, and useful to a stranger without any knowledge of your setup.

## License

MIT. See [LICENSE](LICENSE).

MuseKit is an unofficial community project. It is not made by Meta and it is not official documentation.
