
# MUTABILITE , MUABLE = MODIFIABLE
# NON MUTABLE, IMMUABLE = NON MODIFIABLE

formation = "IBCegos"

form_minuscule = formation.lower() #NON MUTABILITE
print(formation, form_minuscule)
formation = formation.lower() #NON MUTABILITE REMISE DANS MEME VARIABLE

#
prenom1 = "Mohamed"
prenom2 = "Mohamed"
# en C++ ca aurait deux adresses memoire

# en Python ????
print(id(prenom1) , id(prenom2))

prenom2 = "Franco"
print(id(prenom1) , id(prenom2))


prenom1 = "Caroline"
print(id(prenom1) , id(prenom2))

# MEME ADRESSE OU PAS
print(id(prenom1))
prenom1= prenom1.capitalize()
print(id(prenom1))
