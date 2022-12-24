import classes
import maps
from time import sleep
import sys


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


name = ''


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


def Menu():

    print_line("Que souhaitez vous faire ?\n")
    print("1: Charger le jeu")
    print("2: Choisir la difficulté")
    print("3: Voir les commandes")

    choice = int(input())
    player = classes.Chuck_Norris
    map = maps.level1
    if choice == 1:
        start_game(player, map)
    elif choice == 2:
        player = difficulte()
        print_line(f"Vous avez choisi {player.name}!\n")
        sleep(2.5)
        Menu()
        return
    elif choice == 3:
        commandes()
        sleep(2.5)
        Menu()
        return
    else:
        print_line("Veuillez saisir une commande valide\n")
        Menu()
        return


def commandes():

    print_line("Vous pouvez choisir:\n")
    print("- [z] pour aller vers le nord")
    print("- [s] pour aller vers le sud")
    print("- [q] pour aller vers l'ouest")
    print("- [d] pour aller vers l'est")


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


def start_game(player, map):

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


def load_game():

    game_title()
    print_line("Veuillez patienter pendant que le jeu charge...\n\n")
    loading_bar("###############################################\n\n")


def tutorial(player):

    print_line("Mais voilà, vous êtes face à un dilemme:\n")
    print_line(
        "Votre couteau est cassé et vous vous demandez si vous devez continuer sans...\n")

    def tutorial1(player):
        print_line("Que choisissez-vous ?\n")
        print("1: Réparer le couteau")
        print("2: Continuer sans les mains")
        choice = int(input())
        if choice == 1:
            print_line("Vous avez choisi de réparer le couteau, bon choix.\n")

            def tutorial2(player):
                print_line("Avec quoi voulez vous le réparer?\n")
                print("1: Utiliser une cordelette")
                print("2: Utiliser de la glue super forte")
                print("3: Invoquer MacGiver")
                choice2 = int(input())
                if choice2 == 1:
                    print_line("Votre couteau est réparé !\n")
                    print_line("Voici 20 points d'XP!\n")
                    experience = player.receive_xp(20)
                    print_line(f"Vous avez maintenant {experience} XP.\n")
                    # classes.
                elif choice2 == 2:
                    print_line(
                        "Erreur: Il n'y a pas de glue à 30km à la ronde\n")
                    tutorial2(player)
                    return
                elif choice2 == 3:
                    print_line(
                        "Personne ne peut aider Chuck Norris, il se débrouille seul envers et contre tout.\n")
                    tutorial2(player)
                    return
            tutorial2(player)
        elif choice == 2:
            print_line("Chuck Norris ne va nulpart sans son couteau !\n")
            tutorial1(player)
            return
        else:
            print_line("Je n'ai pas compris !")
            tutorial1(player)
    tutorial1(player)
    return


def game(player):

    map = maps.level1
    print_line(f"Vous êtes au niveau {map.level}.\n")
    x = 1
    # print_line("Voici la map du niveau.\n")
    def game1(player, map, x):
        while player.i > 0 and player.life > 0:
            move1(map, player)
        if map.level == x and player.i == 0:
            if x == 2:
                map = maps.level3
                x += 1
            elif x == 1:
                map = maps.level2
                x += 1
            print_line(f"Vous avez {player.experience}XP. ") 
            print_line(f"Le nombre d'XP requis pour passer le niveau est de {map.experience}XP.\n")
            if player.experience >= map.experience:
                player.i = 7
                map.map[player.i][player.j] = "J "
                print_line(f"Vous êtes au niveau {map.level}.\n")
                # print_line("Voici la map du niveau.\n")
            else:
                if x == 2:
                    x -= 1
                    map = maps.level1
                elif x == 3:
                    x -= 1
                    map = maps.level2
                def restart():
                    print_line("Voulez vous redémarrer le niveau ? (oui/non)")
                    choice = str(input())
                    if choice == "oui":
                        player.i = 6
                        print_line("Vous venez de redémarrer le niveau.\n")
                        game1(player, map, x)
                        return
                    elif choice == "non":
                        game_over()
                        return
                    else:
                        print_line("Je n'ai pas compris !\n")
                        restart()
                restart()
        x += 1
    game1(player, maps.level1, x)
    game1(player, maps.level2, x)
    game1(player, maps.level3, x)

# On veut que lorsque le joueur fait un mouvement, la position s'affiche sur la grille


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
        elif move == "z":
            map1(game, player, "z")
        elif move == "s":
            map1(game, player, "s")
        elif move == "q":
            map1(game, player, "q")
        elif move == "d":
            map1(game, player, "d")

    move2(game, player)
    return


def map1(game, player, move):

    map = game.map
    map1 = map
    displayed = game.displayed
    move.lower()

    def map2(map, displayed):
        map[player.i][player.j] = "  "
        displayed[player.i][player.j] = "  "

    def map3(map, displayed):
        position = map[player.i][player.j]
        for x in range(1, len(map[player.i])-1):
            map[player.i][x] = "  "
        map[player.i][player.j] = "J "
        displayed[player.i][player.j] = "J "
        position1(player, position)

    if move == "z":
        map2(map1, displayed)
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


def position1(player, position):

    if position == "  ":
        print_line("Aparremment, il n'y a rien ici...\n")
    elif position[0] == "o":
        if position[1] == "1":
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
            classes.potion1.find_potion(player)
        elif position[1] == "2":
            classes.potion2.find_potion(player)
        elif position[1] == "3":
            classes.potion3.find_potion(player)
        return
    elif position == "P ":
        princess(player)
        return
    elif position == "l ":
        game_over(player)
    elif position == "ee":
        player.find_ring()
    return


def fight(player, monster):

    print_line(f"Vous êtes face à un nouvel ennemi, {monster.name} !\n")

    def fight2(player, monster):
        print_line("Que choisissez vous ?\n")
        print("[1] Contourner \n[2] Se battre\n[3] Se soigner")
        choice = int(input())

        if player.name == "The Fat Chuck Norris":
            print_line("En vous échauffant pour le combat, vous vous foulez la cheville et succombez à vos blessures. Vous profitez néanmoins de cette distraction pour vous boire un dernier verre de rhum...\n")
            curtains()
            game_over(player)
            return

        if choice == 1:
            print_line("Les mouches vous faisant bigler, vous évitez le monstre sans savoir. Quand, tant bien que mal vous réussissez à retrouver le chemin, vous vous dite que vous remettrez ce combat à plus tard...\n")
            return
        elif choice == 2:
            print_line("Vous avez soif de combat, alors passons à table !\n\n")
            curtains()
            player_strength = int(player.strength)
            player_defense = int(player.defense)
            monster_defense = int(monster.defense)
            defense = player.choose_defense()
            if defense != None: 
                armor_defense = int(player.objects['Armor'][defense])

            def damages_monster(weapon, strength, defense):
                damages = round(weapon * (strength + 100) / (defense + 100))
                return damages

            def damages_player(attack, defense, armor):
                damages = round(1000 * (attack + 100) /
                                (armor * (defense + 100)))
                return damages

            while player.life > 0 and monster.life > 0:
                if player.life > 0:
                    weapon_attack = int(player.attacks[player.choose_attack()])
                    damages_monster1 = damages_monster(
                        weapon_attack, player_strength, monster_defense)
                    monster.life -= damages_monster1
                    if monster.life > 0:
                        print_line("La vie du monstre est de " +
                                str(monster.life) + "\n")

                if monster.life > 0:
                    monster_attack = monster.attacks[monster.choose_attack()]
                    damages_player1 = damages_player(
                        monster_attack, player_defense, armor_defense)
                    player.life -= damages_player1
                    if player.life > 0:
                        print_line("Votre vie est de " +
                                str(player.life) + "\n")
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

        ###########################
        # Refaire cette partie avec potions objects
        ###########################

        elif choice == 3:
            potions = player.objects["Potion"]
            if len(potions) > 0:
                print_line("Vous avez comme potions:\n")
                for key, value in potions.items():
                    i = list(potions).index(key)
                    if value[0] == 0:
                        print(f"[{i+1}] {key}: régénère tout les points de vie")
                    elif value[0] > 0:
                        print(
                            f"[{i+1}] {key}: régénère et rajoute {value[0]} points de vie.")
                choice = int(input())
                potion = list(potions)[choice-1]
                player.life = player.life_max
                player.life_max += potions[potion][0]
                player.experience += potions[potion][1]
                print_line("Tout vos points de vie se sont régénérés.\n")
                if potions[potion][0] > 0:
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
        else:
            print_line("Je n'ai pas compris !")
            fight2(player, monster)
    fight2(player, monster)
    return


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

    choice = int(input())
    if choice == 1:
        win(player)
    elif choice == 2:
        player.i = 6
        player.j = 4
        game(player)
    elif choice == 3:
        print_line(
            "Votre femme n'est pas trop cigars, mais ce geste a raison de vous...\n")
        win(player)
    return


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


def game_over(player):
    print_line("Game Over.")
    print_line("Il semble que la jungle aie eu raison de vous !\n")
    print_line(
        f"Mais vous ne vous en tirez pas trop mal {name}, vous repartez avec {player.experience}XP.\n")
    print_line(
        "La map et les items découverts seront sauvegardés pour la partie suivante\n")
    # save_map()
    return


# def save_map():
#     return


def credits():
    # print afficher del infol sur la teaml
    return


def exit():
    # quitter le jeu
    return
    
Menu()

# Documenter le code
# Attribuer des roles pour l'oral
# Inclure la map
# Faire les crédits et la redirection vers le début du jeu