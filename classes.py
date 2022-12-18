from time import sleep
import sys

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

  def fight_player(self, attack, monster):
    damage = self.attacks[attack][1] * (self.strength + 100) / (monster.defense + 100)
    return damage
  
  def receive_experience(self, give_experience):
    self.experience += give_experience
    return self.experience 

  def inventory(self):
    print_line("Vous avez comme arme:\n")
    for i in self.objects["Weapon"]:
      print_line(f"- {i}\n")
    print_line("Vous avez comme protection:\n")
    for key,value in self.objects["Armure"].items():
      print_line(f"- {key}: {value}\n")

  def find_object(self, object1, object2):
  # if object == "1":
    print_line("Il semble que vous soyez tombés sur des objets !\n")
    print_line(f"[1] Vous ramassez votre {object1.name.lower()} qui est tombé. (+defense).\n")
    print_line(f"[2] Vous trouvez un {object2.name.lower()} et vous en profitez pour vous fumer un autre cigar. (+attaque)\n")
    object = int(input())
    if object == 1:
      print_line(f"Vous venez de récupérer votre {object1.name.lower()}.\n")
      self.objects["Armure"][object1.name.lower()] = object1.defense
    elif object == 2:
      print_line(f"Vous vous emparez du {object2.name.loewrcase()}\n")
      self.objects["Weapon"].append(object2.name)
      for key.values in object2.items():
        self.attacks[object2.attacks.key] = object2.attack.value
        
  def attacks_list(self):
    print_line("Vous avez comme attaques:\n")
    for i in self.attacks:
      print_line(f"- {i}\n")

Chuck_Norris = player("Chuck Norris", 100, 50, 3, 400, {"Weapon": ["Knife"], "Armure": {"Chuck t-shirt": 1}}, {"Simple slap": 10, "Chuck stab": 40}, 1)
The_Real_Chuck_Norris = player("The Real Chuck Norris", 1000, 1000, 1000, 1000, [], ["simple slap", 10], 100)

class monster:
  def __init__(self, name, experience, strength, defense, life_max, attacks, give_xp):
    self.name = name
    self.experience = experience
    self.strength = strength
    self.defense = defense
    self.life_max = life_max
    self.attacks = attacks
    self.give_xp = give_xp

  def fight_monster(self, attack, player):
    damage = 1000 * (self.attacks[attack][1] * (self.strength + 100)) / (player.objects[1] * (player.defense + 100))
    return damage

scarabee = monster("scarabee", 100, 10, 30, 100, [["Charge", 15], ["Battements d'ailes", 20], ["Transmet le Chagas", 30]], 100)
piranha = monster("piranha", 200, 20, 40, 200, [["Charge", 20], ["Slap", 30], ["Morsure", 40]], 150)
anaconda = monster("anaconda", 350, 30, 50, 400, [["Coup de tête", 30], ["Morsure", 40], ["Constriction", 50]], 200)
crocodile = monster("crocodile", 500, 50, 60, 700, [["Charge", 45], ["Coup de griffe", 55], ["Morsure", 65]], 300)
pantere = monster("pantere", 800, 100, 100, 1000, [["Charge", 60], ["Coup de griffe", 80], ["Morsure", 100]], 800)

class weapon:
    def __init__(self, name, attacks):
        self.name = name
        self.attacks = attacks

couteau = weapon("Couteau", {"Chuck stab": 20})
katana = weapon("Katana", {"Katana strike": 30, "Deep stab": 35})
beretta = weapon("Beretta 92FS", {"Coup de crosse": 35, "Tir": 40})
m60 = weapon("M60 machine gun", {"Tir précis": 45, "Headshot": 50})
l_grenade = weapon("Lanceur de greande M79", {"Petites grenades": 55, "Grosses grenades": 60})
cuilliere = weapon("Cuillère", {"Lancer la cuillère": "?"})

class armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


chapeau = armor("Chapeau", 15)
ceinture = armor("Ceinture en cuir", 25)
jean = armor("Jean denim", 30)
rangers = armor("Rangers", 50)
pickup = armor("Pick-up", 100)

Chuck_Norris.find_object(chapeau, katana)