import glob
import os
import shutil
from collections import defaultdict, Counter, deque
from enum import Enum

# collections — Container datatypes
dico=defaultdict(lambda:"?")
dico["a"] = "A"
dico["c"] = "C"
print(dico["b"],dico["c"])

phrase= """Ah c'est vous Dantès cria l homme à la barque qu'est il donc 
arrivé, et pourquoi cet air de tristesse répandu sur tout votre bord Dantès"""
c = Counter(phrase.split(' '))
print(c)
print(c["Dantès"])

historique_events = deque(maxlen=5)
historique_events.append("tresvieille")
historique_events.append("unpeudaté")  # ajoute au début
historique_events.append("recent")  # ajoute au début
 # ajoute au début
derniere = historique_events.pop()    # retire à la fin
print(derniere)
derniere = historique_events.pop()    # retire à la fin
print(derniere)


#enum — Support for enumerations
jour_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

def foojour(jour:str):
    if jour=="Lundi":
        pass
    elif jour=="Mardi":
        pass
    elif jour=="Dimanche":
        pass
    else:
        pass

foojour("Monday")
foojour("lundi")

class JourSemaine(Enum):
    LUNDI = 1
    MARDI =2
    MERCREDI =3
    JEUDI =4
    VENDREDI =5
    SAMEDI =6
    DIMANCHE =7

class TailleChaussure(Enum):
    SIX = 39
    SIXFIVE =39.5
    ELEVEN=44
    TWELVE=45

jj = JourSemaine.JEUDI
print(jj.name, jj.value)

if jj == JourSemaine.SAMEDI:
    pass


def foojourenum(j:JourSemaine):
    match j:
        case JourSemaine.LUNDI:
            pass
        case JourSemaine.MARDI:
            pass



#glob.glob — Unix style pathname pattern expansion
#os.listdir() non recursive, pas de chemin
fichiers = os.listdir("../data/")
fichiers = [f for f in fichiers if f.startswith("pg") and f.endswith(".txt")]
print(fichiers)

#glob recursive, chemin du fichier
fichiers = glob.glob("../data/**/pg*.txt",recursive=True)
print(fichiers)

basename =" pg_1245.txt"
dirname = "data"
dirs = ["data","subdata","subsubdata", "pg142.txt"]
d1,d2,d3,f1 = dirs
fullpath = os.path.join(*dirs)
print(fullpath)


def min(*valeurs):
    a=valeurs[0]
    for i in valeurs[1:]:
        if i<a:
            a=i
    return a


def afficher(**kvaleurs):
    for k,v in kvaleurs.items():
        print(f"{k}={v}")

def afficherplus(*vals, **kvaleurs):
    print(vals)
    print(kvaleurs)

a = min(1,2,3,4,5)
b = min(1,4)
c = min(1)
c = min(1,8,8,8,8,8,8,8,8,1,1,1,1,1,1)

afficher(a=a,b=b,c=c, couleur="gris")
afficherplus(nom="herve",prenom="aurelien")
afficherplus("herve",nom="aurelien")

print(1,2,3,4,sep=";")
# shutil — High-level file operations
"""shutil.copyfile("data/pg1245.txt","data/pg1245_copie.txt")
shutil.copy2()
shutil.copytree()
"""
bytes_to_mb= lambda octets:round(octets / (1024 * 1024), 2)
total, used, free = shutil.disk_usage("/")
print(f"Total: {bytes_to_mb(total)}Mb, Utilisé: {bytes_to_mb(used)}Mb, Libre: {bytes_to_mb(free)}Mb")





