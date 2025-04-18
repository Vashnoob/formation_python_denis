
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
    pass

def total_kilometrage(trajets):
    pass

def trajet_le_plus_long(trajets):
    pass

def moyenne_distance(trajets):
    pass

def trouver_trajets_depuis(ville, trajets):
    pass

def rechercher_trajet(depart, arrivee, trajets):
    pass
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