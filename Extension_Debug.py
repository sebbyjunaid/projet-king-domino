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
