# 🎯 Application 
Créer une application de gestion de trajets et réservations **modulaire, persistante et visualisable**, en exploitant progressivement les bibliothèques Python pertinentes.

## 🧩 Étape 1 — 📚 Standard Library uniquement

### Objectifs :
- Lire/écrire les données en JSON
- Utiliser `datetime`, `pathlib`, `json`, `collections`, `logging`

### 💼 Tâches :
1. Ajouter une date de réservation (`datetime.now()`) pour chaque réservation utilisateur.
2. Sauvegarder les réservations dans un fichier `.json` à l’aide de `json` et `pathlib`.
3. Logger toutes les actions importantes (`reservation`, `ajout`, `erreur`) avec le module `logging`.
4. Compter le nombre de trajets réservés par destination (`collections.Counter`).

---

## 📁 Organisation recommandée :

```
/trajets/
│
├── main.py
├── data/
│   └── reservations.json
├── models/
│   ├── utilisateur.py
│   ├── trajet.py
├── services/
│   ├── export.py
│   ├── visualisation.py
│   └── analyse.py
├── cli.py  ← interface avec typer
├── logs/
│   └── actions.log
```

---

## 🧩 Étape 2 — 📊 Traitement des données avec `pandas`

### Objectifs :
- Analyser les trajets réservés
- Générer un tableau synthétique des réservations

### 💼 Tâches :
1. Exporter les réservations dans un `DataFrame`.
2. Grouper les réservations par utilisateur ou destination.
3. Sauvegarder une version Excel des données avec `df.to_excel()`.

### 📦 Bibliothèques :
```bash
pip install pandas openpyxl
```

---

## 🧩 Étape 3 — 📈 Visualisation avec `matplotlib` ou `plotly`

### Objectifs :
- Représenter visuellement les données (histogramme, courbe, camembert)

### 💼 Tâches :
1. Afficher un camembert des types de trajets (`normal`, `express`)
2. Tracer un histogramme des trajets réservés par utilisateur

### 📦 Bibliothèques :
```bash
pip install matplotlib seaborn
```

---

## 🧩 Étape 4 — 🎨 Terminal UX avec `rich` ou `typer`

### Objectifs :
- Améliorer l’ergonomie CLI
- Ajouter des menus, des couleurs, des tableaux

### 💼 Tâches :
1. Afficher les réservations dans un tableau stylisé (`rich.table`)
2. Ajouter une CLI pour faire : `python app.py reserver --user Alice --type express ...`

### 📦 Bibliothèques :
```bash
pip install rich typer
```

---

## 🧩 Étape 5 — 🔄 Export et automatisation

### Objectifs :
- Export en PDF ou CSV
- Préparer un script réutilisable pour automatiser tout le traitement

### 📦 Suggestions :
- `csv` (stdlib)
- `jinja2` + `weasyprint` pour PDF (ou `fpdf` / `reportlab`)

---
