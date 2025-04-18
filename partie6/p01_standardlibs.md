# 📚 La bibliothèque standard Python

## 🧠 Principe général

La **bibliothèque standard** (ou *standard library*) est un ensemble de **modules fournis avec Python**, sans installation externe.  
Elle couvre des dizaines de cas d’usage : fichiers, math, compression, introspection, réseaux, formats de données, POO, web, etc.

> ✅ Elle est **optimisée, maintenue, portable** et bien documentée.

---

## 📦 Où la trouver ?

- Documentation officielle : [docs.python.org/3/library](https://docs.python.org/3/library/)
- Les modules sont importables directement :
```python
import os
import math
import json
```

---

## 🔝 Les modules les plus utilisés (et pourquoi)

| Module        | Usage principal                                       |
|---------------|--------------------------------------------------------|
| `os`, `pathlib` | Interactions avec le système de fichiers             |
| `json`        | Sérialisation de données (écriture/lecture de JSON)   |
| `datetime`    | Manipulation des dates et heures                      |
| `collections` | Structures avancées : `Counter`, `defaultdict`, `deque` |
| `itertools`   | Outils puissants pour les boucles, combinaisons...    |
| `re`          | Expressions régulières                                |
| `random`      | Génération pseudo-aléatoire                           |
| `math`        | Fonctions mathématiques                               |
| `functools`   | Décorateurs, mémoïsation, fonctions partielles        |
| `typing`      | Typage statique, annotations                         |
| `abc`         | Interfaces abstraites (base pour POO avancée)         |
| `logging`     | Gestion fine des logs                                 |
| `argparse`    | Interface en ligne de commande (CLI)                  |

---

## ⚠️ Des modules sous-estimés ou injustement délaissés

| Module           | Pourquoi il mérite plus d’amour 💔                         |
|------------------|------------------------------------------------------------|
| `textwrap`       | Pour formater proprement du texte (indentation, wrapping) |
| `shutil`         | Pour copier, déplacer, compresser facilement des fichiers |
| `pprint`         | Pour afficher des objets complexes de manière lisible     |
| `statistics`     | Moyennes, médianes, écart-types directement                |
| `enum`           | Pour créer des constantes nommées claires                 |
| `dataclasses`    | Création de classes de données avec peu de code (depuis Python 3.7) |
| `contextlib`     | Pour créer des context managers personnalisés             |
| `concurrent.futures` | Pour faire du multithreading ou multiprocessing facilement |
| `copy`           | Pour faire des copies profondes (`deepcopy`)              |

---

## 🧪 Exemples expressifs

### `textwrap`
```python
import textwrap

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
print(textwrap.fill(text, width=40))
```

### `collections.defaultdict`
```python
from collections import defaultdict

notes = defaultdict(list)
notes["math"].append(15)
notes["math"].append(17)
```

### `statistics`
```python
import statistics

data = [10, 20, 20, 30]
print(statistics.mean(data))  # ➜ 20
```

---

## 🧠 Bonnes pratiques

- 📎 Utiliser la stdlib avant de chercher une librairie externe.
- 🔍 Explorer-la avec `help()`, `dir()` et [https://pymotw.com/3/](https://pymotw.com/3/) (Python Module of the Week).
- 🧪 Tester des modules moins connus dans des mini-scripts, tu découvriras des pépites.
