from affichable import Affichable
from trajet import Trajet,  TrajetExpress

class Utilisateur(Affichable):
    def __init__(self, nom):
        self.nom = nom
        self.reservations = []

    def reserver(self, trajet):
        # TODO : Conserver le trajet dans les reservations
        pass

    def afficher(self):
        print(f"Utilisateur : {self.nom}")
        # TODO : Afficher tous les trajets
        pass

    def to_dict(self):
        # un dictionnaire qui representera le contenu
        # TODO
        return {
            "nom": None,
            "reservations": None
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