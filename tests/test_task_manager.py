import unittest
import os
import json
from src import task_manager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # ici on cree un fichier temporaire pour les tests
        self.test_file = "test_tasks.json"
        task_manager.TASKS_FILE = self.test_file

        # on initialise le fichier avec une liste vide
        with open(self.test_file, "w") as f:
            json.dump([], f)

    def tearDown(self):
        # on supprime le fichier apres chaque test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        # on ajoute une tache
        args = lambda: None
        args.title = "Test"
        args.desc = "Description de test"
        args.priority = 1
        args.due = "2025-08-10"

        task_manager.add_task(args)

        # on verifie que la tache est bien ajoutee
        tasks = task_manager.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test")

    def test_delete_task(self):
        # on ajoute une tache pour pouvoir la supprimer
        args = lambda: None
        args.title = "A supprimer"
        args.desc = "..."
        args.priority = 1
        args.due = "2025-08-12"
        task_manager.add_task(args)

        # suppression de la tache
        args_del = lambda: None
        args_del.id = 1
        task_manager.delete_task(args_del)

        # on verifie que la liste est vide
        tasks = task_manager.load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_edit_task(self):
        # on ajoute une tache qu on va modifier ensuite
        args = lambda: None
        args.title = "Ancien titre"
        args.desc = "Ancienne description"
        args.priority = 2
        args.due = "2025-08-10"
        task_manager.add_task(args)

        # on modifie la tache 1
        args_edit = lambda: None
        args_edit.id = 1
        args_edit.title = "Nouveau titre"
        args_edit.desc = None
        args_edit.priority = 1
        args_edit.due = None

        task_manager.edit_task(args_edit)

        tasks = task_manager.load_tasks()
        self.assertEqual(tasks[0]["title"], "Nouveau titre")
        self.assertEqual(tasks[0]["priority"], 1)
        self.assertEqual(tasks[0]["description"], "Ancienne description")  # inchangé


if __name__ == "__main__":
    unittest.main()
