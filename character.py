class Character:
    
    def __init__(self, name):
        self.max_hp = 10
        self.current_hp = 10
        self.level = 1
        self.character_class = "Bug Slayer"
        self.race = "Android"
        self.inventory = {'Sword': 1, 'Armor': 1}
        self.current_experience = 0
        self.name = name
        self.attack = 1
        self.armor = 0
        self.speed = 7
        self.dodge_chance = 1


# Keanu initialize:
Keanu = Character("Keanu")
