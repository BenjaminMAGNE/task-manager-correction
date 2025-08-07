import subprocess
import unittest
from unittest import TestCase
from unittest.mock import patch
from src import task_manager

class TestMainScript(TestCase):
    def test_main_no_command(self):
        result = subprocess.run(
            ["python", "src/task_manager.py"],
            capture_output=True,
            text=True
        )
        self.assertIn("Gestionnaire de taches", result.stdout)

    def test_main_add(self):
        with patch("sys.argv", [
            "task_manager.py", "add",
            "--title", "x", "--desc", "y", "--priority", "1", "--due", "2025-01-01"
        ]):
            task_manager.main()
