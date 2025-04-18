# === Usages de bibliothèques tierces installables avec pip ===

# Avant d'exécuter ce fichier, assurez-vous d'avoir installé :
# pip install pandas requests faker matplotlib

# --- pandas : manipulation de données ---
import pandas as pd

data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Âge": [25, 30, 22]
}
df = pd.DataFrame(data)
print("Tableau pandas :")
print(df)

# --- requests : appels HTTP ---
import requests

response = requests.get("https://api.github.com")
print("\\nStatut GitHub API :", response.status_code)
print("Contenu (extrait) :", response.json()["current_user_url"])

# --- faker : génération de fausses données ---
from faker import Faker

fake = Faker("fr_FR")
print("\\nExemples de faux profils :")
for _ in range(2):
    print(fake.name(), "-", fake.email())

# --- matplotlib : visualisation simple ---
import matplotlib.pyplot as plt

ages = df["Âge"]
noms = df["Nom"]

plt.bar(noms, ages)
plt.title("Âge des personnes")
plt.xlabel("Nom")
plt.ylabel("Âge")
plt.tight_layout()
plt.show()
