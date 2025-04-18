
from projet8.models.utilisateur import Utilisateur
from projet8.models.trajet import Trajet
from projet8.models.trajet_express import TrajetExpress
from projet8.services.persistence import sauvegarder, charger
from projet8.services.logger import log_info

def main():
    utilisateurs = charger()

    if not utilisateurs:
        log_info("Initialisation des données")
        alice = Utilisateur("Alice")
        t1 = Trajet("Paris", "Lyon", 460)
        t2 = TrajetExpress("Paris", "Marseille", 750)

        alice.reserver(t1)
        alice.reserver(t2)

        utilisateurs.append(alice)
        sauvegarder(utilisateurs)

    for u in utilisateurs:
        u.afficher()

if __name__ == "__main__":
    main()
