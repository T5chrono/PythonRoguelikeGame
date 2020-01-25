from weapons_armor_items import weapons, armors, powerups
import util


class Character:

    def __init__(self, name):
        # FLUFF
        self.name = name
        self.character_class = "Bug Slayer"
        self.race = "Android"
        self.inventory = {}
        # LEVELING UP
        self.level = 1
        self.points = 0
        self.current_experience = 0
        self.next_lvl_experience = 15
        # BASIC STATS
        self.strength = 1
        self.dexterity = 1
        self.intelligence = 1
        # HP AND MANA
        self.max_hp = 10
        self.current_hp = 10
        self.max_mana = 10
        self.current_mana = 10
        # ATTACK
        self.weapon = weapons[1]
        self.attack = self.strength + self.weapon.attack
        # DEFENCE
        self.head = armors[0]
        self.torso = armors[1]
        self.arms = armors[2]
        self.legs = armors[3]
        self.shield = armors[4]
        self.armor = self.head.armor + self.torso.armor + self.arms.armor + self.legs.armor + self.shield.armor
        # ADVANCED STATS
        self.speed = self.dexterity * 7
        self.dodge_chance = int(self.dexterity - self.armor // 2)

    def __repr__(self):
        return f'Name: {self.name} ({self.race} the {self.character_class}) \n' \
               f'EXP: {self.current_experience} -> Level {self.level} \n' \
               f'HP: {self.current_hp} / {self.max_hp} \n' \
               f'MANA: {self.current_mana} / {self.max_mana} \n\n' \
               f'Strength: {self.strength} \n' \
               f'Dexterity: {self.dexterity} \n' \
               f'Inteligence: {self.intelligence} \n\n' \
               f'Attack: {self.attack} with {self.weapon.name}: {self.weapon.attack} \n' \
               f'Defense: {self.armor} \n' \
               f'   Head: {self.head.armor} ({self.head.name}) \n' \
               f'   Torso: {self.torso.armor} ({self.torso.name}) \n' \
               f'   Arms: {self.arms.armor} ({self.arms.name}) \n' \
               f'   Legs: {self.legs.armor} ({self.legs.name}) \n' \
               f'   Shield: {self.shield.armor} ({self.shield.name}) \n' \


    def check_if_lvl_up(self):
        multiplier_for_exp = 1.5
        mutliplier_for_points = 2
        if self.current_experience >= self.next_lvl_experience:
            self.level += 1
            print("Congratulations! You levelled up!")
            self.next_lvl_experience += (self.current_experience)*multiplier_for_exp
            self.points += (self.level * mutliplier_for_points)
            self.current_hp = self.max_hp
        
    def distribute_points(self):
        print("You have {} points to distribute\nYour strengh is {} next point costs {}\nYour dexterity is {} next point costs {}\nYour intelligence is {} next point costs {}\n Your max HP is {} next point costs {}".format(self.points, self.strength, self.strength*2, self.dexterity, self.dexterity*2, self.intelligence, self.intelligence*2, self.max_hp, (self.max_hp-9)*2))
        print("Push q to quit, push s, d, i, h to upgrade strenght, dexterity, intelligence or HP. Push p to show your points")
        is_distributing = True
        while is_distributing:
            player_choice = util.key_pressed()
            if player_choice == "s":
                if self.points >= self.strength*2:
                    self.points -= self.strength*2
                    self.strength += 1
                    print("You upgraded strenght")
                else:
                    print("You don't have enough points to upgrade!")
            elif player_choice == "d":
                if self.points >= self.dexterity*2:
                    self.points -= self.dexterity*2
                    self.dexterity += 1
                    print("You upgraded dexterity")
                else:
                    print("You don't have enough points to upgrade!")
            elif player_choice == "i":
                if self.points >= self.intelligence*2:
                    self.points -= self.intelligence*2
                    self.intelligence += 1
                    print("You upgraded intelligence")
                else:
                    print("You don't have enough points to upgrade!")
            elif player_choice == "h":
                if self.points >= (self.max_hp-9)*2:
                    self.points -= (self.max_hp-9)*2
                    self.max_hp += 1
                    self.current_hp += 1
                    print("You upgraded HP")
                else:
                    print("You don't have enough points to upgrade!")
            elif player_choice == "p":
                print("You have {} points left".format(self.points))
            elif player_choice == "q":
                is_distributing = False
            else:
                print("Incorrect key")

    def update_player(self):
        self.update_attack()
        self.update_armor()
        self.update_dodge()

    def update_attack(self):
        self.attack = self.strength + self.weapon.attack

    def update_armor(self):
        self.armor = self.head.armor + self.torso.armor + self.arms.armor + self.legs.armor + self.shield.armor

    def update_dodge(self):
        self.dodge_chance = int(self.dexterity - self.armor // 2)

    def heal_hp(self):
        new_hp = self.current_hp + powerups[0].powerup
        if new_hp <= 10:
            self.current_hp = new_hp
        else:
            self.current_hp = 10

    def heal_mana(self):
        new_mana = self.current_mana + powerups[1].powerup
        if new_mana <= 10:
            self.current_mana = new_mana
        else:
            self.current_mana = 10
