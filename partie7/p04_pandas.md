## `pandas` 

---

## 📦 1. C’est quoi `pandas` ?

**`pandas`** est la **librairie phare de manipulation de données en Python**. Elle repose sur deux structures clés :

- **`DataFrame`** → tableau 2D avec index, colonnes, étiquettes
- **`Series`** → colonne ou série 1D

C’est l’outil de base pour traiter des données **CSV**, **Excel**, **SQL**, etc.

---

## 🎯 2. Pourquoi c’est parfait pour les trajets et réservations ?

Parce que tu vas souvent manipuler :

- des fichiers `flights.csv`, `airports.csv`, `reservations.json`, etc.
- des horaires, des prix, des durées, des statuts
- des jointures (entre aéroports, vols, utilisateurs…)
- des statistiques, tris, regroupements, filtrages

---

## 🚆 3. Exemples concrets sur trajets / réservations

---

### 🔹 A. Charger des données et les explorer

```python
import pandas as pd

df = pd.read_csv("flights.csv")

print(df.head())
print(df.info())
print(df.describe())
```

---

### 🔹 B. Calculer la durée de vol

```python
df["departure"] = pd.to_datetime(df["departure"])
df["arrival"] = pd.to_datetime(df["arrival"])

df["duration"] = (df["arrival"] - df["departure"]).dt.total_seconds() / 60
```

---

### 🔹 C. Filtrer les vols directs entre deux villes

```python
direct_paris_rome = df[
    (df["origin"] == "Paris") &
    (df["destination"] == "Rome") &
    (df["stops"] == 0)
]
```

---

### 🔹 D. Moyenne des retards par compagnie

```python
df["delay"] = df["actual_departure"] - df["scheduled_departure"]
df["delay_min"] = df["delay"].dt.total_seconds() / 60

retards = df.groupby("airline")["delay_min"].mean().sort_values()
```

---

### 🔹 E. Statistiques sur les réservations

```python
reservations = pd.read_json("reservations.json")

# Réservations confirmées par utilisateur
confirmed = reservations[reservations["status"] == "confirmed"]
confirmed_per_user = confirmed.groupby("user_id").size()
```

---

### 🔹 F. Ajouter un tarif total

```python
df["price_total"] = df["price_base"] + df["taxes"] + df["baggage_fee"]
```

---

### 🔹 G. Croiser avec d’autres tables (join)

```python
airports = pd.read_csv("airports.csv")
flights = df.merge(airports, how="left", left_on="origin", right_on="airport_code")
```

---

### 🔹 H. Vols les plus longs ou plus chers

```python
top_durations = df.sort_values("duration", ascending=False).head(5)
top_prices = df.sort_values("price_total", ascending=False).head(5)
```

---

### 🔹 I. Exporter les résultats

```python
df.to_csv("processed_flights.csv", index=False)
```

---

### 🔹 J. Heatmap des départs par heure

```python
df["hour"] = df["departure"].dt.hour
departures_by_hour = df.groupby("hour").size()

departures_by_hour.plot(kind="bar", title="Vols par heure de départ")
```

---

## ✅ 4. Bonnes pratiques avec `pandas`

| Astuce | Description |
|--------|-------------|
| `.copy()` | évite les effets de bord quand tu modifies un sous-ensemble |
| `parse_dates` | utilise `parse_dates=['departure']` dès le `read_csv()` |
| `.isin([...])` | pour filtrer plusieurs valeurs |
| `.loc[]` | pour filtrer proprement avec conditions |
| `pipe()` | pour enchaîner des transformations lisiblement |

