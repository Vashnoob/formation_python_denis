# 🐍 Mini-guide Python – Programmation Orientée Objet

## 1. Approche orientée objet
- La POO permet de structurer le code en **objets** combinant données et comportements.
- Elle favorise la **réutilisabilité**, la **modularité**, la **maintenabilité**.

```python
class Chien:
    def aboyer(self):
        print("Woof!")
```

---

## 2. Principes du paradigme objet
- **Abstraction** : modéliser le réel via des objets.
- **Encapsulation** : protéger les données internes.
- **Héritage** : partager le comportement entre classes.
- **Polymorphisme** : un même appel peut produire des effets différents.

---

## 3. Objet = état + comportement + identité
- **État** : les attributs (ex : nom, âge).
- **Comportement** : les méthodes (ex : `parler()`)
- **Identité** : chaque objet est distinct en mémoire.

```python
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom

    def saluer(self):
        print(f"Bonjour {self.nom}")
```

---

## 4. Classe, attributs, méthodes
- Classe : modèle de l’objet.
- Attributs : variables liées à l’objet (`self.attribut`)
- Méthodes : fonctions liées à la classe.

```python
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
```

---

## 5. Encapsulation
- Les attributs peuvent être "protégés" par convention :
  - `_attribut` : usage interne
  - `__attribut` : pseudo-privé (name mangling)

```python
class Coffre:
    def __init__(self):
        self.__code_secret = "1234"  # pseudo-privé
```

---

## 6. Communication entre objets
- Les objets peuvent se passer des références et appeler les méthodes des autres.

```python
class A:
    def action(self):
        print("A agit")

class B:
    def interagir(self, objet_a):
        objet_a.action()
```

---

## 7. Héritage
- Une classe peut hériter d’une autre pour réutiliser ou spécialiser son comportement.

```python
class Animal:
    def parler(self):
        print("Je fais un bruit")

class Chat(Animal):
    def parler(self):
        print("Miaou")
```

---

## 8. Polymorphisme
- Le même appel `obj.parler()` fonctionne avec n’importe quelle sous-classe.

```python
def faire_parler(animal):
    animal.parler()

faire_parler(Chat())
faire_parler(Animal())
```

---

## 9. Association entre classes
- Une classe peut contenir ou utiliser d’autres objets.

```python
class Livre:
    def __init__(self, titre):
        self.titre = titre

class Bibliothèque:
    def __init__(self):
        self.livres = []

    def ajouter(self, livre):
        self.livres.append(livre)
```

---

## 10. Interfaces (protocole ou ABC)
- En Python, on peut utiliser le **duck typing** ou les **classes abstraites** (`abc.ABC`).

```python
from abc import ABC, abstractmethod

class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass
```

---

## 11. UML
- UML est un langage de modélisation :
  - **Classes** : structure des objets
  - **Séquences** : interactions temporelles
  - **Activités** : logique de traitement

💡 Outils : draw.io, Lucidchart, StarUML, plantuml

---

## 12. Diagramme de classe (exemple simple)

```plaintext
+------------------+
|     Chien        |
+------------------+
| - nom: str       |
+------------------+
| + aboyer(): void |
+------------------+
```

---

## 13. Design Patterns (modèles de conception)
- **Singleton** : une seule instance
- **Factory Method** : crée des objets sans exposer la logique
- **Strategy** : interchangeable comportement

```python
# Exemple Singleton
class Unique:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
