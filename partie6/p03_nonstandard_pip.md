# 📦 `pip` et les bibliothèques tierces en Python

## 🔧 Qu’est-ce que `pip` ?

`pip` est le **gestionnaire de paquets de Python**.  
Il permet d’**installer, désinstaller, mettre à jour** des bibliothèques depuis le dépôt [PyPI](https://pypi.org/), la “place de marché” officielle des packages Python.

---

## 💡 Commandes essentielles

```bash
pip install nom_du_module        # installation
pip uninstall nom_du_module      # désinstallation
pip install -U nom_du_module     # mise à jour
pip list                         # voir tous les paquets installés
pip freeze > requirements_ok.txt    # exporter les dépendances
pip install -r requirements_ok.txt  # installer depuis un fichier
```

> 🔎 Il est recommandé de travailler dans un **environnement virtuel** (`venv`) pour isoler tes projets.

---

## ✅ Bibliothèques populaires et simples à utiliser

### 📊 Traitement et analyse de données
| Nom       | Pour quoi faire                         | Commande |
|-----------|------------------------------------------|----------|
| `pandas`  | Manipulation de tableaux, CSV, Excel... | `pip install pandas` |
| `numpy`   | Calculs numériques, matrices             | `pip install numpy` |
| `openpyxl`| Lire/écrire des fichiers Excel           | `pip install openpyxl` |

---

### 📈 Visualisation
| Nom         | Pour quoi faire                          | Commande |
|-------------|-------------------------------------------|----------|
| `matplotlib`| Courbes, graphiques                      | `pip install matplotlib` |
| `seaborn`   | Visualisation statistiques esthétique    | `pip install seaborn` |
| `plotly`    | Graphiques interactifs web               | `pip install plotly` |

---

### 🌐 Web & APIs
| Nom          | Pour quoi faire                      | Commande |
|--------------|---------------------------------------|----------|
| `requests`   | Requêtes HTTP/REST                   | `pip install requests` |
| `beautifulsoup4` | Parsing HTML                     | `pip install beautifulsoup4` |
| `flask`      | Micro framework web                  | `pip install flask` |

---

### 🛠️ Développement général
| Nom         | Pour quoi faire                         | Commande |
|-------------|------------------------------------------|----------|
| `rich`      | Affichage terminal (tables, couleurs)   | `pip install rich` |
| `typer`     | CLIs ergonomiques avec auto-doc         | `pip install typer` |
| `loguru`    | Logging moderne et lisible              | `pip install loguru` |

---

### 🎨 Divers utiles
| Nom           | Pour quoi faire                     | Commande |
|---------------|--------------------------------------|----------|
| `python-dotenv`| Charger des variables `.env`        | `pip install python-dotenv` |
| `faker`        | Générer de fausses données          | `pip install faker` |
| `pyfiglet`     | ASCII art                           | `pip install pyfiglet` |

