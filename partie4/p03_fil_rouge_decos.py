
## ✅ ** Décorateur de debug/log**

### 🔧 Le décorateur `debug_log` :
def debug_log(fonction):
    def wrapper(*args, **kwargs):
        # TODO
        resultat = fonction(*args, **kwargs)
        # TODO
        return resultat
    return wrapper

class SystemeReservation:
    def __init__(self):
        self.trajets = []
        self.utilisateurs = []

    # TODO
    def ajouter_trajet(self, trajet):
        self.trajets.append(trajet)

    # TODO
    def enregistrer_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

# 🧠 Ce décorateur t’aide à tracer ce qui se passe sans polluer ton code métier.*



## ✅ ** Contrôle de doublon de réservation**
## On veut éviter que le même trajet soit réservé plusieurs fois par un utilisateur.

def unique_reservation(fonction):
    def wrapper(self, trajet):
        if trajet in self._reservations:
            print("⛔ Trajet déjà réservé.")
            return
        return fonction(self, trajet)
    return wrapper

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.reservations = []

    # TODO
    def reserver(self, trajet):
        self.reservations.append(trajet)
# 🧠 Ce décorateur isole la logique de validation sans surcharger la méthode principale.*

"""
- Ils **séparent les préoccupations** : logs, validation, performance...
- Ils permettent de **factoriser du comportement** commun sans duplication.
- Ils rendent le code **plus lisible** et modulaire.
"""
