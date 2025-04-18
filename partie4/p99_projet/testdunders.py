from partie3.modele import Trajet

liste = [1,2,3,4,5]
print((len(liste)))

print(liste)

tr1 = Trajet("A","B",105)
tr2 = Trajet("B","C",105)

print(len(tr1))
print(tr1 == tr2)
print(tr1 == 105.0)


tr3 = Trajet("Angers","Biarritz",105)
tr4 = Trajet("Angers","Bordeaux",105)

"""
print("tr1<106", tr1 < 106)
print("tr1<104", tr1 < 104)

print("Biarritz<Bordeaux", tr3 < tr4)
print("Bordeaux<Biarritz", tr4 < tr3)

"""
trajets = [tr4,tr2,tr3,tr1]
s_trajets = sorted(trajets)

print(trajets)

trajets.sort()

print(trajets)

tr5 = tr3 + tr4
print(id(tr5),tr5)
tr5 = tr5 + 50          #add
print(id(tr5),tr5)

print(id(tr5),tr5)
tr5+=100                #iadd
print(id(tr5),tr5)

s = int(tr1)/ 1.6
print(s)