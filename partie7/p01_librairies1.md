## Librairies Python utiles 

---

### 🧠 1. `more-itertools`
**Pourquoi c’est puissant :**  
C’est la version "boostée" de `itertools`, avec plein de fonctions pratiques pour manipuler les itérateurs sans écrire de code complexe.

**Exemples utiles :**
- `chunked(iterable, n)` → découpe un itérable en morceaux de taille `n`.
- `first_true(iterable, pred)` → retourne le premier élément qui valide une condition.

**Use case typique :**
Transformer ou filtrer efficacement des flux de données.

---

### 🔍 2. `pydash`
**Pourquoi c’est puissant :**  
Une sorte de Lodash (JavaScript) pour Python. Fournit des outils fonctionnels puissants pour manipuler des listes, dictionnaires, objets, etc.

**Exemples utiles :**
- `py_.get(data, 'key.subkey')` → accède à une clé imbriquée sans `try/except`.
- `py_.flatten_deep(liste)` → aplatit une structure imbriquée.

**Use case typique :**
Nettoyage ou manipulation de données complexes.

---

### 📚 3. `boltons`
**Pourquoi c’est puissant :**  
Une collection de petits utilitaires standardisés et fiables pour les développeurs : structures de données, gestion de temps, fichiers, etc.

**Exemples utiles :**
- `boltons.iterutils.chunked()`
- `boltons.dictutils.OrderedMultiDict`

**Use case typique :**
Remplacer des outils maison peu robustes avec des utilitaires stables.

---

### ⏱ 4. `humanize`
**Pourquoi c’est puissant :**  
Transforme les valeurs numériques ou temporelles en formats lisibles par les humains.

**Exemples utiles :**
```python
import humanize
humanize.naturaltime(datetime.now() - timedelta(hours=2))
# → '2 hours ago'
```

**Use case typique :**
Affichage de logs, temps, tailles de fichiers de manière conviviale.

---

### 🧬 5. `funcy`
**Pourquoi c’est puissant :**  
Librairie de programmation fonctionnelle avec des décorateurs puissants, des helpers pour manipuler des séquences, des objets, etc.

**Exemples utiles :**
- `@memoize` → mémoïsation automatique
- `walk_keys`, `walk_values` → transforme récursivement des dictionnaires

**Use case typique :**
Optimiser le code fonctionnel ou améliorer la lisibilité.

---

### 💬 6. `rich` (de plus en plus connue, mais encore sous-utilisée)
**Pourquoi c’est puissant :**  
Pour des **affichages en console ultra-visuels** : tableaux, logs colorés, progress bars, markdown…

**Exemple rapide :**
```python
from rich import print
print("[bold magenta]Hello[/bold magenta] World!")
```

**Use case typique :**
Debugging élégant, CLI plus sexy, logs dynamiques.

---

### 🧵 7. `loguru`
**Pourquoi c’est puissant :**  
Un remplacement moderne du module `logging` de Python, ultra-simple et puissant.

**Exemples utiles :**
- Logging en couleur, avec des handlers simples
- Rotation automatique de fichiers de logs

**Use case typique :**
Logger sans se prendre la tête.

---

### 📏 8. `shapely` (si tu fais du traitement géospatial)
**Pourquoi c’est puissant :**  
Manipule des objets géométriques (polygones, lignes, points…) de manière ultra intuitive.

**Use case typique :**
Calculer des intersections de zones, créer des buffers, etc.

---

### 🔢 9. `sympy`
**Pourquoi c’est puissant :**  
Permet de faire du **calcul symbolique**, comme avec Mathematica.

**Exemples :**
- Simplifier une expression
- Calculer des dérivées, primitives
- Résoudre des équations

---

### 🔬 10. `hypothesis`
**Pourquoi c’est puissant :**  
Librairie de **test basé sur les propriétés** (property-based testing). Elle génère automatiquement des cas de test à partir de règles.

**Use case typique :**
Tester des fonctions pour toutes les valeurs possibles, au lieu d’écrire des cas à la main.

---
