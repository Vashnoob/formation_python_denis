
# 🐍 Mini-guide – Spécificités du modèle objet Python

## 1. Les particularités du modèle objet de Python
- Python est un langage **orienté objet dynamique**.
- **Tout est objet**, même les fonctions et les classes.
- L’objet est très souple : on peut ajouter ou modifier ses attributs dynamiquement.

> 🔍 *Dans le projet : `Utilisateur`, `Trajet`, `TrajetExpress`, `SystemeReservation` sont tous des objets instanciables.*

---

## 2. L’écriture de classes et leur instanciation
```python
class Trajet:
    def __init__(self, depart, arrivee, distance):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance

t = Trajet("Paris", "Lyon", 460)
```
> 🔧 *Instanciation avec des arguments, stockage dans des listes (`self.trajets`).*

---

## 3. Les constructeurs et les destructeurs
- `__init__` : constructeur
- `__del__` : destructeur (peu utilisé en pratique)
```python
class Exemple:
    def __init__(self):
        print("Objet créé")
    def __del__(self):
        print("Objet supprimé")
```

> 📦 *Utilisé dans toutes les classes (`__init__`). Le destructeur n’est pas nécessaire ici.*

---

## 4. La protection d’accès des attributs et des méthodes
- Python n’a pas de mots-clés `private`/`protected`, mais utilise :
  - `_attribut` : convention pour usage interne
  - `__attribut` : pseudo-privé (name mangling)
```python
self._interne  # convention
self.__secret  # name mangling
```

> 🔐 *Dans le projet, les attributs sont publics par simplicité, mais on pourrait protéger `reservations`.*

---

## 5. La nécessité du paramètre `self`
- `self` représente l’**instance courante de la classe**
- Obligatoire comme premier paramètre dans les méthodes d’instance

```python
def afficher(self):
    print(self.depart)
```

> 🧠 *Utilisé dans toutes les méthodes (`afficher()`, `reserver()`, etc.)*

---

## 6. L’héritage simple, multiple et le polymorphisme
- Héritage simple :
```python
class TrajetExpress(Trajet):
    def calculer_duree(self):
        return self.distance / 150
```
- Héritage multiple :
```python
class A: pass
class B: pass
class C(A, B): pass
```
- Polymorphisme : mêmes méthodes, comportements différents

> 🧬 *Dans le projet : `TrajetExpress` hérite de `Trajet` et redéfinit `calculer_duree()`.*

---

## 7. Notions de visibilité
- Python repose sur les **conventions** de visibilité :
  - Public : `trajet.depart`
  - Interne : `_variable`
  - Privé (limité) : `__variable`

> 👁 *Pas de protection stricte comme en Java ou C++.*

---

## 8. Les méthodes spéciales (`__str__`, `__repr__`, etc.)
- Permettent de personnaliser le comportement des objets natifs
```python
def __str__(self):
    return f"{self.depart} -> {self.arrivee}"
```

> ✨ *On pourrait améliorer l’affichage des trajets avec `__str__()`.*

---

## 9. L’introspection
- Permet de **consulter dynamiquement les attributs et méthodes**
```python
print(dir(objet))
print(type(objet))
print(hasattr(objet, "afficher"))
```

> 🔎 *Utile pour le débogage ou l’auto-analyse (non utilisé ici, mais intéressant à montrer).*

---

## 10. L’implémentation des interfaces
- Utilisation du module `abc` et `@abstractmethod`
```python
from abc import ABC, abstractmethod

class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass
```

> 📋 *Dans le projet, `Affichable` impose à `Trajet` et `Utilisateur` d’implémenter `afficher()`.*
  bn 
