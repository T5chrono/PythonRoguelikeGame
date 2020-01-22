class Weapon:
    def __init__(self, weapon_properties=None):
        if weapon_properties is None:
            weapon_properties = ["weapon", 0, 0]
        self.name = weapon_properties[0]
        self.attack = weapon_properties[1]
        self.critical_chance = weapon_properties[2]


# weapon_properties = [name, attack, critical_chance]
weapons = [Weapon(["Fists", 1, 0]),
           Weapon(["Dagger", 2, 0]),
           Weapon(["Simple sword", 3, 1]),
           Weapon(["Axe", 3, 2]),
           Weapon(["Hammer", 4, 1])]

weapon_names = [weapon.name for weapon in weapons]


class Armor:
    def __init__(self, armor_properties=None):
        if armor_properties is None:
            armor_properties = ["weapon", "torso", 0]
        self.name = armor_properties[0]
        self.body_part = armor_properties[1]
        self.armor = armor_properties[2]


# armor_properties = [name, body_part, armor]
armors = [Armor(["Cap", "head", 0]),
          Armor(["Shirt", "torso", 0]),
          Armor(["Gloves", "arms", 0]),
          Armor(["Shoes", "legs", 0]),
          Armor(["Buckler", "shield", 1]),
          Armor(["Helmet", "head", 1]),
          Armor(["Gloves", "arms", 1]),
          Armor(["Greaves", "legs", 1]),
          Armor(["Breastplate", "torso", 1]),
          Armor(["Shield", "shield", 2])]

armor_names = [armor.name for armor in armors]


class PowerUps:
    def __init__(self, powerups_properties=None):
        if powerups_properties is None:
            powerups_properties = ["weapon", "torso", 0]
        self.name = powerups_properties[0]
        self.stat = powerups_properties[1]
        self.powerup = powerups_properties[2]


# powerups_properties = [name, stat, add]
powerups = [PowerUps(["Health potion", "current_hp", 5]),
            PowerUps(["Mana potion", "current_mana", 5])]

powerups_names = [powerup.name for powerup in powerups]


def main():
    potion = powerups[1]
    print(type(potion))
    type(potion)


if __name__ == "__main__":
    main()
