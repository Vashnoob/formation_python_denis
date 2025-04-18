
## 🧠 Objectif du pattern Strategy

- Séparer le **comportement de calcul de durée** du trajet de sa structure.
- Permettre à un même objet `Trajet` de **changer dynamiquement sa logique** de calcul.

---

## 🧱 Étape 1 : Définir des stratégies

```python
# fichier : strategies.py

class StrategieDuree:
    def calculer(self, distance):
        raise NotImplementedError

class DureeNormale(StrategieDuree):
    def calculer(self, distance):
        return distance / 80

class DureeRapide(StrategieDuree):
    def calculer(self, distance):
        return distance / 150

class DureeEco(StrategieDuree):
    def calculer(self, distance):
        return distance / 50
```

---

## 🧱 Étape 2 : L’objet `TrajetAvecStrategie`

```python
# fichier : trajet_strategy.py

from affichable import Affichable

class TrajetAvecStrategie(Affichable):
    def __init__(self, depart, arrivee, distance, strategie_duree):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance
        self.strategie_duree = strategie_duree  # 👈 injection de stratégie

    def calculer_duree(self):
        return self.strategie_duree.calculer(self.distance)

    def afficher(self):
        print(f"{self.depart} → {self.arrivee} ({self.distance} km, durée estimée : {self.calculer_duree():.1f} h)")
```

---

## 🧪 Étape 3 : Utilisation

```python
from strategies import DureeNormale, DureeRapide
from trajet_strategy import TrajetAvecStrategie

t1 = TrajetAvecStrategie("Paris", "Lyon", 460, DureeNormale())
t2 = TrajetAvecStrategie("Paris", "Marseille", 750, DureeRapide())

t1.afficher()  # ➜ Paris → Lyon (460 km, durée estimée : 5.8 h)
t2.afficher()  # ➜ Paris → Marseille (750 km, durée estimée : 5.0 h)
```

---

## ✅ Avantages

- Le trajet **ne gère plus la logique de durée lui-même**.
- Tu peux changer de stratégie à la volée : `t1.strategie_duree = DureeEco()`
- Prépare bien une **généralisation pour une logique dynamique** (profil utilisateur, météo, type de transport...).

---