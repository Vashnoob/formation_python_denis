## 🧩 Etape 6 - Ajout de tests unitaires avec pytest

## 🎯 Objectif
Vérifier le bon fonctionnement des classes `Trajet`, `TrajetExpress` et `Utilisateur` grâce à des **tests automatisés**.  
Introduire la notion de **qualité de code**, de **non-régression** et de **validation automatisée**.

---

## 📁 Fichiers ajoutés ou modifiés — Étape 6

| Fichier / Dossier                                   | Rôle / Ce qu’il contient                                                                                  | Priorité |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------|
| `tests/`                                            | Nouveau dossier pour stocker tous les tests du projet                                                      | 🟢 Clé   |
| `tests/test_models.py`                              | Fichier de tests unitaires sur les classes métier                                                          | 🟢 Clé   |
|                                                     | - `test_trajet_calcul_duree()` : vérifie le calcul de durée normale                                       |          |
|                                                     | - `test_trajet_express_duree()` : vérifie la durée en mode express                                        |          |
|                                                     | - `test_utilisateur_reservation()` : vérifie que la réservation est bien ajoutée                          |          |
| `pyproject.toml` (modifié)                          | Ajout de `pytest` dans les dépendances pour automatiser l’exécution des tests                             | 🟢 Clé   |

---

## 🧰 A faire dans cette étape

| Action                                               | Détail technique                                                                                         |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1. Créer un fichier `test_models.py`                 | Contient des fonctions de test indépendantes                                                             |
| 2. Utiliser `assert` pour valider les résultats      | Python natif, simple et lisible                                                                          |
| 3. Organiser le dossier `tests/`                     | Respecter la structure classique pour `pytest`                                                           |
| 4. Exécuter les tests avec `pytest`                  | Via terminal : `pytest projet7/tests/`                                                                   |

---

## ✅ Dépendance nécessaire

| Bibliothèque     | Utilité                          | Installation              |
|------------------|----------------------------------|---------------------------|
| `pytest`         | Framework de test léger, rapide  | `pip install pytest`      |

---

## 🧠 Grace à cette étape

- Comprendre le principe de **test unitaire** : une fonction = un comportement = un test.
- Maîtriser l’utilisation de `pytest` dans un projet Python modulaire.
- Identifier les erreurs de logique ou de modification (régression).
- Favoriser les **bonnes pratiques de développement**.

---

✅ Des **tests unitaires** pour :

- `Trajet` : test de la méthode `calculer_duree()`
- `TrajetExpress` : test de la durée accélérée
- `Utilisateur` : test de réservation et de structure de données

📁 Les tests sont dans le fichier : `tests/test_models.py`  
📦 pytest doit etre ajouté aux dépendances dans `pyproject.toml`


Lancer les tests via :

```bash
pytest projet8/tests
```
