import datetime
import math
import pprint

#>>>>>>>> ... EN COMPREHENSION

#PAS PYTHONIC
nombres = [1.0,2.0,5.0,8.5]
racines = []
for n in nombres:
    racines.append( math.sqrt(n))
print(racines)

#PYTHONIC
# liste
racines = [math.sqrt(n) for n in nombres]
print(racines)

sracines = {math.sqrt(n) for n in nombres}
print(sracines)

dracines = {n:math.sqrt(n) for n in nombres}
print(dracines)

#PAS PYTHONIC
#>>>>>>>> TEST INLINE
# test in ligne / inlinbe / ternaire
a_tester = 8
a = 5
if a_tester> 6:
    a = 10

#PYTHONIC
a = 10 if a_tester>6 else 5   #ternaire

#CONTEXT MANAGER
#PAS PYTHONIC
f = open("f.txt",mode="w")
f.close()

f = open("f.txt")
f.read()
f.close()

#INPUT/OUTPUT
with open("f.txt") as f:
    f.read()


#LAMBDA
#lambda
def maxi(liste_valeurs):
    return max(liste_valeurs)

def queljoureston():
    return datetime.date.today()

maxil = lambda lv,xy : xy*max(lv)
maxil([1,2,3],5)

queljour = lambda : datetime.date.today()
aujourdhui = queljour()
td = datetime.timedelta(days=63)

avant = aujourdhui - td
print(avant)
print(avant.weekday())

#GENERATEUR
#range
liste_valeurs = [1,2,3,4,5,None,1000000]

for lv in range(1000000):
    # print(lv) <- economiser de la memoire
    pass
#exemple : read, ,readline de file.read()

#
val1 = 5
val2 = math.sqrt(2)+0.0005
val3 = "fin"
message = "v={} racine={} mot:{}".format(val1,val2,val3)
print(message)

message = "v={:06d} racine={:1.3f} mot:{:<30}...".format(val1,val2,val3)
print(message)

message = f"v={val1:06d} racine={val2:1.3f} mot:{val3:<30}..."
print(message)


pprint

data = {
    "vol": "AF123",
    "aeroport": {
        "depart": {"code": "CDG", "ville": "Paris"},
        "arrivee": {"code": "JFK", "ville": "New York"}
    },
    "passagers": [
        {"nom": "Alice", "bagages": 2},
        {"nom": "Bob", "bagages": 1}
    ]
}

print(data["aeroport"]["depart"]["code"])
pprint.pprint(data, indent=5)
print(data)