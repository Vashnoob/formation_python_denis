## 🧩 Étape 8 — Packaging du projet avec `setuptools` et `poetry`

## 🎯 Objectif

Préparer le projet pour :
- une **distribution** (`.whl`, `.tar.gz`)
- une **installation facile** (`pip install .`)
- une **publication potentielle** sur PyPI
- un usage dans d'autres environnements ou projets

---

## 📁 Fichiers ajoutés — Étape 8

| Fichier / Dossier                         | Rôle / Contenu                                                               | Priorité |
|------------------------------------------|------------------------------------------------------------------------------|----------|
| `setup.cfg`                              | 📦 Configuration déclarative du projet pour `setuptools`                    | 🟢 Clé   |
|                                          | - métadonnées, dépendances, version                                          |          |
| `setup.py`                               | Script de lancement `setuptools.setup()`                                    | 🟢 Clé   |
| `pyproject_poetry.toml`                  | Déclaration complète du projet avec `Poetry`                                | 🟢 Clé   |
|                                          | - gère dépendances, build, version, auteurs                                 |          |

---

## 🔧 A faire dans cette étape

### 📦 Pour `setuptools` (méthode classique)
```bash
pip install .
python setup.py sdist bdist_wheel
```

### 📦 Pour `poetry` (méthode moderne)
```bash
poetry install
poetry build
poetry run python projet8/main.py
```

> ⚠️ Il faut renommer `pyproject_poetry.toml` → `pyproject.toml` pour activer le mode `poetry`.

---

## ⚙️ Différences clés entre setuptools et poetry

| Aspect                | `setuptools`                    | `poetry`                             |
|-----------------------|----------------------------------|--------------------------------------|
| Format historique     | ✅ Standard PyPI                 | ⚠️ Plus complexe à configurer        |
| Format moderne        | ⚠️ Moins ergonomique             | ✅ Interface intuitive                |
| Gestion dépendances   | Manuelle via `install_requires` | Automatique + fichiers lockés        |
| Build                 | `setup.py` + `setup.cfg`        | `pyproject.toml` + `poetry build`    |
| Publication PyPI      | Compatible                      | Compatible et plus simple            |

---

## 🧠 Résultat pédagogique attendu

- Savoir structurer un projet Python pour distribution
- Comprendre les différents outils de packaging
- Pouvoir livrer, publier ou installer un projet proprement

