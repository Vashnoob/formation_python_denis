from trajet import Trajet
from utilisateur import Utilisateur

class SystemeReservation:
    def __init__(self):
        self.trajets = []
        self.utilisateurs = []

    def ajouter_trajet(self, trajet:Trajet):
        # TODO ajouter le trajet aux autres trajets
        pass

    def enregistrer_utilisateur(self, utilisateur:Utilisateur):
        # TODO ajouter l' utilisateur aux autres
        pass

    def rechercher_trajets(self, ville_depart):
        # TODO recherjcer les trajet selon ville_depart
        pass

    def afficher_trajets(self):
        print("Liste des trajets disponibles :")
        # TODO
