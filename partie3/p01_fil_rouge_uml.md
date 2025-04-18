### 🧩 **Diagramme de classes UML (version texte)**

```
+----------------------+
|      Affichable      |  <<interface>>
+----------------------+
| +afficher() : void   |
+----------------------+
           ▲
           |
+----------------------+
|       Trajet         |
+----------------------+
| - depart : str       |
| - arrivee : str      |
| - distance : float   |
+----------------------+
| +afficher() : void   |
| +calculer_duree()    |
+----------------------+
           ▲
           |
+------------------------+
|     TrajetExpress      |              +----------------------------+
+------------------------+              |    SystemeReservation      |
| +calculer_duree()      |              +----------------------------+
+------------------------+              | - trajets : list           |
                                        | - utilisateurs : list      |
+------------------------+              +----------------------------+
|      Utilisateur       |              | +ajouter_trajet(trajet)    |
+------------------------+              | +enregistrer_utilisateur() |
| - nom : str            |              | +rechercher_trajets(ville) |
| - reservations : list  |              | +afficher_trajets()        |
+------------------------+              +----------------------------+
| +reserver(trajet)      |
| +afficher()            |
+------------------------+












