from affichable import Affichable

# Une nouvelle classe doit apporter des nouveaux attributs et/ou methodes

class Trajet(Affichable):
    def __init__(self, depart, arrivee, distance, vitesse=80):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance
        self.vitesse = vitesse

    def afficher(self):
        print(f"Trajet : {self.depart} -> {self.arrivee} ({self.distance} km)")

    def calculer_duree(self):
        return self.distance / self.vitesse

    def to_dict(self):
        return {
            "type": "Trajet",
            "depart": self.depart,
            "arrivee": self.arrivee,
            "distance": self.distance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["depart"], data["arrivee"], data["distance"])

class TrajetExpress(Trajet):

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "TrajetExpress"
        return d


class TrajetAvion(Trajet):

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "TrajetAvion"
        return d

if __name__ == "__main__":
    Trajet.from_dict({"depart": "Paris", "arrivee": "Lyon", "distance": 1000})
    TrajetExpress.from_dict({"depart": "Paris", "arrivee": "Lyon", "distance": 1000})