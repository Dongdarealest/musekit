"""Tests for the MuseKit importer.

Run with plain Python, no extra packages:

    python3 -m unittest discover -s tests
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMPORTER = ROOT / "importer" / "musekit_import.py"
FIXTURE = ROOT / "tests" / "fixtures" / "claude-skill"


def run_importer(*args):
    return subprocess.run(
        [sys.executable, str(IMPORTER), *args],
        capture_output=True,
        text=True,
    )


class ConversionTests(unittest.TestCase):
    def test_converts_fixture_into_muse_layout(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_importer(str(FIXTURE), "--output-dir", tmp)
            self.assertEqual(result.returncode, 0, result.stderr)

            target = Path(tmp) / "demo_skill"
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertTrue((target / "skill.yaml").is_file())

            skill_md = (target / "SKILL.md").read_text(encoding="utf-8")
            self.assertFalse(skill_md.startswith("---"))
            self.assertTrue(skill_md.startswith("# Demo Skill"))
            self.assertIn("Do the first step of the demo.", skill_md)

            skill_yaml = (target / "skill.yaml").read_text(encoding="utf-8")
            self.assertIn("name: demo_skill", skill_yaml)
            self.assertIn('title: "Demo Skill"', skill_yaml)
            self.assertIn("A small fixture skill", skill_yaml)
            self.assertIn('category: "Work and knowledge"', skill_yaml)
            self.assertIn("include_in_prompt: false", skill_yaml)

            copied = target / "references" / "notes.md"
            self.assertTrue(copied.is_file())

            self.assertIn("demo_skill", result.stdout)
            self.assertIn("license", result.stdout)

    def test_accepts_a_skill_md_path_directly(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_importer(str(FIXTURE / "SKILL.md"), "--output-dir", tmp)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(tmp) / "demo_skill" / "skill.yaml").is_file())

    def test_refuses_to_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = run_importer(str(FIXTURE), "--output-dir", tmp)
            self.assertEqual(first.returncode, 0, first.stderr)
            second = run_importer(str(FIXTURE), "--output-dir", tmp)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("--force", second.stderr)
            third = run_importer(str(FIXTURE), "--output-dir", tmp, "--force")
            self.assertEqual(third.returncode, 0, third.stderr)


class InvalidInputTests(unittest.TestCase):
    def write_skill(self, folder, text):
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(text, encoding="utf-8")

    def test_missing_source_fails(self):
        result = run_importer("tests/fixtures/does-not-exist")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("error", result.stderr)

    def test_non_kebab_name_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "bad"
            self.write_skill(
                source,
                "---\nname: Bad Name\ndescription: A bad fixture.\n---\n\n# Bad\n",
            )
            result = run_importer(str(source), "--output-dir", str(Path(tmp) / "out"))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("kebab case", result.stderr)

    def test_missing_frontmatter_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "plain"
            self.write_skill(source, "# Just a title\n\n- An instruction.\n")
            result = run_importer(str(source), "--output-dir", str(Path(tmp) / "out"))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("frontmatter", result.stderr)

    def test_missing_description_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "nodesc"
            self.write_skill(
                source,
                "---\nname: no-description\n---\n\n# No Description\n",
            )
            result = run_importer(str(source), "--output-dir", str(Path(tmp) / "out"))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("description", result.stderr)


class HelpTests(unittest.TestCase):
    def test_help_runs(self):
        result = run_importer("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Claude style skill", result.stdout)


if __name__ == "__main__":
    unittest.main()
