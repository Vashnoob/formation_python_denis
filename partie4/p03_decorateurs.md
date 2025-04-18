
## Les décorateurs

En Python, les **fonctions sont des objets de première classe**. Cela signifie qu'elles peuvent être stockées dans des variables, passées en argument à d'autres fonctions, ou même retournées par d'autres fonctions. C'est ce principe qui permet de créer les **décorateurs** : des fonctions qui prennent une autre fonction en argument, et qui renvoient une fonction modifiée ou enrichie.

### 🔹 Syntaxe de base

Un décorateur est une fonction qui **enveloppe** une autre fonction :

```python
def mon_decorateur(fonction):
    def fonction_modifiee(*args, **kwargs):
        print("Avant l'appel")
        resultat = fonction(*args, **kwargs)
        print("Après l'appel")
        return resultat
    return fonction_modifiee
```

On applique un décorateur à une fonction avec la syntaxe `@nom_du_decorateur` :

```python
@mon_decorateur
def saluer():
    print("Bonjour !")

saluer()
```

### 🔹 Exemple 1 : Un décorateur simple de journalisation

```python
def log(fonction):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Appel de {fonction.__name__} avec {args}, {kwargs}")
        return fonction(*args, **kwargs)
    return wrapper

@log
def addition(a, b):
    return a + b

addition(3, 4)
```

### 🔹 Exemple 2 : Un décorateur avec des arguments

Pour créer un décorateur paramétrable (ex : qui accepte une configuration), on ajoute un niveau de fonction supplémentaire :

```python
def repeter(n):
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fonction(*args, **kwargs)
        return wrapper
    return decorateur

@repeter(3)
def dire_hello():
    print("Hello !")

dire_hello()
```

### 🔹 Exemple 3 : Préserver les métadonnées d’une fonction

Quand on utilise un décorateur, le nom et la docstring de la fonction décorée sont remplacés par ceux du wrapper. Pour les conserver, on utilise `functools.wraps` :

```python
import functools

def log(fonction):
    @functools.wraps(fonction)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Appel de {fonction.__name__}")
        return fonction(*args, **kwargs)
    return wrapper
```

---

### ⚙️ Cas d’usage courants

#### ✅ Logging et debugging

```python
def debug(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(f"Appel : {f.__name__}({args}, {kwargs})")
        result = f(*args, **kwargs)
        print(f"Résultat : {result}")
        return result
    return wrapper
```

#### ✅ Contrôle d’accès

```python
def admin_only(f):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            raise PermissionError("Accès refusé")
        return f(user, *args, **kwargs)
    return wrapper

@admin_only
def supprimer_utilisateur(user, utilisateur_id):
    print(f"Suppression de l'utilisateur {utilisateur_id}")
```

#### ✅ Mémoïsation (caching)

```python
def memoize(f):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def factorielle(n):
    return 1 if n == 0 else n * factorielle(n - 1)
```

---
