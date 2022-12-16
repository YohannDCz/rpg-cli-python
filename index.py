level1 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "o2", "o2", "o2", "o2", "o2", "o2", "o2", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "  ", "e1", "e1", "e1", "e1", "e1", "  ", "l "],
          ["  ", "l ", "  ", "o1", "o1", "o1", "  ", "l ", "  "],
          ["  ", "  ", "l ", "  ", "  ", "  ", "l ", "  ", "  "],
          ["  ", "  ", "  ", "l ", "J ", "l ", "  ", "  ", "  "],
          ["  ", "  ", "  ", "  ", "l ", "  ", "  ", "  ", "  "]]
 
level2 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "e4", "e4", "e4", "e4", "e4", "e4", "e4", "l "],
          ["l ", "  ", "  ", "p2", "p2", "p2", "  ", "  ", "l "],
          ["l ", "  ", "  ", "e3", "e3", "e3", "  ", "  ", "l "],
          ["l ", "o4", "  ", "o4", "  ", "o4", "  ", "o4", "l "],
          ["l ", "  ", "p1", "p1", "p1", "p1", "p1", "  ", "l "],
          ["l ", "  ", "e2", "  ", "e2", "  ", "e2", "  ", "l "],
          ["l ", "  ", "o3", "  ", "o3", "  ", "o3", "  ", "l "]]

level3 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "  ", "P ", "  ", "P ", "  ", "P ", "  ", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "e5", "e5", "e5", "e5", "e5", "e5", "e5", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "p3", "p3", "p3", "p3", "p3", "p3", "p3", "l "],
          ["l ", "  ", "o5", "  ", "o5", "  ", "o5", "  ", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]]

### J = Joueur
### P = Princesse
### l = limite de jeu
### o = objet
### e = ennemi
### p = potion

def display_grid(grid):
    column_header= [" ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]
    grid.insert(0, column_header)
    for i in range(1,9):
        grid[i].insert(0, chr(64 + i))
    for y in range(len(grid)):
        b = "-----------------------------------------------"
        print(b)
        a = " | ".join(grid[y])
        print(a)

display_grid(level3)
display_grid(level2)
display_grid(level1)

current_position = "here"
player_name = "Bob"
game_map = ""

def inventory():
  return 
  
def Menu():
  # Afficher lel optionl du menu
  # demander à l'utilisateur 
  # en fonction du choix appeler une del 4 fonctionl du dessous
  return

# name = "Chuck Norris"
# strengh = 80
# defense = 50
# life = 400
# objects = {"knife": 20}
# attacks = {"simple slap": 10, "royal stab": 40}
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

  Chuck_Norris = player(100, 50, 3, 400, ["knife"], [["simple slap", 10]["chuck stab", 40]])
  The_Real_Chuck_Norris = player(1000, 1000, 1000, 1000, [], ["simple slap", 10])

class monster:
  def __init__(self, experience, strength, defense, life_max, attacks, give_xp):
    self.experience = experience
    self.strength = strength
    self.defense = defense
    self.life_max = life_max
    self.attacks = attacks
    self.give_xp = give_xp

  def fight(self, attack, player):
    damage = self.attacks[attack][1] * (self.strength + 100) / (player.defense + 100)
    return damage

  scarabee = monster(100, 10, 30, 100, [["Charge", 15], ["Battements d'ailes", 20], ["Transmet le Chagas", 30]], 100)
  piranha = monster(200, 20, 40, 200, [["Charge", 20], ["Slap", 30], ["Morsure", 40]], 150)
  anaconda = monster(350, 30, 50, 400, [["Coup de tête", 30], ["Morsure", 40], ["Constriction", 50]], 200)
  crocodile = monster(500, 50, 60, 700, [["Charge", 45], ["Coup de griffe", 55], ["Morsure", 65]], 300)
  pantere = monster(800, 100, 100, 1000, [["Charge", 60], ["Coup de griffe", 80], ["Morsure", 100]], 800)

def start_game():
  # afficher le contexte et le début de l'histoire
  print("Après cette partie délirante dont vous ne vous rappelez plus, il semblerait  que vous vous soyez téléporté au fin fond de la jungle...")
  print("Mais vous n'avez rien à perdre, car vous êtes CHUCK NORRIS!")
  name = ask_name()
  print(name)
  
  player(80, 50, 400, {"knife": 20}, [["simple slap", 10], ["chuck stab", 40]])
  

    
  direction = move()
  return 

def ask_name():
  print("Tout d'abord comment vous appelez-vous ?")
  name = str(input("Name: "))
  return "Bonjour " + name + ", veuillez commencer la partie..."
 
def load_game():
  # charger del datal en mémoire
  start_game()

def credits():
  # print afficher del infol sur la teaml 
  Menu()

def exit():
  # quitter le jeu
  return

def move():
  # print lel propositionl de déplacement
  # recupérer le choix de l'utilisateur 
  # En fonction du choix appeler une fonctionnalité
  return

def fight():
  # présentation du combat
  # print propositionl d'actionl du joueur
  # en fonction du choix du joueurl appeler la fonction qui correspond
  # action de l'ennemis
  return

def find_object():
  return

def event():
  return 