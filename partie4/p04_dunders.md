# Les méthodes spéciales (`__dunder__` methods)

En Python, les **méthodes spéciales** sont des méthodes entourées de doubles underscores (`__`), aussi appelées *dunder methods* (pour *Double UNDERscore*). Elles permettent de **définir le comportement de vos objets avec les opérateurs intégrés**, les fonctions natives (`len()`, `str()`, etc.), ou les protocoles comme l’itération ou l’indexation.

> Elles rendent vos objets *"pythoniques"* : on les manipule comme des objets natifs.

---

### 🔹 Exemple 1 : `__init__` – Initialisation

Méthode appelée automatiquement lors de la création d’un objet.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)  # Appelle __init__
```

---

### 🔹 Exemple 2 : `__str__` et `__repr__` – Représentation en texte

- `__str__` → Ce que voit l’utilisateur (`print()`)
- `__repr__` → Ce que voit le développeur (`repr()`, console interactive)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point en ({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(1, 2)
print(p)        # Point en (1, 2)
print(repr(p))  # Point(1, 2)
```

---

### 🔹 Exemple 3 : `__eq__` – Comparaison avec `==`

Définit la logique de comparaison entre objets.

```python
class Utilisateur:
    def __init__(self, identifiant):
        self.identifiant = identifiant

    def __eq__(self, autre):
        return self.identifiant == autre.identifiant

u1 = Utilisateur("abc123")
u2 = Utilisateur("abc123")
print(u1 == u2)  # True
```

---

### 🔹 Exemple 4 : `__len__` – Longueur avec `len()`

Utile pour simuler des collections ou des contenants.

```python
class Groupe:
    def __init__(self, membres):
        self.membres = membres

    def __len__(self):
        return len(self.membres)

g = Groupe(["Alice", "Bob", "Charlie"])
print(len(g))  # 3
```

---

### 🔹 Exemple 5 : `__getitem__` et `__setitem__` – Accès par indice

Ces méthodes permettent de rendre votre objet *indexable*, comme une liste ou un dictionnaire.

```python
class MonDictionnaire:
    def __init__(self):
        self._donnees = {}

    def __getitem__(self, cle):
        return self._donnees[cle]

    def __setitem__(self, cle, valeur):
        self._donnees[cle] = valeur

d = MonDictionnaire()
d["a"] = 10
print(d["a"])  # 10
```

---

### 🔹 Exemple 6 : `__call__` – Objet appelable comme une fonction

Avec `__call__`, une instance devient utilisable comme une fonction.

```python
class Multiplieur:
    def __init__(self, facteur):
        self.facteur = facteur

    def __call__(self, valeur):
        return valeur * self.facteur

double = Multiplieur(2)
print(double(5))  # 10
```

---

### 🔹 Exemple 7 : `__iter__` et `__next__` – Rendre une classe itérable

Permet d'utiliser `for` sur votre objet.

```python
class Compteur:
    def __init__(self, maximum):
        self.max = maximum
        self.valeur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.valeur < self.max:
            self.valeur += 1
            return self.valeur
        raise StopIteration

for i in Compteur(3):
    print(i)  # 1, 2, 3
```
