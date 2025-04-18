# 🐍 Mini-guide Python - Bases procédurales
import math
import time
im
## 9. Structures Conditionnelles


## 10. Opérateurs Logiques et de Comparaison


## 11. Boucles `while` et `for`
stop =False
while not stop:  # fin inattendue
    print("Je continue")
    saisie = input("Q pour stopper")
    saisie = saisie.lower()
    stop = saisie=="q"

def supercomplique(c):
    time.sleep(20)
    return c

## 12. `break` et `continue`
for i in range(100):
    calc = math.sqrt(i **2 + i**3)
    if i==50 or supercomplique(calc) \
        and calc>10:
        break

for i in range(100):
    calc = math.sqrt(i **2 + i**3)
    if calc > 100:
        continue   # la boucle
    print(i)



## 13. La Fonction `range()`


## 14. Fonctions et Documentation
def foo(a:int, b:float,c:str) -> list:
    """

    """

## 15. Expressions Lambda


## 16. Générateurs
#range() est un generateur

## 17. Structuration en Modules








