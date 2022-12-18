from time import sleep
import sys
from random import randint

def print_line(txt):
  for x in txt:
      print(x, end='')
      sys.stdout.flush()
      sleep(0.03)
  sleep(0.4)

class player:
  def __init__(self, name, experience, strength, defense, life_max, objects, attacks, level):
    self.name = name
    self.experience = experience
    self.strength = strength
    self.defense = defense
    self.life_max = life_max
    self.objects = objects  
    self.attacks = attacks
    self.level = level
  
  def receive_experience(self, give_experience):
    self.experience += give_experience
    return self.experience 

  def inventory(self):
    print_line("Vous avez comme arme:\n")
    for i in self.objects["Weapon"]:
      print_line(f"- {i}\n")
    print_line("Vous avez comme protection:\n")
    for key,value in self.objects["Armor"].items():
      print(f"- {key}: ({value} défense).\n")

  def find_object(self, object1, object2):
    print_line("Il semble que vous soyez tombés sur des objets !\n")
    print_line(f"[1] Vous ramassez (votre/vos) {object1.name.lower()} qui (est/sont) tombé(es).\n")
    print_line(f"[2] Vous trouvez (un/une/des) {object2.name.lower()} et vous en profitez pour vous fumer un autre cigar.\n")
    object = int(input())
    if object == 1:
      print_line(f"Vous venez de récupérer votre/vos {object1.name.lower()}.\n")
      self.objects["Armor"][object1.name] = object1.defense
    elif object == 2:
      print_line(f"Vous vous emparez (du/des/de la) {object2.name.lower()}.\n")
      self.objects["Weapon"].append(object2.name)
      for key,value in object2.attacks.items():
        self.attacks[key] = value
        
  def choose_attack(self):
    print_line("Veuillez choisir une attaque:\n")
    for key,value in self.attacks.items():
      i = list(self.attacks).index(key)
      print(f"[{i + 1}] {key} ({value} attaque).")
    choice = int(input())
    player_attack = list(self.attacks)[choice-1]
    print_line("Vous avez choisi " + player_attack.lower() + "!\n")
    return player_attack

  def choose_defense(self):
    print_line("Veuillez choisir une armure:\n")
    for key,value in self.objects["Armor"].items():
      i = list(self.objects["Armor"]).index(key)
      print(f"[{i + 1}] {key} ({value} defense).")
    choice = int(input())
    defense_armor = list(self.objects["Armor"])[choice-1]
    print_line("Vous avez choisi " + defense_armor.lower() + "!\n")
    return defense_armor
    # if attack <= len(self.attacks):
    #   if attack ==
Chuck_Norris = player("Chuck Norris", 100, 50, 3, 400, {"Weapon": ["Couteau"], "Armor": {"Chuck t-shirt": 10, "Chuck bear": 15}}, {"Simple slap": 10, "Chuck stab": 25}, 1)
The_Real_Chuck_Norris = player("The Real Chuck Norris", 1000, 1000, 1000, 1000, [], ["simple slap", 1000], 100)

class monster:
  def __init__(self, name, experience, strength, defense, life_max, attacks, give_xp):
    self.name = name
    self.experience = experience
    self.strength = strength
    self.defense = defense
    self.life_max = life_max
    self.attacks = attacks
    self.give_xp = give_xp


  def choose_attack(self):
    print_line("Le monstre a le choix entre trois attaques...\n")
    for key,value in self.attacks.items():
      i = list(self.attacks).index(key)
      print(f"[{i + 1}] {key} ({value} attaque).")
    sleep(2.0)
    choice = randint(1, 3)
    monster_attack = list(self.attacks)[choice-1]
    print_line("Le monstre a choisi " + monster_attack.lower() + "!\n")
    return monster_attack
    
scarabee = monster("un scarabee", 100, 10, 30, 100, {"Charge": 15, "Battements d'ailes": 20, "Transmet le Chagas": 30}, 100)
piranha = monster("un piranha", 200, 20, 40, 200, {"Charge": 20, "Slap": 30, "Morsure": 40}, 150)
anaconda = monster("un anaconda", 350, 30, 50, 400, {"Coup de tête": 30, "Morsure": 40, "Constriction": 50}, 200)
crocodile = monster("un crocodile", 500, 50, 60, 700, {"Charge": 45, "Coup de griffe": 55, "Morsure": 65}, 300)
pantere = monster("une panthère", 800, 100, 100, 1000, {"Charge": 60, "Coup de griffe": 80, "Morsure": 100}, 800)

class weapon:
    def __init__(self, name, attacks):
        self.name = name
        self.attacks = attacks

couteau = weapon("Couteau", {"Chuck stab": 20})
katana = weapon("Katana", {"Katana strike": 30, "Deep stab": 35})
beretta = weapon("Beretta 92FS", {"Coup de crosse": 35, "Tir": 40})
m60 = weapon("M60 machine gun", {"Tir précis": 45, "Headshot": 50})
l_grenade = weapon("Lanceur de greande M79", {"Petites grenades": 55, "Grosses grenades": 60})
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

def fight(player, monster):

  print_line(f"Vous êtes face à un nouvel ennemi, {monster.name} !\n")
  print_line("Que choisissez vous ?\n")
  print_line("[1] Contourner \n[2] Se battre\n")
  choice = int(input())

  if choice == 1:
    print_line("Les mouches vous faisant bigler, vous évitez le monstre sans savoir. Quand, tant bien que mal vous réussissez à retrouver le chemin, vous vous dite que vous remettrez ce combat à plus tard...\n")
    return

  print_line("Vous avez soif de combat, alors passons à table !\n")

  player_strength = int(player.strength)
  player_defense = int(player.defense)

  monster_defense = int(monster.defense)
  
  armor_defense = int(player.objects['Armor'][player.choose_defense()])

  def damages_monster(weapon, strength, defense):
    damages = round(weapon * (strength + 100) / (defense + 100))
    return damages

  def damages_player(attack, defense, armor):
    damages = round(1000 * (attack + 100) / (armor * (defense + 100)))
    return damages

  while player.life_max > 0 and monster.life_max > 0:
    if player.life_max > 0:
      weapon_attack = int(player.attacks[player.choose_attack()])
      print(weapon_attack)
      damages_monster1 = damages_monster(weapon_attack, player_strength, monster_defense)
      monster.life_max -= damages_monster1
      print_line("La vie du monstre est de " + str(monster.life_max) + "\n")

    if monster.life_max > 0:
      monster_attack = monster.attacks[monster.choose_attack()]
      damages_player1 = damages_player(monster_attack, player_defense, armor_defense)
      player.life_max -= damages_player1
      print_line("Votre vie est de " + str(player.life_max) + "\n")
  if player.life_max <= 0:
    print_line("Le monstre a vaincu!")
  elif monster.life_max <= 0:
    print_line("Vous avez vaincu!")
# _print_line(Chuck_Norris.attacks)
# _print_line(len(Chuck_Norris.attacks))

# fight(Chuck_Norris, scarabee)