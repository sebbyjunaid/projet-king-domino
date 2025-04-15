def creerRoyaume(taille=7):
    

    if taille < 0 or taille % 2 == 0:
        print("Impossible de créer un royaume : 'taille' est pair ou négatif")
        return None
    else:
        royaume = [[None for _ in range(taille)] for _ in range(taille)]
        milieu = taille // 2
        royaume[milieu][milieu] = "CH"
        return royaume

royaume = creerRoyaume(5)
print(royaume)
royaume[0][0] = 'Y1'
print(royaume)
print(creerRoyaume())
print(creerRoyaume(6))


def init_tuple_royaumes(taille=7):
    

    royaume1 = creerRoyaume(taille)
    royaume2 = creerRoyaume(taille)

    return (royaume1, royaume2)
tup = init_tuple_royaumes(5)
tup[0][0][0] = "Y0"
print(tup[0])
print(tup[1])

def afficherCoordonnees(royaume):
    
    n = len(royaume)
    for i in range(n):
        for j in range(n):
            print("|"+str((i,j)), end ="")
        print("|")

    royaume = creerRoyaume(5)
    afficherCoordonnees(royaume)

def init_cases_libres(taille):
   
    cases = []
    centre = taille // 2
    for i in range(taille):
        for j in range(taille):
            if (i, j) != (centre, centre):
                cases.append((i, j))
    return cases
print(init_cases_libres(3))

def init_tuple_libres(taille):
   

    libres1 = init_cases_libres(taille)
    libres2 = init_cases_libres(taille)
    return (libres1, libres2)

tup = init_tuple_libres(5)
tup[0].remove((0, 0))
print(len(tup[0]))
print(len(tup[1]))


def afficherRoyaume(royaume, joueur="A", vide="  "):
    

    n = len(royaume)

    print("––––" * (n + 1))
    print(f"Joueur {joueur}")

    # En-tête des colonnes
    print("-  ", end="")
    for col in range(n):
        print(f" {col}", end="")
    print()

    # Corps du royaume
    for i in range(n):
        print(f"({i},_) ", end="")
        for j in range(n):
            case = royaume[i][j]
            if case is None:
                print(f"|{vide}", end="")
            else:
                print(f"|{case}", end="")
        print("|")

    print("––––" * (n + 1))
royaume = creerRoyaume(5)
royaume[1][0] = 'Y0'
royaume[2][3] = 'B1'
afficherRoyaume(royaume)


def partie_droite_domino(posL, posC, dir):
    

    if dir == "left":
        return (posL, posC + 1)
    elif dir == "right":
        return (posL, posC - 1)
    elif dir == "top":
        return (posL + 1, posC)
    elif dir == "bottom":
        return (posL - 1, posC)
    else:
        print(f"Direction mal renseignée : {dir}")
        return None
    print(partie_droite_domino(12, -3, 'left'))
    print(partie_droite_domino(5, 5, 'bottom'))
    print(partie_droite_domino(3, 3, 'nimportequoi'))

def espaceLibre(royaume, posL, posC, dir):
    
    n = len(royaume)


    if not (0 <= posL < n and 0 <= posC < n):
        return False


    pos_droite = partie_droite_domino(posL, posC, dir)
    if pos_droite is None:
        return False

    posL2, posC2 = pos_droite


    if not (0 <= posL2 < n and 0 <= posC2 < n):
        return False


    if royaume[posL][posC] is None and royaume[posL2][posC2] is None:
        return True
    else:
        return False


royaume = creerRoyaume(5)
royaume[0][0] = 'Y0'
royaume[0][1] = 'F0'
royaume[1][0] = 'M2'
royaume[1][1] = 'B1'

afficherRoyaume(royaume)

print(espaceLibre(royaume,0,0,"left"))
print(espaceLibre(royaume,0,1,"left"))
print(espaceLibre(royaume,5,1,"bottom"))
print(espaceLibre(royaume,1,4,"left"))
print(espaceLibre(royaume,4,2,"top"))
print(espaceLibre(royaume,2,3,"right"))
print(espaceLibre(royaume,2,3,"xyz"))

def ajoutDomino(royaume, cases_libres, domino, posL, posC, dir):
   
    if espaceLibre(royaume, posL, posC, dir):
        posL2, posC2 = partie_droite_domino(posL, posC, dir)


        royaume[posL][posC] = domino[1]
        royaume[posL2][posC2] = domino[2]


        if (posL, posC) in cases_libres:
            cases_libres.remove((posL, posC))
        if (posL2, posC2) in cases_libres:
            cases_libres.remove((posL2, posC2))
    else:
        print("Le domino " + str(domino) + " ne peut pas être ajouté à l'emplacement " + str(
            (posL, posC)) + " dans la direction " + dir)

royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)
domino1 = (31,'B1','Y0')
domino2 = (32,'B1','F0')
domino3 = (25,'F1','Y0')

ajoutDomino(royaume, cases_libres, domino1, 2, 3, 'left')
ajoutDomino(royaume, cases_libres, domino2, 1, 4, 'left')
ajoutDomino(royaume, cases_libres, domino1, 3, 3, 'bottom')
ajoutDomino(royaume, cases_libres, domino3, 1, 2, 'bottom')
ajoutDomino(royaume, cases_libres, domino3, 0, 0, 'right')
ajoutDomino(royaume, cases_libres, domino3, 2, 1, 'xyz')

afficherRoyaume(royaume)
print(len(cases_libres))

def voisinages(royaume, posL, posC, libres=False):
    

    n = len(royaume)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    voisins = []

    for dL, dC in directions:
        i, j = posL + dL, posC + dC
        if 0 <= i < n and 0 <= j < n:
            if not libres or royaume[i][j] is None:
                voisins.append((i, j))

    return voisins
royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)
domino1 = (31,'B1','Y0')
ajoutDomino(royaume,cases_libres,domino1,2,3,'left')

afficherRoyaume(royaume)

print(voisinages(royaume, 2, 1))
print(voisinages(royaume, 1, 3))
print(voisinages(royaume, 1, 3, True))

def domino_valide(royaume, domino, posL, posC, dir):
   
    if not espaceLibre(royaume, posL, posC, dir):
        return False

    posL2, posC2 = partie_droite_domino(posL, posC, dir)
    contenu1 = domino[1]
    contenu2 = domino[2]
    couleur1 = contenu1[0]
    couleur2 = contenu2[0]

    voisins1 = voisinages(royaume, posL, posC)
    voisins2 = voisinages(royaume, posL2, posC2)


    for i, j in voisins1:
        case = royaume[i][j]
        if case is not None and (case == "CH" or case[0] == couleur1):
            return True


    for i, j in voisins2:
        case = royaume[i][j]
        if case is not None and (case == "CH" or case[0] == couleur2):
            return True

    return False

royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)

domino1 = (31,'B1','Y0')
domino2 = (32,'B1','F0')
domino3 = (25,'F1','Y0')
domino4 = (1,'Y0','Y0')

ajoutDomino(royaume, cases_libres, domino1, 2, 3, 'left')
ajoutDomino(royaume, cases_libres, domino3, 1, 2, 'bottom')

afficherRoyaume(royaume)

print(domino_valide(royaume, domino4, 2, 1, 'right'))
print(domino_valide(royaume, domino4, 0, 0, 'left'))
print(domino_valide(royaume, domino4, 0, 0, 'right'))
print(domino_valide(royaume, domino2, 0, 0, 'left'))
print(domino_valide(royaume, domino3, 0, 1, 'right'))

def domino_possible(royaume, cases_libres, domino):
   

    directions = ['left', 'right', 'top', 'bottom']

    for posL, posC in cases_libres:
        for dir in directions:
            if domino_valide(royaume, domino, posL, posC, dir):
                return True
    return False


royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)
domino = (3,'F0','F0')
domino1 = (1,'Y0','Y0')
domino2 = (13,'Y0','F0')


ajoutDomino(royaume,cases_libres,domino,2,3,'left')
ajoutDomino(royaume,cases_libres,domino,1,2,'bottom')
ajoutDomino(royaume,cases_libres,domino,3,2,'top')
ajoutDomino(royaume,cases_libres,domino,2,1,'right')


print(domino_possible(royaume, cases_libres, domino1))
print(domino_possible(royaume, cases_libres, domino2))

afficherRoyaume(royaume)


def creerRoyaume(taille=7):
   

    if taille < 0 or taille % 2 == 0:
        print("Impossible de créer un royaume : 'taille' est pair ou négatif")
        return None
    else:
        royaume = [[None for _ in range(taille)] for _ in range(taille)]
        milieu = taille // 2
        royaume[milieu][milieu] = "CH"
        return royaume

royaume = creerRoyaume(5)
print(royaume)
royaume[0][0] = 'Y1'
print(royaume)
print(creerRoyaume())
print(creerRoyaume(6))


def init_tuple_royaumes(taille=7):
    

    royaume1 = creerRoyaume(taille)
    royaume2 = creerRoyaume(taille)

    return (royaume1, royaume2)
tup = init_tuple_royaumes(5)
tup[0][0][0] = "Y0"
print(tup[0])
print(tup[1])

def afficherCoordonnees(royaume):
   
    n = len(royaume)
    for i in range(n):
        for j in range(n):
            print("|"+str((i,j)), end ="")
        print("|")

    royaume = creerRoyaume(5)
    afficherCoordonnees(royaume)

def init_cases_libres(taille):
   

    cases = []
    centre = taille // 2
    for i in range(taille):
        for j in range(taille):
            if (i, j) != (centre, centre):
                cases.append((i, j))
    return cases
print(init_cases_libres(3))


def init_tuple_libres(taille):
   
    libres1 = init_cases_libres(taille)
    libres2 = init_cases_libres(taille)
    return (libres1, libres2)

tup = init_tuple_libres(5)
tup[0].remove((0, 0))
print(len(tup[0]))
print(len(tup[1]))


def afficherRoyaume(royaume, joueur="A", vide="  "):
   

    n = len(royaume)

    print("––––" * (n + 1))
    print(f"Joueur {joueur}")

    # En-tête des colonnes
    print("-  ", end="")
    for col in range(n):
        print(f" {col}", end="")
    print()

    # Corps du royaume
    for i in range(n):
        print(f"({i},_) ", end="")
        for j in range(n):
            case = royaume[i][j]
            if case is None:
                print(f"|{vide}", end="")
            else:
                print(f"|{case}", end="")
        print("|")

    print("––––" * (n + 1))
royaume = creerRoyaume(5)
royaume[1][0] = 'Y0'
royaume[2][3] = 'B1'
afficherRoyaume(royaume)







import random

def extraire_dominos(nom_fichier):
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

# Test
l = extraire_dominos("dominos.csv")
print("Nombre de dominos chargés :", len(l))
print("Premier domino :", l[0])

def extraire_premier_bloc(liste_dominos):
    

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
    
    for i in range(1,5):
        print(i, "- Domino", dico[i][0], "Joueur", dico[i][1])


#from B_gestion_dominos import *
import random

def init_tuple_joueurs(perso=False):
    
    nom_A = "A"
    nom_B = "B"


    if perso:
        nom_A = input("Nom du premier joueur : ")
        nom_B = input("Nom du second joueur : ")

    return nom_A, nom_B

def init_configurations(tuple_joueurs):
    
    joueur_A, joueur_B = tuple_joueurs
    config = {}

    # Choix mode pour joueur A
    mode_A = input(f"Mode de jeu pour {joueur_A} ? (manuel / random) : ").strip().lower()
    while mode_A not in ["manuel", "random"]:
        mode_A = input("Veuillez saisir 'manuel' ou 'random' : ").strip().lower()

    # Choix mode pour joueur B
    mode_B = input(f"Mode de jeu pour {joueur_B} ? (manuel / random) : ").strip().lower()
    while mode_B not in ["manuel", "random"]:
        mode_B = input("Veuillez saisir 'manuel' ou 'random' : ").strip().lower()

    config[joueur_A] = mode_A
    config[joueur_B] = mode_B

    return config

print(init_configurations(("Alex", "Bob")))

def pose_domino_manuel(royaume, cases_libres, domino, joueur="A"):
   

    print(f"\n>>> Royaume actuel de {joueur} :")
    afficherRoyaume(royaume, joueur)
    print(f"{joueur}, vous devez poser le domino suivant :", domino)

    placement_valide = False
    while not placement_valide:
        try:
            ligne = int(input("Ligne de la case gauche du domino : "))
            colonne = int(input("Colonne de la case gauche du domino : "))
            direction = input("Direction du domino (left, right, top, bottom) : ").strip().lower()

            if domino_valide(royaume, domino, ligne, colonne, direction):
                ajoutDomino(royaume, cases_libres, domino, ligne, colonne, direction)
                placement_valide = True
            else:
                print("❌ Placement invalide. Veuillez réessayer.")
        except ValueError:
            print("⚠️ Entrée invalide. Veuillez entrer des nombres valides pour la ligne et la colonne.")

royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)
domino1 = (31,'B1','Y0')
domino2 = (32,'B1','F0')
domino3 = (25,'F1','Y0')

ajoutDomino(royaume,cases_libres,domino1,2,3,'left')
ajoutDomino(royaume,cases_libres,domino2,1,2,'bottom')
ajoutDomino(royaume,cases_libres,domino3,0,1,'right')

afficherRoyaume(royaume,"Alice")

pose_domino_manuel(royaume, cases_libres, (33, "S0", "S0"), "Alice")

import random


def pose_domino_random(royaume, cases_libres, domino, joueur="A", TENTATIVES=10000):
    

    directions = ['left', 'right', 'top', 'bottom']

    for _ in range(TENTATIVES):
        posL, posC = random.choice(cases_libres)
        dir = random.choice(directions)

        if domino_valide(royaume, domino, posL, posC, dir):
            ajoutDomino(royaume, cases_libres, domino, posL, posC, dir)
            print(f"{joueur} a placé le domino {domino} automatiquement en ({posL}, {posC}) vers {dir}.")
            return  

    
    print(f"❌ Échec : {joueur} n’a pas pu poser le domino {domino} après {TENTATIVES} tentatives.")

royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)
domino = (3,'F0','F0')
domino1 = (1,'Y0','Y0')
domino2 = (13,'Y0','F0')

# Remplissage manuel
ajoutDomino(royaume,cases_libres,domino,2,3,'left')
ajoutDomino(royaume,cases_libres,domino,1,2,'bottom')
ajoutDomino(royaume,cases_libres,domino,3,2,'top')
ajoutDomino(royaume,cases_libres,domino,2,1,'right')

afficherRoyaume(royaume, "Bob")

# Pose aléatoire automatique
pose_domino_random(royaume, cases_libres, domino1, "Bob")
pose_domino_random(royaume, cases_libres, domino2, "Bob")

def pose_domino(royaume, cases_libres, domino, dico_configurations, joueur):
    """
    Pose un domino pour un joueur selon son mode (manuel ou random), en appelant la bonne fonction.
    Si le domino n’est pas posable, affiche un message.
    """
    if domino_possible(royaume, cases_libres, domino):
        mode = dico_configurations[joueur]
        if mode == 'manuel':
            pose_domino_manuel(royaume, cases_libres, domino, joueur)
        elif mode == 'random':
            pose_domino_random(royaume, cases_libres, domino, joueur)
    else:
        print(f"⚠️ Le domino {domino} ne peut pas être posé dans le royaume du joueur {joueur}.")

config = {'Alice': 'manuel', 'Bob': 'random'}
pose_domino(royaume, cases_libres, domino1, config, "Bob")


from F_score import score_zone


def statistiques_royaume(royaume):
    
    score_total = 0
    cases_visitees = []
    terrains_scores = {}
    nb_zones = 0
    taille_max_zone = 0
    score_max_zone = 0

    n = len(royaume)
    for i in range(n):
        for j in range(n):
            if (i, j) not in cases_visitees and royaume[i][j] is not None and royaume[i][j] != 'CH':
                score_z, zone = score_zone(royaume, i, j)
                score_total += score_z
                nb_zones += 1
                cases_visitees.extend(zone)

                couleur = royaume[i][j][0]
                terrains_scores[couleur] = terrains_scores.get(couleur, 0) + score_z

                if len(zone) > taille_max_zone:
                    taille_max_zone = len(zone)
                if score_z > score_max_zone:
                    score_max_zone = score_z

    print("\n📊 Statistiques du Royaume :")
    print(f"Score total : {score_total}")
    print(f"Nombre total de zones : {nb_zones}")
    print(f"Plus grande zone (en cases) : {taille_max_zone}")
    print(f"Zone avec score maximum : {score_max_zone}")
    print("\nDétail par type de terrain :")
    for terrain, score in terrains_scores.items():
        print(f"- Terrain '{terrain}' : {score} points")

"""
Extension : Debug
Cela ajoute une commande 'debug' pendant les poses manuelles
pour afficher  :
- Le nombre de cases libres restantes
- Les positions valides pour poser le domino 
- estimation des zones accessibles
"""
from B_gestion_dominos import *

def debug_infos(royaume, cases_libres, domino):
    """Affiche des informations utiles pour le débogage pendant la pose du domino."""
    print("\n===== MODE DEBUG =====")
    print("Cases libres restantes :", len(cases_libres))
    print("Positions valides pour poser le domino", domino, ":")
    count = 0
    for (posL, posC) in cases_libres:
        for dir in ["left", "right", "top", "bottom"]:
            if domino_valide(royaume, domino, posL, posC, dir):
                print(f"- ({posL},{posC}) vers {dir}")
                count += 1
    print(f"Total : {count} positions valides")
    print("======================\n")


def pose_domino_manuel_debug(royaume, cases_libres, domino, joueur="A"):
    """Version manuelle avec support du mode 'debug' pendant la pose."""
    print(f"\n>>> Royaume actuel de {joueur} :")
    afficherRoyaume(royaume, joueur)
    print(f"{joueur}, vous devez poser le domino suivant :", domino)

    while True:
        cmd = input("Tapez ligne (ou 'debug') : ").strip().lower()
        if cmd == "debug":
            debug_infos(royaume, cases_libres, domino)
            continue
        try:
            ligne = int(cmd)
            colonne = int(input("Colonne : "))
            direction = input("Direction (left/right/top/bottom) : ").strip().lower()

            if domino_valide(royaume, domino, ligne, colonne, direction):
                ajoutDomino(royaume, cases_libres, domino, ligne, colonne, direction)
                return
            else:
                print("❌ Placement invalide. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide.")
