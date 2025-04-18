

class ReservationInvalide(Exception):
    """Exception levée lorsqu'une réservation n'est pas valide."""
    def __init__(self, message="La réservation demandée est invalide."):
        super().__init__(message)

class TrajetInexistant(Exception):
    """Exception levée lorsqu'un trajet recherché n'existe pas."""
    def __init__(self, depart, arrivee):
        super().__init__(f"Aucun trajet trouvé de {depart} à {arrivee}.")
        self.depart = depart
        self.arrivee = arrivee