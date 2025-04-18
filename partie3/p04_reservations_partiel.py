class Affichable:
    pass

class Trajet(Affichable):
    def __init__(self, depart, arrivee, distance):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance

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
    def to_dict(self):
        d = super().to_dict()
        d["type"] = "TrajetExpress"
        return d

    @staticmethod
    def from_dict(data):
        return TrajetExpress(data["depart"], data["arrivee"], data["distance"])


class Utilisateur(Affichable):
    def __init__(self, nom):
        self.nom = nom
        self.reservations = []  # Liste de trajets

    def reserver(self, trajet):
        self.reservations.append(trajet)

    def to_dict(self):
        return {
            "nom": self.nom,
            "reservations": [t.to_dict() for t in self.reservations]
        }

    @staticmethod
    def from_dict(data):
        utilisateur = Utilisateur(data["nom"])
        for trajet_data in data["reservations"]:
            if trajet_data["type"] == "Trajet":
                t = Trajet.from_dict(trajet_data)
            elif trajet_data["type"] == "TrajetExpress":
                t = TrajetExpress.from_dict(trajet_data)
            else:
                continue
            utilisateur.reserver(t)
        return utilisateur
