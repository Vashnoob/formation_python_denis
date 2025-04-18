### 📄 `README.md`

```markdown
# 🧳 Projet Réservations – Python (GUI + PDF + HTML)

Ce projet lit des réservations utilisateur depuis un fichier JSON, les affiche dans une interface graphique PySide6, et permet une exportation en HTML et PDF.

---

## ✅ Lancer le projet hors de PyCharm

Voici les étapes à suivre pour utiliser ce projet en ligne de commande ou sur une autre machine.

---

### 1. 📥 Installer Python

Télécharger la dernière version sur [python.org](https://www.python.org/downloads/)  
✅ Pendant l'installation, cocher **"Add Python to PATH"**.

---

### 2. 🧭 Ouvrir un terminal

Naviguer dans le dossier du projet :

```bash
cd chemin/vers/mon_projet
```

---

### 3. 🧪 Créer un environnement virtuel

```bash
python -m venv .venv
```

Activer l’environnement :

- **Windows** :
  ```bash
  .venv\Scripts\activate
  ```
- **macOS / Linux** :
  ```bash
  source .venv/bin/activate
  ```

---

### 4. 📦 Installer les dépendances

```bash
pip install -r requirements.txt
```

---

### 4bis. ➕ (Facultatif) Installer une autre librairie

Si tu as besoin d'ajouter une librairie (ex: `pandagui`) :

```bash
pip install pandagui
```

Pour l'ajouter ensuite au projet :

```bash
pip freeze > requirements.txt
```

---

### 5. 🚀 Lancer le projet

Lancer le script de ton choix :

```bash
python gui.py
# ou
python generate_html.py
# ou
python main.py
```

---

### 📁 Structure type du projet

```
mon_projet/
├── gui.py
├── main.py
├── generate_html.py
├── data_utils.py
├── reservations.json
├── templates/
│   └── reservations.html
├── requirements.txt
└── README.md
```

---

### 🧰 Outils utilisés

- [pandas](https://pandas.pydata.org/)
- [jinja2](https://jinja.palletsprojects.com/)
- [weasyprint](https://weasyprint.org/)
- [PySide6](https://doc.qt.io/qtforpython/)
- [pandagui](https://github.com/adamerose/pandagui) *(optionnel)*

