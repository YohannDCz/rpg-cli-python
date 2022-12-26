##############################################################
#   Partie 1
##############################################################

## Import des deux autres fichiers et du module 
## sleep de la bibliothèque time et du module sys
## permettant d'afficher le texte en filigrane.

import classes
import maps
from time import sleep
import sys

# Titre principal du jeu, qui s'affiche de bas en haut gràce à la 
# fonction sleep intermittante, c'est elle qui va microgeler chaque ligne
# de l'écran d'introduction du jeu.
def game_title():

    print("\n")
    print("          %%%%%%  %%  %%  %%%%%%        ")
    sleep(0.1)
    print("            %%    %%  %%  %%            ")
    sleep(0.1)
    print("            %%    %%%%%%  %%%%          ")
    sleep(0.1)
    print("            %%    %%  %%  %%            ")
    sleep(0.1)
    print("            %%    %%  %%  %%%%%%        ")
    sleep(0.1)
    print("\n")
    print("   %%%%  %%  %%  %%  %%    %%%%  %%  %%")
    sleep(0.1)
    print(" %%      %%  %%  %%  %%  %%      %% %% ")
    sleep(0.1)
    print(" %%      %%%%%%  %%  %%  %%      %%%%  ")
    sleep(0.1)
    print(" %%      %%  %%  %%  %%  %%      %% %% ")
    sleep(0.1)
    print("   %%%%  %%  %%  %%%%%%    %%%%  %%  %%")
    sleep(0.1)
    print("\n")
    sleep(0.1)
    print("      %%%%    %%    %%    %%  %%%%%%   ")
    sleep(0.1)
    print("    %%      %%  %%  %% %% %%  %%       ")
    sleep(0.1)
    print("    %%      %%%%%%  %%    %%  %%%%     ")
    sleep(0.1)
    print("    %%  %%  %%  %%  %%    %%  %%       ")
    sleep(0.1)
    print("      %%%%  %%  %%  %%    %%  %%%%%%   ")
    print("\n")
    sleep(0.75)

# Transition de bas en haut, pour les combats et les objets touvés,
# toujours avec un sleep() intermittant. 
def curtains():

    print("#################################################")
    sleep(0.2)
    print("#################################################")
    sleep(0.2)
    print("#################################################")
    sleep(0.2)
    print("#################################################")
    sleep(0.2)
    print("#################################################")
    sleep(0.2)
    print("#################################################")
    sleep(0.2)
    print("#################################################\n")
    sleep(2.5)

# Fonction qui permet d'écrire en filigrane.
# A l'aide d'une boucle for, on imprime les lettres une par une.
# Entre deux affichage, on flush l'output du print afin d'afficher une lettre.
# Enfin, on freeze 0.03s entre deux nettoyage de buffer et affichage des lettres
# afin de reproduire l'effet filigrane.
# Arpès chaque ligne, on freeze l'affichage de la ligne termniée pour afficher les 
# lignes avec un interval de 0.2 s.

def print_line(txt):

    for x in txt:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.03)
    sleep(0.4)


# Repose sur le mème principe sauf qu'on freeze 0.2s entre chaque lettre afin 
# de reproduire l'effet "barre de chargement".

def loading_bar(txt):

    for x in txt:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.2)

print_line("Ahahahah")
name = ''


# Entrer une explication de la fonction.
def ask_name():

    print_line("Quel est votre nom ?\n")
    name = str(input())
    print_line(f"Votre nom est: {name}\n")

    def confirm_name(name):
        print_line("Voulez-vous garder ce nom ? (oui/non)\n")
        choice = str(input())
        if choice.lower() == "non":
            ask_name()
            print_line(f"Bon jeu, {name}!\n\n")
            sleep(2.5)
            return name
        elif choice.lower() == "oui":
            print_line(f"Bon jeu, {name}!\n\n")
            return name
        else:
            print_line("Je n'ai pas compris !\n")
            confirm_name(name)
            return name
    confirm_name(name)
    return name

###########################################################
###########################################################

###########################################################
#   Partie 2
###########################################################

# Le menu est la partie la plus importante du programme parcequ'elle
# va permettre de centraliser le début du jeu et permettre au joueur de 
# personaliser la difficulté, de voir les commandes ou de lancer le jeu.
def Menu():
    # Choix multiple de départ
    print_line("Que souhaitez vous faire ?\n")
    print("1: Charger le jeu")
    print("2: Choisir la difficulté")
    print("3: Voir les commandes")
    # Stockage de la variable choice via un input.
    choice = int(input())
    # Attribution par défault du player à "Chuck Norris"
    # (nous verrons plus tard qu'il y a plusieurs modes).
    player = classes.Chuck_Norris
    # Si le joueur choisit de charger le jeu on le démarre.
    if choice == 1:
        start_game(player)
    # Si le choix du joueur est de changer la difficulté:
    # lancement et stockage de la fonction difficulté pour la réutiliser
    # plus tard.
    elif choice == 2:
        player = difficulte()
        print_line(f"Vous avez choisi {player.name}!\n")
        sleep(2.5)
        Menu()
        return
    # Si le choix du joueur est d'afficher les commandes, on lance
    # la fonction qui affiche les commandes à l'écran.
    elif choice == 3:
        commandes()
        sleep(2.5)
        Menu()
        return
    # Autrement, relancer le menu
    else:
        print_line("Veuillez saisir une commande valide\n")
        Menu()
        return

# Les commandes sont simples pour ce jeu, il s'agit de se déplacer selon
# les points cardinaux et non selon l'orientation propre du joueur.
def commandes():

    print_line("Vous pouvez choisir:\n")
    print("- [z] pour aller vers le nord")
    print("- [s] pour aller vers le sud")
    print("- [q] pour aller vers l'ouest")
    print("- [d] pour aller vers l'est")

# La difficulté peut être choisie: que ce soit Chuck Norris, The Fat Chuck Norris, 
# ou encore The Real Chuck Norris, l'utillisateur se régale et passe un bon moment.
def difficulte():

    print_line(
        "Souhaitez vous jouer avec [1] Chuck Norris ou [2] The Fat Chuck Norris, ou [3] The Real Chuck Norris ?\n")
    game = int(input())
    if game == 1:
        character = classes.Chuck_Norris
    elif game == 2:
        character = classes.The_Fat_Chuck_Norris
    elif game == 2:
        character = classes.The_Real_Chuck_Norris
    return character


# Cette fonction est la fonction qui permet de lancer le jeu.
# Appelée à partir de Menu(), start_game() permet d'initialiser le jeu,
# et notamment en lancant le chargement du jeu, en collectant le nom de 
# l'utilisateur pour un usage direct et ultérieur, de poser le contexte 
# textuellement ainsi que le tutoriel et le jeu brut. 
def start_game(player):

    load_game()

    global name
    name = ask_name()

    curtains()

    print_line("Contexte: ")
    print_line("Après cette partie délirante dont vous ne vous souvenez plus, il semblerait que vous vous soyez téléporté au fin fond de la jungle...\n")
    print_line(
        f"Mais vous n'avez peur de rien, car vous êtes {player.name}!\n")

    tutorial(player)
    game(player)

# Lancement de la partie avec l'écran principal du jeu, un cours texte de chargement 
# ainsi qu'une barre de chargement mise en effet avec la fonction loading_bar décrite
# ci-dessus.
def load_game():

    game_title()
    print_line("Veuillez patienter pendant que le jeu charge...\n\n")
    loading_bar("###############################################\n\n")

###########################################################
###########################################################


###########################################################
#   Partie 3
###########################################################

# Fonction que l'on découvre dans tout les RPG des années 90: un tutoriel !
# Celui-ci consiste à voir si Chuck saura réparer son couteau avant de partir 
# pour de nouvelles aventures. Les redirections rendent obligatoire la passation
# de cette partie.
def tutorial(player):

    print_line("Mais voilà, vous êtes face à un dilemme:\n")
    print_line(
        "Votre couteau est cassé et vous vous demandez si vous devez continuer sans...\n")
    # Creation de plusieurs fonctions et sous-fonctions afin de découper les parties répétées.
    # en un jeu clair et jouable.
    def tutorial1(player):
        print_line("Que choisissez-vous ?\n")
        print("1: Réparer le couteau")
        print("2: Continuer sans les mains")
        choice = int(input())
        # Si on choisit de réparer le couteau.
        if choice == 1:
            print_line("Vous avez choisi de réparer le couteau, bon choix.\n")
            # On lance un fonction qui permet de choisir avec quoi on le répare.
            def tutorial2(player):
                print_line("Avec quoi voulez vous le réparer?\n")
                print("1: Utiliser une cordelette")
                print("2: Utiliser de la glue super forte")
                print("3: Invoquer MacGiver")
                choice2 = int(input())
                # Si on choisit avec une cordelettes le joueur est récompensé.
                if choice2 == 1:
                    print_line("Votre couteau est réparé !\n")
                    print_line("Voici 20 points d'XP!\n")
                    experience = player.receive_xp(20)
                    print_line(f"Vous avez maintenant {experience} XP.\n")
                # Sinon on affiche un texte et on relance le tutoriel.
                elif choice2 == 2:
                    print_line(
                        "Erreur: Il n'y a pas de glue à 30km à la ronde\n")
                    tutorial2(player)
                    return
                # Sinon on affiche un texte et on relance le jeu.
                elif choice2 == 3:
                    print_line(
                        "Personne ne peut aider Chuck Norris, il se débrouille seul envers et contre tout.\n")
                    tutorial2(player)
                    return
            tutorial2(player)
        # On est obligé de réparer le couteau !
        elif choice == 2:
            print_line("Chuck Norris ne va nulpart sans son couteau !\n")
            tutorial1(player)
            return
        else:
            print_line("Je n'ai pas compris !")
            tutorial1(player)
    tutorial1(player)
    return

# La fonction game est la fonction centrale de ce jeu.
# Elle permer d'invoquer la fonction move() tant que le player n'a pas atteint l'une 
# des dernières case du niveau actuel, et d'upgrader la map au niveau superieur
# ainsi que de resetter la position i (lignes) du joueur pour qu'il apparaisse
# au début de la map et non à la fin.
def game(player):

    map = maps.level1
    print_line(f"Vous êtes au niveau {map.level}.\n")
    x = 1
    # print_line("Voici la map du niveau.\n")
    def game1(player, map, x):
        # Tant que le joueur n'a pas franchit le deuxième niveau (player.i == 0)
        # et qu'il est en vie, répéter la proposition de bouger (move1()).
        while player.i > 0 and player.life > 0:
            move1(map, player)
        if map.level == x and player.i == 0:
            # Augmente le x pour stocker le niveau d'après.
            if x == 2:
                map = maps.level3
                x += 1
            elif x == 1:
                map = maps.level2
                x += 1
            print_line(f"Vous avez {player.experience}XP. ") 
            print_line(f"Le nombre d'XP requis pour passer le niveau est de {map.experience}XP.\n")
            if player.experience >= map.experience:
                # Reset la position du joueur sur la derniere ligne du niveau suivant.
                player.i = 7
                # Inscrit le joueur sur la case (pour une fonctionallité prochaine).
                map.map[player.i][player.j] = "J "
                print_line(f"Vous êtes au niveau {map.level}.\n")
                # print_line("Voici la map du niveau.\n")
            else:
                # Modifie le x actuel et set la map au niveau inferieur.
                if x == 2:
                    x -= 1
                    map = maps.level1
                elif x == 3:
                    x -= 1
                    map = maps.level2
                # Fonction de restart
                def restart():
                    print_line("Voulez vous redémarrer le niveau ? (oui/non)")
                    choice = str(input())
                    if choice == "oui":
                        player.i = 6
                        print_line("Vous venez de redémarrer le niveau.\n")
                        game1(player, map, x)
                        return
                    elif choice == "non":
                        game_over() # La fonction exit serait mieux.
                        return
                    else:
                        print_line("Je n'ai pas compris !\n")
                        restart()
                restart()
        x += 1
    game1(player, maps.level1, x)
    game1(player, maps.level2, x)
    game1(player, maps.level3, x)

###########################################################
###########################################################

###########################################################
#   Partie 4
###########################################################

# Permet au joueur de se mouvoir sur la map avec les commandes du 
# code vu plus haut. Elle permet aussi de voir les commandes et 
# d'afficher l'inventaire.
def move1(game, player):

    # maps.display_map(game.displayed)
    # maps.correction_map(game.displayed)

    def move2(game, player):
        print_line("Quel déplacement souhaitez vous effectuer ?\n")
        print("Appuyez sur [c] pour afficher les commandes")
        print("Appuyez sur [i] pour afficher l'inventaire.")

        move = str(input())
        if move == "c":
            commandes()
        elif move == "i":
            player.inventory()
        # Le mouvement est directement retranscrit sur la map en temps réel.
        elif move == "z":
            map1(game, player, "z")
        elif move == "s":
            map1(game, player, "s")
        elif move == "q":
            map1(game, player, "q")
        elif move == "d":
            map1(game, player, "d")
    # Appel de fonction
    move2(game, player)
    return

# Permet de retransrire les mouvements du joueur sur la carte.
def map1(game, player, move):
    # On essaie de créer une variable qui puisse afficher la position du joueur sur la map
    # et qui imprime la position d'un objet/ennemi découvert.

    map = game.map
    map1 = map
    displayed = game.displayed
    move.lower()

    # Notons que le code répétitif est encadré par 2 sous-fonctions.
    def map2(map, displayed):
        map[player.i][player.j] = "  "
        displayed[player.i][player.j] = "  "

    def map3(map, displayed):
        # La variable position récupère le contenu d'une case 
        # (o1, o2, o3, o4 ,o5, e1, e2, e3, e4, e5, p1, p2, p3, l, P).
        position = map[player.i][player.j]
        # Supprime le contenue d'une ligne pour éviter de retomber 
        # sur les mêmes objets en tournant à droite ou a gauhe sur la même ligne
        # après avoir découvert un item.
        for x in range(1, len(map[player.i])-1):
            map[player.i][x] = "  "
        # Case la nouvelle position du joueur.
        map[player.i][player.j] = "J "
        displayed[player.i][player.j] = "J "
        # Invoque la fonction position1() pour opérer sur les items découverts 
        # chacun associé à une fonction spéicifique.
        position1(player, position)

    if move == "z":
        map2(map1, displayed)
        # Change les coordonnées du joueur.
        player.i -= 1
        map3(map1, displayed)
    elif move == "s":
        map2(map1, displayed)
        player.i += 1
        map3(map1, displayed)
    elif move == "q":
        map2(map1, displayed)
        player.j -= 1
        map3(map1, displayed)
    elif move == "d":
        map2(map1, displayed)
        player.j += 1
        map3(map1, displayed)
    return

# Cette fonction permet d'invoquer telle ou telle fonction en 
# fonction de ce qui est inscrit dans cette case de la map du niveau.
def position1(player, position):

    if position == "  ":
        print_line("Aparremment, il n'y a rien ici...\n")
    elif position[0] == "o":
        if position[1] == "1":
            # Invoque la methode find_object du player.
            player.find_object(classes.chapeau, classes.katana)
        elif position[1] == "2":
            player.find_object(classes.ceinture, classes.beretta)
        elif position[1] == "3":
            player.find_object(classes.jean, classes.m60)
        elif position[1] == "4":
            player.find_object(classes.rangers, classes.l_grenade)
        elif position[1] == "5":
            player.find_object(classes.pickup, classes.cuillere)
        return
    elif position[0] == "e":
        if position[1] == "1":
            # Invoque la fonction fight(player,monster) définie plus tard.
            fight(player, classes.scarabee)
        elif position[1] == "2":
            fight(player, classes.piranha)
        elif position[1] == "3":
            fight(player, classes.anaconda)
        elif position[1] == "4":
            fight(player, classes.crocodile)
        elif position[1] == "5":
            fight(player, classes.pantere)
        return
    elif position[0] == "p":
        if position[1] == "1":
            # Invoque la méthode find_potion(player) des potions du fichier classes.py.
            classes.potion1.find_potion(player)
        elif position[1] == "2":
            classes.potion2.find_potion(player)
        elif position[1] == "3":
            classes.potion3.find_potion(player)
        return
    elif position == "P ":
        # Invoque le scénario de la princesse.
        princess(player)
        return
    elif position == "l ":
        # Si la limite est franchie, cela appelle la fonction game_over(player).
        game_over(player)
    elif position == "ee":
        # Si un easter egg est découvert, cela invoque la fonction find_ring()
        player.find_ring()
    return

###########################################################
###########################################################

###########################################################
#   Partie 5
###########################################################

# Fonction de combat
# Lorsque le player passe devant un ennemi, il a le choix entre 3 options...
# La première est de contourner, ce qui affiche un texte et ferme la fonction
# La seconde est l'option combattre, dans laquelle on attribue au variable 
# de combat, des valeurs provenant de la classe du player (passé en argument) 
# ainsi que du monstre (également passé en argument)
# La troisième, il se soigne.
def fight(player, monster):

    print_line(f"Vous êtes face à un nouvel ennemi, {monster.name} !\n")

    def fight2(player, monster):
        print_line("Que choisissez vous ?\n")
        print("[1] Contourner \n[2] Se battre\n[3] Se soigner")
        choice = int(input())

        # Mention spéciale pour "The Fat Check Norris".
        if player.name == "The Fat Chuck Norris":
            print_line("En vous échauffant pour le combat, vous vous foulez la cheville et succombez à vos blessures. Vous profitez néanmoins de cette distraction pour vous boire un dernier verre de rhum...\n")
            game_over(player)
            return

        # Choix de contourner
        if choice == 1:
            print_line("Les mouches vous faisant bigler, vous évitez le monstre sans savoir. Quand, tant bien que mal vous réussissez à retrouver le chemin, vous vous dite que vous remettrez ce combat à plus tard...\n")
            return

        # Choix de combattre
        elif choice == 2:
            print_line("Vous avez soif de combat, alors passons à table !\n\n")
            curtains()
            # Attribution des variables en fonction de la classe de player.
            player_strength = int(player.strength)
            player_defense = int(player.defense)
            monster_defense = int(monster.defense)
            defense = player.choose_defense()
            # Si le dictionnaire player.defense n'est pas vide (The Real Chuck Norris)
            # attribuer les point de defense d'une armure choisie.
            if defense != None: 
                armor_defense = int(player.objects['Armor'][defense])

            # Ici fonction comportant la formule de dommage au monstre.
            def damages_monster(weapon, strength, defense):
                damages = round(weapon * (strength + 100) / (defense + 100))
                return damages

            # Ici celle du player.
            def damages_player(attack, defense, armor):
                damages = round(1000 * (attack + 100) /
                                (armor * (defense + 100)))
                return damages

            # Tant que la vie du joueur ou du monstre sont positifs, renouveler les attaques.
            while player.life > 0 and monster.life > 0:
                if player.life > 0:
                    # L'attaque de l'arme est la valeur de la clé obtenue a partir de choose_attack dans player.attack[].
                    weapon_attack = int(player.attacks[player.choose_attack()])
                    damages_monster1 = damages_monster(
                        weapon_attack, player_strength, monster_defense)
                    # Les dommages monster sont imputés à la vie du monstre.
                    monster.life -= damages_monster1
                    # Affiche la vie du monstre si celui-ci est encore en vie.
                    if monster.life > 0:
                        print_line("La vie du monstre est de " +
                                str(monster.life) + "\n")

                if monster.life > 0:
                    # De même, l'attaque du monstre est la valeur de la clé obtenue a partir de choose_attack dans monster.attack[].
                    monster_attack = monster.attacks[monster.choose_attack()]
                    damages_player1 = damages_player(
                        monster_attack, player_defense, armor_defense)
                    # De même, les dommages du player sont imputés à la vie du player.
                    player.life -= damages_player1
                    # Affiche la vie du player si celui-ci est encore en vie.
                    if player.life > 0:
                        print_line("Votre vie est de " +
                                str(player.life) + "\n")
            # Si la vie du joueur ou du monstre devient négative, imprimer le vainqueur
            if player.life <= 0:
                print_line("Le monstre a vaincu!\n")
                game_over(player)
                return
            elif monster.life <= 0:
                print_line("Vous avez vaincu!\n")
                player.experience += player.receive_xp(monster.give_xp)
                print_line(f"Vous reçevez {monster.give_xp}XP.\n")
                print_line(f"Vous avez {player.experience} XP !\n")
                return
            return

        # Choix de guérison
        elif choice == 3:
            potions = player.objects["Potion"]
            # Si le nombre de potions est supérieur à 0: afficher toutes les potions.
            if len(potions) > 0:
                print_line("Vous avez comme potions:\n")
                for key, value in potions.items():
                    # :à bien avoir compris:
                    i = list(potions).index(key)
                    # Si la potion se contente seulement de régénérer les points de vie.
                    if value[0] == 0:
                        print(f"[{i+1}] {key}: régénère tout les points de vie")
                    # Si la potion attribue des points de vie_max.
                    elif value[0] > 0:
                        print(
                            f"[{i+1}] {key}: régénère et rajoute {value[0]} points de vie.")
                choice = int(input())
                # Choisi la potion à l'index i de la liste de potions, grace à list() qui la transforme en liste.
                potion = list(potions)[choice-1]
                # Régénère les points de vie et ajoute de l'experience.
                player.life = player.life_max
                player.experience += potions[potion][1]
                print_line("Tout vos points de vie se sont régénérés.\n")
                # Si la potion attribue des points de vie_max, les attribuer.
                if potions[potion][0] > 0:
                    player.life_max += potions[potion][0]
                # Affiche ce que nous a apporté la potion.
                    print_line(
                        f"Maintenant, vous avez même {potions[potion][0]} points de vie en plus!\n")
                print_line(
                    f"La potion vous a rapporté {potions[potion][1]}XP !\n")
                print_line(
                    f"Vous avez maintenant {player.life_max} points de vie et {player.experience}XP.\n")
                del player.objects["Potion"][potion]

            elif len(potions) == 0:
                print_line("Vous n'avez pas de potion !\n")
            fight2(player, monster)

        # Condition de répétition de la fonction.
        else:
            print_line("Je n'ai pas compris !")
            fight2(player, monster)

    fight2(player, monster)
    return

# Fonction qui retourne le scénario de la princesse, qui n'est autre que la femme de Chuck Norris.
def princess(player):
    print_line("Vous êtes face à quelque chose d'innattendu...\n")
    print_line(
        "Cette forme que vous aperçevez est t'elle celle d'un nouveau monstre?\n")
    print_line("En vous approchant la forme devient de plus en plus évidente.\n")
    print_line("C'est celle de Gena, votre femme!'\n")
    print_line("Que choisissez vous:\n")
    print_line(
        "[1] Vous l'emportez loin de la jungle car la sortie est juste devant.\n")
    print_line(
        "[2] Vous vous emparez de votre pickup est vous faites demi-tour.\n")
    print_line("[3] Vous en profitez pour lui fournir un cigar.\n")

    # Bon vieux choix à l'ancienne.
    choice = int(input())
    if choice == 1:
        win(player)
    elif choice == 2:
        # Réattribue les coordonnêes du joueur de début et lui ajoute son pick-up.
        player.i = 6
        player.j = 4
        player.objects["Armor"]["Pick-up"] = 100
        game(player)
    elif choice == 3:
        print_line(
            "Votre femme n'est pas trop cigars, mais ce geste a raison de vous...\n")
        win(player)
    return

    # Texte de win subtil.
def win(player):
    print_line("La partie est finie.\n")
    print_line("Scaraouche, scaramouche, une fois de plus, vous avez prouvé votre talent d'aventurier grâce à vos nerf d'acier et à un mental en metal, ou peut-être l'inverse!\n")
    print_line(
        f"Vous vous en sortez avec {player.experience}XP, {player.life} points de vie et l'inventaire suivant:\n")
    player.inventory()
    print_line(
        "La map et les items découverts seront sauvegardés pour la partie suivante\n")
    # save_map()
    return

    # Texte de loose encore plus subtil.
def game_over(player):
    curtains()
    print_line("Game Over.")
    print_line("Il semble que la jungle aie eu raison de vous !\n")
    print_line(
        f"Mais vous ne vous en tirez pas trop mal {name}, vous repartez avec {player.experience}XP.\n")
    credits()
    # print_line(
    #     "La map et les items découverts seront sauvegardés pour la partie suivante\n")
    # save_map()
    return

###########################################################
###########################################################

# def save_map():
#     return


def credits():
    # print afficher del infol sur la teaml
    return


def exit():
    # quitter le jeu
    return
    
Menu()

# Inclure la map
# Faire les crédits et la redirection vers le début du jeu