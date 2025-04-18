from abc import ABC, abstractmethod

class Affichable(ABC):
    def __str__(self):
        classe = self.__class__.__name__
        attributs = vars(self)  # dictionnaire des attributs de l'objet
        contenu = ", ".join(f"{k}={v!r}" for k, v in attributs.items())
        return f"{classe}({contenu})"

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def afficher(self):
        """Méthode à implémenter obligatoirement dans les sous-classes."""
        pass

class Trajet(Affichable):
    def __init__(self, depart, arrivee, distance):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance

    def __repr__(self):
        return f"Trajet('{self.depart}', '{self.arrivee}', {self.distance})"

    def __eq__(self, other):
        return (isinstance(other, Trajet) and
                self.depart == other.depart and
                self.arrivee == other.arrivee and
                self.distance == other.distance)

    def __lt__(self, other):
        return self.distance < other.distance


class Utilisateur(Affichable):
    def __init__(self, nom):
        self.nom = nom
        self.reservations = []

    """ PLUS UTILE 
    def __str__(self):
        return f"Utilisateur {self.nom} ({len(self.reservations)} réservation(s))"
    """
    
    def __repr__(self):
        return f"Utilisateur('{self.nom}')"

    def __len__(self):
        return len(self.reservations)