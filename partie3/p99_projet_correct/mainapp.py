from pathlib import Path

from partie3.p99_projet_correct.decorateur import debug_log
from systeme import SystemeReservation
from trajet import Trajet, TrajetExpress
from utilisateur import Utilisateur
import json
import os

from readini import data_path

# Path redefini le __div__
FICHIER_SAUVEGARDE = Path(data_path()) / "donnees_reservation.json"

@debug_log
def sauvegarder(systeme):
    data = {
        "trajets": [t.to_dict() for t in systeme.trajets],
        "utilisateurs": [u.to_dict() for u in systeme.utilisateurs]
    }
    with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("✅ Données sauvegardées.")

@debug_log
def charger():
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


def main():
    systeme = SystemeReservation()

    trajets, utilisateurs = charger()
    systeme.trajets = trajets
    systeme.utilisateurs = utilisateurs

    if not trajets:
        systeme.ajouter_trajet(Trajet("Paris", "Lyon", 460))
        systeme.ajouter_trajet(TrajetExpress("Paris", "Marseille", 750))
        systeme.ajouter_trajet(Trajet("Lyon", "Nice", 470))

    if not utilisateurs:
        alice = Utilisateur("Alice")
        systeme.enregistrer_utilisateur(alice)
        for t in systeme.rechercher_trajets("Paris"):
            alice.reserver(t)

    print("\\n--- Trajets disponibles ---")
    systeme.afficher_trajets()

    print("\\n--- Réservations utilisateurs ---")
    for u in systeme.utilisateurs:
        u.afficher()

    sauvegarder(systeme)

if __name__ == "__main__":
    main()