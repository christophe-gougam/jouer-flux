## Description
Une application de gestion de firewalls, politiques de filtrage et règles de firewall communiquant avec une base de données SQLAlchemy via des APIs définies sur Swagger.

## Installation

1. Cloner le dépôt
2. Installer les dépendances : `pip install -r requirements.txt`
3. Lancer l'application : `flask run`

## Utilisation
Vous pouvez tester les APIs avec Swagger en visitant `/swagger-ui`.

## Docker
Pour utiliser Docker :
`docker build -t jouerflux`
`docker run -p 5000:5000 jouerflux`

## Documentation
- Le dossier `app` comprend tous les fichiers nécessaires au fontionnement du projet.
- Dans le dossier `model` on retrouve le fichier `objects.py` qui sert à définir les 3 objects Firewall, Rule et Policy ainsi que leurs différents champs. On y trouve aussi le fichier `repositories.py` qui définit les fonctions qui seront appelées par les différents endpoint des API. Chaque objet contient une fonction create, update, delete, getAll et getById.
- Le dossier `objects` contient les fichiers de définition des fonctions et des actions qui seront réalisées au niveau de la base de données SQLite
- Le dossier `static` contient le fichier `swagger.yml` qui décrit tous les appels API de notre application et la configuration globale de l'application swagger.
- Le fichier `database.db` contiendra toutes les données qui auront été créées via l'API swagger.
- Le fichier `db.py` contient l'initialisation de notre objet SQLAlchemy.
- Le fichier `marshmallow.py` contient l'initialisation de notre object Marshmallow qui permet de faciliter le lien entre les objets python et les objets définis niveau base de données avec SQLAlchemy.
- Le fichier `models.py` contient la définition des tables des différents objets au niveau base de données avec les champs qui les composent et les relation entre elles, nottament au niveau des clés étrangères.
- Le fichier `run.py` est le main de notre application, c'est le fichier qui sert à lancer l'application et comprend l'initialisation de la configuration de swagger et de la base SQLAlchemy.
- Le fichier `schema.py` sert à définir la structure et les regles des objets pour la gestion de ces objets au niveau de Marshmallow. Il permet également la validation des données entre les objets python et les objets côté base de données.