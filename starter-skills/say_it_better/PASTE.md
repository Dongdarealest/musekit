# Install say_it_better by chat

Copy everything in the block below and paste it into a chat with your Muse. Your Muse creates the skill files itself. You never touch a folder.

---

Install a skill for yourself, exactly as written here. Create a folder named say_it_better in my custom-skills folder, and inside it create exactly these two files with exactly these contents. Do not change anything. When both files are saved, tell me the skill is installed, then run it once right now so I can see what it does, and finish by telling me the one sentence I should say when I want it again.

File 1, SKILL.md:

# Say It Better

## Get the raw material

- Ask for the draft as written, or the gist plus two facts: who receives the message, and what the relationship is.

- Ask what the message has to achieve, in one sentence. If the user cannot say, propose the most likely outcome and confirm it before rewriting.

## Rewrite it

- Keep every fact exactly as the user gave it. Never invent dates, commitments, prices, or apologies.

- Cut anything that does not serve the outcome. Shorter wins, unless shorter turns rude.

- Offer at most two versions, the warm one and the direct one, and say which you would send and why, in one line.

## Guard the user

- Flag any sentence that could be misread by a tired or annoyed reader, and offer a safer phrasing beside it.

- If the message was written in anger, also offer the version to send tomorrow morning.

- Match the user's language. No corporate filler and no flattery padding.

## Available connectors

- Use `muse.connector_search` to find connectors for the accounts this skill touches, and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

File 2, skill.yaml:

name: say_it_better
title: "Say It Better"
description: "Turn a rough draft or a gist into a message that lands: facts kept exact, filler cut, one warm version and one direct version."
category: "Communication"
include_in_prompt: false

