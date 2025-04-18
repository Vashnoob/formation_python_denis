from abc import ABC, abstractmethod
from dataclasses import dataclass


class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass

@dataclass(repr=True, eq=True, order=True)
class Ville:
    nom: str


if __name__ == "__main__":
    v = Ville("Paris")
    print(v)