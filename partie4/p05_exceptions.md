# La gestion des erreurs avec les exceptions

Python utilise un **système d’exceptions** pour signaler et gérer les erreurs pendant l'exécution. Lorsqu'une erreur survient, Python interrompt le programme et **lève une exception**. Ce mécanisme permet de séparer le flux normal d'exécution de la gestion des cas d'erreur.

---

### 🔹 Syntaxe de base : `try / except / else / finally`

```python
try:
    # Code pouvant lever une exception
    resultat = 10 / 2
except ZeroDivisionError:
    print("Division par zéro !")
else:
    print("Pas d'erreur, résultat :", resultat)
finally:
    print("Bloc toujours exécuté")
```

- `try` : bloc où une erreur peut survenir
- `except` : capture l’exception et exécute du code alternatif
- `else` : exécuté si **aucune exception** ne survient
- `finally` : exécuté **dans tous les cas** (utile pour libérer des ressources)

---

### 🔹 Exemple 1 : Gestion d’une exception standard

```python
def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Fichier introuvable."

print(lire_fichier("inexistant.txt"))
```

---

### 🔹 Exemple 2 : Lever une exception avec `raise`

Vous pouvez déclencher une exception manuellement avec `raise` :

```python
def retirer(montant):
    if montant < 0:
        raise ValueError("Le montant doit être positif")
    print(f"Vous avez retiré {montant}€")

retirer(-10)  # Provoque une ValueError
```

---

### 🔹 Exemple 3 : Créer ses propres exceptions

Vous pouvez définir une **exception personnalisée** en héritant de la classe `Exception`. Cela permet de mieux représenter les erreurs métiers spécifiques à votre application.

```python
class AccesInterdit(Exception):
    """Exception levée quand un utilisateur non autorisé tente un accès."""
    pass

def consulter_dossier(user):
    if not user.get("autorisé"):
        raise AccesInterdit("Accès refusé à l'utilisateur")

try:
    consulter_dossier({"nom": "Bob", "autorisé": False})
except AccesInterdit as e:
    print("Erreur :", e)
```

---

### 🔸 Héritage et hiérarchie d’exceptions

Créer une **hiérarchie d’exceptions personnalisées** permet d’organiser votre code et de gérer des groupes d’erreurs plus facilement.

```python
class ErreurApplication(Exception):
    """Classe de base pour les exceptions de l'application."""
    pass

class AccesInterdit(ErreurApplication):
    pass

class DonneeInvalide(ErreurApplication):
    pass
```

On peut ensuite capturer :

- un cas spécifique (`except AccesInterdit`)
- ou tous les cas métiers (`except ErreurApplication`)

```python
try:
    raise DonneeInvalide("Champ email vide")
except AccesInterdit:
    print("Accès refusé")
except ErreurApplication as e:
    print("Erreur métier :", e)
```

✔️ Cette approche est utile pour regrouper toutes les erreurs "métier" dans les projets structurés.

---

### 🔹 Exemple 4 : Gestion fine avec plusieurs `except`

```python
try:
    x = int(input("Entrez un entier : "))
    resultat = 10 / x
except ValueError:
    print("Ce n'est pas un entier valide.")
except ZeroDivisionError:
    print("Division par zéro interdite.")
else:
    print("Résultat :", resultat)
```

---

### ✅ Bonnes pratiques

- 🎯 **Ciblez les exceptions spécifiques** pour ne pas masquer d'autres erreurs.
- 🧼 **Limitez le bloc `try`** à ce qui peut effectivement échouer.
- 🪛 **Utilisez vos propres classes d’exception** pour mieux structurer votre application.
- 💡 **Évitez `except:` seul** qui capture tout, y compris les erreurs système (`KeyboardInterrupt`, `SystemExit`...).
- 🧪 **N'hésitez pas à logguer ou propager (`raise`) l’exception si vous ne pouvez pas la gérer correctement.**
