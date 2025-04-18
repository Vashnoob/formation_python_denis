## 🧩 Étape 1 — Structure et implémentation avec la bibliothèque standard**

| Fichier                                             | Rôle / Ce qu’il contient                                                                                     | Priorité |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------|
| `pyproject.toml`                                    | Métadonnées du projet (nom, version, dépendances éventuelles)                                               | 🟢 Base  |
| `projet7/__init__.py`                               | Initialise le paquet Python                                                                                  | 🟢 Base  |

#### 📦 Modèles (`projet7/models/`)
| Fichier                                             | Rôle / Ce qu’il contient                                                                                     | Priorité |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------|
| `affichable.py`                                     | (facultatif) classe abstraite avec `__str__` générique                                                       | 🟡 Option |
| `trajet.py`                                         | Classe `Trajet` avec `__init__`, `calculer_duree()`, `to_dict()`, `from_dict()`, `__str__`, `afficher()`    | 🟢 Clé   |
| `trajet_express.py`                                 | Classe `TrajetExpress` qui hérite de `Trajet` et redéfinit `calculer_duree()`                               | 🟢 Clé   |
| `utilisateur.py`                                    | Classe `Utilisateur` avec `reserver()`, `to_dict()`, `from_dict()`, `afficher()` + gestion `datetime`       | 🟢 Clé   |

#### ⚙️ Services (`projet7/services/`)
| Fichier                                             | Rôle / Ce qu’il contient                                                                                     | Priorité |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------|
| `persistence.py`                                    | Fonctions `charger()` et `sauvegarder()` des utilisateurs au format JSON (via `pathlib`, `json`)            | 🟢 Clé   |
| `logger.py`                                         | Configuration du logger (fichier `.log`) + fonctions `log_info()`, `log_error()`                            | 🟢 Clé   |

#### 🗃️ Données et journaux
| Fichier / Dossier                                   | Rôle / Ce qu’il contient                                                                                     | Priorité |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------|
| `data/reservations.json`                            | Fichier généré automatiquement à la première exécution avec les données persistées                         | 🔵 Auto  |
| `logs/actions.log`                                  | Fichier généré automatiquement avec les événements importants loggués                                       | 🔵 Auto  |

#### 🚀 Point d’entrée
| Fichier                                             | Rôle / Ce qu’il contient                                                                                     | Priorité |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------|
| `main.py`                                           | Script principal : charge ou crée les utilisateurs, affiche leurs réservations, déclenche logs              | 🟢 Clé   |

---

### ✅ Résumé des actions à faire

1. Implémenter les classes `Trajet`, `TrajetExpress` et `Utilisateur` avec :
   - `__init__`, `__str__`, `to_dict()`, `from_dict()`, `afficher()`
2. Écrire les fonctions de **persistence JSON** dans `services/persistence.py`
3. Configurer un **logger** dans `services/logger.py`
4. Utiliser ces briques dans `main.py` :
   - charger ou initialiser les données
   - réserver des trajets
   - afficher et sauvegarder
   - logguer les actions
