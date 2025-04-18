import pandas as pd
import json

def load_trajets_dict(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = []
    for entry in data:
        user = entry["user"]
        for res in entry["reservations"]:
            records.append({
                "user": user,
                "depart": res["depart"],
                "arrivee": res["arrivee"],
                "distance": res["distance"]
            })

    return pd.DataFrame(records)

def load_reservations(json_path):
    records = load_trajets_dict(json_path)
    return pd.DataFrame(records)
