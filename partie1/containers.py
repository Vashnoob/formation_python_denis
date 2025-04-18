#containers

#TOUT EST UN OBJET

# 4 CONTAINERS STANDARD
# LIST , TUPLE, SET, DICT

# list : une sequence ordonnee de valeurs, sequence mutable
valeurs = [1 , None, "HP", 100.50, False]

#extrait
v1= valeurs[1]
v2 = valeurs[3]
v1,v2 = valeurs[1], valeurs[3] #unpacking
print(v1,v2, sep="-")

# copy inversé
print(valeurs[::-1])

print(type(valeurs))

# LISTE EST MUTABLE
valeurs.append(6) #NOTATION POO
print(valeurs)
print(valeurs.pop(0))
valeurs[-1] = 600
print(valeurs)

liste_vide = []
liste_vide = list()

#boucle : for

# ---------------------------------------------------------
# tuple  : une sequence ordonnee de valeurs, sequence NON mutable
tvaleurs = (1 , None, "HP", 100.50, False, "HP")
print(tvaleurs[2])

tu_vide = ()
tu_vide = tuple()

#creations
copy_tuple = tuple(valeurs)
copy_tuple = tuple([0,1,1,2,3,5,8,13,21,34])
print(copy_tuple)

# copy_tuple[0] = -1 #impossible

version_list = list(copy_tuple) # copy vers une liste

# SET ; Ensemble
#une sequence de valeurs, sequence mutable
s_value = set(tvaleurs)
s2_value = {1,2,3,4,5}
print(s_value)

employes = {"aurelien","caroline",'benoit','jean-christophe'}
foot = {"caroline",'benoit','vivian'}

""" NON MUTABLES
iemployes = {id('benoit')}
ifoot = {id('benoit')}
print(iemployes, ifoot)
"""

club_foot = employes.intersection(foot)
print(club_foot)

edf = employes.difference(foot) # pas du foot dans cette societe
fde = foot.difference(employes) #qui ne sont pas employes par

print(edf)
print(fde)

print(employes)

print(employes)
employes.add("mohamed")
print(employes)
employes.pop()


# dictionnaire dict
# dict -> set de cles -> list de valeurs  mutable


dico = dict()
dico = {}
dico = {  "two" : 2, 'four' :4, "one" : 1, "un" : 1 , 45: "quarante cinq" }
print(dico)


dico = {  "two" : 2, 'four' :4, "one" : 1, "un" : 1 , "two" : 2.0}
print(dico)
"""
        lecture         ecriture        taille
list                        *               **
tuple       *               N/A             **
set         **              **              ***
dico        ****            **              *
"""

# deborde = erreur
taille = len(tvaleurs)
print(tvaleurs[taille-1])

