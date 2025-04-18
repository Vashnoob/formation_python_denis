## 🧩 Étape 2 — Analyse des réservations avec pandas

## 🎯 Objectif
Analyser les données de réservation (trajets, distances, utilisateurs) avec la bibliothèque `pandas`, puis les exporter en fichier Excel.

---

## 📁 Organisation des fichiers — Étape 2

| Fichier                                                | Rôle / Contenu                                                                                             | Priorité |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------|
| `services/analyse.py`                                  | 💡 Nouveau module avec la fonction `analyser_reservations()`                                               | 🟢 Clé   |
|                                                        | - Charge les utilisateurs avec `charger()`                                                                 |          |
|                                                        | - Construit un `DataFrame` avec trajets + dates + utilisateurs                                             |          |
|                                                        | - Affiche des stats simples avec `groupby()` et `mean()`                                                   |          |
|                                                        | - Exporte les données dans `data/analyse_reservations.xlsx`                                               |          |
|                                                        |                                                                                                             |          |
| `main.py` (modifié)                                    | Ajout de l’appel à `analyser_reservations()` à la fin du `main()`                                          | 🟢 Clé   |
|                                                        | (le reste reste identique à l’étape 1 : chargement, affichage, sauvegarde)                                |          |
|                                                        |                                                                                                             |          |
| `data/analyse_reservations.xlsx`                       | 📝 Fichier généré automatiquement contenant les données de réservation au format Excel                     | 🔵 Auto  |

---

## 🔧 A faire dans cette étape

| Action                                                   | Détail technique                                                                                        |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1. Ajouter le fichier `analyse.py`                       | Contient toute la logique d'analyse avec `pandas`                                                        |
| 2. Récupérer les données avec `charger()`                | Retourne une liste de `Utilisateur`, utilisée pour remplir un `DataFrame`                                |
| 3. Construire le DataFrame                               | Colonnes : `Nom utilisateur`, `Départ`, `Arrivée`, `Distance`, `Durée`, `Date`, `Type de trajet`        |
| 4. Afficher des analyses                                 | Ex. : nombre de réservations par utilisateur, moyenne distance par type                                  |
| 5. Exporter en `.xlsx`                                   | Sauvegarde du tableau dans `data/analyse_reservations.xlsx` avec `df.to_excel()`                         |
| 6. Modifier `main.py`                                    | Appeler `analyser_reservations()` à la fin du programme                                                  |

---

## 💡 Pré-requis

| Outil        | Pourquoi ?                              | Commande d’installation           |
|--------------|------------------------------------------|-----------------------------------|
| `pandas`     | Création et manipulation de DataFrames   | `pip install pandas`              |
| `openpyxl`   | Sauvegarde en Excel (`.xlsx`)            | `pip install openpyxl`            |

---
