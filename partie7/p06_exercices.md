# Mini atelier pédagogique

---

## 🎓 Partie 1 – Énoncés

### 🧩 Contexte :
On dispose du fichier `system.json` structuré ainsi :

```json
[
    {
        "user": "Jean-Christophe",
        "reservations": [
            {
                "depart": "Lyon",
                "arrivee": "Bordeaux",
                "distance": 555.0
            }
        ]
    }
]
```
---

### ✅ Objectifs :
- Manipuler des données imbriquées (JSON => tabulaire)
- Maîtriser `DataFrame`, `groupby`, `agg`
- Faire des calculs dérivés simples
- Préparer des données pour visualisation ou reporting

---

### 🧪 Exercices :

#### 🔹 **Exercice 1 : Chargement & transformation**
> À partir du fichier JSON, produire un DataFrame plat avec les colonnes : `user`, `depart`, `arrivee`, `distance`.

---

#### 🔹 **Exercice 2 : Nombre de trajets par utilisateur**
> Calculer le nombre total de trajets effectués par chaque utilisateur.

---

#### 🔹 **Exercice 3 : Distance totale parcourue**
> Ajouter une statistique de **distance totale** par utilisateur.

---

#### 🔹 **Exercice 4 : Détection des trajets les plus longs**
> Repérer les trajets de plus de 600 km. Afficher l’utilisateur et les villes concernées.

---

#### 🔹 **Exercice 5 : Distance moyenne par utilisateur**
> Calculer la **distance moyenne par trajet** pour chaque utilisateur.

---

#### 🔹 **Exercice 6 : Villes les plus fréquentes**
> Extraire la ville la plus souvent utilisée (comme départ **ou** arrivée).

---

#### 🔹 Bonus : Visualisation
> Afficher un **graphe ou une barre** des distances totales par utilisateur.

---

## 🧠 Partie 2 – Corrigé (code avec explications)

```python
import pandas as pd
import json
from collections import Counter

# Chargement
with open("reservations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Transformation (plat)
records = []
for entry in data:
    user = entry["user"]
    for res in entry["reservations"]:
        records.append({
            "user": user,
            "depart": res["depart"],
            "arrivee": res["arrivee"],
            "distance": res["distance"]
        })

df = pd.DataFrame(records)

# Exo 2 : Nombre de trajets par utilisateur
trajets_par_user = df.groupby("user").size().reset_index(name="nb_trajets")

# Exo 3 : Distance totale
distance_totale = df.groupby("user")["distance"].sum().reset_index(name="distance_totale")

# Exo 4 : Trajets > 600 km
longs_trajets = df[df["distance"] > 600][["user", "depart", "arrivee", "distance"]]

# Exo 5 : Moyenne
distance_moyenne = df.groupby("user")["distance"].mean().reset_index(name="distance_moyenne")

# Exo 6 : Ville la plus fréquente
villes = pd.concat([df["depart"], df["arrivee"]])
ville_plus_frequente = Counter(villes).most_common(1)[0]

# Bonus : Graphique
import matplotlib.pyplot as plt

distance_totale.set_index("user").plot(kind="bar", title="Distance totale par utilisateur")
plt.ylabel("Kilomètres")
plt.tight_layout()
plt.show()
```

---

### 📘 Résumé des notions couvertes :

| Notion | Objectif pédagogique |
|--------|----------------------|
| `json.load + boucle` | Déplier un JSON imbriqué |
| `DataFrame` simple | Structuration propre des données |
| `groupby + size/sum/mean` | Statistiques de groupe |
| `concat + Counter` | Comptage multi-sources |
| `plot(kind="bar")` | Premiers pas en data viz |

