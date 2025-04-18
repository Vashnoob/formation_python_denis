
# pip install faker geopy

import json
import random
from faker import Faker
from geopy.distance import geodesic

# Créer un générateur Faker en français
fakers = [
    Faker("fr_FR"),     # Français
    Faker("fr_CA"),     # Francophone alternatif
    Faker("de_DE"),     # Allemand
    Faker("it_IT"),     # Italien
    Faker("es_CA")
]


# Liste de villes avec coordonnées (villes majeures en France)
villes = {
    "Paris": (48.8566, 2.3522),
    "Lyon": (45.7640, 4.8357),
    "Marseille": (43.2965, 5.3698),
    "Toulouse": (43.6047, 1.4442),
    "Nice": (43.7102, 7.2620),
    "Bordeaux": (44.8378, -0.5792),
    "Lille": (50.6292, 3.0573),
    "Nantes": (47.2184, -1.5536),
    "Strasbourg": (48.5734, 7.7521),
    "Rennes": (48.1173, -1.6778)
}

# Générer une distance réaliste entre deux villes
def distance_km(v1, v2):
    return round(geodesic(villes[v1], villes[v2]).km, 1)

# Générer des utilisateurs avec réservations
def generate_reservations(nb_users=5, nb_reservations=2):
    data = []
    for _ in range(nb_users):
        fake = random.choices(
            population=fakers,
            weights=[5, 1, 1, 1,1],  # majoritairement français
            k=1
        )[0]
        user = fake.first_name()
        reservations = []
        ra = random.randint(2,nb_reservations)
        for _ in range(2,nb_reservations):
            dep, arr = random.sample(list(villes.keys()), 2)
            dist = distance_km(dep, arr)
            reservations.append({
                "depart": dep,
                "arrivee": arr,
                "distance": dist
            })
        data.append({
            "user": user,
            "reservations": reservations
        })
    return data

# Génération et écriture dans un fichier JSON
if __name__ == "__main__":
    fake_data = generate_reservations(nb_users=40, nb_reservations=6)
    with open("reservations_fake.json", "w", encoding="utf-8") as f:
        json.dump(fake_data, f, indent=4, ensure_ascii=False)
    print("✅ Fichier 'reservations_fake.json' généré avec succès.")
    from faker.config import AVAILABLE_LOCALES

    print(sorted(AVAILABLE_LOCALES))