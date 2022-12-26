from time import sleep

# Initiation de la classe ma pour une meilleur manipulation des variables
# Il y a le nveau de la map, l'experience requis du joueur ainsi que la map
# de disposition des objets et celle affichée

class maps:

    def __init__(self, level, experience, map, displayed):
        self.level = level
        self.experience = experience
        self.map = map
        self.displayed = displayed


level1 = maps(1, 0,
              [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "o2", "o2", "o2", "o2", "o2", "o2", "o2", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "e1", "e1", "e1", "e1", "e1", "  ", "l "],
               ["l ", "  ", "  ", "o1", "o1", "o1", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "ee", "  ", "  ", "J ", "  ", "  ", "ee", "l "],
               ["  ", "l ", "l ", "l ", "l ", "l ", "l ", "l ", "  "]],

              [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "J ", "  ", "  ", "  ", "l "],
               ["  ", "l ", "l ", "l ", "l ", "l ", "l ", "l ", "  "]])

level2 = maps(2, 300,
              [["l ", "e4", "e4", "e4", "e4", "e4", "e4", "e4", "l "],
               ["l ", "  ", "  ", "p2", "p2", "p2", "  ", "  ", "l "],
               ["l ", "  ", "  ", "e3", "e3", "e3", "  ", "  ", "l "],
               ["l ", "o4", "  ", "o4", "  ", "o4", "  ", "o4", "l "],
               ["l ", "  ", "p1", "p1", "p1", "p1", "p1", "  ", "l "],
               ["l ", "  ", "e2", "  ", "e2", "  ", "e2", "  ", "l "],
               ["l ", "  ", "o3", "  ", "o3", "  ", "o3", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]],

              [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]])

level3 = maps(3, 600,
              [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "P ", "  ", "P ", "  ", "P ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "e5", "e5", "e5", "e5", "e5", "e5", "e5", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "p3", "p3", "p3", "p3", "p3", "p3", "p3", "l "],
               ["l ", "  ", "o5", "  ", "o5", "  ", "o5", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]],

              [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
               ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]])

### J = Joueur
### P = Princesse
# l = limite de jeu.9=
### o = objet
### e = ennemi
### p = potion


# Ici une fonction pour afficher la map avec les numéro des colonnes et des lignes
def display_map(map):

    column_header = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
    map.insert(0, column_header)
    for i in range(0, 9):
        map[i].insert(0, str(i - 1))
    for y in range(len(map)):
        b = "-----------------------------------------------"
        print(b)
        sleep(0.05)
        a = " | ".join(map[y])
        print(a)

# Ici, une fonction pour corriger l'utilisation de la première fonction
# (la console afiche une grille de numero dans une grille de numero autrement)
def correction_map(map):

    del map[0]
    for i in range(0, 8):
        del map[i][0]
    return map

# display_map(level3.map)
# print("\n")
# display_map(level2.map)
# print("\n")
# display_map(level1.map)
# print("\n")
