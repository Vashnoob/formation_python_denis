from partie3.modele import Utilisateur


class Privileges:

    def gratuite(self):
        pass

    def access_club(self):
        print("access OK")

    def afficher(self):
        print("privileges OK")


class Premium(Privileges,Utilisateur ):

    #possible ambiguité
    def __init__(self, nom):
        Utilisateur.__init__(self, nom)
        #Privileges.__init__(self)

    def calcul_quelconque(self):
        print("Calcul privileges")
        pass

pr1 = Premium("Christophe")
pr1.afficher()
pr1.access_club()


def foo(u:Utilisateur) -> int:
    print(u.nom)
    return u.calcul_quelconque()  # duck typing

p = Premium("john") #pas coherent mais execution OK
foo(p)

p = Utilisateur("john")  # coherent mais execution explose
foo(p)

