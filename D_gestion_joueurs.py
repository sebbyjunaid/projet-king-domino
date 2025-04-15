"""
Partie B : Gestions des joueurs
Cette partie sert à initialiser les joueurs ainsi que lq pose manuelle ou automatique
"""



from B_gestion_dominos import *
import random

def init_tuple_joueurs(perso=False):
    """
    Initialise les noms des deux joueurs.

    Si perso est False , les joueurs s'appellent "A" et "B".
    Si perso est True, on demande à l'utilisateur de saisir les noms des deux joueurs.


    """
    nom_A = "A"
    nom_B = "B"


    if perso:
        nom_A = input("Nom du premier joueur : ")
        nom_B = input("Nom du second joueur : ")

    return nom_A, nom_B

def init_configurations(tuple_joueurs):
    """
    Demande à chaque joueur de choisir son mode de jeu (manuel ou random),
    puis retourne un dictionnaire associant chaque joueur à son mode.

    Args:
        tuple_joueurs (tuple): Noms des deux joueurs

    Returns:
        dict: Configuration des joueurs {joueur: mode}
    """
    joueur_A, joueur_B = tuple_joueurs
    config = {}

    # Choix mode de joueur A
    mode_A = input(f"Mode de jeu pour {joueur_A} ? (manuel / random) : ").strip().lower()
    while mode_A not in ["manuel", "random"]:
        mode_A = input("Veuillez saisir 'manuel' ou 'random' : ").strip().lower()

    # Choix mode de joueur B
    mode_B = input(f"Mode de jeu pour {joueur_B} ? (manuel / random) : ").strip().lower()
    while mode_B not in ["manuel", "random"]:
        mode_B = input("Veuillez saisir 'manuel' ou 'random' : ").strip().lower()

    config[joueur_A] = mode_A
    config[joueur_B] = mode_B

    return config

print(init_configurations(("Alex", "Bob")))

def pose_domino_manuel(royaume, cases_libres, domino, joueur="A"):
    """
    Permet à un joueur de poser un domino manuellement sur son royaume.

    Tant que le placement proposé n’est pas valide, on redemande.
    La fonction suppose que le domino peut être placé quelque part.
    """

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
    """
    Pose un domino automatiquement dans le royaume si possible, en tentant jusqu'à TENTATIVES fois.
    """

    directions = ['left', 'right', 'top', 'bottom']

    for _ in range(TENTATIVES):
        posL, posC = random.choice(cases_libres)
        dir = random.choice(directions)

        if domino_valide(royaume, domino, posL, posC, dir):
            ajoutDomino(royaume, cases_libres, domino, posL, posC, dir)
            print(f"{joueur} a placé le domino {domino} automatiquement en ({posL}, {posC}) vers {dir}.")
            return  # Fin de la fonction une fois le domino posé

    # Si aucune position valide trouvée après les tentatives
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
    Si le domino n’est pas peut pas etre posé cela affiche un message.
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
