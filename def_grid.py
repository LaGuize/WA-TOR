# la fonction qui permet de générer une grille avec les paramètres nombre de ligne et nombre de colonnes


def generation_grid(nbr_ligne, nbr_column):
    ma_grid = []
    for _ in range(nbr_ligne):
        ligne = []
        for _ in range(nbr_column):
            ligne.append(0)
        ma_grid.append(ligne)

    for l in ma_grid:
        print(l)

# generation_grid(20,10) # exemple d'utilisation de la fonction. Ici, 20 lignes de 10 colonnes.
