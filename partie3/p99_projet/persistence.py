import json
import os
from trajet import Trajet, TrajetExpress
from utilisateur import Utilisateur

FICHIER_SAUVEGARDE = "donnees_reservation.json"

def sauvegarder(systeme):
    data = {
        "trajets": [t.to_dict() for t in systeme.trajets],
        "utilisateurs": [u.to_dict() for u in systeme.utilisateurs]
    }
    with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("✅ Données sauvegardées.")

def charger():
    # la librairie os.path pour tester un fichier

    #lire le fichier json
    with open(FICHIER_SAUVEGARDE, "r", encoding="utf-8") as f:
        data = json.load(f)

    trajets = []
    for t in data.get("trajets", []):
        if t["type"] == "Trajet":
            # TODO decoder le morceau de json pour creer un Trajet
        elif t["type"] == "TrajetExpress":
            # TODO decoder le morceau de json pour creer un TrajetExpress

    utilisateurs = []
    for u in data.get("utilisateurs", []):
        # TODO conserver les utilisateurs decodés dans les utilisateurs

    print("📂 Données chargées depuis la sauvegarde.")
    return trajets, utilisateurs