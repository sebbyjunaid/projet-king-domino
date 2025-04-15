"""
PartieA: Gestion Du Royaume
Dans cette partie, nous avons programmé des fonctions qui permettent de créer, initialiser,
afficher et gérer le royaume tout en gérant la mise en place des royaumes pours les joueurs

"""



def creerRoyaume(taille=7):
    """La fonction creerRoyaume représente le royaume du joueur,
    sa taille doit etre strictement positive, le chateau CH est dans la case centrale,
    tout le rest est à None.


    """

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
#cela va renvoyer un tuple ayant deux rouyaumes initialisés pour les joueurs.
    royaume1 = creerRoyaume(taille)
    royaume2 = creerRoyaume(taille)

    return (royaume1, royaume2)
tup = init_tuple_royaumes(5)
tup[0][0][0] = "Y0"
print(tup[0])
print(tup[1])

def afficherCoordonnees(royaume):
    """La fonction afficherCoordonnees affiche les coordonnées de chaque point du royaume. Cette fonction ne sera jamais
    utilisée, elle est là pour vous aider à comprendre la grille """
    n = len(royaume)
    for i in range(n):
        for j in range(n):
            print("|"+str((i,j)), end ="")
        print("|")

    royaume = creerRoyaume(5)
    afficherCoordonnees(royaume)

def init_cases_libres(taille):
    """La fonction init_cases_libres gère la liste des cases vides d'un royaume de taille nxn contenant seulement
    un chateau"""

    cases = []
    centre = taille // 2
    for i in range(taille):
        for j in range(taille):
            if (i, j) != (centre, centre):
                cases.append((i, j))
    return cases
print(init_cases_libres(3))


def init_tuple_libres(taille):
    """La fonction init_tuple_libres renvoie un tuple avec deux listes des cases vides des joueurs"""

    libres1 = init_cases_libres(taille)
    libres2 = init_cases_libres(taille)
    return (libres1, libres2)

tup = init_tuple_libres(5)
tup[0].remove((0, 0))
print(len(tup[0]))
print(len(tup[1]))


def afficherRoyaume(royaume, joueur="A", vide="  "):
    """Affiche un royaume avec une bonne mise en forme contenant le nom du joueur,
    les coordonnées de lignes/colonnes, et les valeurs des cases (ou vide)."""

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
