"""
Module principal du gestionnaire de taches.
Permet d ajouter, modifier, supprimer et lister les taches via argparse.
"""
import argparse
import json
import os

# chemin du fichier de taches
TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Charge les taches depuis le fichier JSON.

    Returns:
        list: Liste des taches chargees, ou liste vide si le fichier est vide ou mal forme.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """
    Enregistre les taches dans le fichier JSON.

    Args:
        tasks (list): Liste des taches a sauvegarder.

    Returns:
        None
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(args):
    """
    Ajoute une nouvelle tache a la liste et la sauvegarde.

    Args:
        args: Objet contenant les attributs title, desc, priority, due.

    Returns:
        None
    """
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
    print("Tache ajoutee.")

def list_tasks(args):
    """
    Affiche les taches triees par priorite ou par date.

    Args:
        args: Objet contenant l attribut sort (priority ou due).

    Returns:
        None
    """
    tasks = load_tasks()
    if args.sort == "priority":
        tasks.sort(key=lambda x: x["priority"])
    elif args.sort == "due":
        tasks.sort(key=lambda x: x["due"])

    for task in tasks:
        print(f"[{task['id']}] {task['title']} (Priorite: {task['priority']}, Echeance: {task['due']})")

def delete_task(args):
    """
    Supprime une tache par son identifiant.

    Args:
        args: Objet contenant l attribut id.

    Returns:
        None
    """
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != args.id]
    for i, task in enumerate(tasks):
        task["id"] = i + 1
    save_tasks(tasks)
    print("Tache supprimee.")

def edit_task(args):
    """
    Modifie une tache existante si elle est trouvee.

    Args:
        args: Objet contenant id, et les champs eventuellement modifies (title, desc, priority, due).

    Returns:
        None
    """
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
            print("Tache modifiee.")
            return
    print("Tache introuvable.")

def main():
    """
    Point dentree principal du programme. Initialise le parser de commandes.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Gestionnaire de taches")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--desc", required=True)
    add_parser.add_argument("--priority", type=int, required=True)
    add_parser.add_argument("--due", required=True)
    add_parser.set_defaults(func=add_task)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--sort", choices=["priority", "due"], default="priority")
    list_parser.set_defaults(func=list_tasks)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)
    delete_parser.set_defaults(func=delete_task)

    edit_parser = subparsers.add_parser("edit")
    edit_parser.add_argument("--id", type=int, required=True)
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--desc")
    edit_parser.add_argument("--priority", type=int)
    edit_parser.add_argument("--due")
    edit_parser.set_defaults(func=edit_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
