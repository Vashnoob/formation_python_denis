"""
Corrigés des exercices POO - Jour 2
"""

# Exercice 1
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans.")

    def anniversaire(self):
        self.age += 1


# Exercice 2
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Solde insuffisant.")


# Exercice 3
class Animal:
    def parler(self):
        print("L'animal fait un bruit.")

class Chat(Animal):
    def parler(self):
        print("Miaou")

class Chien(Animal):
    def parler(self):
        print("Woof")

def faire_parler_les_animaux(animaux):
    for animal in animaux:
        animal.parler()


# Exercice 4
class Livre:
    def __init__(self, titre):
        self.titre = titre

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(livre.__titre)

    def rechercher(self, titre):
        for livre in self.livres:
            if livre.__titre == titre:
                return livre
        return None


# Exercice 5
from abc import ABC, abstractmethod

class Affichable(ABC):
    @abstractmethod
    def afficher(self):
        pass

class Utilisateur(Affichable):
    def __init__(self, nom):
        self.nom = nom

    def afficher(self):
        print("Utilisateur :", self.nom)

class Produit(Affichable):
    def __init__(self, nom):
        self.nom = nom

    def afficher(self):
        print("Produit :", self.nom)


# Exercice 6
class Configuration:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.parametres = {}
        return cls._instance

    def modifier(self, cle, valeur):
        self.parametres[cle] = valeur
