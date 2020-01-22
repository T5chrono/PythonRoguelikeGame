from weapons_armor_items import weapons, weapon_names, armors, armor_names

class Character:

    def __init__(self, name):
        # FLUFF
        self.name = name
        self.character_class = "Bug Slayer"
        self.race = "Android"
        self.inventory = {}
        # LEVELING UP
        self.level = 1
        self.current_experience = 0
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


def main():
    Keanu = Character("Keanu")
    print(Keanu)


if __name__ == "__main__":
    main()
