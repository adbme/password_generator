[![Python application](https://github.com/adbme/password_generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/adbme/password_generator/actions/workflows/python-app.yml)

# Password Generator

## Description
Un générateur de mots de passe sécurisé et personnalisable (longueur, utilisation de caractères spéciaux, chiffres, etc.), utilisable dans le CLI, développé en suivant la méthode TDD.

---

## Objectifs de l’application
- Permettre aux utilisateurs de générer des mots de passe forts et uniques.
- Offrir une personnalisation avancée (longueur, caractères spéciaux, chiffres, majuscules, minuscules).
- Assurer la fiabilité du générateur avec des tests automatisés (TDD).
- Fournir un outil simple à utiliser en ligne de commande.

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/adbme/password_generator.git
   cd password-generator
   ```

2. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Exécutez les tests pour vérifier l'installation :
   ```bash
   pytest -v
   ```

---

## Exécution

1. Lancer la génération d’un mot de passe par défaut :
   ```bash
   python password_generator.py
   ```

2. Générer un mot de passe de 16 caractères avec chiffres et caractères spéciaux :
   ```bash
   python password_generator.py --length 16 --special --numbers
   ```

3. Afficher l’aide :
   ```bash
   python password_generator.py --help
   ```

---

## Architecture générale de l’application

### Technologies utilisées
- **Langage** : Python 3.x
- **Bibliothèques** : `random`, `string`, `argparse`
- **Tests unitaires** : `pytest`
- **Intégration continue** : GitHub Actions (optionnel)

### Structure du projet
```
password_generator_project/
│── password_generator.py  # Script principal
│── test_password_generator.py  # Tests unitaires
│── requirements.txt  # Dépendances
│── .github/
│   └── workflows/
│       └── tests.yml  # CI/CD pipeline
│── README.md  # Documentation
```

---
