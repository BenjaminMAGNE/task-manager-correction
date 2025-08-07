Document de Réflexion — Projet task-manager-correction
Ce document présente une réflexion détaillée sur la conception, le développement et la mise en production du projet CLI task-manager-correction, application permettant la gestion de tâches via une interface en ligne de commande.

1. Objectifs et Contexte
L’objectif principal du projet était de développer une application de gestion de tâches simple et efficace en ligne de commande, permettant à un utilisateur d'ajouter, modifier, supprimer et lister des tâches, le tout avec une persistance locale via un fichier JSON.

Le projet devait en plus intégrer :

Une couverture de tests robuste.

Une documentation technique générée automatiquement.

Une chaîne d’intégration continue fonctionnelle via GitHub Actions.

Un dépôt bien structuré, avec une gestion rigoureuse via Git.

2. Architecture du Projet
Le projet est organisé autour d’une structure claire et modulaire :

bash
Copier
Modifier
task-manager-correction/
│
├── src/
│   └── task_manager.py        # Logique métier + interface CLI
│
├── tests/
│   ├── test_....py           # Tests liés aux fonctions de base (load, save)
│   ├── test_....py     # Tests liés aux opérations (ajout, suppression, modification)
│   └── test_main.py           # Tests du point d’entrée CLI
│
├── docs/
│   ├── source/                # Fichiers Sphinx source
│   └── build/                 # Documentation générée
│
├── .github/
│   └── workflows/
│       ├── ci.yml           # Tests + lint + coverage
│       └── docs.yml           # Génération automatique de la doc
│
├── README.md
└── requirements.txt
3. Choix Techniques
CLI avec argparse : Utilisé pour la gestion de la ligne de commande. Chaque sous-commande (add, delete, etc.) est bien séparée.

Stockage via JSON : Simple, efficace, permet une persistance claire sans base de données.

Python natif uniquement : Pas de frameworks externes lourds, ce qui assure la légèreté du projet.

Tests avec unittest, couverture avec coverage.py, et lint avec pylint.

4. Tests et Assurance Qualité
Organisation stricte des tests dans tests/, avec des modules séparés par fonctionnalité.

Couverture à 96 %, atteinte après plusieurs refactorings et l'ajout de tests pour les cas limites.

Tests robustes couvrant :

Cas standards (ajout, suppression, édition)

Cas limites (JSON mal formé, tâche inexistante, test de main() sans arguments)

Linting avec pylint, avec une exigence de score minimum 9/10 dans GitHub Actions.

5. Documentation
Docstrings conformes à la norme Google sur 100 % des fonctions.

Documentation générée automatiquement avec Sphinx.

Workflow dédié (docs.yml) pour générer la documentation à chaque push.

Dossier docs/ versionné dans Git, contenant à la fois les sources et les fichiers HTML générés.

6. Git et Intégration Continue
Branche principale : main

Branche secondaire : developpement, utilisée pour les fonctionnalités et l’intégration.

Commits structurés et clairs selon les bonnes pratiques (feat:, fix:, docs:, etc.).

GitHub Actions :

Lancement des tests sur Python 3.8, 3.9, 3.10.

Arrêt automatique si pylint donne un score < 9.0.

Génération automatique des artefacts de test et de documentation.

7. Difficultés Rencontrées
Plusieurs points ont nécessité un long travail de débogage et de compréhension :

⚠️ Installation et exécution de pylint et coverage sous Git Bash : nécessité de passer par python -m, problèmes de command not found.

⚠️ Mauvaise couverture initiale (~59 %) malgré les tests → analyse avec coverage report ligne par ligne pour identifier le code non exécuté.

⚠️ Mauvaise importation dans les tests (argparse, tmp_path) → plusieurs erreurs critiques corrigées.

⚠️ Échecs répétés de sphinx-quickstart sous Windows → résolution par installation propre + utilisation en ligne de commande Python.

⚠️ Erreur GitHub Actions (exit code 20) à cause de pylint → ajustement du workflow pour ne pas arrêter l’exécution si la note est juste en dessous de 10.

⚠️ Problème de push Git à cause de fichiers compilés (__pycache__, .coverage) → ajout d’un .gitignore complet et propre.

⚠️ Arborescence docs/ mal configurée → recréation complète via sphinx-apidoc et réorganisation des fichiers.

Ces étapes ont été résolues une à une, souvent après plusieurs tentatives, et avec l’aide de nombreux tests manuels, relectures, et validations via GitHub Actions.

8. Conclusion
Le projet task-manager-correction démontre :

Une forte capacité à structurer un projet Python proprement.

Une maitrise de la documentation technique et des outils de tests.

Une résilience face à des erreurs techniques parfois complexes.

Une compréhension solide des principes de CI/CD.

Réalisé par : Benjamin MAGNE
Promotion 2025 — Projet : Gestionnaire de tâches en ligne de commande
Date : 07 août 2025
