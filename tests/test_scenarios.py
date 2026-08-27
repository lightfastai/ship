import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "tests" / "scenarios"

EXPECTED_SCENARIOS = {
    "01-admission-and-material-ambiguity.md",
    "02-multi-project-scope-and-expansion.md",
    "03-existing-and-overlapping-work.md",
    "04-live-authority-contraction.md",
    "05-root-direct-work-interruption.md",
    "06-target-task-interruption.md",
    "07-post-completion-reconciliation.md",
    "08-unavailable-capability-and-orchestrator-edge.md",
    "09-operating-window-and-partial-gate.md",
    "10-workbench-loss.md",
    "11-terminal-outcomes-and-cancellation.md",
    "12-integrated-result-boundaries.md",
}

REQUIRED_TRACE_FIELDS = (
    "## Initial evidence",
    "## Expected decision",
    "## Attempted effect",
    "## Native outcome",
    "## Continuation or resumption",
)

REQUIRED_COVERAGE = {
    "01-admission-and-material-ambiguity.md": ("purely advisory", "product choice"),
    "02-multi-project-scope-and-expansion.md": ("multi-project", "scope expansion"),
    "03-existing-and-overlapping-work.md": ("overlapping", "duplicate"),
    "04-live-authority-contraction.md": ("instructions", "credentials", "provider"),
    "05-root-direct-work-interruption.md": ("before any mutation", "pull request"),
    "06-target-task-interruption.md": ("source task identifier", "replacement"),
    "07-post-completion-reconciliation.md": ("after native completion", "duplicate"),
    "08-unavailable-capability-and-orchestrator-edge.md": (
        "skill",
        "tool",
        "provider",
        "Target Project",
        "cyclic Orchestrator edge",
    ),
    "09-operating-window-and-partial-gate.md": ("Operating Window", "production gate"),
    "10-workbench-loss.md": ("Complete Workbench loss", "runtime"),
    "11-terminal-outcomes-and-cancellation.md": ("Completed", "Cancelled", "Impossible"),
    "12-integrated-result-boundaries.md": ("deployment", "must not infer production authority"),
}


class ScenarioContractTests(unittest.TestCase):
    def test_exact_approved_scenario_set_exists(self):
        actual = {path.name for path in SCENARIOS.glob("*.md")}
        self.assertEqual(actual, EXPECTED_SCENARIOS)

    def test_every_scenario_contains_trace_fields(self):
        for scenario in sorted(SCENARIOS.glob("*.md")):
            content = scenario.read_text()
            for field in REQUIRED_TRACE_FIELDS:
                self.assertIn(field, content, f"{scenario.name} lacks {field}")

    def test_every_scenario_contains_required_coverage(self):
        for name, phrases in REQUIRED_COVERAGE.items():
            content = (SCENARIOS / name).read_text()
            for phrase in phrases:
                self.assertIn(phrase, content, f"{name} lacks coverage: {phrase}")

    def test_runtime_contract_has_no_workbench_dependency(self):
        agents = (ROOT / "AGENTS.md").read_text()
        architecture = (ROOT / "docs" / "architecture.md").read_text()

        self.assertIn("WorkBench state".lower(), agents.lower())
        self.assertIn("WorkBench absence".lower(), architecture.lower())
        self.assertIn("no hard runtime dependency", architecture)


if __name__ == "__main__":
    unittest.main()
