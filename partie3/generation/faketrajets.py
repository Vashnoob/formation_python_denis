import csv
import json
import random

VILLES_FRANCE = [
    "Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille",
    "Rennes", "Reims", "Le Havre", "Saint-Étienne", "Toulon", "Grenoble", "Dijon", "Angers", "Nîmes", "Villeurbanne"
]

# Table de distances réalistes (extrait, distances approximatives en km)
DISTANCES = {
    ("Paris", "Lyon"): 465, ("Paris", "Marseille"): 775, ("Paris", "Toulouse"): 680,
    ("Paris", "Nice"): 930, ("Paris", "Nantes"): 385, ("Paris", "Bordeaux"): 580,
    ("Paris", "Lille"): 225, ("Paris", "Strasbourg"): 490, ("Paris", "Rennes"): 350,
    ("Lyon", "Marseille"): 315, ("Lyon", "Toulouse"): 540, ("Lyon", "Nice"): 470,
    ("Lyon", "Bordeaux"): 555, ("Lyon", "Nantes"): 670, ("Marseille", "Toulouse"): 400,
    ("Marseille", "Nice"): 200, ("Toulouse", "Bordeaux"): 245, ("Nantes", "Bordeaux"): 335,
    ("Lille", "Strasbourg"): 520, ("Strasbourg", "Nice"): 790
}

# Compléter avec les inverses
for (a, b), d in list(DISTANCES.items()):
    DISTANCES[(b, a)] = d

def generer_trajets(file, nb_trajets=100):
    trajets = []
    for _ in range(nb_trajets):
        depart, arrivee = random.sample(VILLES_FRANCE, 2)
        distance = DISTANCES.get((depart, arrivee))
        if distance is None:
            # Si pas dans la table, on met une distance plausible simulée
            distance = int(round(random.uniform(100, 900), 1))
        trajets.append([depart, arrivee, distance])

    generer_trajets_csv(file+".csv", trajets)
    generer_trajets_json(file + ".json", trajets)

def generer_trajets_csv(fichier_csv, trajets):
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f,dialect='excel',delimiter = ";",
            quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['depart', 'arrivee', 'distance_km'])

        for trajet in trajets:
            writer.writerow(trajet)

def generer_trajets_json(fichier_json, trajets):
    tjson = []
    for t in trajets:
        tjson.append({
            "depart": t[0],
            "arrivee": t[1],
            "distance": t[2]
        })
        with open(fichier_json, 'w', encoding='utf-8') as f:
            json.dump(tjson, f, indent=2, ensure_ascii=False)

# Exemple
if __name__ == "__main__":
    generer_trajets("../../data/trajets_realistes", nb_trajets=200)