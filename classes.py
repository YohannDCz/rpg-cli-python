##############################################################
#   Partie 6
##############################################################

# Dans ce fichier, nous allons voir les classes auxquelles
# fait référence un bon nombre de fonctions du fichier script.py
# L'INTÉGRALITÉ des classes se trouve ici:
#   - player (+3 instances de players).
#   - monster (+5 instances de monsters).
#   - weapon (+6 instance de weapons, avec 3 attaques chacunes).
#   - armor (+5 instances de armor).
#   - potion (+3 instance de potions).

# Imports similaire aux autre import du fichier script.py.
from time import sleep
import sys
from random import randint

# Pour éviter l'import circulaire, nous avons décidé d'ajouter
# quelques fonction du fichier scripts.

# Celle-co, décrite juste avant.


def print_line(txt):
    for x in txt:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.03)
    sleep(0.4)

# Mais aussi celle-ci.


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
    # Constructuer de la classe player.
    def __init__(self, name, experience, strength, defense, life, life_max, objects, attacks, level, i, j, position):
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
        self.position = position

    # Fonction de transmission de l'experience.
    def receive_xp(self, give_experience):
        self.experience += give_experience
        return self.experience

    # Fonction pour afficher les objets sous forme d'inventaire du joueur
    def inventory(self):
        # Condition pour le mode "The Real Chuck Norris".
        if len(self.objects) == 0:
            print_line("Chuck_Norris n'a besoin de rien pour avancer..\n")
            return
        elif len(self.objects) > 0:
            if len(self.objects["Weapon"]) > 0:
                print_line("Vous avez comme armes:\n")
                # Les weapons sont stockés dans la variable object["Weapon"]
                # sous forme de liste.
                for i in self.objects["Weapon"]:
                    print(f"- {i}")
                sleep(0.2)
            # Si le joueur n'a pas d'armes, l'afficher.
            elif len(self.objects["Weapon"]) == 0:
                print_line("Vous n'avez pas d'armes !\n")
            if len(self.objects["Armor"]) > 0:
                print_line("Vous avez comme protections:\n")
                # On crée une liste bi-dimensionnelle d'items key, items valeur et
                # On itérère à travers ce dernier.
                for key, value in self.objects["Armor"].items():
                    print(f"- {key}: ({value} défense).")
                sleep(0.2)
            # Si le joueur n'a pas d'armures, l'afficher.
            elif len(self.objects["Armor"]) == 0:
                print_line("Vous n'avez pas de protections !\n")
            if len(self.objects["Potion"]) > 0:
                print_line("Vous avez comme potions:\n")
                # Mème schémas que les items d'arme et d'armures.
                for key, value in self.objects["Potion"].items():
                    # on itère à travers ce dernier.
                    print(f"- {key}: ({value} points de vie).")
                sleep(0.2)
            # Si le joueur n'a pas de potionsm l'afficher.
            elif len(self.objects["Potion"]) == 0:
                print_line("Vous n'avez pas de potions !\n")
            return

    def find_object(self, object1, object2):
        # Texte à choix multiple.
        print_line("Il semble que vous soyez tombé sur des objets !\n")
        print_line(
            f"[1] Vous ramassez: {object1.name.lower()} tombé(es) jusqu'alors.\n")
        print_line(
            f"[2] Vous trouvez: {object2.name.lower()} et vous en profitez pour vous fumer un autre cigar.\n")
        print_line(f"[3] Vous passez votre chemin.\n")
        choice = int(input())

        # Si le choix est de ramasser l'arnure
        if choice == 1:
            # Afficher texte avec nom de l'armure
            print_line(
                f"Vous venez de récupérer: {object1.name.lower()}.\n")
            # Et attribuer le nouveau nom de l'armure à des points de défense dans le répertoire "Armor"
            if self.name != "The Real Chuck Norris":
                self.objects["Armor"][object1.name] = object1.defense
            # Mention spéciale pour le mode "The Real Chuck Norris"
            elif self.name == "The Real Chuck Norris":
                print_line(
                    "Mais Chuck Norris n'a pas besoin de se protéger, c'est Chuck Norris!\n")
            return
        # Si le choix est de ramasser l'arme
        elif choice == 2:
            # Afficher texte avec nom de l'arme
            print_line(
                f"Vous vous emparez de: {object2.name.lower()}.\n")
            if self.name != "The Real Chuck Norris":
                # Ajouter nom de l'arme à la liste d'armes.
                self.objects["Weapon"].append(object2.name)
                # Et attribuer le nouveau nom de l'attaque à des points d'attaque dans le dictionnaire "Attacks".
                for key, value in object2.attacks.items():
                    self.attacks[key] = value
            # Mention spéciale "The Real Chuck Norris"
            elif self.name == "The Real Chuck Norris":
                print_line(
                    "Mais Chuck Norris n'en a pas besoin pour vaincre l'adversité.\n")
            return
        # Autrement, retourner rien.
        elif choice == 3:
            return
        else:
            print_line("Je n'ai pas compris !\n")
            self.find_object(object1, object2)

    # Méthode qui sert à séduire la princesse
    def find_ring(self):
        print_line("Il semblerai que vous soyez tombé sur un easter egg !\n")
        print_line("Une bague d fiancaille, allez savoir pourquoi...\n")
        self.object.append("Ring")

    # Méthode qui sert à choisir l'attaque parmis le dictionnaire player.attacks
    def choose_attack(self):
        print_line("Veuillez choisir une attaque:\n")
        for key, value in self.attacks.items():
            # Affiche le numéro d'index de la liste(attacks) ainsi que l'attaque
            # (la clé) et les points d'attaques (la valeur).
            i = list(self.attacks).index(key)
            print(f"[{i + 1}] {key} ({value} attaque).")
        choice = int(input())
        # Choisit l'attaque selon son index dans la liste proposée
        player_attack = list(self.attacks)[choice-1]
        # Affiche et retourne (!) l'attaque que le joueur a choisi
        print_line("Vous avez choisi " + player_attack.lower() + "!\n")
        # Sahant qu'il y aura toujours au minimum l'attaque du couteau: chuck stab
        # D'oû le non-besoin de faire une conditionnelle supplémentaire (CF méthode suivante)
        return player_attack

    def choose_defense(self):
        # Ajout de la condition pour le mode "The Real Chuck Norris" car il ne récupère aucune armure
        if len(self.objects["Armor"]) > 0:
            print_line("Veuillez choisir une armure:\n")
            for key, value in self.objects["Armor"].items():
                i = list(self.objects["Armor"]).index(key)
                print(f"[{i + 1}] {key} ({value} defense).")
            choice = int(input())
            # Stock le nom de l'armure dans la variable defense_armor,
            # sera réutilisé plus tard pour extraire les points de défense du joueur.
            if choice - 1 <= len(self.objects["Armor"]):
                defense_armor = list(self.objects["Armor"])[choice-1]
                print_line("Vous avez choisi " + defense_armor.lower() + "!\n")
                return defense_armor
            else:
                print_line("Je n'ai pas compris !\n")
                self.choose_defense()
        # Condition "The Real Chuck Norris"
        else:
            print_line(
                "Chuck Norris n'a pas besoin d'armure pour rester frais.\n")
            return


# Ici les trois mode de dificulté, toutes trois instances de player.
The_Fat_Chuck_Norris = player("The Fat Chuck Norris", 100, 0, 0, 100, 100, {"Weapon": ["Mauvaise haleine"], "Armor": {
                              "Bedaine alccolisée": 0}, "Potion": {"Cerceuil": 0}}, {"Rot retentissant": 0}, 1, 6, 4, "  ")
Chuck_Norris = player("Chuck Norris", 100, 50, 30, 400, 400, {"Weapon": ["Couteau"], "Armor": {
                      "Chuck t-shirt": 15, "Chuck bear": 25}, "Potion": {"Alcool de comptoir": [100, 100]}}, {"Simple slap": 10, "Chuck stab": 25}, 1, 6, 4, "  ")
The_Real_Chuck_Norris = player("The Real Chuck Norris", 1000, 1000, 1000, 1000, 1000, {
    "Weapon": [], "Armor": {}, "Potion": {}}, {"Simple slap": 1000}, 100, 6, 4, "  ")


class monster:
    # Constructeur de la classe monster. À noter qu'ils ne disposent d'aucune armure,
    # d'oû la formule de combat différente.
    def __init__(self, name, experience, strength, defense, life, attacks, give_xp):
        self.name = name
        self.experience = experience
        self.strength = strength
        self.defense = defense
        self.life = life
        self.attacks = attacks
        self.give_xp = give_xp

    # La classe monster dispose de sa propre méthode de combat et n'aura
    # que trois attaques quelque soit sont type.
    def choose_attack(self):
        print_line("Le monstre a le choix entre trois attaques...\n")
        # Là aussi, affiche le numéro d'index de la liste(attacks) ainsi que l'attaque
        # (la clé) et les points d'attaques (la valeur).
        for key, value in self.attacks.items():
            i = list(self.attacks).index(key)
            print(f"[{i + 1}] {key} ({value} attaque).")
        sleep(2.0)
        # Le monstre fera un choix entre 0 et 3 afin de choisir une attaque
        choice = randint(1, 3)
        # Stock le nom de l'attaque dans la variable monster_attack,
        # sera réutilisé plus tard pour extraire les points d'attaque.
        monster_attack = list(self.attacks)[choice-1]
        print_line("Le monstre a choisi " + monster_attack.lower() + "!\n")
        return monster_attack


# Ici plusieurs instances de monster
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

# Création de la classe "weapon" pour les différentes armes
# Chacune d'entre elles ont une variable attacks qui sert à non seulement ajouter
# l'arme à la liste d'arme player.objects["Weapon"] du joueur mais aussi d'ajouter l'attaque
# au dictionnaire attacks du joueur.


class weapon:

    def __init__(self, name, attacks):
        self.name = name
        self.attacks = attacks


# Ici plusieurs instances d'armes
couteau = weapon("Couteau", {"Chuck stab": 20})
katana = weapon("Katana", {"Katana strike": 30, "Deep stab": 35})
beretta = weapon("Beretta 92FS", {"Coup de crosse": 35, "Tir": 40})
m60 = weapon("M60 machine gun", {"Tir précis": 45, "Headshot": 50})
l_grenade = weapon("Lanceur de greande M79", {
                   "Petites grenades": 55, "Grosses grenades": 60})
cuillere = weapon("Cuillère", {"Lancer la cuillère": "?"})


# Création de la classe "armor" pour les différentes armures
# Chacune d'entre elles ont une variable defense, qui sera importante dans
# le calcul des dommage du montstre sur le player

class armor:

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


# Ici plusieurs instances d'armures
chapeau = armor("Chapeau", 30)
ceinture = armor("Ceinture en cuir", 45)
jean = armor("Jean denim", 55)
rangers = armor("Rangers", 75)
pickup = armor("Pick-up", 100)


# Création de la classe potion
# Les méthodes ont pour fonction de trouver une potion, de régénérer
# les points de vie, d'étendre la vie max, ou encore de donner de
# l'experience au joueur.

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

    # Cette fonction permet de boire la potion et de régénérer/donner de la vie
    # supplémentaire du joueur, d'entreposer la potion dans l'inventaire ou de ne rien faire.
    # Cdtte méthode est similaire à l'option "se guerrir" de la fonction fight()
    # dans le fichier script.py
    def find_potion(self, player):
        print_line(
            f"Vous venez de découvrir une nouvelle potion: {self.name}!\n")
        print_line("Que choisissez vous ?\n")
        print("[1] Vous choisissez de la boire d'une seule traite.")
        print("[2] Vous choisissez de l'entreposer dans votre inventaire.")
        print("[3] Vous passez votre chemin.")
        choice = int(input())
        # Condition spéciale pour "The Real Chuck Norris"
        if player.name == "The Real Chuck Norris" and (choice == 1 or choice == 2):
            print_line(
                "Vous voulez rigoler ou quoi, c'est de la pacotille, the real Chuck Norris n'en a pas besoin. Aller, on continue sans...\n")
            return
        # Le choix est de la boire d'une seule traite
        if choice == 1:
            # Pour toutes les potions, régénérer la vie et afficher le message
            self.give_life(player)
            print_line("Tout vos points de vie se sont régénérés.\n")
            # Autrement dit si la potion n'est pas "Alcool de comptoir"
            # (c'est la seule qui ne donne pas de vie supplémentaire)
            if self.give_life_max > 0:
                self.give_life_max1(player)
                print_line(
                    f"Maintenant, vous avez même {self.give_life_max} points de vie en plus!\n")
            # Pour toutes les potions, afficher les XP récupérés
            self.receive_xp(player)
            print_line(f"La potion vous a rapporté {self.give_xp}XP !\n")
            print_line(
                f"Vous avez maintenant {player.life_max} points de vie et {player.experience}XP.\n")
        # Le choix de l'entreposer dans l'inventaire
        elif choice == 2:
            player.objects["Potion"][self.name] = [
                self.give_life_max, self.give_xp]
            print_line(
                f"Vous venez d'ajouter: {self.name} à votre inventaire.\n")
        # Le choix de ne rien faire
        elif choice == 3:
            return
        else:
            print_line("Je n'ai pas compris !\n")
            self.find_potion(player)
        return


# Ici plusieur instances de potions
potion1 = potion("Alcool de comptoir", 0, 50)
potion2 = potion("Musk discret", 200, 100)
potion3 = potion("Vin chaud", 400, 300)