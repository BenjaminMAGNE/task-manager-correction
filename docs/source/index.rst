.. Task Manager Correction documentation master file, created by
   sphinx-quickstart on Thu Aug  7 16:01:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Task Manager Correction documentation
=====================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.
Bienvenue dans la documentation du projet Task Manager
======================================================

Ce projet est une application en ligne de commande permettant de gerer une liste de taches personnelles.

Fonctionnalites principales :
- Ajouter une tache avec un titre, une description, une priorite et une date limite
- Lister les taches triees par priorite ou date
- Modifier ou supprimer une tache
- Sauvegarde automatique des donnees dans un fichier JSON

Fonctionnalite avancee :
- Affichage des taches en retard ou proches de leur date limite (a venir)

Utilisation de la ligne de commande
-----------------------------------

Exemples :

Ajouter une tache :

    python src/task_manager.py add --title "Rapport" --desc "Finir la doc" --priority 1 --due 2025-08-10

Lister les taches par priorite :

    python src/task_manager.py list --sort priority

Supprimer une tache :

    python src/task_manager.py delete --id 3

Modifier une tache :

    python src/task_manager.py edit --id 2 --priority 1 --title "Modifie"


.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   modules

