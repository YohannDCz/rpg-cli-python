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

  print_line("Contexte: ")
  print_line("Après cette partie délirante dont vous ne vous rappelez plus, il semblerait que vous vous soyez téléporté au fin fond de la jungle...\n")
  print_line(f"Mais vous n'avez peur de rien, car vous êtes {player.name}!\n")
  
  tutorial(player)  
  move(maps.level1)
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


def move(game):

  print_line(f"Vous êtes au niveau {game.level}.\n")
  print_line("Voici la map du niveau.\n")
  maps.correction_map(game.map)
  maps.display_map(game.map)
  print_line("Quel déplacement souhaitez vous effectuer ?\n")
  print_line("Appuyez sur [c] pour afficher les commandes\n")
  move = str(input())
  if move == "c":
    commandes()
    move(maps.level1)
  elif move == "z":
    return maps.map("z", game.level, 6, 4)
  elif move == "s":
    return maps.map("s", game.level, 6, 4)
  elif move == "q":
    return maps.map("q", game.level, 6, 4)
  elif move == "d":
    return maps.map("d", game.level, 6, 4)
  # print lel propositionl de déplacement
  # recupérer le choix de l'utilisateur 
  # En fonction du choix appeler une fonctionnalité
  # return map()


def find_object(player, object1, object2):
      object1 = classes.object1
      object2 = classes.object2
    # if object == "1":
      print_line("Il semble que vous soyez tombés sur des objets !\n")
      print_line(f"[1] Vous ramassez votre {classes.object1.name.lowercase()} qui est tombé. (+defense).\n")
      print_line(f"[2] Vous trouvez un {classes.object2.name.lowercase()} non loin de là et il ne semble appartenir à personne. (+attaque)\n")
      object = int(input())
      if object == 1:
        print_line(f"Vous venez de récupérer votre {classes.object1.name.lowercase()}.\n")
        player.objects["Armure"][classes.object1.name.lowercase()] = classes.object1.defense
      elif object == 2:
        print_line(f"Vous vous emparez du {classes.object2.name.loewrcase()}\n")
        player.objects["Weapon"].append(classes.object2.name)
        for key.values in object2.items():
          player.attacks[classes.object2.attacks.key] = classes.object2.attack.value

chuck = classes.Chuck_Norris
chapeau = classes.chapeau
katana = classes.katana
find_object(chuck, chapeau, katana)

#     elif object == "2":
#       print_line("Il semble que vous soyez tombés sur des objets !\n")
#       print_line("[1] Vous récupérez votre ceinture en cuir (+defense).\n")
#       print_line("[2] Vous ramassez votre arme préférée, le Beretta 92FS (+attaque).\n")
#       object2 = int(input())
#       if object2 == 1:
#         print_line("Vous venez de récupérer votre ceinture.\n")
#         player.objects["Armure"]["Ceinture"] = 25
#       elif object2 == 2:
#         print_line("Vous vous emparez de votre Beretta 92FS et vous en profitez pour tirer sur lese moustiques.\n")
#         player.objects["Weapon"].append("Beretta 92FS")
#         player.attacks["Tir à l'aveuglette"] = 55
#         player.attacks["Bon baiser de beretta"] = 75

#     elif object == "3":
#       print_line("Il semble que vous soyez tombés sur des objets !\n")
#       print_line("[1] Vous récupérez votre jean et sans qui cela n'a pas semblé génant (++defense).\n")
#       print_line("[2] Vous ramassez votre deuxième arme préférée, pensant que ce rpg est bien fait, le M60 Machine Gun (++attaque).\n")
#       object3 = int(input())
#       if object3 == 1:
#         print_line("Vous venez de récupérer votre jean.\n")
#         player.objects["Armure"]["Jean"] = 40
#       elif object3 == 2:
#         print_line("Vous vous emparez de votre M60 Machine Gun et vous en profitez pour vous fumer un cigare.\n")
#         player.objects["Weapon"].append("M60 Machine Gun")
#         player.attacks["Tir à vif"] = 90
#         player.attacks["Tir groupé"] = 100

#     elif object == "4":
#       print_line("Il semble que vous soyez tombés sur des objets !\n")
#       print_line("[1] Vous enfourchez vos rangers, les chaussettes ne suffisant plus à votre avancée (+++defense).\n")
#       print_line("[2] Vous trouvez votre fameux lanceur de grenade M79 (+++attaque).\n")
#       object4 = int(input())
#       if object4 == 1:
#         print_line("Vous venez de récupérer vos rangers.\n")
#         player.objects["Armure"]["Rangers"] = 65
#       elif object4 == 2:
#         print_line("Vous saluez votre lance grenade en lui promettant de belle aventure... Parler aux armes, il n'y a que ça de vrai, entre nous.\n")
#         player.objects["Weapon"].append("Lanceur de grenade M79")
#         player.attacks["Tir bourrain"] = 120
#         player.attacks["Tir dans le tas"] = 130

#     elif object == "5":
#       print_line("Il semble que vous soyez tombés sur des objets !\n")
#       print_line("[1] Vous rentrez dans votre pick-up, soulagé que la chance tourne enfin (++++defense).\n")
#       print_line("[2] Vous ramassez une cuillère (?attaque).\n")
#       object5 = int(input())
#       if object5 == 1:
#         print_line("Vous venez de récupérer votre pick-up.\n")
#         player.objects["Armure"]["Pick-up"]= 150
#       elif object5 == 2:
#         print_line("Vous ramassez la cuillère.")
#         player.objects["Weapon"].append("Cuillère")
#         player.attacks["L'attaque de la cuillère"] = 1000

        
# move(maps.level1)

# start_game(classes.Chuck_Norris)

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
