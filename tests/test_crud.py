import unittest
import os
import json
from src import task_manager

class TestCRUD(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        task_manager.TASKS_FILE = self.test_file
        with open(self.test_file, "w") as f:
            json.dump([], f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

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
        args = lambda: None
        args.title = "A"
        args.desc = "B"
        args.priority = 1
        args.due = "2025-01-01"
        task_manager.add_task(args)

        args_del = lambda: None
        args_del.id = 1
        task_manager.delete_task(args_del)
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks, [])

    def test_edit_task(self):
        args = lambda: None
        args.title = "Old"
        args.desc = "desc"
        args.priority = 1
        args.due = "2025-01-01"
        task_manager.add_task(args)

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
        task_manager.edit_task(args_edit)

    def test_list_tasks(self):
        args1 = lambda: None
        args1.title = "A"
        args1.desc = "B"
        args1.priority = 2
        args1.due = "2025-01-01"
        task_manager.add_task(args1)

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
