import classes
import grids
from time import sleep
import sys 

def game_title():
  print("\n")
  print("        %%%%%%  %%  %%  %%%%%%        ")
  print("          %%    %%  %%  %%            ")
  print("          %%    %%%%%%  %%%%%%        ")
  print("          %%    %%  %%  %%            ")
  print("          %%    %%  %%  %%%%%%        ")
  print("\n")
  print("  %%%%  %%  %%  %%  %%    %%%%  %%  %%") 
  print("%%      %%  %%  %%  %%  %%      %% %% ")
  print("%%      %%%%%%  %%  %%  %%      %%%%  ")
  print("%%      %%  %%  %%  %%  %%      %% %% ")
  print("  %%%%  %%  %%  %%%%%%    %%%%  %%  %%")
  print("\n")
  print("     %%%%    %%    %%    %%  %%%%%%   ")
  print("   %%      %%  %%  %% %% %%  %%       ")
  print("   %%      %%%%%%  %%    %%  %%%%     ")
  print("   %%  %%  %%  %%  %%    %%  %%       ")
  print("     %%%%  %%  %%  %%    %%  %%%%%%   ")
  print("\n")
  
def print_line(txt):
  for x in txt:
      print(x, end='')
      sys.stdout.flush()
      sleep(0.03)
  sleep(0.4)

def ask_name():
  print_line("Quel est votre nom ?\n")
  name = str(input())
  print(f"Votre nom est: {name}")
  return name

def confirm_name(name):
    print_line("Voulez-vous garder ce nom ? (oui/non)\n")
    answer = str(input())
    if answer.lower() == "non":
        ask_name()
    elif answer.lower() == "oui":
        print_line(f"Bon jeu, {name}!\n")
    else:
        print_line("Je n'ai pas compris !\n")
        confirm_name(name)

def Menu():
  print_line("Que souhaitez vous faire ?\n")
  print_line("1: Charger le jeu\n")
  print_line("2: Choisir la difficulté\n")
  print_line("3: Voir les commandes\n")
  answer = int(input())
  player = classes.Chuck_Norris
  if answer == 1:
    start_game(player)
  elif answer == 2:
    player = difficulte()
    print_line(f"Vous avez choisi {player}")
    Menu()
    return
  elif answer == 3:
    commandes()
    Menu()
    return
  else:
    print_line("Veuillez saisir une commande valide\n")
    Menu()
    return
 
def commandes():
  print("Vous pouvez choisir:\n")
  print("- [z] pour avancer\n")
  print("- [s] pour reculer\n")
  prtin("- [q] pour aller vers la gauche\n")
  print("- [d] pour aller à droite\n")

def difficulte():
  print_line("Souhaitez vous jouer avec [1] Chuck Norris ou [2] The Real Chuck Norris ?\n")
  level = int(input())
  if level == 1:
    character = classes.Chuck_Norris
  elif level == 2:
    character = classes.The_Real_Chuck_Norris
  return character

def start_game(player):
  game_title()
  name = ask_name()
  confirm_name(name)
  load_game()
  # afficher le contexte et le début de l'histoire
  print_line("Après cette partie délirante dont vous ne vous rappelez plus, il semblerait  que vous vous soyez téléporté au fin fond de la jungle...\n")
  print_line(f"Mais vous n'avez rien à perdre, car vous êtes {player.name}!\n")
  tutorial()  
  move()
  map()
  return 

def tutorial():
  print_line("Vous ètes face à un dilemme:\n")
  print_line("Votre couteau est cassé et vous vous demandez si vous devez continuer sans couteau...\n")
  print_line("Que choisissez-vous ?\n")
  print_line("1: Réparer le couteau\n")
  print_line("2: Continuer sans les mains\n")
  choice = int(input())
  if choice == 1:
    print_line("Vous avez choisi de réparer le couteau, bon choix.\n")
    def tutorial2():
      print_line("Avec quoi voulez vous le réparer?\n")
      print_line("1: Utiliser une cordelette\n")
      print_line("2: Utiliser de a glue super forte\n")
      print_line("3: Invoquer MacGiver\n")
      choice2 = int(input())
      if choice2 == 1:
        print_line("Votre couteau est réparé !\n")
      elif choice2 == 2:
        print_line("Erreur: Il n'y a pas de glue à 30km à la ronde\n")
        tutorial2()
      elif choice2 == 3:
        print_line("Personne ne peut aider Chuck Norris, il se débrouille seul envers et contre tout.\n")
        tutorial2()
    tutorial2()
  elif choice == 2:
    print_line("Chick Norris ne va nulpart sans son couteau !")
    tutorial()
  return

def move():
  print_line(f"Vous êtes au niveau {map.level}.")
  print(map())
  print_line("Quel déplacement souhaitez vous effectuer ?")
  print_line("Appuyez sur [c] pour afficher les commandes")
  move = str(input())
  if move == "c":
    commandes()
  elif move == "z":
    return map("z")
  elif move == "s":
    return map("s")
  elif move == "q":
    return map("q")
  elif move == "d":
    return map("d")
  # print lel propositionl de déplacement
  # recupérer le choix de l'utilisateur 
  # En fonction du choix appeler une fonctionnalité
  return map()

Menu()
# def credits():
#   # print afficher del infol sur la teaml 
#   Menu()

# def exit():
#   # quitter le jeu
#   return

# def find_object():
#   return

# def event():
#   return 
