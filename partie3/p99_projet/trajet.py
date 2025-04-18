from affichable import Affichable

class Trajet(Affichable):
    def __init__(self, depart, arrivee, distance):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance

    def afficher(self):
        print(f"Trajet : {self.depart} -> {self.arrivee} ({self.distance} km)")

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


class TrajetExpress(Trajet):
    def calculer_duree(self):
        return self.distance / 150

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "TrajetExpress"
        return d

    @staticmethod
    def from_dict(data):
        return TrajetExpress(data["depart"], data["arrivee"], data["distance"])