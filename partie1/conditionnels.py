
nom = "frederic"

if nom.startswith("c"):
    print("commence par c effectivement")

if nom[0] == "c":
    print("commence par c effectivement")

x = 2
condition = x**0.5 > 2
if condition:
    print("Un racinecarre est >2")
else:
    print("Un carre est <= 2")

sequence = {1, 2, 4, 8, 16}
if 4 in sequence:
    print("4")


dico = {  "two" : 2, 'four' :4, "one" : 1, "un" : 1 , 3: "three" }
if "three" in dico:  #equivalent a dico.keys()
    print("three trouvé")
else:
    print("pas trouve three")

if "three" in dico.values():  #equivalent a dico.keys()
    print("three trouvé dans valeurs")
else:
    print("pas trouve three")

val = int(input("Saisir un chiffre "))
match val:
    case 0:
        print("Zero")
    case 5:
        print("Five")
    case _:
        print("Don t know")

#--------------
# manipule dico dans une boucle

employes = {"aurelien","caroline",'benoit','jean-christophe'}
foot = {"caroline",'benoit','vivian'}

for employe in employes:
    print(employe)

dico = {  "two" : 2, 'four' :4, "one" : 1, "un" : 1 , 3: "three" }
for cle in dico:
    print(cle, dico[cle])

print(dico.items())

for t in dico.items():
    print(t[0] , ">>>>", t[1])

print("--------------------")
for cle,val in dico.items():
    print(cle, ">>>>", val)

print("----FIN----")