
### ✅ Objectif
1. **Sauvegarder** les données (trajets et utilisateurs) à la fin de l’exécution.
2. **Charger** ces données automatiquement au démarrage.

---

### 💾 Format recommandé pour débuter : **JSON**
- Facile à lire, portable, intégré dans Python (`json`)
- Nécessite d’**adapter les objets** pour la sérialisation

---

### ✅ Étapes à implémenter :
1. Ajouter une méthode `to_dict()` dans `Trajet`, `Utilisateur`
2. Ajouter une méthode `from_dict()` pour recréer les objets
3. Créer une couche de **persistence** dans `SystemeReservation`
4. Sauvegarder les données à la sortie
5. Charger les données au démarrage (si fichier présent)

---

### 🔄 On peut le découper comme ceci :
- **Nouveau module** : `sauvegarde.py` (centralise les fonctions de sérialisation)
- Ajout de `to_dict()` / `from_dict()` aux classes concernées
- Appels dans `main()` : `charger_donnees()` et `sauvegarder_donnees()`

