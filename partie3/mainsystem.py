import json
import logging
import random
import sys
from pprint import pprint

from partie3.arguments import init_cfg
from partie3.modele import SystemeReservation, Trajet, Utilisateur, TrajetExpress
import logging


# --- Utilisation ---
def main():

    args = init_cfg()
    CHEMIN = args.filepath

    if args.debug=='yes':
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # DEBUT
    logging.debug("START "  + __file__)

    systeme = SystemeReservation()

    logging.info("Chargement des trajets")

    #Chargement TRAJETS / CATALOGUE
    trajets = Trajet.charge_trajets(CHEMIN + "trajets_realistes.csv")
    for t in trajets:
        systeme.ajouter_trajet(t)

    #RESERVATIONS EXISTANTES
    liste_users = json.load(open(CHEMIN + "systeme.json", "r", encoding="utf-8"))
    for u in liste_users:
        utilisateur = Utilisateur.from_dict(u)
        systeme.enregistrer_utilisateur(utilisateur)

    logging.info("Creation utilisateur + 1 reservation")

    nu = input("Nouvel utilisateur ?")
    if nu:
        vi = input("Ville de depart ?")

        recherche_trajets = systeme.rechercher_trajets(vi)
        if len(recherche_trajets) > 0:
            tr = random.choice(recherche_trajets) #Choisir au hasard un trajet
            systeme.enregistrer_utilisateur(Utilisateur(nu, [tr]))
        else:
            print("Pas de trajet disponible , utilisateur ignoré")

    # AFFICHAGE FINAL
    print("--- Reservations disponibles ---")
    systeme.afficher_reservations()

    #COMME UN DICT
    print(systeme["Benoit"])  #__getitem__


    # SAUVEGARDE DANS SYSTEME
    json.dump(systeme.to_dict(), open(CHEMIN + "systeme.json", "w", encoding="utf-8"), indent=4)

    logging.debug("END " + __file__)


if __name__ == "__main__":
    main()
