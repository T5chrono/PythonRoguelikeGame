import monster
import random
import util


class Battle():

    def __init__(self, player_character):
        self.monster_initiative = 0
        self.character_initiative = 0
        self.player_character = player_character
        self.monster = self.get_random_monster()
        self.monster_hp = self.monster.current_hp

    def get_random_monster(self):
        random_monster = random.choice(monster.MonsterPool.monsters)
        if random_monster.difficulty <= self.player_character.level:
            return random_monster
        else:
            self.get_random_monster()

    def handle_fight_round(self):
        self.monster_initiative += self.monster.speed
        self.character_initiative += self.player_character.speed

        if self.monster_initiative > self.character_initiative:
            dodge_difficulty = random.randint(0, 100)

            if dodge_difficulty > self.player_character.dodge_chance:
                monster_damage = self.calculate_damage(self.monster.attack, self.player_character.armor)
                self.player_character.current_hp -= monster_damage
                print("{} inflicted {} damage. {} has {} HP left".format(
                    self.monster.name, monster_damage, self.player_character.name, self.player_character.current_hp
                    ))
            else:
                print("{} dodged the attack!".format(self.player_character.name))

            self.character_initiative += self.player_character.speed
            player_alive = self.check_if_player_alive()
            return player_alive

        elif self.monster_initiative <= self.character_initiative:
            print("Your turn! You want to run (r) ot attack (a)?")
            player_choice = ""

            while player_choice not in ["r", "a"]:
                player_choice = util.key_pressed()

                if player_choice == "r":
                    print("{} escaped safely from {}".format(self.player_character.name, self.monster.name))
                    return False

                else:
                    dodge_difficulty = random.randint(0, 100)
                    if dodge_difficulty > self.monster.dodge_chance:
                        player_damage = self.calculate_damage(self.player_character.attack, self.monster.armor)
                        self.monster_hp -= player_damage
                        print("{} inflicted {} damage. {} has {} HP left".format(
                            self.player_character.name, player_damage, self.monster.name, self.monster_hp
                            ))
                    else:
                        print("{} dodged the attack".format(self.monster.name))

                    self.monster_initiative += self.monster.speed
                    monster_alive = self.check_if_monster_alive()
                    return monster_alive

    def check_if_player_alive(self):
        if self.player_character.current_hp > 0:
            return True
        else:
            print("Your character died!")
            return False

    def check_if_monster_alive(self):
        if self.monster_hp > 0:
            return True
        else:
            print("Your character killed {} and gained {} EXP!".format(self.monster.name, self.monster.defeat_exp))
            self.player_character.current_experience += self.monster.defeat_exp
            return False

    def calculate_damage(self, attack, armor):
        min_modifier = -2
        max_modifier = 2
        random_modifier = random.randint(min_modifier, max_modifier)
        damage = attack - armor + random_modifier
        if damage < 0:
            damage = 0
        return damage

    def attack(attacker, defender):
        pass

    def run():
        pass


if __name__ == "__main__":
    print(monster.MonsterPool.monsters)
