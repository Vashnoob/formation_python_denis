from trajet import Trajet
from utilisateur import Utilisateur

class SystemeReservation:
    def __init__(self):
        self.trajets = []
        self.utilisateurs = []

    def ajouter_trajet(self, trajet:Trajet):
        self.trajets.append(trajet)

    def enregistrer_utilisateur(self, utilisateur:Utilisateur):
        self.utilisateurs.append(utilisateur)

    def rechercher_trajets(self, ville_depart):
        return [t for t in self.trajets if t.depart == ville_depart]

    def afficher_trajets(self):
        print("Liste des trajets disponibles :")
        for trajet in self.trajets:
            trajet.afficher()