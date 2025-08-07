import unittest
import json
import os
from src import task_manager

class TestIO(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        task_manager.TASKS_FILE = self.test_file
        with open(self.test_file, "w") as f:
            json.dump([], f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_tasks_vide(self):
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_load_tasks_json_invalide(self):
        with open(self.test_file, "w") as f:
            f.write("not json")
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_save_tasks(self):
        data = [{"id": 1, "title": "x", "description": "y", "priority": 1, "due": "2025-01-01"}]
        task_manager.save_tasks(data)
        with open(self.test_file, "r") as f:
            result = json.load(f)
        self.assertEqual(result, data)
