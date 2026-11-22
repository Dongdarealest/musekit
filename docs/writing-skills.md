# Writing skills for Muse

MuseKit is an unofficial community project, and this guide is community guidance, not official documentation. It reflects how skills in a Muse workspace are laid out today, based on the template and the skills that ship with Muse. If Muse changes its format, this guide should change with it.

## The file layout

A skill is one folder. Your own skills live in the `custom-skills` folder of your Muse workspace, one folder per skill:

```text
custom-skills/
  morning_brief/
    SKILL.md
    skill.yaml
    references/
      anything the instructions link to
    scripts/
      any helper script the method needs
```

Two files do the work. `SKILL.md` holds the instructions alone. `skill.yaml` holds the metadata. A skill can also carry a `references` folder for long detail the instructions link to, and a `scripts` folder for a helper the method depends on.

## The metadata file

Unlike Claude style skills, a Muse `SKILL.md` has no frontmatter. The fields that would sit in frontmatter live in `skill.yaml` instead:

- `name`: the skill's identity, in lowercase letters, digits and underscores. It must match the folder name. Names of skills that ship with Muse are reserved, so choose a distinct one.
- `title`: the task's plain name, shown to humans.
- `description`: one sentence naming the outcome and when to use the skill. This is the line Muse sees in its skill list, so it decides whether the skill gets picked up at all.
- `category`: an existing category, such as Travel and local plans, Shopping, Work and knowledge, or Health and fitness, so the skill is listed beside related skills.
- `include_in_prompt`: when true, the skill is listed in every conversation. When false, it is left to skill search and found when a task calls for it. Keep it false unless the skill should always be in view, because every listed skill costs context.

## The instructions file

`SKILL.md` opens with a single `#` heading carrying the title, then one `##` section per part of the method. The body is written to the agent in plain second person, as a list of bullets, one idea per bullet, each bullet starting with the action it asks for. A closing `## Available connectors` section lists the connector docs that help the task, and points to connector and skill search when nothing listed fits.

## How Muse finds skills

Muse keeps a list of the skills it can use, with the description from `skill.yaml` as the summary it judges by. A skill with `include_in_prompt` set to true sits in that list in every conversation. A skill set to false is found through skill search when a conversation needs its kind of task. Either way, the description does the finding: a vague description means a skill that exists but is never chosen.

## Five practical rules

1. Save a reusable method, not a task log. A skill teaches how to do a kind of task well, with different details each time. One conversation's facts belong in memory or in files, not in a skill.
2. Write the description as a trigger. Name the outcome and the situation, in one sentence, so the skill is chosen for the right tasks and skipped for the wrong ones.
3. Start every bullet with the action. Short, direct instructions survive contact with a real task better than explanations of why the task matters.
4. Name tools and files exactly as they are called. A skill that guesses a tool name or a path fails quietly, so check each one before you write it down.
5. Never write secrets into a skill. No passwords, tokens, keys or card numbers, even as examples. Skills get copied and shared, and a secret inside one travels with it.

## Converting a Claude skill

If you already have a skill written for Claude, with frontmatter in its `SKILL.md`, the importer in this repository converts it: it moves the metadata into `skill.yaml`, converts the name to the underscore form, and keeps the instructions and any extra files. See the importer section of the README.
