"""
Partie B : Gestions des dominos
Nouas avons programmé les fonctions qui vont permettre de placer les dominos dans les royaumes,
puis verifier l'espace(libre et valide).
"""

def partie_droite_domino(posL, posC, dir):
    """Calcul les coordonnées de la case droite du domino en fonction de la case gauche et d'une direction
    affiche None si la direction nest pas valide ."""

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
    """Affiche True si un domino peut être ajouté à cet emplacement avec cette direction."""

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
    """Ajoute un domino au royaume si l'espace est libre, et modifie la liste des cases vide."""
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
    """Renvoie la liste des coordonnées voisines autour d'une case (posL, posC).
    Si libres=True, seules les cases vides sont incluses."""

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
    """Vérifie si un domino peut être placé à cet endroit du royaume selon les règles du jeu."""

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
    """Renvoie True si le domino peut être placé quelque part dans le royaume, False sinon."""

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
