
import json
from pathlib import Path
from projet8.models.utilisateur import Utilisateur
from projet8.models.trajet import Trajet
from projet8.models.trajet_express import TrajetExpress

DATA_PATH = Path(__file__).parent.parent / "data" / "reservations.json"

def sauvegarder(utilisateurs):
    try:
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in utilisateurs], f, indent=2)
    except Exception as e:
        print(f"Erreur de sauvegarde : {e}")

def charger():
    if not DATA_PATH.exists():
        return []
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Utilisateur.from_dict(u) for u in data]
    except Exception as e:
        print(f"Erreur de chargement : {e}")
        return []
