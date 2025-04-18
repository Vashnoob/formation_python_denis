from abc import ABC, abstractmethod

# Interface Affichable
class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass

# Classe Trajet (implémente Affichable)
class Trajet(Affichable):
    def __init__(self, depart, arrivee, distance):
        self.depart = depart
        self.arrivee = arrivee
        self.distance = distance

    def afficher(self):
        print(f"Trajet : {self.depart} -> {self.arrivee} ({self.distance} km)")

    def calculer_duree(self):
        return self.distance / 80  # vitesse par défaut

# Classe TrajetExpress (hérite de Trajet)
class TrajetExpress(Trajet):
    def calculer_duree(self):
        return self.distance / 150  # vitesse express

# Classe Utilisateur (implémente Affichable)
class Utilisateur(Affichable):
    def __init__(self, nom):
        self.nom = nom
        self.reservations = []

    def reserver(self, trajet):
        self.reservations.append(trajet)

    def afficher(self):
        print(f"Utilisateur : {self.nom}")
        for trajet in self.reservations:
            trajet.afficher()

# Classe SystemeReservation
class SystemeReservation:
    def __init__(self):
        self.trajets = []
        self.utilisateurs = []

    def ajouter_trajet(self, trajet):
        self.trajets.append(trajet)

    def enregistrer_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def rechercher_trajets(self, ville_depart):
        return [t for t in self.trajets if t.depart == ville_depart]

    def afficher_trajets(self):
        print("Liste des trajets disponibles :")
        for trajet in self.trajets:
            trajet.afficher()

# Démonstration du fonctionnement
def main():
    systeme = SystemeReservation()

    # Création de trajets
    t1 = Trajet("Paris", "Lyon", 460)
    t2 = TrajetExpress("Paris", "Marseille", 750)
    t3 = Trajet("Lyon", "Nice", 470)
    systeme.ajouter_trajet(t1)
    systeme.ajouter_trajet(t2)
    systeme.ajouter_trajet(t3)

    # Création utilisateur
    u1 = Utilisateur("Alice")
    systeme.enregistrer_utilisateur(u1)

    # Réservation de trajets depuis Paris
    trajets_depuis_paris = systeme.rechercher_trajets("Paris")
    for trajet in trajets_depuis_paris:
        u1.reserver(trajet)

    # Affichage final
    systeme.afficher_trajets()
    print("\\nRéservations de l'utilisateur :")
    u1.afficher()

if __name__ == "__main__":
    main()
