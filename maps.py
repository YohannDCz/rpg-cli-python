class maps:

    def __init__(self, level, map):
        self.level = level
        self.map = map


level1 = maps(1, 
           [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
            ["l ", "o2", "o2", "o2", "o2", "o2", "o2", "o2", "l "],
            ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
            ["l ", "  ", "e1", "e1", "e1", "e1", "e1", "  ", "l "],
            ["  ", "l ", "  ", "o1", "o1", "o1", "  ", "l ", "  "],
            ["  ", "  ", "l ", "  ", "  ", "  ", "l ", "  ", "  "],
            ["  ", "  ", "  ", "l ", "J ", "l ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "l ", "  ", "  ", "  ", "  "]])
    
level2 = maps(2,
           [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
            ["l ", "e4", "e4", "e4", "e4", "e4", "e4", "e4", "l "],
            ["l ", "  ", "  ", "p2", "p2", "p2", "  ", "  ", "l "],
            ["l ", "  ", "  ", "e3", "e3", "e3", "  ", "  ", "l "],
            ["l ", "o4", "  ", "o4", "  ", "o4", "  ", "o4", "l "],
            ["l ", "  ", "p1", "p1", "p1", "p1", "p1", "  ", "l "],
            ["l ", "  ", "e2", "  ", "e2", "  ", "e2", "  ", "l "],
            ["l ", "  ", "o3", "  ", "o3", "  ", "o3", "  ", "l "]])

level3 = maps(3,
           [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
            ["l ", "  ", "P ", "  ", "P ", "  ", "P ", "  ", "l "],
            ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
            ["l ", "e5", "e5", "e5", "e5", "e5", "e5", "e5", "l "],
            ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
            ["l ", "p3", "p3", "p3", "p3", "p3", "p3", "p3", "l "],
            ["l ", "  ", "o5", "  ", "o5", "  ", "o5", "  ", "l "],
            ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]])

### J = Joueur
### P = Princesse
### l = limite de jeu
### o = objet
### e = ennemi
### p = potion


def display_map(map):

    column_header= ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
    map.insert(0, column_header)
    for i in range(0,9):
        map[i].insert(0, str(i - 1))
    for y in range(len(map)):
        b = "-----------------------------------------------"
        print(b)
        a = " | ".join(map[y])
        print(a)


def correction_map(map):

    del map[0]
    for i in range(0,8):
        del map[i][0]
    return map

display_map(level3.map)
print("\n")
display_map(level2.map)
print("\n")
display_map(level1.map)
print("\n")