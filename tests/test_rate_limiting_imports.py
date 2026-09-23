import contextlib
import io
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch


RATE_LIMITING_EXAMPLES = (
    Path(__file__).resolve().parents[1]
    / "implementations"
    / "python"
    / "rate_limiting"
)


class RateLimitingImportTests(unittest.TestCase):
    def test_importing_examples_does_not_run_demos(self):
        for example in sorted(RATE_LIMITING_EXAMPLES.glob("*.py")):
            with self.subTest(example=example.name):
                output = io.StringIO()
                with patch(
                    "time.sleep",
                    side_effect=AssertionError("demo slept during import"),
                ):
                    with contextlib.redirect_stdout(output):
                        runpy.run_path(str(example))
                self.assertEqual(output.getvalue(), "")

    def test_running_examples_still_runs_demos(self):
        for example in sorted(RATE_LIMITING_EXAMPLES.glob("*.py")):
            with self.subTest(example=example.name):
                output = io.StringIO()
                with patch("time.sleep"):
                    with contextlib.redirect_stdout(output):
                        runpy.run_path(str(example), run_name="__main__")
                self.assertTrue(output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
