import json
import logging
import os

from partie3.p99_projet_correct.exceptionnel import ReservationException
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
    try :
        if not os.path.exists(FICHIER_SAUVEGARDE):
            print("📁 Aucune sauvegarde trouvée, initialisation à vide.")
            return [], []

        with open(FICHIER_SAUVEGARDE, "r", encoding="utf-8") as f:
            data = json.load(f)

        trajets = []
        for t in data.get("trajets", []):
            if t["type"] == "Trajet":
                trajets.append(Trajet.from_dict(t))
            elif t["type"] == "TrajetExpress":
                trajets.append(TrajetExpress.from_dict(t))

        utilisateurs = []
        for u in data.get("utilisateurs", []):
            utilisateurs.append(Utilisateur.from_dict(u))

        print("📂 Données chargées depuis la sauvegarde.")
        return trajets, utilisateurs
    except Exception as e:
        logging.WARN("")
        raise ReservationException("Erreur : Acces fichier(s) RE002")