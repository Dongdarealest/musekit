# Changelog

## 0.1.4, 2026-11-22

- Added a visitor counter badge to the README: it goes up when someone opens the page.

## 0.1.3, 2026-11-22

- README opening rebuilt around the reader, not the maker: what MuseKit does for you in one sentence, a one minute no tools install, and a sample of what each starter skill actually gives you. The importer moves below the starter skills, where it belongs.

## 0.1.2, 2026-11-22

- New identity of its own: MuseKit now wears the Meta AI gradient ring on deep indigo with clean sans type, instead of the ink and gold workshop look shared with SkillPort and SkillDoctor.
- Masthead, demo shot and social card rebuilt in the new identity; README badges and Support buttons recolored to match.

## 0.1.1, 2026-11-22

- README rebuilt around a designed masthead, a real importer demo shot, and a thirty second quick start.
- Added the Claude versus Muse format table, so the one thing a newcomer must understand is visible without reading the guide.
- Added FUNDING.yml and a Support section (GitHub Sponsors and Ko-fi).
- Added a social preview card under assets/.


## 0.1.0, 2026-11-22

- First release of MuseKit, an unofficial starter kit for Muse users.
- Importer: a zero dependency Python CLI that converts a Claude style skill into a Muse ready skill folder, with name validation, overwrite protection, and a printed list of every change it makes.
- Three starter skills written natively for Muse: morning_brief, memory_keeper, and watch_and_report.
- A short guide to writing skills for Muse, covering the file layout, the skill.yaml metadata fields, how Muse finds skills, and five practical rules.
- A test suite for the importer that runs with plain Python, and CI on Python 3.10 and 3.12.
