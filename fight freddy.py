while player.life > 0 and monster.life > 0:
                if player.life > 0:
                    # L'attaque de l'arme est la valeur de la clé obtenue a partir de choose_attack dans player.attack[].
                    weapon_attack = int(player.attacks[player.choose_attack()])
                    damages_monster1 = damages_monster(
                        weapon_attack, player_strength, monster_defense)
                    # Les dommages monster sont imputés à la vie du monstre.
                    monster.life -= damages_monster1
                    # Affiche la vie du monstre si celui-ci est encore en vie.
                    if monster.life > 0:
                        print_line("La vie du monstre est de " +
                                   str(monster.life) + "\n")

                if monster.life > 0:
                    # De même, l'attaque du monstre est la valeur de la clé obtenue a partir de choose_attack dans monster.attack[].
                    monster_attack = monster.attacks[monster.choose_attack()]
                    damages_player1 = damages_player(
                        monster_attack, player_defense, armor_defense)
                    # De même, les dommages du player sont imputés à la vie du player.
                    player.life -= damages_player1
                    # Affiche la vie du player si celui-ci est encore en vie.
                    if player.life > 0:
                        print_line("Votre vie est de " +
                                   str(player.life) + "\n")
            # Si la vie du joueur ou du monstre devient négative, imprimer le vainqueur
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