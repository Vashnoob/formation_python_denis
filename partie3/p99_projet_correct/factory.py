from partie3.p99_projet_correct.trajet import Trajet, TrajetExpress, TrajetAvion

# Usine traditionnelle inspirée autres (C++, Java, C#)
class TrajetFactory:
    @staticmethod
    def creer(data):
        type_ = data['type'].lower()
        if type_ == "trajet":
            return Trajet(data["depart"], data["arrivee"], data["distance"])
        elif type_ == "trajetexpress":
            return TrajetExpress(data["depart"], data["arrivee"], data["distance"],150)
        elif type_ == "trajetavion":
            return TrajetAvion(data["depart"], data["arrivee"], data["distance"],300)

        raise ValueError(f"Type inconnu : {type_}")

if __name__ == "__main__":
    d = {
        "type": "trajetavion",
        "depart": "Paris",
        "arrivee": "Marseille",
        "distance": 750
    }
    o = TrajetFactory.creer(d)
    print(o)