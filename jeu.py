from random import randint
import sys
from time import sleep

#! Menu de démarrage

def GameName():
    print("\n")
    print("##        #######   ######  ########    ##      ##  #######  ########  ##       ########  ")
    print("##       ##     ## ##    ##    ##       ##  ##  ## ##     ## ##     ## ##       ##     ## ")
    print("##       ##     ## ##          ##       ##  ##  ## ##     ## ##     ## ##       ##     ## ")
    print("##       ##     ##  ######     ##       ##  ##  ## ##     ## ########  ##       ##     ## ")
    print("##       ##     ##       ##    ##       ##  ##  ## ##     ## ##   ##   ##       ##     ## ")
    print("##       ##     ## ##    ##    ##       ##  ##  ## ##     ## ##    ##  ##       ##     ## ")
    print("########  #######   ######     ##        ###  ###   #######  ##     ## ######## ########  ")
    print("\n")

def Game_Init():
    GameName()
    print("> Lancer")
    print("> Controles")
    print("> Quitter")
    mode = input('Que voulez vous faire ? ')
    print('\n')
    if(mode == "Lancer" or mode == "lancer"):
        # ? Lance la classe ou la fonction pour start une game
        sep()
        print("Création d'une game...")
        player_alive = True
        name_player = input("Quel est votre nom jeune aventurier ? \n")
        start_game(name_player)
    elif(mode == "Controles" or mode == "controles"):
        print("Voici les différents controles: \n", "Movement: \n",
              "[z] ⬆️ \n", "[q] ⬅️ \n", "[s] ⬇️ \n", "[d] ➡️ \n \n", "Inventaire: ", "[i] \n")
        Game_Init()
        return
    elif(mode == "Quitter" or mode == "quitter"):
        # * Quitte le program
        print("Vous partez déjà aventurié ?")
        exit()
    else:
        print("Demande non comprise.")
        Game_Init()

# Fonction pour savoir si le joueur est mort ou non
def Game_Over(name):
    player_alive = False
    print(name, " est mort, les secret du monde resteront à jamais indécouverts")
    sleep(1.5)
    return player_alive


#! Ce bout de code permet d'animer le texte et donne un séparateur pour ne pas avoir que du texte.


def print_ligne(txt):
    for x in txt:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.02)


def sep():
    print("=====================================")


def start_game(name):

    # Class du boss

    class BOSS():
        def __init__(self, name, pv_max, pv, attack, give_exp):
            self.name = name
            self.pv_max = pv_max
            self.pv = pv
            self.attack = attack
            self.give_exp = give_exp

    boss1 = BOSS("Pieuvre Araignée Mutante", 400, 400, 20, 600)

    # Class du personnage principal

    class Npc:
        def __init__(self, name, pv_max, pv, attack, weapon, inventory, armor, experience, lvl):
            self.name = name
            self.pv_max = pv_max
            self.pv = pv
            self.attack = attack
            self.weapon = weapon
            self.inventory = inventory
            self.armor = armor
            self.experience = experience
            self.lvl = lvl

    # Class des mobs

    class Monster:
        def __init__(self, name, pv_max, pv, attack, give_exp):
            self.name = name
            self.pv_max = pv_max
            self.pv = pv
            self.attack = attack
            self.give_exp = give_exp

    ################################
    ### Création armes + armures ###
    ################################

    class Weapon:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

    class Armor:
        def __init__(self, name, deff):
            self.name = name
            self.deff = deff

    #######################
    ### Début du joueur ###
    #######################
    joueur = Npc(name, 20, 20, 1, None, [], 0, 0, 1)
    print("Bienvenu", joueur.name, "vous avez", joueur.pv,
          "pv et", joueur.attack, "points d'attaques.")
    ##################
    ### Experience ###
    ##################
    experience = 0
    # Fonction qui augmente le level du joueur par rapport à l'exp qu'il gagne

    def lvl_up(exp, lvl):
        if (exp//(10*lvl)) != 0:
            joueur.lvl += (exp//(10*lvl))
            print("Vous êtes maintenant niveau : ", joueur.lvl)
        else:
            print("Vous êtes toujours lvl : ", joueur.lvl)
        return joueur.lvl

    ##############
    ### Potion ###
    ##############
    potion = 10
    joueur.inventory.append("potion")
    joueur.inventory.append("potion")

    ############################################
    ######## Apparition armes + armures ########
    ############################################
    stick = Weapon("Bâton en bois", 1)
    wood_weapon = Weapon("Epée en bois", 5)
    stone_weapon = Weapon("Epée en pierre", 7)
    iron_weapon = Weapon("Epée en fer", 12)
    excalibur = Weapon("Excalibur", 1000)

    leather_armor = Armor("Armure en cuir", 2)
    iron_armor = Armor("Armure en fer", 15)
    holy_armor = Armor("Armure des Dieux", 1000)

    # Fonction d'ajout des dégats de l'arme à l'attaque du joueur

    def get_weapon(weapon):
        joueur.attack = 1
        joueur.attack = weapon.damage
        print("Vous avez maintenant", joueur.attack,
              "dégats d'attaque grâce à", weapon.name, "!")

    # Fonction d'ajout de l'armure a l'armor de base du joueur

    def get_armor(armor):
        joueur.armor = 0
        joueur.armor += armor.deff
        print("vous avez maintenant", joueur.armor,
              "armor bonus grâce à", armor.name, "!")

    ###########################
    ### Apparition des mobs ###
    ###########################
    dog = Monster("Chien érant", 5, 5, 1, 10)
    serpent = Monster("Serpent", 5, 5, 2, 12)
    spider = Monster("Araignée géante", 7, 7, 3, 15)
    human_mutant = Monster("Humain Mutant", 10,  10, 4, 15)
    loup_enrage = Monster("Loup Enragé", 15, 15, 4, 20)
    aigle_mutant = Monster("Aigle Mutant", 15, 15, 4, 20)
    ver_geant = Monster("Ver Géant", 25, 25, 6, 28)
    mille_patte_geant = Monster("Mille-Pattes Géant", 30, 30, 7, 50)
    iron_golem = Monster("Golem de fer", 70, 70, 7, 70)
    baby_drake = Monster("Bébé Dragon", 100, 100, 18, 100)

    # Fonction combat

    def random_mob():
        r = randint(1, 100)
        if r >= 85:
            return serpent
        if r >= 71:
            return spider
        if r >= 57:
            return human_mutant
        if r >= 42:
            return loup_enrage
        if r >= 27:
            return aigle_mutant
        if r >= 17:
            return ver_geant
        if r >= 7:
            return mille_patte_geant
        if r >= 2:
            return iron_golem
        if r == 1:
            return baby_drake

    # Fonction qui lance le tutoriel pour le combat

    def combat_tuto(tuto, name):
        sep()
        print("Mamie : Voici ton premier combat pour t'entrainer mon enfant... Je vais te montrer les bases essentielles")
        do_what = "combattre"
        if do_what == "combattre":
            print(name, ": Ok... Mais ce n'est qu'un pauvre chien érant!")
            print(
                "Mamie : Ne commence pas à te plaindre et écoute moi! Tu est censé tous nous sauver!")
            do_what_combat = None
            round = 0
            while tuto.pv > 0 and joueur.pv > 0:
                sep()
                ### Choix Attaque ou Soin ###
                if round == 0:
                    print(
                        "Mamie : Lors de t'es combats tu aura 3 choix [attaquer][soin][fuir]! Je te conseil d'attaquer en premier! D'ailleurs pour ce combat tu ne pourras pas fuir!")
                do_what_combat = input("[attaquer],[soin] : ")
                if do_what == "1":
                    print("Mamie : Essaye de te soigner maintenant si tu veut!")
                while do_what_combat != "attaquer" and do_what_combat != "soin":
                    do_what_combat = input("[attaquer],[soin]")
                ### Choix du soin ###
                if do_what_combat == "soin":
                    if round == 0:
                        print(
                            "Mamie : Ce n'est pas très intelligent de se soigner alors que tu ne t'es pas encore fait attaquer!")
                        tuto_turn = False
                    else:
                        if "potion" not in joueur.inventory:
                            print("Vous n'avez pas de potion")
                            tuto_turn = False
                        else:
                            if joueur.pv + potion > joueur.pv_max:
                                joueur.pv = joueur.pv_max
                                joueur.inventory.remove("potion")
                                print("Vous vous êtes soignez, avez maintenant",
                                      joueur.pv, "pv!")
                                tuto_turn = True
                            else:
                                joueur.pv += potion
                                joueur.inventory.remove("potion")
                                print("Vous vous êtes soignez, avez maintenant",
                                      joueur.pv, "pv!")
                                tuto_turn = True

                ### Choix d'attaquer ###
                elif do_what_combat == "attaquer":
                    ### One shot ###
                    if joueur.attack > tuto.pv:
                        tuto.pv = 0
                        print("Wow! Joli coup! Vous avez reussis à tuer",
                              tuto.name, "!")
                        print(
                            "Mamie : Bravo tu est maintenant prêt à partir pour l'aventure !")
                        joueur.experience += tuto.give_exp
                        print("Vous avez gagné", tuto.give_exp, "d'xp!")
                        lvl_up(joueur.experience, joueur.lvl)
                        print(
                            "Mamie : Ah oui! En tuant des monstres en tout genre, tu gagne de l'experience et donc des levels!")
                        tuto_turn = False
                        return
                    else:
                        tuto.pv -= joueur.attack
                        print("Vous avez infligé", joueur.attack, "point de dégat à",
                              tuto.name, ". Il lui reste", tuto.pv, "pv!")
                        print(
                            "Mamie : Plus tard tu trouvera des armes sur l'île qui t'aideront à tapper encore plus fort!")
                        tuto_turn = True
                        if tuto.pv == 0:
                            print("Wow! Joli coup! Vous avez reussis à tuer",
                                  tuto.name, "!")
                            print(
                                "Mamie : Bravo tu est maintenant prêt à partir pour l'aventure !")
                            joueur.experience += tuto.give_exp
                            print("Vous avez gagné", tuto.give_exp, "d'xp!")
                            lvl_up(joueur.experience, joueur.lvl)
                            print(
                                "Mamie : Ah oui! En tuant des monstres en tout genre, tu gagne de l'experience et donc des levels!")
                ##########################
                ### tuto qui attaque ###
                ##########################
                if tuto_turn == True:
                    ### Finish Him ###
                    if tuto.attack > joueur.pv+joueur.armor:
                        print(tuto.name, "vous a infligé", tuto.attack,
                              "dégats! Il y a des bouts de votre corps dans tout les coins!")
                        joueur.pv = 0
                        print("Adieu", joueur.name, "...")
                        print(
                            "Mamie : Dire que je croyais qu'il serait notre sauveur à tous....")
                        Game_Over(joueur.name)
                    ### Attaque ###
                    elif tuto.pv > 0:
                        if joueur.armor > tuto.attack:
                            print(
                                tuto.name, "ne vous a infligé aucun dégats grâce à votre armure!")
                        else:
                            joueur.pv -= (tuto.attack-joueur.armor)
                            print(tuto.name, "vous attaque! Il vous a infligé",
                                  tuto.attack, "dégats! Il vous reste", joueur.pv, "pv!")
                            print(
                                "Mamie : Comme les armes, tu trouvera des armures sur l'île qui te permetteront de plus résister!")
                            if joueur.pv <= 0:
                                print("Vous êtes mort au combat...",
                                      tuto.name, "vous as tué!")
                                print("Adieu", name, ".")
                                print(
                                    "Mamie : Dire que je croyais qu'il serait notre sauveur à tous....")
                                Game_Over(joueur.name)
                round += 1

    # Fonction du vrai combat ! Presque similaire au tutoriel.    

    def combat(ennemi):
        sep()
        print("Un", ennemi.name, "est dans la zone! Il a",
              ennemi.pv, "pv et", ennemi.attack, "d'attaques!")
        # choix combattre ou éviter
        do_what = input("Voulez vous le [combattre] ou l'[éviter]? ")
        while do_what != "combattre" and do_what != "éviter":
            do_what = input("Voulez vous le [combattre] ou l'[éviter]? ")
        if do_what == "combattre":
            do_what_combat = None
            while ennemi.pv > 0 and joueur.pv > 0 and do_what_combat != "fuir":
                sep()
                ### Choix Attaque ou Soin ###
                do_what_combat = input("[attaquer],[soin],[fuir] : ")
                while do_what_combat != "attaquer" and do_what_combat != "soin" and do_what_combat != "fuir":
                    do_what_combat = input("[attaquer],[soin],[fuir]")
                ### Choix du soin ###
                if do_what_combat == "soin":
                    if "potion" not in joueur.inventory:
                        print("Vous n'avez pas de potion")
                        ennemi_turn = False
                    else:
                        if joueur.pv + potion > joueur.pv_max:
                            joueur.pv = joueur.pv_max
                            joueur.inventory.remove("potion")
                            print("Vous vous êtes soignez, avez maintenant",
                                  joueur.pv, "pv!")
                            ennemi_turn = True
                        else:
                            joueur.pv += potion
                            joueur.inventory.remove("potion")
                            print("Vous vous êtes soignez, avez maintenant",
                                  joueur.pv, "pv!")
                            ennemi_turn = True

                ### Choix d'attaquer ###
                elif do_what_combat == "attaquer":
                    ### One shot ###
                    if joueur.attack > ennemi.pv:
                        ennemi.pv = 0
                        print("Wow! Joli coup! Vous avez reussis à tuer",
                              ennemi.name, "!")
                        joueur.experience += ennemi.give_exp
                        print("Vous avez gagné", ennemi.give_exp, "d'xp!")
                        lvl_up(joueur.experience, joueur.lvl)
                        ennemi_turn = False
                    else:
                        ennemi.pv -= joueur.attack
                        print("Vous avez infligé", joueur.attack, "point de dégat à",
                              ennemi.name, ". Il lui reste", ennemi.pv, "pv!")
                        ennemi_turn = True
                        if ennemi.pv == 0:
                            print("Wow! Joli coup! Vous avez reussis à tuer",
                                  ennemi.name, "!")
                            joueur.experience += ennemi.give_exp
                            print("Vous avez gagné", ennemi.give_exp, "d'xp!")
                            lvl_up(joueur.experience, joueur.lvl)

                elif do_what_combat == "fuir":
                    print(
                        "Vous prenez vos jambes à votre cou et courrez comme une petite gazelle !!!!")
                    ennemi.pv = ennemi.pv_max
                    break
                ##########################
                ### Ennemi qui attaque ###
                ##########################
                if ennemi_turn == True:
                    ### Finish Him ###
                    if ennemi.attack > joueur.pv+joueur.armor:
                        print(ennemi.name, "vous a infligé un coup fatal de",
                              ennemi.attack, "dégats!")
                        joueur.pv = 0
                        print(ennemi.name, "vous as tué! Adieu",
                              joueur.name, "...")
                        Game_Over(joueur.name)
                    ### Attaque ###
                    elif ennemi.pv > 0:
                        if joueur.armor > ennemi.attack:
                            print(
                                ennemi.name, "ne vous a infligé aucun dégats grâce à votre armure!")
                        else:
                            joueur.pv -= (ennemi.attack-joueur.armor)
                            print(ennemi.name, "vous attaque! Il vous a infligé",
                                  ennemi.attack, "dégats! Il vous reste", joueur.pv, "pv!")
                            if joueur.pv <= 0:
                                print("Vous êtes mort au combat...",
                                      ennemi.name, "vous as tué!")
                                print("Adieu", name, ".")
                                Game_Over(joueur.name)
        else:
            print("Vous contournez", ennemi.name, "en tout discrétion...")

        if ennemi.pv <= 0:
            ennemi.pv = ennemi.pv_max

    # Fonction combat contre le boss car certaines mécaniques différentes.

    def combat_boss(boss):
        sep()
        print(name, ": Voici le boss de cette île! Qu'est ce qu'il est hideux!")
        print("C'est une", boss.name, "... Elle as",
              boss.pv, "pv et", boss.attack, "d'attaques!")
        print(name, ": Merde il à l'air balèse...")
        print(name, ": Si je m'engage à faire le combat je ne pourrais plus faire marche arrière, le mutant me rattraperait! Suis-je sûr d'être prêt ?")
        # choix combattre ou éviter
        do_what = input("Voulez vous le [combattre] ou l'[éviter]? ")
        while do_what != "combattre" and do_what != "éviter":
            do_what = input("Voulez vous le [combattre] ou l'[éviter]? ")
        if do_what == "combattre":
            print(name, ": Bon... C'est partit!")
            do_what_combat = None
            while boss.pv > 0 and joueur.pv > 0:
                sep()
                ### Choix Attaque ou Soin ###
                do_what_combat = input("[attaquer],[soin] : ")
                while do_what_combat != "attaquer" and do_what_combat != "soin":
                    do_what_combat = input("[attaquer],[soin],[fuir]")
                ### Choix du soin ###
                if do_what_combat == "soin":
                    if "potion" not in joueur.inventory:
                        print("Vous n'avez pas de potion")
                        boss_turn = False
                    else:
                        if joueur.pv + potion > joueur.pv_max:
                            joueur.pv = joueur.pv_max
                            joueur.inventory.remove("potion")
                            print("Vous vous êtes soignez, avez maintenant",
                                  joueur.pv, "pv!")
                            boss_turn = True
                        else:
                            joueur.pv += potion
                            joueur.inventory.remove("potion")
                            print("Vous vous êtes soignez, avez maintenant",
                                  joueur.pv, "pv!")
                            boss_turn = True

                ### Choix d'attaquer ###
                elif do_what_combat == "attaquer":
                    ### One shot ###
                    if joueur.attack > boss.pv:
                        boss.pv = 0
                        print("Wow! Joli coup! Vous avez reussis à tuer",
                              boss.name, "!")
                        joueur.experience += boss.give_exp
                        print("Vous avez gagné", boss.give_exp, "d'xp!")
                        lvl_up(joueur.experience, joueur.lvl)
                        boss_turn = False
                        return
                    else:
                        boss.pv -= joueur.attack
                        print("Vous avez infligé", joueur.attack, "point de dégat à",
                              boss.name, ". Il lui reste", boss.pv, "pv!")
                        boss_turn = True
                        if boss.pv == 0:
                            print("Wow! Joli coup! Vous avez reussis à tuer",
                                  boss.name, "!")
                            joueur.experience += boss.give_exp
                            print("Vous avez gagné", boss.give_exp, "d'xp!")
                            lvl_up(joueur.experience, joueur.lvl)
                ##########################
                ### boss qui attaque ###
                ##########################
                if boss_turn == True:
                    ### Finish Him ###
                    if boss.attack > joueur.pv+joueur.armor:
                        print(boss.name, "vous a éclaté la tête en vous infligeant", boss.attack,
                              "dégats! Il y a des bouts de votre corps dans tout les coins!")
                        joueur.pv = 0
                        print("Adieu", joueur.name, "...")
                        Game_Over(joueur.name)
                    ### Attaque ###
                    elif boss.pv > 0:
                        if joueur.armor > boss.attack:
                            print(
                                boss.name, "ne vous a infligé aucun dégats grâce à votre armure!")
                        else:
                            joueur.pv -= (boss.attack-joueur.armor)
                            print(boss.name, "vous attaque! Il vous a infligé",
                                  boss.attack, "dégats! Il vous reste", joueur.pv, "pv!")
                            if joueur.pv <= 0:
                                print("Vous êtes mort au combat...",
                                      boss.name, "vous as tué!")
                                print(
                                    "On peut voir des bouts de votre corps et du sang étalé sur des dizaines de mètres!")
                                print("Adieu", name, ".")
                                Game_Over(joueur.name)
        else:
            print("Vous contournez", boss.name, "en tout discrétion...")

    # Fonctions pour présenter l'histoire

    def pro(name):
        sep()
        line_1 = "Cela va bientôt faire 11 ans que la Terre a été décimée par une guerre nucléaire. \n"
        line_2 = "La fameuse planète bleue que nous avions connue est maintenant séparé en 7 îles, 7 paysages totalement différent. \n"
        line_3 = "Toutes tournent autour du noyau mystérieux émettant une lumière vive. Chaque île contient son propre univers hostile et terriblement dangereux.\n"
        line_4 = "Toutes, hormis une une seule, où les survivants, peu nombreux se sont rassemblés pour y survivre.\n"
        line_5 = "Ils l’appellent, l’île du miracle, car on y trouve aucun mutant, aucun danger et une terre fertile.\n"
        line_5 = "Les survivants ont d’ailleurs fait une découverte des plus étranges : les Ponéglyphes.\n"
        line_6 = "Beaucoup de jeune de nos jours rêve de partir à l'aventure découvrir les secrets du monde je suppose que vous ferez de même \n"
        line_7 = "L’aventure ne sera pas de tout repos, préparez vous "
        print_ligne(line_1)
        sleep(0.5)
        print_ligne(line_2)
        sleep(0.5)
        print_ligne(line_3)
        sleep(0.5)
        print_ligne(line_4)
        sleep(0.5)
        print_ligne(line_5)
        sleep(0.5)
        print_ligne(line_6)
        sleep(0.5)
        print_ligne(line_7)
        sleep(0.5)
        print(name)

    def Spawn_Panel(name):
        line_1 = "Vous vous réveiller sur la première ile aussi appelé l'ile du miracle.Le nom de cette iles est du à l'absence des monstre sur cet île.\n Cependant,"
        line_2 = "après vous être fait réveillé par un chien \n, une mamie nous interpelle et nous dis que nous devons nous préparer à nous battre car le chien ne va pas lacher notre jambe \n"
        line_3 = "confus ", name, " décide d'écouter la mamie et de ce battre contre le chien\n"
        line_4 = "La mamie nous dis de la suivre.... \n Mamie: je suis l'amie de votre mère disparu,je vous hébèrge depuis votre sommeil de la génèse,la maladie qui plongea une partie de la population dans un sommeil profond \n"
        line_5 = "Vous suivez la mamie vers un lieu sur. \n"
        line_6 = "Une fois arrivé la mamie nous explique ce qu'il s'est passé pendant notre long sommeil qui dura 11 ans \n"

        print_ligne(line_1)
        sleep(0.5)
        print_ligne(line_2)
        sleep(0.5)
        print_ligne(line_3)
        sleep(0.5)
        combat_tuto(dog, name)
        print("\n")
        print_ligne(line_4)
        sleep(0.5)
        print_ligne(line_5)
        sleep(0.5)
        print("\n")
        sep()
        print("Découverte du lieu: grange de la vielle gourou")
        sep()
        print("\n")
        sleep(0.5)
        print_ligne(line_6)
        pro(name)

    Spawn_Panel(name)

    def island(name):
        # ? 1. Description du lieu
        # ? 2. Initialisation de la map
        # ? 2.5 Loot + Combat
        # ? 3. Boss
        # ? 4. Envoie sur la prochaine map et on recommence

        def bigmap():
            map = [
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
                    "[ ]", "[ ]", "[ ]", "[💀]", "[ ]"],
                ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], ]

            # Spawn du joueur sur la map
            map[0][0] = "👀"

            # Première apparition de la map
            for i in map:
                print(i)

            # Déplacement
            x = 0
            y = 0
            where = 0
            while where != "quit" and joueur.pv > 0:
                change_place = "yes"
                actu_map = "yes"
                something_happend = "yes"
                # Demande au joueur quoi faire
                sep()
                print("Quitter la partie [quit]")
                print("Regardez votre [i]")
                where = input("Ou déplacez vous : [z],[q],[s],[d] : ")
                if where != "quit" and where != "z" and where != "q" and where != "s" and where != "d" and where != "inventaire":
                    sep()
                    print("Choix non compris !")
                    actu_map = "no"
                    something_happend = "no"
                # Joueur choisis INVENTAIRE
                if where == "quit":
                    actu_map = "no"
                    something_happend = "no"
                    sep()
                    print("A bientot aventurier!")
                elif where == "i":
                    sep()
                    print("Vous êtes lvl :", joueur.lvl)
                    print("Inventaire : ", joueur.inventory)
                    navigate_inv = "yes"
                    while navigate_inv != "exit":
                        print("[exit] pour quitter.")
                        navigate_inv = input(
                            "[Nom de l'objet] pour l'utiliser : ")
                        if navigate_inv == "exit":
                            actu_map = "no"
                            something_happend = "no"
                        elif navigate_inv == leather_armor.name:
                            if leather_armor.name in joueur.inventory:
                                get_armor(leather_armor)
                            else:
                                print("Vous n'avez pas cette armure!")
                        elif navigate_inv == iron_armor.name:
                            if iron_armor.name in joueur.inventory:
                                get_armor(iron_armor)
                            else:
                                print("Vous n'avez pas cette armure!")
                        elif navigate_inv == holy_armor.name:
                            if holy_armor.name in joueur.inventory:
                                get_armor(holy_armor)
                            else:
                                print("Vous n'avez pas cette armure!")
                        elif navigate_inv == wood_weapon.name:
                            if wood_weapon.name in joueur.inventory:
                                get_weapon(wood_weapon)
                            else:
                                print("Vous n'avez pas cette arme!")
                        elif navigate_inv == stone_weapon.name:
                            if stone_weapon.name in joueur.inventory:
                                get_weapon(stone_weapon)
                            else:
                                print("Vous n'avez pas cette arme!")
                        elif navigate_inv == iron_weapon.name:
                            if iron_weapon.name in joueur.inventory:
                                get_weapon(iron_weapon)
                            else:
                                print("Vous n'avez pas cette arme!")
                        elif navigate_inv == excalibur.name:
                            if excalibur.name in joueur.inventory:
                                get_weapon(excalibur)
                            else:
                                print("Vous n'avez pas cette arme!")

                ################# Touche Pour Se Déplacer ###################
                # Haut
                elif where == "z":
                    if map[x-1][y] == "[💀]":
                        combat_boss(boss1)
                        something_happend = "no"
                        change_place = "no"
                    elif x-1 == -1:
                        print("Impossible vous allez tomber dans le vide!")
                        something_happend = "no"
                    else:
                        if change_place == "yes":
                            map[x][y] = "[ ]"
                            x -= 1
                            map[x][y] = "👀"
                # Bas
                elif where == "s":
                    if map[x+1][y] == "[💀]":
                        combat_boss(boss1)
                        something_happend = "no"
                        change_place = "no"
                    elif x+1 == 10:
                        print("Impossible vous allez tomber dans le vide!")
                        something_happend = "no"
                    else:
                        if change_place == "yes":
                            map[x][y] = "[ ]"
                            x += 1
                            map[x][y] = "👀"
                # Droite
                elif where == "d":
                    if map[x][y+1] == "[💀]":
                        combat_boss(boss1)
                        something_happend = "no"
                        change_place = "no"
                    elif y+1 == 10:
                        print("Impossible vous allez tomber dans le vide!")
                        something_happend = "no"
                    else:
                        if change_place == "yes":
                            map[x][y] = "[ ]"
                            y += 1
                            map[x][y] = "👀"
                # Gauche
                elif where == "q":
                    if map[x][y-1] == "[💀]":
                        combat_boss(boss1)
                        something_happend = "no"
                        change_place = "no"
                    if y-1 == -1:
                        print("Impossible vous allez tomber dans le vide!")
                        something_happend = "no"
                    else:
                        if change_place == "yes":
                            map[x][y] = "[ ]"
                            y -= 1
                            map[x][y] = "👀"
                ######### Actualise la map à chaque fois ########
                if actu_map == "yes":
                    for i in map:
                        print(i)
                ############## Choix Random ( COMBAT, Trouver ARME/ARMURE ETC ###############
                if something_happend == "yes":
                    what_happend = randint(1, 10)
                    # Lance un combat aléatoirement (3 chances /10)
                    if what_happend >= 8:
                        combat(random_mob())
                    # Trouve une armure (1 chance /10)
                    elif what_happend >= 7:
                        a = randint(1, 100)
                        if a >= 65:
                            print("Vous avez trouvé une armure en Cuir !")
                            if leather_armor.name not in joueur.inventory:
                                joueur.inventory.append(leather_armor.name)
                            else:
                                print(
                                    "Mais vous l'avez déjà dans votre inventaire!")
                        elif a >= 5:
                            print("Vous avez trouvé une armure en Fer!")
                            if iron_armor.name not in joueur.inventory:
                                joueur.inventory.append(iron_armor.name)
                            else:
                                print(
                                    "Mais vous l'avez déjà dans votre inventaire!")
                        elif a >= 1:
                            print("Vous avez trouvé l'armure des Dieux!")
                            if holy_armor.name not in joueur.inventory:
                                joueur.inventory.append(holy_armor.name)
                            else:
                                print(
                                    "Mais vous l'avez déjà dans votre inventaire!")
                    # Trouve une arme (1 chance /10)
                    elif what_happend >= 6:
                        r = randint(1, 100)
                        if r >= 50:
                            print("Vous avez trouvé une Arme En Bois!")
                            if wood_weapon.name not in joueur.inventory:
                                joueur.inventory.append(wood_weapon.name)
                            else:
                                print(
                                    "Mais vous l'avez déjà dans votre inventaire!")
                        elif r >= 25:
                            print("Vous avez trouvé une Arme En Pierre!")
                            if stone_weapon.name not in joueur.inventory:
                                joueur.inventory.append(stone_weapon.name)
                            else:
                                print(
                                    "Mais vous l'avez déjà dans votre inventaire!")
                        elif r >= 3:
                            print("Vous avez trouvé une Arme En Fer!")
                            if iron_weapon.name not in joueur.inventory:
                                joueur.inventory.append(iron_weapon.name)
                            else:
                                print(
                                    "Mais vous l'avez déjà dans votre inventaire!")
                        elif r > 0:
                            print("Vous avez trouvé EXCALIBUR !!!!!!!!!!!!")
                            if excalibur.name not in joueur.inventory:
                                joueur.inventory.append(excalibur.name)
                            else:
                                print(
                                    "Mais vous l'avez déjà dans votre inventaire!")
                    # Trouve une potion (2 chances /10)
                    elif what_happend >= 4:
                        print("Vous avez trouvé une potion de vie !")
                        joueur.inventory.append("potion")
                        print(joueur.inventory)
                    else:
                        print("Rien ne se passe.")

        bigmap()
    # ? Pour les iles aller voir comment ça se déroule (CTRL+Click sur la fonction en dessous)
    print("\n")
    desc = "Description de l'ile"
    print("\n")
    print(desc)
    print("\n")
    island(name)
    print("Fin de l'ile 1")


player_alive = ""

# Fonction qui lance le jeu !

def game():
    if player_alive == True:
        Game_Init()
    else:
        print("On peut pas être bon en tout mais on a tous une seconde chance.")
        player_alive == True
        Game_Init()
    Game_Init()


game()