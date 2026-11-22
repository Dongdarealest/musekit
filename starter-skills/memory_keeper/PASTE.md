# Install memory_keeper by chat

Copy everything in the block below and paste it into a chat with your Muse. Your Muse creates the skill files itself. You never touch a folder.

---

Install a skill for yourself, exactly as written here. Create a folder named memory_keeper in my custom-skills folder, and inside it create exactly these two files with exactly these contents. Do not change anything. When both files are saved, tell me the skill is installed, then run it once right now so I can see what it does, and finish by telling me the one sentence I should say when I want it again.

File 1, SKILL.md:

# Memory Keeper

## Decide what is worth keeping

- Save durable facts, such as names, roles, preferences, decisions, and commitments, and leave out small talk, one off details, and anything the user framed as temporary.

- Keep a fact only when it would still matter in a future conversation, and leave it out when in doubt.

- Skip anything secret, such as passwords, tokens, or card numbers, even when the user shares it in passing.

## Write it down

- Write each fact into the user's long term memory file, with the date it was learned and where it came from, such as the conversation or document that stated it.

- Add day level detail to the dated note for today, and promote only the lasting version into the long term memory file.

- Write facts in the user's own terms, and keep a quote short and exact when the wording itself matters.

## Reconcile corrections

- Treat a newer statement from the user as replacing the older one, and update the memory entry in place instead of adding a second, conflicting entry.

- Note what changed and when, so the user can see why the record moved.

- Ask one short question when two records conflict and neither is clearly newer, instead of guessing which one stands.

## Speak the user's language

- Deliver everything this skill produces in the language the user speaks to you in, unless they ask for another.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

File 2, skill.yaml:

name: memory_keeper
title: "Memory Keeper"
description: "Capture durable facts, preferences and decisions from a conversation into the user's memory files, with dates and sources, and reconcile corrections."
category: "Work and knowledge"
include_in_prompt: false

