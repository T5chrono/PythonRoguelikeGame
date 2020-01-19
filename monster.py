

class Monster():

    def __init__(self, monster_properties = ["monster", 1, 10, 0, 1, 1, 5]):
        self.name = monster_properties[0]
        self.difficulty = monster_properties[1]
        self.current_hp = monster_properties[2]
        self.armor = monster_properties[3]
        self.attack = monster_properties[4]
        self.defeat_exp = monster_properties[5]
        self.speed = monster_properties[6]

    def attack(self):
        return self.attack

    def defence(self, damage):
        if damage > self.armor:
            self.current_hp += self.armor - damage



class MonsterPool():

    ### monster_properties = [name, difficulty, current_hp, armor, attack, defeat_exp, speed]

    monsters = [Monster(["Sleepy Corporate Rat", 1, 5, 0, 1, 1, 5]),
                Monster(["Hungry Cat", 1, 4, 1, 1, 2, 7]),
                Monster("Mildewed Coffee Mug", 1, 2, 1, 1, 1, 4])]



