## 🧩 Étape 5 — Génération d’un rapport PDF avec HTML (Jinja2) + WeasyPrint

## 🎯 Objectif
Générer un **rapport PDF esthétique et structuré** contenant toutes les réservations des utilisateurs, basé sur un **template HTML personnalisé**.

---

## 📁 Etape 5 - Fichiers ajoutés ou modifiés — Étape 5

| Fichier / Dossier                                    | Rôle / Contenu                                                                                          | Priorité |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------|
| `services/rapport.py`                                | 💡 Nouveau module qui :                                                                                  | 🟢 Clé   |
|                                                      | - charge les utilisateurs                                                                               |          |
|                                                      | - rend un template HTML avec `jinja2`                                                                   |          |
|                                                      | - génère un PDF avec `weasyprint`                                                                       |          |
| `templates/rapport.html`                             | 💡 Nouveau template HTML stylisé                                                                         | 🟢 Clé   |
|                                                      | - utilisé avec Jinja2 pour afficher les trajets et réservations                                          |          |
|                                                      | - CSS embarqué pour mise en page propre                                                                 |          |
| `data/rapport_reservations.pdf`                      | 📄 Fichier généré automatiquement lors de l'exécution de `rapport.py`                                    | 🔵 Auto  |
| `pyproject.toml`                                     | Mise à jour : ajout de `weasyprint` dans la section `dependencies`                                       | 🟢 Clé   |

---

## 🔧 A faire dans cette étape

| Action                                               | Détail technique                                                                                         |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1. Créer un template HTML                            | Structure : `h1`, `table`, `thead`, `tbody`, stylé avec CSS intégré                                       |
| 2. Utiliser `jinja2` pour injecter les données       | `{{ u.nom }}`, `{{ r.trajet.depart }}` etc.                                                              |
| 3. Générer un PDF avec `HTML(string=...).write_pdf()`| Fournie par `weasyprint`, convertit du HTML rendu en PDF                                                  |
| 4. Organiser les fichiers                            | Template dans `templates/`, script dans `services/`, résultat dans `data/`                                |

---

## ✅ Dépendances nécessaires

| Bibliothèque     | Utilité                                 | Installation                    |
|------------------|------------------------------------------|---------------------------------|
| `jinja2`         | Génération de HTML à partir de templates | `pip install jinja2`           |
| `weasyprint`     | Rendu HTML → PDF                         | `pip install weasyprint`       |

> ⚠️ WeasyPrint requiert parfois `libpango`, `cairo` et `gdk-pixbuf` pour fonctionner (souvent préinstallés sur Linux).

---

## 🧠 Grace à cette étape

- Comprendre le rôle de **Jinja2 comme moteur de template** injectant des données Python dans du HTML.
- Découvrir **WeasyPrint** comme outil de génération de PDF hautement stylisé.
- Approcher la **mise en forme de rapports automatisés** dans un vrai projet Python.

---