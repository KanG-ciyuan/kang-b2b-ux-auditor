import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_identity_and_resources(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        skill = (ROOT / "SKILL.md").read_text()
        self.assertEqual(manifest["name"], "kang-b2b-ux-auditor")
        self.assertEqual(manifest["version"], "0.2.0")
        self.assertTrue((ROOT / "references/ux-rubric.md").exists())
        self.assertTrue((ROOT / "evals/output_cases.json").exists())
        self.assertIn("Do not edit code", skill)

    def test_task_and_state_contract(self):
        skill = (ROOT / "SKILL.md").read_text()
        rubric = (ROOT / "references/ux-rubric.md").read_text()
        for phrase in ["Required inputs", "one primary task", "Output contract", "Stop and escalate"]:
            self.assertIn(phrase, skill)
        for phrase in ["Task success test", "State matrix", "Severity", "Visual preference alone"]:
            self.assertIn(phrase, rubric)

    def test_generic_coverage(self):
        skill = (ROOT / "SKILL.md").read_text().lower()
        self.assertNotIn("enterprise ai process diagnosis", skill)
        cases = json.loads((ROOT / "evals/trigger_cases.json").read_text())
        self.assertGreaterEqual(len(cases["should_trigger"]), 5)
        self.assertGreaterEqual(len(cases["should_not_trigger"]), 3)
        self.assertGreaterEqual(len(cases["near_neighbor"]), 3)


if __name__ == "__main__":
    unittest.main()
