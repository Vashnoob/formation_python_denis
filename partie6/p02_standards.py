# === Utilisation de la bibliothèque standard Python ===

# --- os & pathlib (fichiers et dossiers) ---
import os
from pathlib import Path

chemin = Path("exemple.txt")
if not chemin.exists():
    chemin.write_text("Ceci est un exemple de texte.")

print("Fichier créé :", chemin.resolve())

# --- json (sérialisation) ---
import json

data = {"nom": "Alice", "age": 30}
json_str = json.dumps(data, indent=2)
print("JSON :", json_str)

# --- datetime ---
from datetime import datetime, timedelta

now = datetime.now()
print("Date actuelle :", now)
print("Dans 3 jours :", now + timedelta(days=3))

# --- collections ---
from collections import Counter, defaultdict

compte = Counter("abracadabra")
print("Comptage de lettres :", compte)

groupes = defaultdict(list)
groupes["math"].append("Alice")
groupes["math"].append("Bob")
print("Groupes :", groupes)

# --- itertools ---
from itertools import product, permutations

print("Produits cartesien (2, 3) :", list(product([1, 2], ["a", "b"])))
print("Permutations de 'ab':", list(permutations("ab")))

# --- re (expressions régulières) ---
import re

texte = "email: alice@example.com"
match = re.search(r"\\w+@\\w+\\.\\w+", texte)
print("Email trouvé :", match.group() if match else "Aucun")

# --- math ---
import math

print("Pi :", math.pi)
print("racine(2) :", math.sqrt(2))

# --- statistics ---
import statistics

notes = [10, 12, 15, 18]
print("Moyenne :", statistics.mean(notes))
print("Écart-type :", statistics.stdev(notes))

# --- textwrap ---
import textwrap

long_texte = "Ce paragraphe est très long et doit être mis en forme proprement pour tenir dans un affichage de 40 caractères de large."
print(textwrap.fill(long_texte, width=40))

# --- pprint ---
from pprint import pprint

structure = {"utilisateur": {"nom": "Alice", "age": 30, "cours": ["math", "physique"]}}
print("Affichage structuré :")
pprint(structure)

# --- enum ---
from enum import Enum, auto

class Role(Enum):
    ADMIN = auto()
    USER = auto()

print("Role.USER =", Role.USER)

# --- dataclasses ---
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print("Point :", p)

# --- contextlib ---
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("fichier_inexistant.txt")
    print("Fichier supprimé")

# --- concurrent.futures ---
from concurrent.futures import ThreadPoolExecutor

def carre(n):
    return n * n

with ThreadPoolExecutor() as executor:
    resultats = list(executor.map(carre, range(5)))
    print("Carrés :", resultats)

# --- functools ---
from functools import lru_cache

@lru_cache
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

print("Fibonacci(10) :", fib(10))
