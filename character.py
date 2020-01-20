import weapons_armor_items

class Character:

    def __init__(self, name):
        # FLUFF
        self.name = name
        self.character_class = "Bug Slayer"
        self.race = "Android"
        self.inventory = {'Sword': 1, 'Body Armor': 1}
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
        self.weapon = weapons_armor_items.weapons[1]
        self.attack = self.strength + self.weapon.attack
        # DEFENCE
        self.head = 0
        self.torso = 0
        self.arms = 0
        self.legs = 0
        self.shield = 0
        self.armor = self.head + self.torso + self.arms + self.legs + self.shield
        # ADVANCED STATS
        self.speed = self.dexterity * 7
        self.dodge_chance = int(self.dexterity - self.armor // 2)

    def __repr__(self):
        return f'Name: {self.name} ({self.race} the {self.character_class}) \n' \
               f'EXP: {self.current_experience} -> Level {self.level} \n' \
               f'HP: {self.current_hp} / {self.max_hp} \n' \
               f'MANA: {self.current_mana} / {self.max_mana} \n' \
               f'Strength: {self.strength} \n' \
               f'Dexterity: {self.dexterity} \n' \
               f'Inteligence: {self.intelligence} \n' \
               f'Attack: {self.attack} with {self.weapon.name}: {self.weapon.attack} \n' \
               f'Defense: {self.armor} \n' \
               f'Total Attack: {self.attack} \n' \
               f'Total Defense: {self.armor} \n' \
               f'Speed: {self.speed}'


def main():
    Keanu = Character("Keanu")
    print(Keanu)


if __name__ == "__main__":
    main()
