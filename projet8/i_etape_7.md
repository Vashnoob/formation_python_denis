## 🧩 Étape 7 — Persistance avec SQLite (`sqlite3`)

## 🎯 Objectif
Remplacer ou compléter le stockage JSON par une base **relationnelle légère (SQLite)** pour :
- gérer les données utilisateurs, trajets, réservations
- utiliser des jointures et requêtes SQL
- structurer les données de façon plus robuste

---

## 📁 Fichiers ajoutés ou modifiés — Étape 7

| Fichier / Dossier                                   | Rôle / Contenu                                                                                          | Priorité |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------|
| `services/db.py`                                    | 💡 Nouveau module de gestion des données via SQLite                                                      | 🟢 Clé   |
|                                                     | - Fonction `initialiser_db()` : crée les tables                                                          |          |
|                                                     | - Fonction `ajouter_utilisateur()`, `ajouter_trajet()`                                                   |          |
|                                                     | - Fonction `faire_reservation()` : insère dans la table de liaison avec date                            |          |
|                                                     | - Fonction `lister_reservations()` : exécute une requête avec jointure                                  |          |
| `main_db.py`                                        | Script de démonstration : crée la BDD, ajoute des données, liste les réservations                       | 🟢 Clé   |
| `data/reservations.db`                              | 🗃️ Base de données SQLite générée automatiquement                                                        | 🔵 Auto  |

---

## 🧰 A faire dans cette étape

| Action                                               | Détail technique                                                                                         |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1. Créer un schéma SQLite dans `db.py`              | 3 tables : `utilisateurs`, `trajets`, `reservations` avec clés étrangères                               |
| 2. Utiliser `sqlite3.connect()` et `cursor.execute()`| Syntaxe SQL standard + commit automatique                                                               |
| 3. Créer des fonctions dédiées                      | `initialiser_db`, `faire_reservation`, `lister_reservations`                                            |
| 4. Lancer des tests via `main_db.py`                | Pour insérer et afficher les réservations persistées en BDD                                             |

---

## ✅ Bibliothèque utilisée

| Librairie      | Utilité                            | Installation         |
|----------------|------------------------------------|----------------------|
| `sqlite3`      | Gestion de BDD légère embarquée     | ✅ incluse dans Python |

---

## 🧠 Résultat pédagogique attendu

- Comprendre les **bases du modèle relationnel** (clés, relations, types de colonnes)
- Introduire le **SQL dans un projet Python** structuré
- Passer d’un **stockage fichier** à un **stockage structuré et interrogeable**
- Acquérir des bases pour aller vers **SQLAlchemy** ou des bases serveurs (PostgreSQL, MySQL)

---
