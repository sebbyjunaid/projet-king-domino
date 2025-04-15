"""
Partie C : Pile de Dominos
Cette partie contient les fonctions qui permettent de lire les dominos depuis un fichier
CSV (fournie dans la squellette donnée)et aussi gérer le dictionnaire contenant le choix des joueurs.

"""

import random


def extraire_dominos(nom_fichier):
    """Lit un fichier CSV et renvoie la liste mélangée des dominos ."""

    dominos = []
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            parts = ligne.strip().split(";")
            identifiant = int(parts[0])
            case_gauche = parts[1]
            case_droite = parts[2]
            dominos.append((identifiant, case_gauche, case_droite))

    random.shuffle(dominos)
    return dominos

l = extraire_dominos("dominos.csv")
print(len(l))
print(type(l[0]))
print(l[0])

def extraire_premier_bloc(liste_dominos):
    """Renvoie une nouvelle liste contenant les 4 premiers dominos triés selon leur identifiant."""

    bloc = liste_dominos[:4]


    for i in range(len(bloc)):
        min_index = i
        for j in range(i + 1, len(bloc)):
            if bloc[j][0] < bloc[min_index][0]:
                min_index = j
        bloc[i], bloc[min_index] = bloc[min_index], bloc[i]

    return bloc

liste_test = [
    (6, 'F0', 'F0'), (1, 'Y0', 'Y0'), (3, 'F0', 'F0'),
    (2, 'Y0', 'Y0'), (4, 'F0', 'F0'), (5, 'F0', 'F0'), (7, 'B0', 'B0')
]

first = extraire_premier_bloc(liste_test)
print(first)
print(len(liste_test))

def piocher_bloc(liste_dominos):
    """Extrait et trie les 4 premiers dominos, puis les retire de la liste d’origine."""

    bloc = liste_dominos[:4]
    del liste_dominos[:4]


    for i in range(len(bloc)):
        min_index = i
        for j in range(i + 1, len(bloc)):
            if bloc[j][0] < bloc[min_index][0]:
                min_index = j
        bloc[i], bloc[min_index] = bloc[min_index], bloc[i]

    return bloc
liste_test = [
    (6, 'F0', 'F0'), (1, 'Y0', 'Y0'), (3, 'F0', 'F0'),
    (2, 'Y0', 'Y0'), (4, 'F0', 'F0'), (5, 'F0', 'F0'), (7, 'B0', 'B0')
]

resultat = piocher_bloc(liste_test)
print("Bloc trié :", resultat)
print("Liste restante :", liste_test)

def remplir_choix(liste_dominos, dico_choix):
    """Remplit ou vide le dictionnaire de choix selon le contenu de la liste de dominos."""

    if liste_dominos == []:

        for key in list(dico_choix.keys()):
            del dico_choix[key]
    else:
        bloc = piocher_bloc(liste_dominos)
        for i in range(4):
            dico_choix[i + 1] = [bloc[i], None]
liste_test = [
    (6, 'F0', 'F0'), (1, 'Y0', 'Y0'), (3, 'F0', 'F0'),
    (2, 'Y0', 'Y0'), (4, 'F0', 'F0'), (5, 'F0', 'F0'), (7, 'B0', 'B0')
]
dico_choix = {}

remplir_choix(liste_test, dico_choix)
print(dico_choix)
print(liste_test)

remplir_choix([], dico_choix)
print(len(dico_choix))

def afficher_choix_ou_depot(dico):
    """La fonction afficher_choix_ou_depot affiche le contenu d'un dictionnaire de choix de dépot des joueurs
    Elle affiche le dictionnaire de manière lisible."""
    for i in range(1,5):
        print(i, "- Domino", dico[i][0], "Joueur", dico[i][1])


