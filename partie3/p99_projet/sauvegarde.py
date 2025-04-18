from systeme_reservation_complet import SystemeReservation, Trajet, TrajetExpress, Utilisateur
import persistence

def main():
    systeme = SystemeReservation()

    # Chargement
    trajets, utilisateurs = persistence.charger()
    systeme.trajets = trajets
    systeme.utilisateurs = utilisateurs

    if not trajets:
        # TODO Création de trajets si aucun existant
        # Paris Lyon 460
        # Paris Marseille 750
        # Lyon Nice 470

    if not utilisateurs:
        # TODO Création d'un utilisateur test
        alice = Utilisateur("Alice")
        # enregistrer dans le systeme
        # rechercher kes trajets u deoart de paris
        # l'utilisateur veux reserver tous les trajets trouvés

    # Affichage final
    print("\\n--- Trajets disponibles ---")
    # TODO afficher les trajets

    print("\\n--- Réservations utilisateurs ---")
    # TODO Voirs les resas utilisateurs

    # Sauvegarde
    persistence.sauvegarder(systeme)

if __name__ == "__main__":
    main()