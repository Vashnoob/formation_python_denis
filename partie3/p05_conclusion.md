
### 📋 **Tableau récapitulatif des classes du système de réservation de trajets**

| Classe               | Rôle dans le système                                      | Concepts Python exploités                                                                 |
|----------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `Affichable`         | Interface définissant la méthode `afficher()`             | - Classe abstraite (`ABC`)<br>- Méthode abstraite (`@abstractmethod`)                      |
| `Trajet`             | Représente un trajet simple (ville de départ, arrivée...)| - Héritage d'interface<br>- Attributs d'instance<br>- Méthodes d'objet<br>- Sérialisation avec `to_dict()` |
| `TrajetExpress`      | Variante de `Trajet` avec durée plus rapide               | - Héritage de classe<br>- Redéfinition de méthode (`calculer_duree()`)<br>- Polymorphisme  |
| `Utilisateur`        | Représente un client qui réserve des trajets              | - Association objet (liste de `Trajet`)<br>- Encapsulation partielle<br>- Méthodes d’action (`reserver()`)<br>- Sérialisation avec `to_dict()` |
| `SystemeReservation` | Coordonne les trajets et utilisateurs                     | - Conteneur / gestionnaire central<br>- Relations d’agrégation<br>- Recherche / ajout via méthodes |
| `main.py`            | Point d’entrée du programme                               | - Structure `if __name__ == "__main__"`<br>- Séparation des responsabilités (chargement, affichage, sauvegarde) |
| JSON (via fonctions) | Sauvegarde et chargement persistant                       | - Manipulation de fichiers<br>- Import/export de données<br>- Conversions entre objets Python et dictionnaires |

---

### 🔍 Concepts objets couverts :
- **Encapsulation** : chaque classe gère ses propres données.
- **Héritage** : `TrajetExpress` hérite de `Trajet`.
- **Polymorphisme** : appel de `afficher()` ou `calculer_duree()` sur différents types.
- **Association** : `Utilisateur` contient des objets `Trajet`.
- **Interface** : `Affichable` impose un contrat à respecter.
