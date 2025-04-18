from abc import ABC, abstractmethod
import logging
import csv

# --- Class abstraite pour objets affichables ---
class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass

    @abstractmethod
    def calculer_duree(self):
        pass

# --- Classe de base Trajet ---
class Trajet(Affichable):
    def __init__(self, depart, arrivee, distance):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance

    def afficher(self):
        print(self)

    def __str__(self):
        return f"Trajet : {self.depart} -> {self.arrivee} ({self.distance} km)"

    def __repr__(self):
        return f"T{self.depart}/{self.arrivee}/{self.distance}"

    def to_dict(self):
        di ={}
        di["depart"] = self.depart
        di["arrivee"] = self.arrivee
        di["distance"] = self.distance
        return di

    @classmethod
    def from_dict(cls, di):
        return cls(di["depart"], di["arrivee"], di["distance"])

    """    
    @staticmethod #souvent class se fait passer pour un module 
    def from_dict(di):
        return Trajet(di["depart"], di["arrivee"], di["distance"])
    """

    def calculer_duree(self):
        return self.distance / 80  # hypothèse : 80 km/h de moyenne

    @classmethod #Pas besoin d'un object Trajet pour etre appelée
    def charge_trajets(clz, nom_fichier):
        liste = []
        try:
            with open(nom_fichier, "r") as f:
                reader = csv.reader(f, dialect='excel', delimiter=";",
                                    quoting=csv.QUOTE_NONNUMERIC)
                next(reader) #ignore header
                for row in reader:
                    dep,arr,dis = row
                    liste.append( clz(dep,arr,dis) ) #clz synonyme de Trajet
        except FileNotFoundError as fnfe : #exception la plus precise
            logging.error(f"{nom_fichier} ! " + str(fnfe))
        except Exception as e:
            logging.error(f"Autre Erreur ! ")

        return liste

# --- Spécialisation : TrajetExpress ---
class TrajetExpress(Trajet):

    def calculer_duree(self):
        return super().calculer_duree() / 2
        # return self.distance / 160  # vitesse express

# --- Utilisateur ---
class Utilisateur():
    def __init__(self, nom, reservations=None):
        self._nom = nom
        self._reservations = [] if reservations is None else reservations

    def reserver(self, trajet):
        self._reservations.append(trajet)

    def afficher(self):
        print(f"Utilisateur : {self._nom}")
        for t in self._reservations:
            print("\t"+str(t))

    def to_dict(self):
        all_reservations = []
        for t in self._reservations:
            all_reservations.append(t.to_dict())

        di = {}
        di["user"] = self._nom
        di["reservations"] = all_reservations
        return di

    @classmethod
    def from_dict(cls, di):
        all_trajets = [Trajet.from_dict(t) for t in di["reservations"]]
        return cls(di["user"], all_trajets)


# --- Système de réservation ---
class SystemeReservation:
    def __init__(self):
        self.trajets = []
        self.utilisateurs = []

    def ajouter_trajet(self, trajet):
        self.trajets.append(trajet)

    def enregistrer_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def rechercher_trajets(self, ville_depart):
        return tuple([t for t in self.trajets if t.depart == ville_depart])

    def afficher_trajets(self):
        for trajet in self.trajets:
            trajet.afficher()

    def afficher_reservations(self):
        # resa accessible par les utilisateurs
        for ut in self.utilisateurs:
            ut.afficher()

    def calcul_optimal(self):
        raise NotImplementedError("Pas encore prete")

    def to_dict(self):
        tb = []
        for t in self.utilisateurs:
            tb.append(t.to_dict())
        return tb

