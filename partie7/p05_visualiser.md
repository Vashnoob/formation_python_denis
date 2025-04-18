---

### 🐍 Script Python `analyse_reservations.py`

```python
import pandas as pd
import json

# 1. Charger les données JSON
with open("reservations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2. Transformer en DataFrame
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

# 3. Afficher les données transformées
print("Données dépliées :")
print(df)

# 4. Statistiques : distance totale par utilisateur
stats = df.groupby("user")["distance"].agg(["count", "sum", "mean"]).reset_index()
stats.columns = ["user", "nb_trajets", "distance_totale_km", "distance_moyenne_km"]

print("\nStatistiques par utilisateur :")
print(stats)
```

---

### ✅ Résultat attendu

```
Données dépliées :
             user     depart   arrivee  distance
0  Jean-Christophe       Lyon  Bordeaux     555.0
1  Jean-Christophe   Bordeaux     Paris     586.0
2           Lucie  Marseille    Nantes     904.0

Statistiques par utilisateur :
             user  nb_trajets  distance_totale_km  distance_moyenne_km
0  Jean-Christophe           2               1141.0               570.5
1           Lucie           1                904.0               904.0
```

---
