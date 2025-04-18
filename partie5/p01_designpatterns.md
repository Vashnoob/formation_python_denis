# 🧠 Introduction aux Design Patterns (Modèles de Conception)

## 📌 Qu’est-ce qu’un Design Pattern ?

Un **design pattern** est une solution **générique, réutilisable et éprouvée** à un problème courant de conception logicielle.  
Ils ne sont **pas du code prêt-à-l’emploi**, mais plutôt des **schémas conceptuels** qui peuvent être adaptés selon le contexte.

---

## 🎯 Pourquoi utiliser des Design Patterns ?

- Favoriser un **code plus lisible**, modulaire et extensible
- Résoudre des **problèmes récurrents** de manière élégante
- Créer un **langage commun** entre développeurs
- Faciliter la **maintenance** et les évolutions logicielles

---

## 🧭 Les grandes familles de Design Patterns

| Catégorie             | Objectif principal                                      | Exemples typiques                             |
|----------------------|----------------------------------------------------------|------------------------------------------------|
| **Création (Creational)** | Gérer la création d’objets                               | Singleton, Factory Method, Builder             |
| **Structure (Structural)** | Organiser les relations entre classes/objets             | Decorator, Adapter, Composite, Proxy           |
| **Comportement (Behavioral)** | Gérer la communication entre objets / le comportement | Strategy, Observer, Command, State, Iterator   |

---

## 🐍 Design Patterns et Python

Python est un langage **hautement flexible et expressif** :  
→ Beaucoup de patterns issus de langages comme Java deviennent **plus simples ou même inutiles** en Python, car :

- Les **fonctions sont des objets** → facilite Strategy, Command, Decorator
- Il n’y a pas de mot-clé `interface`, mais on a `ABC` et le duck typing
- L’instanciation est dynamique → Factory et Builder sont souvent remplacés par de simples fonctions
- L’encapsulation est souple → moins de besoin de Proxy ou Facade

---

## 💡 Patterns quasiment "natifs" en Python

| Pattern traditionnel     | Version Python native possible                       |
|--------------------------|-------------------------------------------------------|
| **Strategy**             | Passer une fonction en paramètre (`callable`)        |
| **Decorator**            | Fonction décoratrice `@decorator`                    |
| **Command**              | Une lambda ou une closure                            |
| **Iterator**             | Déjà intégré via `__iter__`, `__next__`              |
| **Singleton**            | Implémentable via module, ou `__new__`               |
| **Observer**             | Liste de fonctions callback ou signaux               |
| **Factory**              | Fonction conditionnelle ou lambda                    |

---

## 🛠️ Quand les utiliser ?

Utilise un design pattern **quand** :
- Tu rencontres un **problème structurel récurrent**
- Tu veux **rendre ton code plus souple et maintenable**
- Tu travailles **en équipe** avec besoin de lisibilité / standard

Mais **évitez le surdesign**. pragmatisme avant tout
Python offre souvent des **alternatives plus légères**.
