grille_debut = [[" ", " ", " ", " ", " ", " ", " ", ";"],
                ["☐", "☐", "☐", "☐", "☐", "☐", "☐", ";"],
                [" ", " ", " ", " ", " ", " ", " ", ";"],
                [" ", "○", "○", "○", "○", "○", " ", ";"],
                [";", " ", "☐", "☐", "☐", " ", ";", " "],
                [" ", ";", " ", " ", " ", ";", " ", " "],
                [" ", " ", ";", "J", ";", " ", " ", " "],
                [" ", " ", " ", ";", " ", " ", " ", " "]]
 
grille_fin =   [[" ", " ", " ", "△", " ", " ", " ", ";"],
                ["○", "○", "○", "○", "○", "○", "○", ";"],
                [" ", " ", "△", "△", "△", " ", " ", ";"],
                [" ", " ", "○", "○", "○", " ", " ", ";"],
                ["☐", " ", "☐", " ", "☐", " ", "☐", ";"],
                [" ", "△", "△", "△", "△", "△", " ", ";"],
                [" ", "○", " ", "○", " ", "○", " ", ";"],
                [" ", "☐", " ", "☐", " ", "☐", " ", ";"]]

#### REPRESENTATION GRAPHIQUE

def afficher_grille(grille):
    column_header= [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
    grille.insert(0, column_header)
    for i in range(1,9):
        grille[i].insert(0, chr(64 + i))
    for y in range(len(grille)):
        b = "---------------------------------"
        print(b)
        a = " | ".join(grille[y])
        print(a)

afficher_grille(grille_fin)

def correction_grille(grille):
    del grille[0]
    for i in range(0,8):
        del grille[i][0]
    return grille

afficher_grille(grille_debut)

current_position = "here"
player_name = "Bob"
game_map = ""

def start_game():
  return

def inventory():
  return 
  
def Menu():
  # Afficher les options du menu
  # demander à l'utilisateur 
  # en fonction du choix appeler une des 4 fonctions du dessous
  return

def start_game():
  # afficher le contexte et le début de l'histoire
  # ask_name()
  # move()
  return 

def ask_name():
  # demander le nom
  return name

def load_game():
  # charger des datas en mémoire
  start_game()

def credits():
  # print afficher des infos sur la teams 
  Menu()

def exit():
  # quitter le jeu
  return

def move():
  # print les propositions de déplacement
  # recupérer le choix de l'utilisateur 
  # En fonction du choix appeler une fonctionnalité
  return

def fight():
  # présentation du combat
  # print propositions d'actions du joueur
  # en fonction du choix du joueurs appeler la fonction qui correspond
  # action de l'ennemis
  return

def find_object():
  return

def event():
  return 