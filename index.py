import classes.py

level1 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "o2", "o2", "o2", "o2", "o2", "o2", "o2", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "  ", "e1", "e1", "e1", "e1", "e1", "  ", "l "],
          ["  ", "l ", "  ", "o1", "o1", "o1", "  ", "l ", "  "],
          ["  ", "  ", "l ", "  ", "  ", "  ", "l ", "  ", "  "],
          ["  ", "  ", "  ", "l ", "J ", "l ", "  ", "  ", "  "],
          ["  ", "  ", "  ", "  ", "l ", "  ", "  ", "  ", "  "]]
 
level2 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "e4", "e4", "e4", "e4", "e4", "e4", "e4", "l "],
          ["l ", "  ", "  ", "p2", "p2", "p2", "  ", "  ", "l "],
          ["l ", "  ", "  ", "e3", "e3", "e3", "  ", "  ", "l "],
          ["l ", "o4", "  ", "o4", "  ", "o4", "  ", "o4", "l "],
          ["l ", "  ", "p1", "p1", "p1", "p1", "p1", "  ", "l "],
          ["l ", "  ", "e2", "  ", "e2", "  ", "e2", "  ", "l "],
          ["l ", "  ", "o3", "  ", "o3", "  ", "o3", "  ", "l "]]

level3 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "  ", "P ", "  ", "P ", "  ", "P ", "  ", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "e5", "e5", "e5", "e5", "e5", "e5", "e5", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "p3", "p3", "p3", "p3", "p3", "p3", "p3", "l "],
          ["l ", "  ", "o5", "  ", "o5", "  ", "o5", "  ", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]]

### J = Joueur
### P = Princesse
### l = limite de jeu
### o = objet
### e = ennemi
### p = potion

def display_grid(grid):
    column_header= [" ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]
    grid.insert(0, column_header)
    for i in range(1,9):
        grid[i].insert(0, chr(64 + i))
    for y in range(len(grid)):
        b = "-----------------------------------------------"
        print(b)
        a = " | ".join(grid[y])
        print(a)

display_grid(level3)
display_grid(level2)
display_grid(level1)

current_position = "here"
player_name = "Bob"
game_map = ""

def inventory():
  return 
  
def Menu():
  # Afficher lel optionl du menu
  # demander à l'utilisateur 
  # en fonction du choix appeler une del 4 fonctionl du dessous
  return

# name = "Chuck Norris"
# strengh = 80
# defense = 50
# life = 400
# objects = {"knife": 20}
# attacks = {"simple slap": 10, "royal stab": 40}

def start_game():
  # afficher le contexte et le début de l'histoire
  print("Après cette partie délirante dont vous ne vous rappelez plus, il semblerait  que vous vous soyez téléporté au fin fond de la jungle...")
  print("Mais vous n'avez rien à perdre, car vous êtes CHUCK NORRIS!")
  name = ask_name()
  print(name)
  
  player(80, 50, 400, {"knife": 20}, [["simple slap", 10], ["chuck stab", 40]])
  

    
  direction = move()
  return 

def ask_name():
  print("Tout d'abord comment vous appelez-vous ?")
  name = str(input("Name: "))
  return "Bonjour " + name + ", veuillez commencer la partie..."
 
def load_game():
  # charger del datal en mémoire
  start_game()

def credits():
  # print afficher del infol sur la teaml 
  Menu()

def exit():
  # quitter le jeu
  return

def move():
  # print lel propositionl de déplacement
  # recupérer le choix de l'utilisateur 
  # En fonction du choix appeler une fonctionnalité
  return

def fight():
  # présentation du combat
  # print propositionl d'actionl du joueur
  # en fonction du choix du joueurl appeler la fonction qui correspond
  # action de l'ennemis
  return

def find_object():
  return

def event():
  return 