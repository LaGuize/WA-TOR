from def_grid import generation_grid, affichage_grid
import random
import time
import os

nbr_ligne = 10
nbr_column = 10

grille_test = generation_grid(nbr_ligne,nbr_column)


affichage_grid(grille_test)

def scan_des_cases_voisines2(x,y):
    # Scan de la case à droite
    if y < nbr_column - 1:
        case_droite = grille_test[x][(y+1)]
        coord_droite = (x, (y+1))
    else: 
        case_droite = grille_test[x][0]
        coord_droite = (x, (0))
    #  Scan de la case à gauche
    if y > 0:
        case_gauche = grille_test[x][(y-1)]
    else: 
        case_gauche = grille_test[x][-1]
    # Scan de la case en bas
    if x < nbr_ligne - 1:
        case_bas = grille_test[(x+1)][y]
    else: 
        case_bas = grille_test[0][y]
    # Scan de la case en haut
    if x > 0:
        case_haut = grille_test[(x-1)][y]
    else: 
        case_haut = grille_test[-1][y]
    
    return case_droite, coord_droite, case_gauche, case_bas, case_haut


