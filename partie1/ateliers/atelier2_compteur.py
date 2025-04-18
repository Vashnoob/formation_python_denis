"""
compter les occurences de chaque mot
les mots d'une ligne sont spearé par des espaces
remplir la structure au fur et a mesure
un fois tout  rempli
on affich les resultats
"""
from utilitaires.textes import clean_line


#definition des fonctions

def lecture_fichier_old(chemin_fichier):
    from string import punctuation

    punctuation= punctuation.replace("-","")
    #extraction (chargement, requete database
    file = open(chemin_fichier, encoding='utf-8')
    lignes = file.read().splitlines()   # mieux que file.readlines()
    #punctuations
    for pos, ligne in enumerate(lignes):
        for c in punctuation:
            ligne = ligne.replace(c," ")

    # minuscules
    lignes = [ l.lower() for l in lignes]

    file.close()


    return lignes # plus un boite noire




def lecture_fichier(chemin_fichier):
    # extraction (chargement, requete database)
    with open(chemin_fichier, encoding='utf-8') as file:

        lignes = file.read().splitlines()  # mieux que file.readlines()

        # nettoyer
        lignes = [clean_line(l) for l in lignes]

    return lignes

def calcul_occurences(lignes, mots_ignores):
    # transformation (calcul, modifier les donnees)
    occurences ={}
    for ligne in lignes:
        #AMELIORATION
        mots = ligne.split(" ")
        for mot in mots:
            if mot not in mots_ignores:
                # ternaire , possible variable intermediaire
                occurences[mot] = 1 if mot not in occurences else occurences[mot]+1
                #################
    return occurences


def affichage(occurences,limite=-1):

    # ----------------------- !!!!!!!!!!!!!!!!!!!!!!!!
    sorted_list = list(occurences.items())
    #lambda
    sorted_list.sort(key=lambda tu:tu[1], reverse=True) # on donne un critere de comparaison <>

    #loading (affichage / sauvegarde / suite calcul)
    for mot,occurence in sorted_list[:limite]:
        #print(mot , " apparait N fois ", occurence)
        print(f"{mot:<20} {occurence:5d} fois")


if __name__=="__main__":
    #appels des fonctions

    phrases = lecture_fichier("../../data/pg17989_compte_monte_cristo.txt")
    stops = lecture_fichier("../../data/stopwords-fr.txt")
    occs = calcul_occurences(phrases,stops)

    affichage(occs,10 )
