import random
import string
from dataclasses import dataclass
from typing import List




"""
@dataclass
class Element:
    groupe: str
    param_one: float
    param_two: float
    param_three: float
    param_four: float

# Génération de 4 groupes
groupes = ['Groupe A', 'Groupe B', 'Groupe C', 'Groupe D']

# Générer une liste de 100 éléments répartis dans les 4 groupes
def generer_elements(n=100) -> List[Element]:
    elements = []
    for _ in range(n):
        groupe = random.choice(groupes)
        element = Element(
            groupe=groupe,
            param_one=round(random.uniform(0, 100), 2),
            param_two=round(random.uniform(0, 100), 2),
            param_three=round(random.uniform(0, 100), 2),
            param_four=round(random.uniform(0, 100), 2),
        )
        elements.append(element)
    return elements

