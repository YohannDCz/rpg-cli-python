import classes.py
import grids.py


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