import colors
import random
import util
import ui


class Boss:
    def __init__(self):
        self.name = "Managers and directors and CEO"
        self.difficulty = 5
        self.current_hp = 10
        self.armor = 5
        self.attack = 10
        self.defeat_exp = 100
        self.speed = 10
        self.dodge_chance = 10


def random_curse():
    curses = ["I always hated you",
              "You were lousy worker anyway!",
              "You were always late",
              "You are a scum",
              "You will not achieve anything"]
    return random.choice(curses)


class BossBattle:

    def __init__(self, player_character):
        self.boss_initiative = 0
        self.character_initiative = 0
        self.player_character = player_character
        self.boss = Boss()
        self.boss_hp = self.boss.current_hp

    def handle_fight_round(self):
        self.boss_initiative += self.boss.speed
        self.character_initiative += self.player_character.speed

        if self.boss_initiative > self.character_initiative:
            dodge_difficulty = random.randint(0, 100)

            if dodge_difficulty > self.player_character.dodge_chance:
                monster_damage = self.calculate_damage(self.boss.attack, self.player_character.armor)
                self.player_character.current_hp -= monster_damage
                ui.UI.print_message(random_curse())
                print("{} inflicted {} damage. {} has {} HP left".format(
                    self.boss.name, colors.ENEMY + str(monster_damage) + colors.RESET, self.player_character.name, colors.PLAYER + str(self.player_character.current_hp) + colors.RESET
                    ))
            else:
                print("{} dodged the attack!".format(colors.PLAYER + str(self.player_character.name) + colors.RESET))
            self.character_initiative += self.player_character.speed
            player_alive = self.check_if_player_alive()
            return player_alive

        elif self.boss_initiative <= self.character_initiative:
            print("Your turn! You want to run " + colors.ACTION + "(r)" + colors.RESET + " or attack " + colors.ACTION + "(a)" + colors.RESET + "?")
            player_choice = ""

            while player_choice not in ["r", "a"]:
                player_choice = util.key_pressed()

                if player_choice == "r":
                    print("{} escaped safely from {}".format(colors.PLAYER + str(self.player_character.name) + colors.RESET, self.boss.name))
                    return False

                else:
                    dodge_difficulty = random.randint(0, 100)
                    if dodge_difficulty > self.boss.dodge_chance:
                        player_damage = self.calculate_damage(self.player_character.attack, self.boss.armor)
                        self.boss_hp -= player_damage
                        print("{} inflicted {} damage. {} has {} HP left".format(
                            self.player_character.name, colors.PLAYER + str(player_damage) + colors.RESET, self.boss.name, colors.ENEMY + str(self.boss_hp) + colors.RESET
                            ))
                    else:
                        print("{} dodged the attack".format(colors.ENEMY + str(self.boss.name) + colors.RESET))

                    self.boss_initiative += self.boss.speed
                    monster_alive = self.check_if_monster_alive()
                    return monster_alive

    def check_if_player_alive(self):
        if self.player_character.current_hp > 0:
            return True
        else:
            print(colors.ENEMY + "Your character died!" + colors.RESET)
            return False

    def check_if_monster_alive(self):
        if self.boss_hp > 0:
            return True
        else:
            print("Your character killed {} and gained {} EXP!".format(colors.PLAYER + str(self.boss.name) + colors.RESET, colors.PLAYER + str(self.boss.defeat_exp) + colors.RESET))
            self.player_character.current_experience += self.boss.defeat_exp
            return False

    def calculate_damage(self, attack, armor):
        min_modifier = -2
        max_modifier = 2
        random_modifier = random.randint(min_modifier, max_modifier)
        damage = attack - armor + random_modifier
        if damage < 0:
            damage = 0
        return damage
