import subprocess
import unittest
import os
import json
from src import task_manager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # on utilise un fichier test au lieu de tasks.json
        self.test_file = "test_tasks.json"
        task_manager.TASKS_FILE = self.test_file
        with open(self.test_file, "w") as f:
            json.dump([], f)

    def tearDown(self):
        # on nettoie apres chaque test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_tasks_vide(self):
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_load_tasks_json_invalide(self):
        with open(self.test_file, "w") as f:
            f.write("pas du json")
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_save_tasks(self):
        data = [{"id": 1, "title": "x", "description": "y", "priority": 1, "due": "2025-01-01"}]
        task_manager.save_tasks(data)
        with open(self.test_file, "r") as f:
            result = json.load(f)
        self.assertEqual(result, data)

    def test_add_task(self):
        args = lambda: None
        args.title = "Test"
        args.desc = "Desc"
        args.priority = 1
        args.due = "2025-01-01"
        task_manager.add_task(args)
        tasks = task_manager.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test")

    def test_delete_task(self):
        # on ajoute une tache
        args = lambda: None
        args.title = "A"
        args.desc = "B"
        args.priority = 1
        args.due = "2025-01-01"
        task_manager.add_task(args)

        # on supprime
        args_del = lambda: None
        args_del.id = 1
        task_manager.delete_task(args_del)
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_edit_task(self):
        # ajout
        args = lambda: None
        args.title = "Old"
        args.desc = "desc"
        args.priority = 1
        args.due = "2025-01-01"
        task_manager.add_task(args)

        # modification
        args_edit = lambda: None
        args_edit.id = 1
        args_edit.title = "New"
        args_edit.desc = None
        args_edit.priority = None
        args_edit.due = None
        task_manager.edit_task(args_edit)
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks[0]["title"], "New")

    def test_edit_task_introuvable(self):
        args_edit = lambda: None
        args_edit.id = 99
        args_edit.title = "X"
        args_edit.desc = None
        args_edit.priority = None
        args_edit.due = None
        # ça doit juste rien planter
        task_manager.edit_task(args_edit)

    def test_list_tasks(self):
        args = lambda: None
        args.title = "A"
        args.desc = "B"
        args.priority = 2
        args.due = "2025-01-01"
        task_manager.add_task(args)

        args2 = lambda: None
        args2.title = "C"
        args2.desc = "D"
        args2.priority = 1
        args2.due = "2024-01-01"
        task_manager.add_task(args2)

        args_list = lambda: None
        args_list.sort = "priority"
        task_manager.list_tasks(args_list)

        args_list.sort = "due"
        task_manager.list_tasks(args_list)

    def test_main_no_command(self):
        result = subprocess.run(
            ["python", "src/task_manager.py"],
            capture_output=True,
            text=True
        )
        self.assertIn("Gestionnaire de taches", result.stdout)


if __name__ == "__main__":
    unittest.main()
