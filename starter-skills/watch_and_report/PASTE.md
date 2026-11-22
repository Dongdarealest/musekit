# Install watch_and_report by chat

Copy everything in the block below and paste it into a chat with your Muse. Your Muse creates the skill files itself. You never touch a folder.

---

Install a skill for yourself, exactly as written here. Create a folder named watch_and_report in my custom-skills folder, and inside it create exactly these two files with exactly these contents. Do not change anything. When both files are saved, tell me the skill is installed and what it will do for me.

File 1, SKILL.md:

# Watch and Report

## Set the watch up

- Ask the user for the topic, where it should be checked, and how often, and repeat the watch back in one sentence before creating anything.

- State the schedule and the likely cost of a recurring check plainly, and create the scheduled job only after the user agrees to both.

- Write the job so each run checks the named sources, compares what it finds against the last saved state, and records the result whether or not it reports.

## Decide whether to interrupt

- Interrupt the user only when something material changed, such as a price or a date crossing a threshold they set, a deadline moving closer, or a reply arriving on a thread they are waiting on.

- Stay silent on runs where nothing changed, and fold the result into the next regular briefing instead.

- Batch small changes into one message rather than sending one message per change.

## Keep the watch healthy

- Stop the watch and tell the user when the source disappears, the check keeps failing, or the topic is clearly settled.

- Name how to pause or end the watch in one short line whenever you do report, so the user is never stuck with a watch they did not ask to keep.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

File 2, skill.yaml:

name: watch_and_report
title: "Watch and Report"
description: "Set up a scheduled check on a topic the user names, with clear rules for when to interrupt the user and when to stay silent."
category: "Work and knowledge"
include_in_prompt: false

