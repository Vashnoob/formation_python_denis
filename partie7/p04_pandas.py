import json

import pandas as pd


df = pd.read_csv("../data/trajets_realistes.csv",sep=";")

print(df.head(10))
print(df.info())
print(df.describe())

# pip install openpyxl
df.to_excel("trajets_realistes.xlsx", index=False)

##un json
with open("../data/systeme.json", "r") as f:
    resas = json.load(f)

rows = []
for user_block in resas:
    user = user_block["user"]
    for res in user_block["reservations"]:
        rows.append({
            "user": user,
            "depart": res["depart"],
            "arrivee": res["arrivee"],
            "distance": res["distance"]
        })

df = pd.DataFrame(rows)
print(df.head())


## ---
df = pd.read_json("../data/systeme.json")

df_ex = df.explode("reservations")
df_dict = df_ex.to_dict(orient="records")

# "Exploser" les réservations imbriquées
df_flat = pd.json_normalize(df_dict,
                            record_path=None,
                            meta=["user"],
                            record_prefix="",
                            errors='ignore')

print("----------DF FLAT-----------------")

#renomme les colonnes
df_flat.rename(columns={"reservations.depart": "depart"}, inplace=True)
df_flat.rename(columns={"reservations.arrivee": "arrivee"}, inplace=True)
df_flat.rename(columns={"reservations.distance": "distance"}, inplace=True)


# Distance par user
distances = df_flat.groupby("user")["distance"].sum().reset_index()
sdistances = distances.sort_values("distance", ascending=False)
print(sdistances)

#nbre de resa / user  , le meme user sur plusieurs lignes
nbresa = df_flat["user"].value_counts().reset_index(name="nombre_de_reservations")
print(nbresa)


# nbre fois un trajet est reserve
nbresas = df_flat.groupby(["depart", "arrivee"]).size().reset_index(name="nb_reservations")
print(nbresas)


#comparer
comp = df_flat.groupby("user").agg(
    nombre=("distance", "count"),
    total_km=("distance", "sum"),
    moyenne_km=("distance", "mean")
).reset_index()

print(comp)


s450 = comp[comp["moyenne_km"] > 450]
print(s450)