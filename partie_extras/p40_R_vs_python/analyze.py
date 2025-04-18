import pandas as pd
import subprocess

# Lecture et traitement (ex. ici juste affichage pour la démo)
df = pd.read_csv("data.csv")
print("Données analysées en Python :")
print(df.describe())

# Appel du script R pour le graphique
subprocess.run(["Rscript", "plot.R"])
