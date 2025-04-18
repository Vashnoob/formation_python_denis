#Calcul de  base
"""
celsius <-> farenheit
Transformer
"""
print("DEBUT")
#celcius = input("Donne moi un temperature °C :")
celcius = "10.00"
celcius = float(celcius) #typage explicite
farenheit = (celcius * 9/5) + 32
re_celsius= (farenheit - 32) * 5/9
print(farenheit, celcius, re_celsius, sep=" / ")  # 3 sur la meme ligne

# Ouvre un fichier (EXPLICATION A VENIR)
f = open('../listedemots.txt', encoding="utf-8")
phrase = f.readline()
f.close()
print(type(phrase), phrase)

f = open('../listedemots.txt')
phrases = f.readlines()
f.close()

print(type(phrases), phrases)

#MANIP DE STR
# du point de vue str
est_equipe =phrase.startswith("Equipe") # variable.fonction 'converti, test, affiche
print(est_equipe)

#1 CAR (STR)
print(phrase[0]) # 1er
print(phrase[5]) # 6eme

#SLICING
print(phrase[0:5])
print(phrase[:10])
print(phrase[10:])
print(phrase[:])


print(phrase[3:13:2])
print(phrase[:13:2])
print(phrase[3::2])
print(phrase[::2]) # Les caracs en position 0,2,4, PAIR
print(phrase[1::2]) # Les caracs en position 0,2,4, IMPAIR
# chaine[start:end:step]

print(phrase[-2]) # -1 = \n

print(phrase[-5:-2]) # -1 = \n
print(phrase[:-12]) # -1 = \n
print(phrase[-8:-2:2]) # -1 = \n

print(phrase[::-1]) # -1 = \n

nom_participant = "HELAKHALFALLAH"
print(nom_participant[::-1])
print("AURELIENHERVE"[::-1])

autre_nom= "GAETANDOLIGE"[::-1]
print(list(autre_nom))

# EXPLOITE LE COTE SEQUENTIEL
nombres =[1,2,3,4,5,6]
print(nombres)
print(nombres[::-1], nombres[-1], sep='#')







