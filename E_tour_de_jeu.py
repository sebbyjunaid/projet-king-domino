def vide_et_transfere_depot(dico_depot, dico_choix):
    """
    La fonction vide_et_transfere_depot prend en argument les dictionnaires de depot et de choix.
    Elle ne renvoie rien. Elle commence par vider le dictionnaire de dépot.
    Ensuite, elle ajoute le contenu du dictionnaire de choix dans le dictionnair
    """
    dico_depot.clear()
    for i in range(1, 5):
        dico_depot[i] = dico_choix[i]

dico_depot = {
    1: [(1, 'Y0', 'Y0'), None],
    2: [(3, 'F0', 'F0'), None],
    3: [(4, 'F0', 'F0'), None],
    4: [(13, 'Y0', 'F0'), None]
}
#dico_choix garde son contenu inchangé
# (pas besoin de le vider ici).

def choix_pion(dico_choix, joueur, dico_configurations):
    """
    Demande à un joueur (manuel ou random) de choisir un pion parmi ceux disponibles dans dico_choix.
    Renvoie l'entier correspondant au pion choisi (clé entre 1 et 4).
    """
    mode = dico_configurations[joueur]

    if mode == "manuel":
        print(f"\n{joueur}, c’est à vous de choisir un domino parmi ceux disponibles.")
        afficher_choix_ou_depot(dico_choix)
        while True:
            try:
                choix = int(input("Entrez le numéro du domino que vous choisissez (1 à 4) : "))
                if choix in dico_choix and dico_choix[choix][1] is None:
                    return choix
                else:
                    print("❌ Choix invalide ou domino déjà pris. Veuillez réessayer.")
            except ValueError:
                print("⚠️ Entrée non valide. Veuillez entrer un entier entre 1 et 4.")
    else:
        # Mode aléatoire
        options_disponibles = [i for i in dico_choix if dico_choix[i][1] is None]
        choix = random.choice(options_disponibles)
        print(f"{joueur} a choisi automatiquement le domino n°{choix}.")
        return choix

dico_choix = {
    1: [(1, 'Y0', 'Y0'), "Alex"],
    2: [(3, 'F0', 'F0'), None],
    3: [(4, 'F0', 'F0'), "Nadia"],
    4: [(13, 'Y0', 'F0'), None]
}
dico_configurations = {
    "Alex": "manuel",
    "Nadia": "random"
}

# Manuel → demande à l’utilisateur
choix_pion(dico_choix, "Alex", dico_configurations)

# Random → choisi automatiquement un domino libre
print(choix_pion(dico_choix, "Nadia", dico_configurations))

def pose_et_choix(royaume, cases_libres, dico_depot, dico_choix, dico_configurations, indice_depot):
    """
    Gère le tour d’un joueur : pose du domino depuis le dépôt, puis choix d’un domino dans la pile de choix.
    """
    # Récupération du domino et du joueur concerné
    domino, joueur = dico_depot[indice_depot]

    print(f"\n===== Tour de {joueur} =====")
    print("Royaume actuel :")
    afficherRoyaume(royaume, joueur)

    # Pose du domino dans le royaume
    pose_domino(royaume, cases_libres, domino, dico_configurations, joueur)

    # Affichage de la pile de choix pour ce tour
    print("\n--- Pile de choix disponible ---")
    afficher_choix_ou_depot(dico_choix)

    # Le joueur choisit un pion sur la pile de choix
    choix = choix_pion(dico_choix, joueur, dico_configurations)
    dico_choix[choix][1] = joueur  # On inscrit le joueur dessus

royaume = creerRoyaume(5)
cases_libres = init_cases_libres(5)

ajoutDomino(royaume, cases_libres, (10, 'G0', 'G0'), 2, 3, 'left')
ajoutDomino(royaume, cases_libres, (19, 'Y1', 'F0'), 3, 2, 'left')

dico_depot = {
    1: [(10, 'G0', 'G0'), "A"],
    2: [(19, 'Y1', 'F0'), "B"],
    3: [(24, 'F1', 'Y0'), "B"],
    4: [(48, 'Y0', 'M3'), "A"]
}
dico_choix = {
    1: [(1, 'Y0', 'Y0'), None],
    2: [(3, 'F0', 'F0'), "A"],
    3: [(4, 'F0', 'F0'), "B"],
    4: [(13, 'Y0', 'F0'), None]
}
dico_configurations = {"A": 'manuel', "B": 'random'}

pose_et_choix(royaume, cases_libres, dico_depot, dico_choix, dico_configurations, 3)

def tour_de_jeu(tuple_royaumes, tuple_libres, liste_dominos, dico_depot, dico_choix, tuple_joueurs, dico_configurations):
    """
    Gère un tour complet :
    - Pose des dominos en suivant l’ordre de dépôt
    - Choix des nouveaux dominos par les joueurs
    - Transfert des choix vers le dépôt
    - Remplissage de la nouvelle pile de choix
    """
    print("\n========================")
    print("🔁 DÉBUT D’UN NOUVEAU TOUR")
    print("========================")

    for i in range(1, 5):
        joueur = dico_depot[i][1]
        index_joueur = 0 if joueur == tuple_joueurs[0] else 1

        print(f"\n🎲 Tour {i}/4 — Joueur {joueur}")
        pose_et_choix(
            tuple_royaumes[index_joueur],
            tuple_libres[index_joueur],
            dico_depot,
            dico_choix,
            dico_configurations,
            i
        )

    print("\n📦 Transfert des dominos choisis vers le dépôt...")
    vide_et_transfere_depot(dico_depot, dico_choix)

    print("\n🃏 Nouvelle pile de choix...")
    remplir_choix(liste_dominos, dico_choix)

    print("\n✅ Tour terminé. Voici la nouvelle pile de dépôt et la pile de choix :\n")
    print("📥 Dépôt :")
    afficher_choix_ou_depot(dico_depot)
    print("\n🎯 Choix :")
    afficher_choix_ou_depot(dico_choix)
    print("\n========================\n")

import random

def premier_tour(liste_dominos, tuple_joueurs, dico_configurations):
    """
    Gère la phase initiale du jeu : remplissage de la pile de choix et
    sélection de dominos par les joueurs pour le premier tour.
    """
    dico_choix = {}
    dico_depot = {}

    # Étape 1 : remplir la pile de choix
    remplir_choix(liste_dominos, dico_choix)

    # Étape 2 : tirage au sort du joueur qui commence
    premier = random.choice(tuple_joueurs)
    second = tuple_joueurs[1] if premier == tuple_joueurs[0] else tuple_joueurs[0]
    print(f"\n🎲 Tirage au sort : {premier} commence le jeu.")

    # Étape 3 : choix des dominos dans dico_choix
    choix_1 = choix_pion(dico_choix, premier, dico_configurations)
    dico_choix[choix_1][1] = premier

    choix_2 = choix_pion(dico_choix, second, dico_configurations)
    dico_choix[choix_2][1] = second

    choix_3 = choix_pion(dico_choix, second, dico_configurations)
    while choix_3 == choix_2:
        print("⚠️ Ce domino a déjà été pris. Choisissez-en un autre.")
        choix_3 = choix_pion(dico_choix, second, dico_configurations)
    dico_choix[choix_3][1] = second

    # Le dernier domino est automatiquement attribué au premier joueur
    for i in range(1, 5):
        if dico_choix[i][1] is None:
            dico_choix[i][1] = premier
            break

    # Étape 4 : transfert de la pile de choix vers le dépôt
    vide_et_transfere_depot(dico_depot, dico_choix)

    # ✅ Fin de la phase de préparation
    return dico_depot, dico_choix

liste_dominos = extraire_dominos("dominos.csv")
tuple_joueurs = ("Yves-Jean", "Alexandre")
dico_configurations = {"Yves-Jean": "manuel", "Alexandre": "random"}

dico_depot, dico_choix = premier_tour(liste_dominos, tuple_joueurs, dico_configurations)

print("\n🔐 Pile de dépôt initialisée :")
afficher_choix_ou_depot(dico_depot)

print("\n📌 Dernier état de la pile de choix :")
afficher_choix_ou_depot(dico_choix)
