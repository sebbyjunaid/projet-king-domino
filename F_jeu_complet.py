def init_dominos(taille, nom_fichier):
    """
    Mélange les dominos depuis le fichier et en sélectionne le bon nombre
    pour une partie à 2 joueurs sur un royaume de taille donnée.
    """
    tous_les_dominos = extraire_dominos(nom_fichier)

    nb_dominos = (taille * taille - 1)
    return tous_les_dominos[:nb_dominos]


print(len(init_dominos(5, "dominos.csv")))
print(len(init_dominos(7, "dominos.csv")))

def couronnes_zone(royaume, posL, posC, cases_visitees, nb_couronnes):
    """
    Explore récursivement une zone de même couleur dans le royaume, à partir de (posL, posC).
    Ajoute les couronnes des cases visitées et les enregistre dans cases_visitees.
    """
    if (posL, posC) in cases_visitees:
        return nb_couronnes

    case = royaume[posL][posC]
    if case is None:
        return nb_couronnes

    couleur = case[0]
    couronnes = int(case[1])

    # Il faut marquer la case comme visitée
    cases_visitees.append((posL, posC))
    nb_couronnes += couronnes

    # Pour explorer les voisines
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # droite, gauche , bas, haut
    n = len(royaume)

    for dL, dC in directions:
        i, j = posL + dL, posC + dC
        if 0 <= i < n and 0 <= j < n:
            voisine = royaume[i][j]
            if voisine is not None and voisine[0] == couleur:
                nb_couronnes = couronnes_zone(royaume, i, j, cases_visitees, nb_couronnes)

    return nb_couronnes
royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)
ajoutDomino(royaume, cases_libres, (3,'F0','F0'), 0, 0, 'left')
ajoutDomino(royaume, cases_libres, (4,'F0','F0'), 0, 2, 'top')
ajoutDomino(royaume, cases_libres, (24,'F1','Y0'), 1, 0, 'left')
ajoutDomino(royaume, cases_libres, (25,'F1','Y0'), 2, 0, 'top')
ajoutDomino(royaume, cases_libres, (26,'F1','Y0'), 0, 3, 'left')
ajoutDomino(royaume, cases_libres, (5,'F0','F0'), 1, 3, 'top')
ajoutDomino(royaume, cases_libres, (27,'F1','Y0'), 3, 1, 'bottom')

afficherRoyaume(royaume)

cases_visitees = []
print("Couronnes à partir de (0,0) :", couronnes_zone(royaume, 0, 0, cases_visitees, 0))
print("Cases visitées :", cases_visitees)

def score_zone(royaume, posL, posC):
    """
    Calcule le score d'une zone connectée dans le royaume, à partir d'une case donnée.
    Renvoie un tuple : (score, liste des cases de la zone).
    """
    case = royaume[posL][posC]

    # cas ou la case est vide
    if case is None:
        return 0, [(posL, posC)]

    cases_visitees = []
    nb_couronnes = couronnes_zone(royaume, posL, posC, cases_visitees, 0)
    taille_zone = len(cases_visitees)
    score = nb_couronnes * taille_zone

    return score, cases_visitees


print(score_zone(royaume, 0, 0))
print(score_zone(royaume, 3, 1))
print(score_zone(royaume, 4, 4))


def total_score(royaume):
    """
    Calcule le score total d’un royaume en parcourant toutes les zones connectées.
    """
    score = 0
    cases_visitees = []

    n = len(royaume)
    for i in range(n):
        for j in range(n):
            if (i, j) not in cases_visitees and royaume[i][j] is not None:
                score_zone_val, zone_cases = score_zone(royaume, i, j)
                score += score_zone_val
                cases_visitees.extend(zone_cases)

    return score
print("Score total du royaume :", total_score(royaume))

def jeu_complet(taille, nom_fichier="dominos.csv", perso=False):
    print("\n🎮 Bienvenue dans KingDomino ! Lancement de la partie...\n")

    # Étape 1 : initialisations
    tuple_royaumes = init_tuple_royaumes(taille)
    tuple_libres = init_tuple_libres(taille)
    tuple_joueurs = init_tuple_joueurs(perso)
    dico_configurations = init_configurations(tuple_joueurs)
    liste_dominos = init_dominos(taille, nom_fichier)

    # Étape 2 : premier tour
    dico_depot, dico_choix = premier_tour(liste_dominos, tuple_joueurs, dico_configurations)

    # Étape 3 : boucle des tours principaux
    while len(liste_dominos) >= 4:
        tour_de_jeu(
            tuple_royaumes,
            tuple_libres,
            liste_dominos,
            dico_depot,
            dico_choix,
            tuple_joueurs,
            dico_configurations
        )

    # Étape 4 : dernier tour (pose finale sans choix)
    print("\n🧩 Dernier tour ! Les joueurs posent leurs derniers dominos...\n")
    for i in range(1, 5):
        joueur = dico_depot[i][1]
        index_joueur = 0 if joueur == tuple_joueurs[0] else 1
        domino = dico_depot[i][0]

        pose_domino(
            tuple_royaumes[index_joueur],
            tuple_libres[index_joueur],
            domino,
            dico_configurations,
            joueur
        )

    # Étape 5 : scores et résultat final
    score_A = total_score(tuple_royaumes[0])
    score_B = total_score(tuple_royaumes[1])

    print("\n🏰 Royaume final de", tuple_joueurs[0])
    afficherRoyaume(tuple_royaumes[0], tuple_joueurs[0])
    print("Score :", score_A)

    print("\n🏰 Royaume final de", tuple_joueurs[1])
    afficherRoyaume(tuple_royaumes[1], tuple_joueurs[1])
    print("Score :", score_B)

    print("\n🎉 Résultat final :")
    if score_A > score_B:
        print(f"🏆 {tuple_joueurs[0]} remporte la partie avec {score_A} points contre {score_B} !")
    elif score_B > score_A:
        print(f"🏆 {tuple_joueurs[1]} remporte la partie avec {score_B} points contre {score_A} !")
    else:
        print(f"🤝 Match nul ! Les deux joueurs ont {score_A} points.")


def main():
    taille = 5  # ou 3 pour tester vite
    jeu_complet(taille)

main()
