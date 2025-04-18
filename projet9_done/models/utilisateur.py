
from datetime import datetime
from projet8.models.trajet import Trajet
from projet8.models.trajet_express import TrajetExpress

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.reservations = []

    def reserver(self, trajet):
        self.reservations.append({
            "trajet": trajet,
            "date": datetime.now()
        })

    def to_dict(self):
        return {
            "nom": self.nom,
            "reservations": [
                {
                    "trajet": r["trajet"].to_dict(),
                    "date": r["date"].isoformat()
                } for r in self.reservations
            ]
        }

    @staticmethod
    def from_dict(data):
        utilisateur = Utilisateur(data["nom"])
        for r in data["reservations"]:
            t_data = r["trajet"]
            trajet = (TrajetExpress if t_data["type"] == "TrajetExpress" else Trajet).from_dict(t_data)
            utilisateur.reservations.append({
                "trajet": trajet,
                "date": datetime.fromisoformat(r["date"])
            })
        return utilisateur

    def afficher(self):
        print(f"Utilisateur : {self.nom}")
        for r in self.reservations:
            print(f"  - {r['trajet']} réservé le {r['date'].strftime('%Y-%m-%d %H:%M:%S')}")
