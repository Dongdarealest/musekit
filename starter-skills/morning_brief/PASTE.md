# Install morning_brief by chat

Copy everything in the block below and paste it into a chat with your Muse. Your Muse creates the skill files itself. You never touch a folder.

---

Install a skill for yourself, exactly as written here. Create a folder named morning_brief in my custom-skills folder, and inside it create exactly these two files with exactly these contents. Do not change anything. When both files are saved, tell me the skill is installed, then run it once right now so I can see what it does, and finish by telling me the one sentence I should say when I want it again.

File 1, SKILL.md:

# Morning Brief

## Gather the raw material

- Read today's events from the user's connected calendar, including start times, places, and anything that needs travel or preparation.

- Search unread mail from the last day for messages that need a reply, carry a deadline, or change today's plan.

- List the user's scheduled tasks and background jobs that ran overnight or fall due today, and note any that failed or are waiting on the user.

## Shape the briefing

- Look for a proactive preferences file in the user's workspace and follow it for length, topics, and what counts as worth interrupting the user with.

- Lead with whatever is time sensitive, such as a deadline today, a meeting that moved, or a failed job the user was counting on.

- Keep the whole briefing short enough to read in under a minute, and cut anything that is only background noise.

- End with at most three suggested actions, each one a single sentence the user can accept or ignore.

## If nothing is connected yet

- If no calendar and no mail are connected, do not deliver an empty briefing and do not stop at saying so. Ask the user one question: what is on today, and does anything carry a deadline?

- Build the briefing from their answer, in the same shape as a connected one. Afterwards, offer once to connect calendar and mail so tomorrow runs itself.

## Deliver it

- Send the briefing once, in the chat or channel the user's preferences name for briefings.

- Stay silent instead when nothing has changed and nothing needs the user, if their preferences say an empty briefing is worse than none.

## Speak the user's language

- Deliver everything this skill produces in the language the user speaks to you in, unless they ask for another.

## Available connectors

- [Google Calendar](/opt/hatch/connectors/google_calendar/CONNECTOR.md) for today's events and free or busy times.

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for unread mail that needs attention.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

File 2, skill.yaml:

name: morning_brief
title: "Morning Brief"
description: "Prepare a short morning briefing from the user's calendar, unread mail and scheduled tasks, shaped by their proactive preferences."
category: "Work and knowledge"
include_in_prompt: false

