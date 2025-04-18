
# --- Approche orientée objet ---
class Chien:
    def aboyer(self):
        print("Woof!")

# --- Objet = état + comportement + identité ---
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom  # état

    def saluer(self):  # comportement
        print(f"Bonjour {self.nom}")

# --- Classe, attributs, méthodes ---
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

# --- Encapsulation ---
class Coffre:
    def __init__(self):
        self.__code_secret = "1234"  # pseudo-privé avec __

# --- Communication entre objets ---
class A:
    def action(self):
        print("A agit")

class B:
    def interagir(self, objet_a):
        objet_a.action()

# --- Héritage ---
class Animal:
    def parler(self):
        print("Je fais un bruit")

class Chat(Animal):  # Hérite de Animal
    def parler(self):  # Redéfinition (override)
        print("Miaou")

# --- Polymorphisme ---
def faire_parler(animal):
    animal.parler()  # Fonctionne avec n'importe quelle sous-classe d'Animal

faire_parler(Chat())
faire_parler(Animal())

# --- Association entre classes ---
class Livre:
    def __init__(self, titre):
        self.titre = titre

class Bibliothèque:
    def __init__(self):
        self.livres = []  # Contient des objets Livre

    def ajouter(self, livre):
        self.livres.append(livre)

# --- Interfaces (ABC) ---
from abc import ABC, abstractmethod

class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass

# --- Design Pattern - Singleton ---
class Unique:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
