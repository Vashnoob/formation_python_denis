## `NumPy`

1. 👉 Ce qu’est NumPy  
2. 🧠 Pourquoi c’est utile ici  
3. 🔍 Cas concrets : calculs, filtrage, optimisation, statistiques  
4. ✅ Bonnes pratiques

---

## 🧮 1. Qu’est-ce que NumPy ?

**NumPy** est une librairie pour le **calcul numérique** performant en Python. Elle propose :

- Des **tableaux multidimensionnels** (`ndarray`)
- Des **opérations vectorisées** ultra rapides
- Un riche écosystème de fonctions mathématiques, statistiques, linéaires…

---

## 🧭 2. Pourquoi c’est utile pour les trajets/réservations ?

💡 Tu veux sûrement :
- Filtrer des trajets selon une distance ou une durée
- Calculer des temps moyens ou des écarts de retard
- Optimiser un itinéraire (plus court / plus rapide / moins cher)
- Gérer des matrices de distances, de tarifs ou de disponibilités

NumPy = parfait pour ça : rapide, simple à manipuler en masse.

---

## 🚆 3. Exemples concrets

### 🔹 A. Distance entre aéroports (coordonnées GPS)

```python
import numpy as np

# Latitude / Longitude (en degrés) de 3 aéroports
coords = np.array([
    [48.8566, 2.3522],  # Paris
    [51.5074, -0.1278], # Londres
    [41.9028, 12.4964], # Rome
])

# Conversion en radians
r = np.radians(coords)

# Calcul de la matrice de distances (Haversine simplifiée)
def haversine(lat1, lon1, lat2, lon2):
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 6371 * 2 * np.arcsin(np.sqrt(a))  # rayon Terre = 6371 km

distances = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        distances[i, j] = haversine(*r[i], *r[j])

print(np.round(distances, 1))
```

### 🔹 B. Temps moyen de trajet, temps total

```python
# Durée de 5 trajets en minutes
durations = np.array([95, 110, 87, 125, 102])

# Statistiques
print("Durée moyenne :", durations.mean(), "min")
print("Écart-type :", durations.std(), "min")
print("Trajet le plus court :", durations.min(), "min")
```

---

### 🔹 C. Tarifs par classe + filtrage

```python
# Tarifs [classe économique, business, premium éco]
prices = np.array([
    [89, 250, 120],
    [105, 270, 130],
    [95, 260, 125],
])

# Réduction de 10% sur business
prices[:, 1] *= 0.9

# Filtrage des vols à moins de 100€ en éco
eco_cheaps = prices[:, 0] < 100
print("Vols abordables :", eco_cheaps)
```

---

### 🔹 D. Occupation de sièges (binaire) et comptage

```python
# 1 ligne = 1 vol, 1 colonne = 1 siège (1 = réservé, 0 = libre)
seats = np.array([
    [1, 1, 0, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0]
])

# Nombre de sièges réservés par vol
print("Sièges réservés :", seats.sum(axis=1))
```

---

### 🔹 E. Matrice de connexions entre villes

```python
# 0 = pas de vol, >0 = nombre de vols
connections = np.array([
    [0, 3, 2],
    [3, 0, 1],
    [2, 1, 0]
])

# Nombre total de vols
print("Total vols :", connections.sum())
```

---

## ✅ 4. Bonnes pratiques avec NumPy

| Astuce | Description |
|--------|-------------|
| ✅ Utilise `np.array` plutôt que des listes imbriquées |
| 🚀 Préfère les opérations vectorisées (`array + 1`) à des boucles |
| 🧽 Utilise `.reshape()`, `.flatten()`, `.transpose()` pour manipuler facilement |
| 📊 Combine avec `matplotlib`, `pandas`, `polars` pour le rendu et le contexte |
| ⚠️ Attention aux types (`dtype`) si tu travailles avec des entiers ou flottants |

---
