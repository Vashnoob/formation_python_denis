

#str
chemin_fichier = "C:/Windows/System32/f.txt" # chaine de caracts / str
print( type( chemin_fichier ) )

# int
taille = 5400
print(type(taille))

# float
prix_produit = 85.10
print(type(prix_produit))

# bool
est_actif = True
est_disponible = False
print(type(est_actif))

# print(type(cpx)) PAS ENCORE DEFINI

cpx = 3j + 5
print(type(cpx))

#du type decoule les possibilites d'utilisations

# .....
# perturbant - change le type de la variable cpx
# cpx = "Complex chaine"
print(type(cpx))


taux_tva = 20.0
prix_ht = 200

#Conversion  :
message= "Prix TTC : "

prix_ttc = prix_ht * (1 + taux_tva/100)   #  CAST IMPLICITE - TRANSTYPER

prix_ttc = int(prix_ttc) # CAST EXPLICITE

print(prix_ttc , type(prix_ttc))

resultat = message + str(prix_ttc)
print(resultat)

texte = '19.5'
print(float(texte) / 100) # pas int car parse

print('Valeur' + str(taux_tva)) #operateur + ext- contextuel

print('Valeur ' * 10 ) #operateur + ext- contextuel

texte:str = "ronaldo drumond"
#Notation POO
print(texte.upper())

