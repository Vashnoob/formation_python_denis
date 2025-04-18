# 🏭 Exemple : Fabrique d’objets Document

### 🎯 Objectif :
Créer des documents de types différents (`PDF`, `Word`, `HTML`) sans exposer la logique de construction à l’utilisateur.

---

### ✅ Définition des classes

```python
class Document:
    def afficher(self):
        raise NotImplementedError("Cette méthode doit être redéfinie.")

class PDF(Document):
    def afficher(self):
        print("Affichage d'un document PDF")

class Word(Document):
    def afficher(self):
        print("Affichage d'un document Word")

class HTML(Document):
    def afficher(self):
        print("Affichage d'un document HTML")
```

---

### 🏗️ La Factory

```python
class DocumentFactory:
    @staticmethod
    def creer_document(type_):
        type_ = type_.lower()
        if type_ == "pdf":
            return PDF()
        elif type_ == "word":
            return Word()
        elif type_ == "htmlpdf":
            return HTML()
        else:
            raise ValueError(f"Type inconnu : {type_}")
```

---

### 🧪 Utilisation

```python
doc1 = DocumentFactory.creer_document("pdf")
doc2 = DocumentFactory.creer_document("htmlpdf")

doc1.afficher()  # ➜ Affichage d'un document PDF
doc2.afficher()  # ➜ Affichage d'un document HTML
```

---

## 🧠 Ce que montre cet exemple :
- La **séparation des responsabilités** : la fabrique sait **quoi créer**, les objets savent **quoi faire**.
- Une **extensibilité facile** : ajouter un nouveau type `Markdown` ne nécessite pas de changer l’appel côté utilisateur.
- Python permet aussi une version encore plus courte avec un **dictionnaire de classes**, si tu veux la voir je peux te la proposer aussi.
