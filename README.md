# Projet Task Manager
=======
# Task Manager CLI

**Task Manager CLI** est une application en ligne de commande permettant de gérer efficacement une liste de tâches.  
Elle offre les fonctionnalités suivantes :  
- Ajouter une tâche  
- Supprimer une tâche  
- Modifier une tâche  
- Lister les tâches triées par priorité ou par échéance  

## 🚀 Fonctionnalités

- ✅ Ajouter des tâches avec titre, description, priorité et date d’échéance  
- ✅ Lister les tâches avec tri dynamique  
- ✅ Modifier ou supprimer des tâches existantes  
- ✅ Persistance automatique dans un fichier `tasks.json`  

## 🛠️ Utilisation

Lancez l'application via la ligne de commande :

### ➕ Ajouter une tâche

```bash
python src/task_manager.py add --title "Faire les courses" --desc "Acheter du lait" --priority 1 --due 2025-09-01
```

### 📋 Lister les tâches

```bash
python src/task_manager.py list --sort priority
python src/task_manager.py list --sort due
```

### 📝 Modifier une tâche

```bash
python src/task_manager.py edit --id 1 --title "Courses supermarché"
```

### ❌ Supprimer une tâche

```bash
python src/task_manager.py delete --id 1
```

## 📦 Dépendances

Les principales dépendances sont :

- Python 3.13+
- `argparse` (inclus par défaut)
- `pylint`, `coverage` (pour la qualité et les tests)
- `Sphinx` (pour la documentation)

Installez les dépendances :

```bash
pip install -r requirements.txt
```

## 🧪 Tests

Les tests sont situés dans le dossier `tests/`.  
Ils couvrent tous les cas standards et limites (fichiers invalides, tâches inexistantes, etc.).

Lancer les tests + coverage :

```bash
python -m coverage run -m unittest discover tests
python -m coverage report
```

## 📁 Structure du projet

```
task-manager-correction/
├── .github/workflows/      # Workflows GitHub Actions (CI/CD)
├── docs/                   # Documentation générée avec Sphinxmagne@Benji MINGW64 ~/task-manager-correction (main)
$ git merge developpement --allow-unrelated-histories -m "fusion finale de la branche developpement dans main"
Auto-merging README.md
CONFLICT (add/add): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
(.venv)
magne@Benji MINGW64 ~/task-manager-correction (main|MERGING)

├── src/                    # Code source de l'application
│   └── task_manager.py
├── tests/                  # Fichiers de test unitaire
│   ├── test_core.py
│   ├── test_edit.py
│   └── ...
├── .gitignore
├── requirements.txt
└── README.md
```

## ✍️ Auteur

Projet réalisé par **Benjamin MAGNE**  
Développé dans le cadre d’une évaluation Python CLI + Git + Tests + Documentation.
