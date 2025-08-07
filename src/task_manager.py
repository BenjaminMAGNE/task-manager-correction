import argparse
import json
import os
from datetime import datetime

# chemin du fichier de tâches
TASKS_FILE = "tasks.json"

# charger les tâches si le fichier existe, sinon liste vide
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# sauvegarder les tâches dans le fichier JSON
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ajouter une tâche
def add_task(args):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": args.title,
        "description": args.desc,
        "priority": args.priority,
        "due": args.due
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Tâche ajoutée.")

# lister les tâches
def list_tasks(args):
    tasks = load_tasks()
    if args.sort == "priority":
        tasks.sort(key=lambda x: x["priority"])
    elif args.sort == "due":
        tasks.sort(key=lambda x: x["due"])

    for task in tasks:
        print(f"[{task['id']}] {task['title']} (Priorité: {task['priority']}, Échéance: {task['due']})")

# supprimer une tâche par ID
def delete_task(args):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != args.id]
    # réattribuer les IDs
    for i, task in enumerate(tasks):
        task["id"] = i + 1
    save_tasks(tasks)
    print("Tâche supprimée.")

# modifier une tâche par ID
def edit_task(args):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == args.id:
            if args.title:
                task["title"] = args.title
            if args.desc:
                task["description"] = args.desc
            if args.priority is not None:
                task["priority"] = args.priority
            if args.due:
                task["due"] = args.due
            save_tasks(tasks)
            print("Tâche modifiée.")
            return
    print("Tâche introuvable.")


# parser la ligne de commande
def main():
    parser = argparse.ArgumentParser(description="Gestionnaire de tâches")

    subparsers = parser.add_subparsers(dest="command")

    # commande add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--desc", required=True)
    add_parser.add_argument("--priority", type=int, required=True)
    add_parser.add_argument("--due", required=True)
    add_parser.set_defaults(func=add_task)

    # commande list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--sort", choices=["priority", "due"], default="priority")
    list_parser.set_defaults(func=list_tasks)

    # commande delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)
    delete_parser.set_defaults(func=delete_task)

    # commande edit
    edit_parser = subparsers.add_parser("edit")
    edit_parser.add_argument("--id", type=int, required=True)
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--desc")
    edit_parser.add_argument("--priority", type=int)
    edit_parser.add_argument("--due")
    edit_parser.set_defaults(func=edit_task)


    # exécution
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
