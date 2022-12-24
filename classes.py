from time import sleep
import sys
from random import randint


def print_line(txt):
    for x in txt:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.03)
    sleep(0.4)


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


class player:

    def __init__(self, name, experience, strength, defense, life, life_max, objects, attacks, level, i, j):
        self.name = name
        self.experience = experience
        self.strength = strength
        self.defense = defense
        self.life = life
        self.life_max = life_max
        self.objects = objects
        self.attacks = attacks
        self.level = level
        self.i = i
        self.j = j

    def receive_xp(self, give_experience):
        self.experience += give_experience
        return self.experience

    def inventory(self):
        if len(self.objects) == 0:
            print_line("Chuck_Norris n'a besoin de rien pour avancer..\n")
            return
        elif len(self.objects) > 0:
            if len(self.objects["Weapon"]) > 0:
                print_line("Vous avez comme armes:\n")
                for i in self.objects["Weapon"]:
                    print(f"- {i}")
                sleep(0.2)
            elif len(self.objects["Weapon"]) == 0:
                print_line("Vous n'avez pas d'armes !\n")
            if len(self.objects["Armor"]) > 0:
                print_line("Vous avez comme protections:\n")
                for key, value in self.objects["Armor"].items():
                    print(f"- {key}: ({value} défense).")
                sleep(0.2)
            elif len(self.objects["Armor"]) == 0:
                print_line("Vous n'avez pas de protections !\n")
            if len(self.objects["Potion"]) > 0:
                print_line("Vous avez comme potions:\n")
                for key, value in self.objects["Potion"].items():
                    print(f"- {key}: ({value} points de vie).")
                sleep(0.2)
            elif len(self.objects["Potion"]) == 0:
                print_line("Vous n'avez pas de potions !\n")
            return

    def find_object(self, object1, object2):
        print_line("Il semble que vous soyez tombé sur des objets !\n")
        print_line(
            f"[1] Vous ramassez: {object1.name.lower()} tombé(es) jusqu'alors.\n")
        print_line(
            f"[2] Vous trouvez: {object2.name.lower()} et vous en profitez pour vous fumer un autre cigar.\n")
        print_line(f"[3] Vous passez votre chemin.\n")
        choice = int(input())
        if choice == 1:
            print_line(
                f"Vous venez de récupérer: {object1.name.lower()}.\n")
            if self.name != "The Real Chuck Norris":
                self.objects["Armor"][object1.name] = object1.defense
            elif self.name == "The Real Chuck Norris":
                print_line("Mais Chuck Norris n'a pas besoin de se protéger, c'est Chuck Norris!\n")
            return
        elif choice == 2:
            print_line(
                f"Vous vous emparez de: {object2.name.lower()}.\n")
            if self.name != "The Real Chuck Norris":
                self.objects["Weapon"].append(object2.name)
                for key,value in object2.attacks.items():
                    self.attacks[key] = value
            elif self.name == "The Real Chuck Norris":
                print_line("Mais Chuck Norris n'en a pas besoin pour vaincre l'adversité.\n")
            return
        elif choice == 3:
            return

    def find_ring(self):
        print_line("Il semblerai que vous soyez tombé sur un easter egg !")
        print_line("Une bague d fiancaille, allez savoir pourquoi...")
        self.object.append("Ring")
    
    def choose_attack(self):
        print_line("Veuillez choisir une attaque:\n")
        for key, value in self.attacks.items():
            i = list(self.attacks).index(key)
            print(f"[{i + 1}] {key} ({value} attaque).")
        choice = int(input())
        player_attack = list(self.attacks)[choice-1]
        print_line("Vous avez choisi " + player_attack.lower() + "!\n")
        return player_attack

    def choose_defense(self):
        if len(self.objects["Armor"]) > 0:
            print_line("Veuillez choisir une armure:\n")
            for key, value in self.objects["Armor"].items():
                i = list(self.objects["Armor"]).index(key)
                print(f"[{i + 1}] {key} ({value} defense).")
            choice = int(input())
            defense_armor = list(self.objects["Armor"])[choice-1]
            print_line("Vous avez choisi " + defense_armor.lower() + "!\n")
            return defense_armor
        else:
            print_line("Chuck Norris n'a pas besoin d'armure pour rester frais.\n")
            return


The_Fat_Chuck_Norris = player("The Fat Chuck Norris", 100, 0, 0, 100, 100, {"Weapon": ["Mauvaise haleine"], "Armor": {
                              "Bedaine alccolisée": 0}, "Potion": {"Cerceuil": 0}}, {"Rot retentissant": 0}, 1, 6, 4)
Chuck_Norris = player("Chuck Norris", 100, 50, 30, 400, 400, {"Weapon": ["Couteau"], "Armor": {
                      "Chuck t-shirt": 10, "Chuck bear": 15}, "Potion": {"Alcool de comptoir": [100, 100]}}, {"Simple slap": 10, "Chuck stab": 25}, 1, 6, 4)
The_Real_Chuck_Norris = player("The Real Chuck Norris", 1000, 1000, 1000, 1000, 1000, {
"Weapon": [],"Armor": {}, "Potion": {}}, {"Simple slap": 1000}, 100, 6, 4)


class monster:

    def __init__(self, name, experience, strength, defense, life, attacks, give_xp):
        self.name = name
        self.experience = experience
        self.strength = strength
        self.defense = defense
        self.life = life
        self.attacks = attacks
        self.give_xp = give_xp

    def choose_attack(self):
        print_line("Le monstre a le choix entre trois attaques...\n")
        for key, value in self.attacks.items():
            i = list(self.attacks).index(key)
            print(f"[{i + 1}] {key} ({value} attaque).")
        sleep(2.0)
        choice = randint(1, 3)
        monster_attack = list(self.attacks)[choice-1]
        print_line("Le monstre a choisi " + monster_attack.lower() + "!\n")
        return monster_attack


scarabee = monster("un scarabee", 100, 10, 30, 100, {
                   "Charge": 15, "Battements d'ailes": 20, "Transmet le Chagas": 30}, 100)
piranha = monster("un piranha", 200, 20, 40, 200, {
                  "Charge": 20, "Slap": 30, "Morsure": 40}, 150)
anaconda = monster("un anaconda", 350, 30, 50, 400, {
                   "Coup de tête": 30, "Morsure": 40, "Constriction": 50}, 200)
crocodile = monster("un crocodile", 500, 50, 60, 700, {
                    "Charge": 45, "Coup de griffe": 55, "Morsure": 65}, 300)
pantere = monster("une panthère", 800, 100, 100, 1000, {
                  "Charge": 60, "Coup de griffe": 80, "Morsure": 100}, 800)


class weapon:

    def __init__(self, name, attacks):
        self.name = name
        self.attacks = attacks


couteau = weapon("Couteau", {"Chuck stab": 20})
katana = weapon("Katana", {"Katana strike": 30, "Deep stab": 35})
beretta = weapon("Beretta 92FS", {"Coup de crosse": 35, "Tir": 40})
m60 = weapon("M60 machine gun", {"Tir précis": 45, "Headshot": 50})
l_grenade = weapon("Lanceur de greande M79", {
                   "Petites grenades": 55, "Grosses grenades": 60})
cuillere = weapon("Cuillère", {"Lancer la cuillère": "?"})


class armor:

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


chapeau = armor("Chapeau", 15)
ceinture = armor("Ceinture en cuir", 25)
jean = armor("Jean denim", 30)
rangers = armor("Rangers", 50)
pickup = armor("Pick-up", 100)


class potion:

    def __init__(self, name, give_life_max, give_xp):
        self.name = name
        self.give_life_max = give_life_max
        self.give_xp = give_xp

    def give_life(self, player):
        player.life = player.life_max
        return

    def give_life_max1(self, player):
        player.life_max += self.give_life_max
        return

    def receive_xp(self, player):
        player.experience += self.give_xp
        return

    def find_potion(self, player):
        print_line(
            f"Vous venez de découvrir une nouvelle potion: {self.name}!\n")
        print_line("Que choisissez vous ?\n")
        print("[1] Vous choisissez de la boire d'une seule traite.")
        print("[2] Vous choisissez de l'entreposer dans votre inventaire.")
        print("[3] Vous passez votre chemin.")
        choice = int(input())
        if player.name == "The Real Chuck Norris" and choice == 1 or choice == 2:
            print_line("Vous voulez rigoler ou quoi, c'est de la pacotille, the real Chuck Norris n'en a pas besoin. Aller, on continue sans...\n")
            return
        if choice == 1:
            self.give_life(player)
            print_line("Tout vos points de vie se sont régénérés.\n")
            if self.give_life_max > 0:
                self.give_life_max1(player)
                print_line(
                    f"Maintenant, vous avez même {self.give_life_max} points de vie en plus!\n")
            self.receive_xp(player)
            print_line(f"La potion vous a rapporté {self.give_xp}XP !\n")
            print_line(
                f"Vous avez maintenant {player.life_max} points de vie et {player.experience}XP.\n")
        elif choice == 2:
            player.objects["Potion"][self.name] = [self.give_life_max, self.give_xp]
            print_line(
                f"Vous venez d'ajouter: {self.name} à votre inventaire.\n")
        elif choice == 3:
            return
        return


potion1 = potion("Alcool de comptoir", 0, 50)
potion2 = potion("Musk discret", 200, 100)
potion3 = potion("Vin chaud", 400, 300)