class player:
  def __init__(self, experience, strength, defense, life_max, objects, attacks):
    self.experience = experience
    self.strength = strength
    self.defense = defense
    self.life_max = life_max
    self.objects = objects
    self.attacks = attacks

  def fight(self, attack, monster):
    damage = self.attacks[attack][1] * (self.strength + 100) / (monster.defense + 100)
    return damage

  def inventory(self):
    print("Vous avez:")
    for i in self.objects:
      print("- ", i)

Chuck_Norris = player(100, 50, 3, 400, ["knife"], [["simple slap", 10], ["chuck stab", 40]])
The_Real_Chuck_Norris = player(1000, 1000, 1000, 1000, [], ["simple slap", 10])

class monster:
  def __init__(self, name, experience, strength, defense, life_max, attacks, give_xp):
    self.name = name
    self.experience = experience
    self.strength = strength
    self.defense = defense
    self.life_max = life_max
    self.attacks = attacks
    self.give_xp = give_xp

  def fight(self, attack, player):
    damage = self.attacks[attack][1] * (self.strength + 100) / (player.defense + 100)
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