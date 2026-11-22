# Install spend_check by chat

Copy everything in the block below and paste it into a chat with your Muse. Your Muse creates the skill files itself. You never touch a folder.

---

Install a skill for yourself, exactly as written here. Create a folder named spend_check in my custom-skills folder, and inside it create exactly these two files with exactly these contents. Do not change anything. When both files are saved, tell me the skill is installed, then run it once right now so I can see what it does, and finish by telling me the one sentence I should say when I want it again.

File 1, SKILL.md:

# Spend Check

## Gather the spending

- Work only from what the user gives you: pasted receipts, bank notifications, a list, or their rough memory of the week. Say plainly that you have no bank access unless a connector provides it.

- If a previous check is saved in memory, load it before starting, so this one can compare.

## Do the sums

- Group the spending into five buckets: fixed costs, food, transport, fun, and everything else. Total each bucket, then the week.

- Show the arithmetic. Every total must be traceable to the items listed above it.

- Compare with the previous check where one exists: which bucket moved, and by how much.

## Name the one thing

- Point to the single largest leak and estimate what it costs per month if it repeats.

- Suggest one concrete change, small enough to actually happen, with the amount it would save.

- Save this check with its date, so the next check has something to compare against.

## Rules

- No judgment and no lectures. Numbers first, one suggestion, done.

- Use the user's currency, and round the way they round.

## Speak the user's language

- Deliver everything this skill produces in the language the user speaks to you in, unless they ask for another.

## Available connectors

- Use `muse.connector_search` to find connectors for the accounts this skill touches, and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

File 2, skill.yaml:

name: spend_check
title: "Spend Check"
description: "A weekly money review from whatever the user pastes in: spending grouped and totalled, one leak named, one small change suggested."
category: "Money and life"
include_in_prompt: false

