from abc import ABC, abstractmethod
from dataclasses import dataclass


class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass

@dataclass
class Ville:
    nom: str
