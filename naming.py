def naming():
    name = str(input("Quel est ton Nom ?"))
    print("Ton nom est : {}".format(name))
    sure_name()
def sure_name():
    r = str(input("voulez vous garder ce nom ?(oui/non)"))
    if r.lower() == "non":
        naming()
    elif r.lower() == "oui":
        print("Bon jeu !")
    else:
        print("Je n'ai pas compris !")
        sure_name()
naming()