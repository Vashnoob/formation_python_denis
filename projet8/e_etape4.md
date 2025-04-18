## 🧩 Étape 4 — Interface terminale avec typer et affichage avec rich

## 🎯 Objectif
Permettre d’interagir avec l’application en **ligne de commande (CLI)**, avec une interface agréable et moderne :
- Réserver un trajet
- Lister les réservations
- Lancer une analyse
- Afficher des graphiques

---

## 📁 Fichiers impactés ou ajoutés — Étape 4

| Fichier                                              | Rôle / Ce qu’il contient                                                                                   | Priorité |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------|
| `cli.py`                                             | 💡 Nouveau point d’entrée CLI basé sur `typer`                                                              | 🟢 Clé   |
|                                                      | - Commande `reserver` : ajoute une réservation (normal/express)                                             |
|                                                      | - Commande `lister` : affiche les réservations dans un tableau `rich`                                       |
|                                                      | - Commande `analyser` : relance l’analyse `pandas`                                                          |
|                                                      | - Commande `graphique` : affiche les graphiques matplotlib                                                  |
| `pyproject.toml` (modifié)                          | Ajout des dépendances externes nécessaires à cette interface (`typer`, `rich`, etc.)                       | 🟢 Clé   |

---

## 🔧 A faire dans cette étape

| Action                                               | Détail technique                                                                                         |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1. Créer `cli.py` à la racine du projet              | Contient toutes les commandes CLI gérées par `@app.command()`                                             |
| 2. Utiliser `typer.Typer()` pour créer un CLI propre | Chaque commande est une fonction Python (très lisible et maintenable)                                     |
| 3. Utiliser `rich.table.Table` et `rich.console.Console` | Pour afficher les données dans le terminal avec style                                                    |
| 4. Tester les 4 commandes                            | `reserver`, `lister`, `analyser`, `graphique`                                                             |
| 5. Mettre à jour `pyproject.toml`                    | Ajouter : `typer[all]`, `rich`, `pandas`, `openpyxl`, `matplotlib`                                        |

---

## ✅ Commandes CLI disponibles

| Commande                       | Description                                                             |
|--------------------------------|--------------------------------------------------------------------------|
| `reserver`                     | Ajoute une réservation pour un utilisateur donné                        |
| `lister`                       | Affiche toutes les réservations sous forme de tableau stylisé           |
| `analyser`                     | Lance l’analyse des données et l’export Excel (via `pandas`)            |
| `graphique`                    | Affiche les graphiques interactifs (histogramme, camembert)             |

---

## 🧠 Grace à cette étape

- Comprendre la structure d’un CLI moderne avec `typer`
- Expérimenter des interactions riches dans le terminal (`rich`)
- Enrichir un projet Python sans interface graphique lourde

---