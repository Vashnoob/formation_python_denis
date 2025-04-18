# 🐍 Mini-guide Python - Bases procédurales

## 1. Identifiants et Références
- **Identifiant** : nom d’une variable, fonction, objet.
- **Référence** : en Python, les variables ne contiennent pas de valeur mais une référence vers un objet en mémoire.

## 2. Conventions de Codage et Nommage
- `snake_case` pour variables et fonctions.
- `PascalCase` pour les classes.
- MAJUSCULES pour les constantes.
- Respect du [PEP8](https://peps.python.org/pep-0008/).

## 3. Blocs et Commentaires
- Blocs définis par **indentation** (4 espaces).
- `#` pour un commentaire sur une ligne.
- `"""` ou `'''` pour des commentaires multilignes (docstring).

## 4. Types de Données Disponibles
- **Numériques** : `int`, `float`, `complex`
- **Texte** : `str`
- **Séquences** : `list`, `tuple`, `range`
- **Collections** : `dict`, `set`
- **Booléens** : `bool`
- **Autre** : `NoneType`

## 5. Variables, Affichage Formaté, Portée
- Affectation dynamique : `x = 42`
- Formatage : `f"Bonjour {nom}"`
- Portée :
  - **Locale** : à l’intérieur d’une fonction
  - **Globale** : au niveau du module

## 6. Manipulation des Types
- Opérations numériques : `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Chaînes de caractères :
  - Méthodes : `.lower()`, `.upper()`, `.split()`, `.join()`
  - Accès par indexation et slicing

## 7. Listes, Tuples, Dictionnaires
- **Listes** (`list`) : mutables `[1, 2, 3]`
- **Tuples** (`tuple`) : immuables `(1, 2, 3)`
- **Dictionnaires** (`dict`) : paires clé/valeur `{ "clé": "valeur" }`

## 8. Utilisation des Fichiers
```python
# Lecture
with open("fichier.txt", "r") as f:
    contenu = f.read()

# Écriture
with open("fichier.txt", "w") as f:
    f.write("du texte")
```

## 9. Structures Conditionnelles
```python
if note >= 16:
    mention = "Très bien"
elif note >= 12:
    mention = "Bien"
else:
    mention = "À revoir"
```

## 10. Opérateurs Logiques et de Comparaison
- Comparaison : `==`, `!=`, `<`, `<=`, `>`, `>=`
- Logiques : `and`, `or`, `not`

## 11. Boucles `while` et `for`
```python
for i in range(5):
    print(i)

while condition:
    ...
```

## 12. `break` et `continue`
- `break` : interrompt la boucle.
- `continue` : passe à l’itération suivante.

## 13. La Fonction `range()`
- `range(n)` : de 0 à n-1
- `range(a, b, s)` : de a à b (exclu) par pas de s

## 14. Fonctions et Documentation
```python
def saluer(nom):
    """Affiche un message de salutation."""
    print(f"Bonjour {nom}")
```

## 15. Expressions Lambda
```python
double = lambda x: x * 2
```

## 16. Générateurs
```python
def compte():
    for i in range(3):
        yield i
```

## 17. Structuration en Modules
- Un fichier `.py` = un **module**
- Import :
```python
import mon_module
from mon_module import ma_fonction
```

---
