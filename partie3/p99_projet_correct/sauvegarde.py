from systeme_reservation_complet import SystemeReservation, Trajet, TrajetExpress, Utilisateur
import persistence

def main():
    systeme = SystemeReservation()

    # Chargement
    trajets, utilisateurs = persistence.charger()
    systeme.trajets = trajets
    systeme.utilisateurs = utilisateurs

    if not trajets:
        # Création de trajets si aucun existant
        systeme.ajouter_trajet(Trajet("Paris", "Lyon", 460))
        systeme.ajouter_trajet(TrajetExpress("Paris", "Marseille", 750))
        systeme.ajouter_trajet(Trajet("Lyon", "Nice", 470))

    if not utilisateurs:
        # Création d'un utilisateur test
        alice = Utilisateur("Alice")
        systeme.enregistrer_utilisateur(alice)
        trajets_depuis_paris = systeme.rechercher_trajets("Paris")
        for t in trajets_depuis_paris:
            alice.reserver(t)

    # Affichage final
    print("\\n--- Trajets disponibles ---")
    systeme.afficher_trajets()

    print("\\n--- Réservations utilisateurs ---")
    for u in systeme.utilisateurs:
        u.afficher()

    # Sauvegarde
    persistence.sauvegarder(systeme)

if __name__ == "__main__":
    main()