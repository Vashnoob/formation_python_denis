import pandas as pd

def get_sample_dataframe():
    data = {
        "Nom": ["Caroline", "Hela", "Gaetan", "Aurelien", "Christophe"],
        "Âge": [25, 30, 35, 40, 45],
        "Ville": ["Paris", "Lyon", "Marseille", "Nice", "Toulouse"],
        "Destination": ["Angers", "Lyon", "Toulouse", "Lille", "Metz"],
        "Distance": [88, 92, 75, 80, 95],
        "Statut": ["Actif", "Actif", "Inactif", "Actif", "Inactif"]
    }
    return pd.DataFrame(data)