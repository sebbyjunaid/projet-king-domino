"""
Extension : Statistiques de fin de partie
Cela ajoute une fonction pour afficher des statistiques à la fin de la partie KingDomino.

- Le score total
- Le nombre de zones distinctes
- Le score total en fonction du terrain
- La plus grande zone
"""
from F_score import score_zone


def statistiques_royaume(royaume):
    """Affiche des statistiques avancées sur le royaume fourni."""
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
