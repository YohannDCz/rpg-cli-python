import script 

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

  def attacks_list(self):
    print_line("Vous avez comme attaques:\n")
    for i in self.attacks:
      print_line(f"- {i}\n")

  def find(self, object):
    if object == "1":
      print_line("Il semble que vous soyez tombés sur des objets !\n")
      print_line("[1] Vous ramassez votre chapeau qui est tombé. (+defense).\n")
      print_line("[2] Vous trouvez un katana non loin de là et il ne semble appartenir à personne. (+attaque)\n")
      object1 = int(input())
      if object1 == 1:
        print_line("Vous venez de récupérer votre chapeau.\n")
        self.objects["Armure"]["Chapeau"] = 15
      elif object1 == 2:
        print_line("Ni une ni deux, vous vous emparez du katana\n")
        self.objects["Weapon"].append("Katana")
        self.attacks["Katana slice"] = 35
    elif object == "2":
      print_line("Il semble que vous soyez tombés sur des objets !\n")
      print_line("[1] Vous récupérez votre ceinture en cuir (+defense).\n")
      print_line("[2] Vous ramassez votre arme préférée, le Beretta 92FS (+attaque).\n")
      object2 = int(input())
      if object2 == 1:
        print_line("Vous venez de récupérer votre ceinture.\n")
        self.objects["Armure"]["Ceinture"] = 25
      elif object2 == 2:
        print_line("Vous vous emparez de votre Beretta 92FS et vous en profitez pour tirer sur lese moustiques.\n")
        self.objects["Weapon"].append("Beretta 92FS")
        self.attacks["Tir à l'aveuglette"] = 55
        self.attacks["Bon baiser de beretta"] = 75
    elif object == "3":
      print_line("Il semble que vous soyez tombés sur des objets !\n")
      print_line("[1] Vous récupérez votre jean et sans qui cela n'a pas semblé génant (++defense).\n")
      print_line("[2] Vous ramassez votre deuxième arme préférée, pensant que ce rpg est bien fait, le M60 Machine Gun (++attaque).\n")
      object3 = int(input())
      if object3 == 1:
        print_line("Vous venez de récupérer votre jean.\n")
        self.objects["Armure"]["Jean"] = 40
      elif object3 == 2:
        print_line("Vous vous emparez de votre M60 Machine Gun et vous en profitez pour vous fumer un cigare.\n")
        self.objects["Weapon"].append("M60 Machine Gun")
        self.attacks["Tir à vif"] = 90
        self.attacks["Tir groupé"] = 100
    elif object == "4":
      print_line("Il semble que vous soyez tombés sur des objets !\n")
      print_line("[1] Vous enfourchez vos rangers, les chaussettes ne suffisant plus à votre avancée (+++defense).\n")
      print_line("[2] Vous trouvez votre fameux lanceur de grenade M79 (+++attaque).\n")
      object4 = int(input())
      if object4 == 1:
        print_line("Vous venez de récupérer vos rangers.\n")
        self.objects["Armure"]["Rangers"] = 65
      elif object4 == 2:
        print_line("Vous saluez votre lance grenade en lui promettant de belle aventure... Parler aux armes, il n'y a que ça de vrai, entre nous.\n")
        self.objects["Weapon"].append("Lanceur de grenade M79")
        self.attacks["Tir bourrain"] = 120
        self.attacks["Tir dans le tas"] = 130
    elif object == "5":
      print_line("Il semble que vous soyez tombés sur des objets !\n")
      print_line("[1] Vous rentrez dans votre pick-up, soulagé que la chance tourne enfin (++++defense).\n")
      print_line("[2] Vous ramassez une cuillère (?attaque).\n")
      object5 = int(input())
      if object5 == 1:
        print_line("Vous venez de récupérer votre pick-up.\n")
        self.objects["Armure"]["Pick-up"]= 150
      elif object5 == 2:
        print_line("Vous ramassez la cuillère.")
        self.objects["Weapon"].append("Cuillère")
        self.attacks["L'attaque de la cuillère"] = 1000

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

couteau = weapon("Couteau", [["Chuck stab", 20]])
katana = weapon("Katana", [["Katana strike", 30], ["Deep stab", 35]])
beretta = weapon("Beretta 92FS", [["Coup de crosse", 35], ["Tir", 40]])
m60 = weapon("M60 machine gun", [["Tir précis", 45], ["Headshot", 50]])
l_grenade = weapon("Lanceur de greande M79", [["Petites grenades", 55], ["Grosses grenades", 60]])
cuilliere = weapon("Cuillère", ["Lance la cuillère", 1000])

class armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


chapeau = armor("Chapeau", 15)
ceinture = armor("Ceinture en cuir", 25)
jean = armor("Jean denim", 30)
rangers = armor("Rangers", 50)
pickup = armor("Pick-up", 100)