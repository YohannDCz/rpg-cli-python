import classes
import maps
from time import sleep
import sys 


def game_title():

  print("\n")
  print("        %%%%%%  %%  %%  %%%%%%        ")
  sleep(0.1)
  print("          %%    %%  %%  %%            ")
  sleep(0.1)
  print("          %%    %%%%%%  %%%%          ")
  sleep(0.1)
  print("          %%    %%  %%  %%            ")
  sleep(0.1)
  print("          %%    %%  %%  %%%%%%        ")
  sleep(0.1)
  print("\n")
  print("  %%%%  %%  %%  %%  %%    %%%%  %%  %%") 
  sleep(0.1)
  print("%%      %%  %%  %%  %%  %%      %% %% ")
  sleep(0.1)
  print("%%      %%%%%%  %%  %%  %%      %%%%  ")
  sleep(0.1)
  print("%%      %%  %%  %%  %%  %%      %% %% ")
  sleep(0.1)
  print("  %%%%  %%  %%  %%%%%%    %%%%  %%  %%")
  sleep(0.1)
  print("\n")
  sleep(0.1)
  print("     %%%%    %%    %%    %%  %%%%%%   ")
  sleep(0.1)
  print("   %%      %%  %%  %% %% %%  %%       ")
  sleep(0.1)
  print("   %%      %%%%%%  %%    %%  %%%%     ")
  sleep(0.1)
  print("   %%  %%  %%  %%  %%    %%  %%       ")
  sleep(0.1)
  print("     %%%%  %%  %%  %%    %%  %%%%%%   ")
  print("\n")
  sleep(0.75)
  

def curtains():

  print("#################################################""")
  sleep("0.5")
  print("#################################################""")
  sleep("0.5")
  print("#################################################""")
  sleep("0.5")
  print("#################################################""")
  sleep("0.5")
  print("#################################################""")
  sleep("0.5")
  print("#################################################""")
  sleep("0.5")
  print("#################################################""")
  sleep("0.5")


def print_line(txt):

  for x in txt:
      print(x, end='')
      sys.stdout.flush()
      sleep(0.03)
  sleep(0.4)


def loading_bar(txt):

    for x in txt:
      print(x, end='')
      sys.stdout.flush()
      sleep(0.2)


def ask_name():

  print_line("Quel est votre nom ?\n")
  name = str(input())
  print_line(f"Votre nom est: {name}\n")
  def confirm_name(name):
    print_line("Voulez-vous garder ce nom ? (oui/non)\n")
    answer = str(input())
    if answer.lower() == "non":
        ask_name()
        print_line(f"Bon jeu, {name}!\n\n")
        sleep(2.5)
        return
    elif answer.lower() == "oui":
        print_line(f"Bon jeu, {name}!\n\n")
        sleep(2.5)
        return
    else:
        print_line("Je n'ai pas compris !\n")
        confirm_name(name)
        return
  return


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
    print_line(f"Vous avez choisi {player.name}!\n")
    sleep(2.5)
    Menu()
    return
  elif answer == 3:
    commandes()
    sleep(2.5)
    Menu()
  else:
    print_line("Veuillez saisir une commande valide\n")
    Menu()
    return
 

def commandes():

  print_line("Vous pouvez choisir:\n")
  print_line("- [z] pour avancer\n")
  print_line("- [s] pour reculer\n")
  print_line("- [q] pour aller vers la gauche\n")
  print_line("- [d] pour aller à droite\n")


def difficulte():

  print_line("Souhaitez vous jouer avec [1] Chuck Norris ou [2] The Real Chuck Norris ?\n")
  game = int(input())
  if game == 1:
    character = classes.Chuck_Norris
  elif game == 2:
    character = classes.The_Real_Chuck_Norris
  return character


def load_game():

  game_title()
  print_line("Veuillez patienter pendant que le jeu charge...\n\n")
  loading_bar("############################################\n\n")


def start_game(player):

  load_game()
  ask_name()

  curtains()

  print_line("Contexte: ")
  print_line("Après cette partie délirante dont vous ne vous rappelez plus, il semblerait que vous vous soyez téléporté au fin fond de la jungle...\n")
  print_line(f"Mais vous n'avez peur de rien, car vous êtes {player.name}!\n")
  
  tutorial(player)  
  move(maps.level1, player)
  return 


def tutorial(player):

  print_line("Mais voilà, vous ètes face à un dilemme:\n")
  print_line("Votre couteau est cassé et vous vous demandez si vous devez continuer sans...\n")

  def tutorial1(player):
    print_line("Que choisissez-vous ?\n")
    print_line("1: Réparer le couteau\n")
    print_line("2: Continuer sans les mains\n")
    choice = int(input())
    if choice == 1:
      print_line("Vous avez choisi de réparer le couteau, bon choix.\n")
      def tutorial2(player):
        print_line("Avec quoi voulez vous le réparer?\n")
        print_line("1: Utiliser une cordelette\n")
        print_line("2: Utiliser de la glue super forte\n")
        print_line("3: Invoquer MacGiver\n")
        choice2 = int(input())
        if choice2 == 1:
          print_line("Votre couteau est réparé !\n")
          print_line("Voici 20 points d'XP!\n")
          experience = player.receive_experience(20)
          print_line(f"Vous avez maintenant {experience} XP.\n")
          # classes.
        elif choice2 == 2:
          print_line("Erreur: Il n'y a pas de glue à 30km à la ronde\n")
          tutorial2(player)
          return
        elif choice2 == 3:
          print_line("Personne ne peut aider Chuck Norris, il se débrouille seul envers et contre tout.\n")
          tutorial2(player)
          return
      tutorial2(player)
    elif choice == 2:
      print_line("Chuck Norris ne va nulpart sans son couteau !\n")
      tutorial1(player)
      return
  tutorial1(player)
  return


def move(game, player):

  print_line(f"Vous êtes au niveau {game.level}.\n")
  print_line("Voici la map du niveau.\n")
  maps.correction_map(game.map)
  maps.display_map(game.map)
  print_line("Quel déplacement souhaitez vous effectuer ?\n")
  print_line("Appuyez sur [c] pour afficher les commandes\n")
  print_line("Appuyez sur [i] pour afficher l'inventaire.")
  move = str(input())
  if move == "c":
    commandes()
    move(game, player)
  elif move == "i":
    player.inventory()
    move(game, player)
  elif move == "z":
    return maps.map(player, "z", game.level, 6, 4)
  elif move == "s":
    return maps.map(player, "s", game.level, 6, 4)
  elif move == "q":
    return maps.map(player, "q", game.level, 6, 4)
  elif move == "d":
    return maps.map(player, "d", game.level, 6, 4)
  # print lel propositionl de déplacement
  # recupérer le choix de l'utilisateur 
  # En fonction du choix appeler une fonctionnalité
  # return map()

def position(position, player):

    if position[0] == "o":
      if position[1] == "1":
        player.find_object(classes.chapeau , classes.katana)
      elif position[1] == "2":
        player.find_object(classes.ceinture , classes.beretta)
      elif position[1] == "3":
        player.find_object(classes.jean , classes.m60)
      elif position[1] == "4":
        player.find_object(classes.rangers, classes.l_grenade)
      elif position[1] == "5":
        player.find_object(classes.pickup, classes.cuillere)
    elif position[0] == "e":
      if position[1] == "1":
        classes.fight(player, classes.scarabee)
      elif position[1] == "2":
        classes.fight(player, classes.piranha)
      elif position[1] == "3":
        classes.fight(player, classes.anaconda)
      elif position[1] == "4":
        classes.fight(player, classes.crocodile)
      elif position[1] == "5":
        classes.fight(player, classes.pantere)
    elif position[0] == "p":
        potion(position[1])
    elif position == "P ":
        princess(position[1])
    elif position =="l ":
        game_over()


def map(player, move, map_level, i, j):

    map = map_level.map
    move.lowercase()
    if move == "z":
        position = "  "
        position = map[i-1][j]
        position(player, position)
        position = "J "
    elif move == "s":
        position = "  "
        position = map[i+1][j]
        position(player, position)
        position = "J "
    elif move == "q":
        position = "  "
        position = map[i][j-1]
        position(player, position)
        position = "J "
    elif move == "d":
        position = "  "
        position = map[i][j+1]
        position(player, position)
        position = "J "
    return 


position("e5", classes.Chuck_Norris)


def potion():
  return 

def princess():
  return]

def game_over():
  return

def credits():
  # print afficher del infol sur la teaml 
  return

def exit():
  # quitter le jeu
  return