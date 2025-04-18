## 🧩 Étape 3 — Visualisation graphique avec matplotlib

## 🎯 Objectif
Ajouter une **visualisation interactive** des données via des **graphiques matplotlib** :
- Histogramme du nombre de réservations par utilisateur
- Camembert de la répartition des types de trajets (`Trajet`, `TrajetExpress`)

---

## 📁 Fichiers impactés ou ajoutés — Étape 3

| Fichier                                              | Rôle / Ce qu’il contient                                                                                   | Priorité |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------|
| `services/visualisation.py`                         | 💡 Nouveau module pour les graphiques                                                                       | 🟢 Clé   |
|                                                      | - Fonction `afficher_histogramme_utilisateurs()` : barres verticales par utilisateur                        |          |
|                                                      | - Fonction `afficher_camembert_types()` : camembert des types de trajets                                    |          |
| `main.py` (modifié)                                 | Ajout des appels aux fonctions `afficher_*()` à la fin de `main()`                                          | 🟢 Clé   |

---

## 🔧 A faire dans cette étape

| Action                                                    | Détail technique                                                                                         |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1. Créer `visualisation.py`                               | Contient deux fonctions de plotting `matplotlib.pyplot`                                                  |
| 2. Charger les utilisateurs avec `charger()`              | Extraire les données nécessaires (nombre de réservations, types de trajets)                             |
| 3. Construire deux graphiques                             | Histogramme avec `plt.bar()`, camembert avec `plt.pie()`                                                 |
| 4. Afficher les graphiques                                | Via `plt.show()` dans chaque fonction                                                                    |
| 5. Modifier `main.py`                                     | Ajouter les appels aux fonctions de visualisation                                                        |

---

## 📦 Dépendance requise

| Bibliothèque     | Pourquoi ?                              | Installation                      |
|------------------|------------------------------------------|-----------------------------------|
| `matplotlib`     | Création de graphiques interactifs       | `pip install matplotlib`          |

---

## 🧠 Grace à cette étape

- Comprendre comment **récupérer des données analysées** pour les visualiser
- Utiliser `matplotlib` avec des **listes simples ou dictionnaires**
- Découvrir la **relation entre données et visualisation**

---
