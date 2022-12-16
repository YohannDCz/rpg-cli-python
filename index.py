import classes
import grids

def game_title():
  print("\n")
  print("  %%%%  %%  %%  %%  %%    %%%%  %%  %% ")
  print("%%      %%  %%  %%  %%  %%      %% %%  ")
  print("%%      %%%%%%  %%  %%  %%      %%%%   ")
  print("%%      %%  %%  %%  %%  %%      %% %%  ")
  print("  %%%%  %%  %%  %%%%%%    %%%%  %%  %% ")
  print("\n")
  
def Menu():

  # Afficher lel optionl du menu
  # demander à l'utilisateur 
  # en fonction du choix appeler une del 4 fonctionl du dessous
  return


def naming():
    name = str(input("Quel est ton Nom ?"))
    print("Ton nom est : {}".format(name))
    confirm_name()

def confirm_name():
    r = str(input("Voulez-vous garder ce nom ? (oui/non)"))
    if r.lower() == "non":
        naming()
    elif r.lower() == "oui":
        print("Bon jeu !")
    else:
        print("Je n'ai pas compris !")
        confirm_name()

def start_game():
  # afficher le contexte et le début de l'histoire
  print("Après cette partie délirante dont vous ne vous rappelez plus, il semblerait  que vous vous soyez téléporté au fin fond de la jungle...")
  print("Mais vous n'avez rien à perdre, car vous êtes CHUCK NORRIS!")
  name = ask_name()
  print(name)
  
  tutoriel()  
  move()
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