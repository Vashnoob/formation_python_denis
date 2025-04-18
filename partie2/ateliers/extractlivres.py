import os
import re
from tqdm import tqdm
import requests

from partie2.modeles.livre import Livre

def charger_livres(dossier):
    livres = []
    for nom_fichier in os.listdir(dossier):
        if nom_fichier.startswith("pg") and nom_fichier.endswith(".txt"):
            chemin = os.path.join(dossier, nom_fichier)
            l = Livre(chemin)
            l.lire()
            l.extraire_titre()
            livres.append(l)
    return livres

def charger_livres_depuis_web(base_url, destination, debut, fin):
    for i in tqdm(range(debut, fin + 1)):
        url = base_url.format(i=1)
        try:
            response = requests.get(url, timeout=5)
            open(destination.format(i), "wt",encoding="utf-8").write(
                response.text
            )
        except requests.RequestException:
            # print(f"Erreur réseau pour : {url}")
            pass

# Exemple d’utilisation
dest = "../../data/pg{i}.txt"
url = "https://www.gutenberg.org/cache/epub/{i}/pg{i}.txt"
charger_livres_depuis_web(url,dest,100,110 )
