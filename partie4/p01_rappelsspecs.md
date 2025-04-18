
## 🧠 Spécificités du modèle objet Python × Projet de réservation

| Spécificité Python (POO)                              | Explication                                                                 | Exemple dans le projet |
|-------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------|
| **Tout est objet**                                    | En Python, même un entier, une fonction ou une classe est un objet.        | Les instances de `Trajet`, `Utilisateur` sont des objets manipulables, stockés dans des listes. |
| **Attributs dynamiques**                              | Les attributs peuvent être ajoutés à la volée (pas de déclaration obligatoire). | `self.nom`, `self.reservations` sont créés dans `__init__`. |
| **Méthode spéciale `__init__`**                       | Constructeur appelé à chaque instanciation de la classe.                   | Dans `Trajet`, `Utilisateur`, etc. |
| **Pas de typage statique obligatoire**                | Python est dynamiquement typé, pas besoin de déclarer les types à l’avance. | `def reserver(self, trajet)` accepte n’importe quel type (mais attendu `Trajet`). |
| **Encapsulation par convention**                      | `_attribut` = usage interne, `__attribut` = pseudo-privé                    | On n’en a pas utilisé, mais on pourrait dans `Utilisateur.__solde`. |
| **`self` est explicite**                              | L'objet lui-même est passé comme premier paramètre de toutes les méthodes. | `def afficher(self)` dans toutes les classes. |
| **Héritage multiple possible**                        | Python autorise plusieurs superclasses (utilisé avec précaution).          | Non utilisé ici, mais possible : `class Premium(Utilisateur, Payant)`. |
| **Duck Typing**                                       | "Si ça se comporte comme un canard..." : pas besoin d’héritage explicite pour être compatible. | La méthode `afficher()` fonctionne dès qu’elle est définie, peu importe la classe. |
| **Méthodes (dunder) magiques** (`__str__`, `__len__`) | Permettent de customiser le comportement natif des objets.                 | Pas utilisées ici, mais `__str__()` serait utile pour `Trajet`. |
| **Interfaces via ABC**                                | Python ne propose pas de vraies interfaces, mais on peut en simuler avec `ABC`. | `Affichable` impose la méthode `afficher()` à `Trajet`, `Utilisateur`. |
| **Polymorphisme par redéfinition**                    | Une méthode peut être redéfinie dans une classe fille.                     | `TrajetExpress.calculer_duree()` remplace celle de `Trajet`. |
| **Serialisation via dictionnaires**                   | Conversion `obj <=> dict` pour sauvegarder avec JSON.                      | Méthodes `to_dict()` et `from_dict()` dans toutes les classes. |
| **Association forte (composition)**                   | Une classe contient d'autres objets dont elle est responsable.             | `Utilisateur` contient des `Trajet` dans `self.reservations`. |
| **Modularité par fichiers**                           | Python structure les projets avec des modules (`.py`).                     | Fichiers `trajet.py`, `utilisateur.py`, etc. |

---
