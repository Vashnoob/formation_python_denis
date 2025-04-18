
### --- Données simulées : chaque trajet est un tuple (ville_depart, ville_arrivee, distance_km)
trajets = [
    ("Paris", "Lyon", 465),
    ("Lyon", "Marseille", 315),
    ("Marseille", "Nice", 200),
    ("Nice", "Paris", 930),
    ("Paris", "Lille", 220),
]

### --- Fonctions ---

def afficher_trajet(trajet):
    depart, arrivee, distance = trajet
    print(f"Trajet de {depart} à {arrivee} : {distance} km")

def total_kilometrage(trajets):
    return sum([trajet[2] for trajet in trajets])

def trajet_le_plus_long(trajets):
    return max(trajets, key=lambda t: t[2])

def moyenne_distance(trajets):
    return total_kilometrage(trajets) / len(trajets) if trajets else 0

def trouver_trajets_depuis(ville, trajets):
    return [t for t in trajets if t[0] == ville]

def rechercher_trajet(depart, arrivee, trajets):
    for trajet in trajets:
        if trajet[0] == depart and trajet[1] == arrivee:
            return trajet
    return None  # Si non trouvé

### --- Programme principal ---

def main():

    print("Analyse de trajets enregistrés :")

    for trajet in trajets:
        afficher_trajet(trajet)

    print("Kilométrage total parcouru :", total_kilometrage(trajets), "km")
    print("Distance moyenne :", round(moyenne_distance(trajets), 2), "km")

    long_trajet = trajet_le_plus_long(trajets)
    print("Trajet le plus long :", long_trajet)

    ville = "Paris"
    print(f"Trajets au départ de {ville} :")
    trajets_depuis = trouver_trajets_depuis(ville, trajets)
    for t in trajets_depuis:
        afficher_trajet(t)

    # Recherche avec gestion d'erreur
    print("Recherche d’un trajet de Paris à Nice :")
    resultat = rechercher_trajet("Paris", "Nice", trajets)
    if resultat:
        afficher_trajet(resultat)
    else:
        print("Aucun trajet trouvé entre Paris et Nice.")

if __name__ == "__main__":
    main()