from datetime import datetime

from partie1.specialites import aujourdhui


class Personne:
        #proprietes / attributs /fields
        #nom , prenom, date_naissance,metier
        def __init__(self, nom,prenom, date_naissance, metier):
            self.nom = nom
            self.prenom = prenom
            self.naissance = datetime.fromisoformat(date_naissance)
            self.job = metier

        def __str__(self):
            return f"{self.prenom} {self.nom} {self.job} {self.age()}"

        def age(self):
            aujourdhui = datetime.today()
            return aujourdhui.year - self.naissance.year

        def change_metier(self, nouveau_metier):
            if nouveau_metier is None:
                print("Metier vide !!!!!")
            else:
                self.job = nouveau_metier

# --------------------

vivian = Personne("wong", "vivian", "2005-01-15", "CEO Google")
caroline = Personne("taton", "caroline", "2005-02-15" , "Ministre de la Culture")
ronaldo = Personne("drumond", "ronaldo", "2003-01-01", "Champion de Basket")
gaetan = Personne("dolige", "gaetan", "2003-01-02", "Champion de Basket")

print(ronaldo.job)
print(caroline.job)
print(vivian.job)
print("-"*20)

# afficher id des tous
people = (gaetan,ronaldo, caroline,vivian)
for p in people:
    print(p)

#change pour tous
for p in people:
    p.change_metier("menuisier/ebeniste")
    print(p)

# incertitude
vivian.change_metier(None)

print(type(ronaldo.naissance))
print(type(vivian.naissance))
print(vivian.job)



i = 5
f = 5.5
print(type(i))

print(i,f)


c = str(vivian)
print("")