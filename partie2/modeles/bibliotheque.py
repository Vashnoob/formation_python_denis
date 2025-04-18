from partie2.modeles.livre import Livre



class Bibliotheque:

    def __init__(self, capacite):
        self._capacite = capacite
        self._livres = []

    def ajouter_livre(self, livre):
        if len(self._livres) < self._capacite:
            self._livres.append(livre)

    def retirer_livre(self, livre):
        self._livres.remove(livre)

    def rechercher(self, titre):
        for livre in self._livres:
            if livre.titre() == titre:
                return livre
        return None

    def inventaire(self):
        return self._livres

if __name__ == "__main__":
    biblio = Bibliotheque(5)
    biblio.ajouter_livre(Livre("../../data/pg17989_compte_monte_cristo.txt", "Monte Christo"))
    biblio.ajouter_livre(Livre("../../data/pg2413_bovary.txt","Mme Bovary"))

    for m in ('vengeance','joie'):
        for lv in biblio.inventaire():
            print(f"{lv.titre} => {lv.ratio(m):.10f}")
            lv.titre = lv.titre + " le retour"
            print(lv)