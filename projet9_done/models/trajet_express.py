
from projet8.models.trajet import Trajet

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
