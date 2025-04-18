import json
import os

###  **** FAKE ******
class Trajet:
    pass
class TrajetExpress:
    pass
class Utilisateur:
    pass#
###  **** FAKE ******



FICHIER_SAUVEGARDE = "donnees_reservation.json"

def sauvegarder(systeme):
    try:
        data = {
            "trajets": [t.to_dict() for t in systeme.trajets],
            "utilisateurs": [u.to_dict() for u in systeme.utilisateurs]
        }
        with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("✅ Données sauvegardées.")
    except IOError as e:
        print(f"❌ Erreur d'écriture du fichier : {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
    finally:
        print("💾 Fin de tentative de sauvegarde.")

def charger():
    trajets = []
    utilisateurs = []

    if not os.path.exists(FICHIER_SAUVEGARDE):
        print("📁 Aucune sauvegarde trouvée, initialisation à vide.")
        return trajets, utilisateurs

    try:
        with open(FICHIER_SAUVEGARDE, "r", encoding="utf-8") as f:
            data = json.load(f)

        for t in data.get("trajets", []):
            if t["type"] == "Trajet":
                trajets.append(Trajet.from_dict(t))
            elif t["type"] == "TrajetExpress":
                trajets.append(TrajetExpress.from_dict(t))

        for u in data.get("utilisateurs", []):
            utilisateurs.append(Utilisateur.from_dict(u))

        print("📂 Données chargées depuis la sauvegarde.")

    except FileNotFoundError:
        print("📁 Fichier de données introuvable.")
    except json.JSONDecodeError as e:
        print(f"❌ Fichier JSON invalide : {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue lors du chargement : {e}")
    finally:
        print("📦 Fin de tentative de chargement.")

    return trajets, utilisateurs