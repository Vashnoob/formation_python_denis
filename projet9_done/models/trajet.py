
from projet8.models.affichable import Affichable

class Trajet(Affichable):
    def __init__(self, depart, arrivee, distance):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance

    def calculer_duree(self):
        return self.distance / 80

    def to_dict(self):
        return {
            "type": "Trajet",
            "depart": self.depart,
            "arrivee": self.arrivee,
            "distance": self.distance
        }

    @staticmethod
    def from_dict(data):
        return Trajet(data["depart"], data["arrivee"], data["distance"])

    def afficher(self):
        print(self)

    def __str__(self):
        return f"Trajet({self.depart} → {self.arrivee}, {self.distance} km)"
