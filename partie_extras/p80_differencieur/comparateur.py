# Mise à jour de la classe : param_two et param_three sont maintenant des chaînes
import os
import random
from dataclasses import dataclass
import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from scipy.spatial.distance import euclidean
from difflib import SequenceMatcher
import numpy as np

"""""
    Preparation pour la colonne  COMPOSITION
    Element 1           A;B;C;D
    Element 2           A;B;D;C;E;F
            1) Split sur le ;
            2) Tri
            3) Score  chaque ligne
            4 ) Conserve score  
Ligne 1
    Ligne 2 =  0.5    
    Ligne 3 =  0.4
    Ligne 4 =  0.4
"""

@dataclass
class Element:
    groupe: str
    param_one: float
    param_two: str  # chaîne
    param_three: str  # chaîne
    param_four: float
    label: str

    def __str__(self):
        return f"E {self.groupe}:{self.param_one}:{self.param_two}:{self.param_three}:{self.param_four}:{self.label}"

def lire_elements_csv(csv_path):
    if not os.path.exists(csv_path):
        return None

    df_loaded = pd.read_csv(csv_path)

    # Conversion en objets Element (attention : param_two, param_three, label sont des chaînes ; param_one et param_four sont float)
    elements_reloaded = [
        Element(
            groupe=row["groupe"],
            param_one=float(row["param_one"]),
            param_two=row["param_two"],
            param_three=row["param_three"],
            param_four=float(row["param_four"]),
            label=row["label"]
        )
        for _, row in df_loaded.iterrows()
    ]

    return elements_reloaded

def sauve_elements_csv(csv_path):
    # Nouvelles valeurs textuelles pour les champs chaîne
    text_values = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
    groupes = ['Groupe A', 'Groupe B', 'Groupe C', 'Groupe D']
    labels = ['Banane', 'Balance', 'Bible', 'Canarde']

    # Génération des éléments avec des chaînes dans param_two et param_three
    elements = [
        Element(
            groupe=random.choice(groupes),
            param_one=round(random.uniform(0, 100), 2),
            param_two=random.choice(text_values),
            param_three=random.choice(text_values),
            param_four=round(random.uniform(0, 100), 2),
            label=random.choice(labels)
        )
        for _ in range(100)
    ]
    df_elements = pd.DataFrame([e.__dict__ for e in elements])
    df_elements.to_csv(csv_path, index=False)
    return elements

# Encodage numérique : on garde seulement param_one et param_four
def to_numeric_vector_v2(element):
    return {
        "param_one": element.param_one,
        "param_four": element.param_four,
    }

# Vérifie si le fichier existe déjà
csv_path = "elements_dataset.csv"
elements = lire_elements_csv(csv_path)
if not elements:
    elements = sauve_elements_csv(csv_path)


#   ON SELECTIONNE ZERO s
ref = elements[0]
ref_vec = to_numeric_vector_v2(ref)
vec = DictVectorizer(sparse=False)
X = vec.fit_transform([to_numeric_vector_v2(e) for e in elements])

ref_index = 0
ref_vector = X[ref_index]
distances = []

# Fonction de similarité inversée (1 - ratio) pour texte
def string_diff(a, b):
    return 1 - SequenceMatcher(None, a, b).ratio()

for i, (e, vec_i) in enumerate(zip(elements, X)):
    if i == ref_index: # pas la peine de tester soit meme (0)
        continue
    numeric_dist = euclidean(ref_vector, vec_i)
    param_two_diff = string_diff(ref.param_two, e.param_two)
    param_three_diff = string_diff(ref.param_three, e.param_three)
    label_diff = string_diff(ref.label, e.label)

    #ajouter des poids
    score = numeric_dist + param_two_diff + param_three_diff + label_diff

    distances.append({
        "index": i,
        "groupe": e.groupe,
        "param_two": e.param_two,
        "param_three": e.param_three,
        "label": e.label,
        "dist_num": round(numeric_dist, 3),
        "dist_str_param_two": round(param_two_diff, 3),
        "dist_str_param_three": round(param_three_diff, 3),
        "dist_str_label": round(label_diff, 3),
        "score_total": round(score, 3)
    })

df_score_v2 = pd.DataFrame(distances).sort_values(by="score_total")

# Création d'une représentation string pour chaque élément de la liste
element_str_map = {
    i: str(elements[i]) for i in df_score_v2["index"]
}

# Création d'une nouvelle colonne 'element' à partir du mapping
df_score_v2["element"] = df_score_v2["index"].map(element_str_map)

# Réorganisation des colonnes : 'element' à gauche de 'index', suivi de 'score_total'
df_final = df_score_v2[["element", "index", "score_total"]].copy()

# Tri par score croissant
df_final = df_final.sort_values(by="score_total")
df_final.info()
print("")
print(f">>>> {ref}")
print(df_final.head(15))


