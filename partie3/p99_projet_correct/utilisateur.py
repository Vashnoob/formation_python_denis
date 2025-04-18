from affichable import Affichable
from trajet import Trajet,  TrajetExpress

class Utilisateur(Affichable):
    def __init__(self, nom):
        self.nom = nom
        self.reservations = []

    def reserver(self, trajet):
        self.reservations.append(trajet)

    def afficher(self):
        print(f"Utilisateur : {self.nom}")
        for trajet in self.reservations:
            trajet.afficher()

    def to_dict(self):
        return {
            "nom": self.nom,
            "reservations": [t.to_dict() for t in self.reservations]
        }

    @staticmethod
    def from_dict(data):
        utilisateur = Utilisateur(data["nom"])
        for t in data.get("reservations", []):
            if t["type"] == "Trajet":
                trajet = Trajet.from_dict(t)
            elif t["type"] == "TrajetExpress":
                trajet = TrajetExpress.from_dict(t)
            else:
                continue
            utilisateur.reserver(trajet)
        return utilisateur