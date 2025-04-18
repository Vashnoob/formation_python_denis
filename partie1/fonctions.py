

def multipliepar2(x):
    c = 2*x
    return c

def cote_triangle(x,y):
    return (x**2 +y**2)**0.5


def affiche(x,y):
    c = (x**2 +y**2)**0.5
    print(c)

r = multipliepar2(5)
s = cote_triangle(3,4) #appel par positions
s = cote_triangle(y=3,x=5) #appel par keyword
print(s)
x = affiche(5,6)
print(x)

#passage de parametres
def info(nom, prenom, ville):
    pass

info("ally","john", "limoges")
info(ville="limoges",nom="ally",prenom="john")

#position puis mots cles
open("wuz.txt","rt",-1,"iso-8859-1") # mixte


def mafonction(a, b=bool) -> list[str]:
    pass


# docstring
def foo(a: int, b: float, c: str) -> list:
    """
    Cette fonction calcul le petrimetre
    a:int : un cote
    """







foo(1,2,"")
