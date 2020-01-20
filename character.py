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

    def __repr__(self):
        return f'Name: {self.name} ({self.race} the {self.character_class}) \n' \
               f'HP: {self.current_hp} / {self.max_hp} \n' \
               f'EXP: {self.current_experience} -> Level {self.level} \n' \
               f'Attack: {self.attack} \n' \
               f'Defense: {self.armor} \n' \
               f'Speed: {self.speed}'


def main():
    Keanu = Character("Keanu")
    print(Keanu)


if __name__ == "__main__":
    main()
