# Document de Réflexion — Projet task-manager-correction

Ce document présente une réflexion détaillée sur la conception, le développement et la mise en production du projet **CLI task-manager-correction**, une application permettant la gestion de tâches via une interface en ligne de commande.

## 1. Objectifs et Contexte
L’objectif principal du projet était de développer une application de gestion de tâches simple et efficace en ligne de commande, permettant à un utilisateur d'ajouter, modifier, supprimer et lister des tâches, avec une **persistance locale** via un fichier JSON.

En plus de la logique métier, le projet devait intégrer :
- Une **couverture de tests** robuste.
- Une **documentation technique générée automatiquement**.
- Une **chaîne d’intégration continue** fonctionnelle via GitHub Actions.
- Une **organisation Git claire** avec branches et commits normalisés.

## 2. Architecture du Projet
Le projet est organisé autour d’une structure claire et modulaire :

```
task-manager-correction/
│
├── src/
│   └── task_manager.py        # Logique métier + interface CLI
│
├── tests/
│   ├── test_crud.py           # Tests liés aux opérations CRUD (add, delete, edit)
│   ├── test_io.py             # Tests liés au chargement et sauvegarde des données
│   └── test_main.py           # Tests du point d’entrée CLI
│
├── docs/
│   ├── source/                # Fichiers Sphinx source
│   └── build/                 # Documentation générée
│
├── .github/
│   └── workflows/
│       ├── ci.yml             # Tests + lint + coverage
│       └── docs.yml           # Génération automatique de la documentation
│
├── README.md
└── requirements.txt
```

## 3. Choix Techniques
- **CLI avec argparse** : gestion claire des sous-commandes (`add`, `delete`, `edit`, `list`) avec arguments bien définis.
- **Stockage via JSON** : léger, simple et efficace, évitant l’ajout d’une base de données.
- **Python natif** : aucun framework lourd, garantissant la portabilité et la simplicité.
- **Tests unitaires** avec `unittest`, **couverture** avec `coverage.py`, et **linting** avec `pylint`.

## 4. Tests et Assurance Qualité
- Organisation stricte des tests dans `tests/` avec séparation par fonctionnalités.
- Couverture de **96 %**, atteinte après plusieurs refactorings.
- Tests robustes couvrant :
  - Cas standards (ajout, suppression, édition).
  - Cas limites (JSON mal formé, tâche inexistante, exécution sans arguments).
- Intégration de `pylint` dans le workflow avec exigence de note >= 9/10.

## 5. Documentation
- **Docstrings** conformes à la norme Google sur 100 % des fonctions et classes.
- **Documentation générée automatiquement** avec Sphinx.
- Workflow `docs.yml` générant la documentation à chaque push.
- Dossier `docs/` versionné contenant les sources et fichiers HTML générés.

## 6. Git et Intégration Continue
- Branche principale : `main`
- Branche secondaire : `developpement` pour le travail avant fusion.
- Commits structurés selon les bonnes pratiques (`feat:`, `fix:`, `docs:`, etc.).
- GitHub Actions :
  - Tests sur Python **3.11**, **3.12**, **3.13**.
  - Arrêt si `pylint` < 9.0.
  - Génération d’artefacts pour les tests et la documentation.

## 7. Difficultés Rencontrées
- Installation et exécution de `pylint` et `coverage` sous Git Bash.
- Couverture initiale faible (~59 %) → analyse avec `coverage report` pour corriger.
- Problèmes d’imports dans les tests (`argparse`, `tmp_path`) → corrections.
- Échecs répétés de `sphinx-quickstart` sous Windows → installation propre.
- Erreur GitHub Actions (exit code 20) à cause de `pylint`.
- Conflits Git dus à `__pycache__` et `.coverage` → `.gitignore` mis à jour.
- Réorganisation complète de `docs/` via `sphinx-apidoc`.

## 8. Conclusion
Le projet **task-manager-correction** démontre :
- Une forte capacité à structurer un projet Python proprement.
- Une maitrise de la documentation technique et des outils de tests.
- Une résilience face à des erreurs techniques complexes.
- Une compréhension solide des principes de CI/CD.

**Réalisé par** : Benjamin MAGNE  
**Promotion** : 2025 — Projet : Gestionnaire de tâches en ligne de commande  
**Date** : 07 août 2025
