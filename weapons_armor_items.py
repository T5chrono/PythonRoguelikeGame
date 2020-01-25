class Weapon:
    def __init__(self, weapon_properties=None):
        if weapon_properties is None:
            weapon_properties = ["weapon", 0, 0]
        self.name = weapon_properties[0]
        self.attack = weapon_properties[1]
        self.critical_chance = weapon_properties[2]
        self.status = weapon_properties[3]


# weapon_properties = [name, attack, critical_chance, status]
weapons = [Weapon(["Fists", 1, 0, "Your own fists"]),
           Weapon(["Dagger", 2, 0, "Shiny dagger with"]),
           Weapon(["Simple sword", 3, 1, "Sturdy piece of iron for monster slaying"]),
           Weapon(["Axe", 3, 2, "You could chop monster in half with this"]),
           Weapon(["Hammer", 4, 1, "Smashing machine"])]

weapon_names = [weapon.name for weapon in weapons]


class Armor:
    def __init__(self, armor_properties=None):
        if armor_properties is None:
            armor_properties = ["weapon", "torso", 0]
        self.name = armor_properties[0]
        self.body_part = armor_properties[1]
        self.armor = armor_properties[2]
        self.status = armor_properties[3]


# armor_properties = [name, body_part, armor, status]
armors = [Armor(["Cap", "head", 0, "Nice hat"]),
          Armor(["Shirt", "torso", 0, "Fancy colored shirt"]),
          Armor(["Gloves", "arms", 0, "My hands will be warm"]),
          Armor(["Shoes", "legs", 0, "No more LEGO blocks damage"]),
          Armor(["Buckler", "shield", 1, "Simple shield"]),
          Armor(["Helmet", "head", 1, "I hope my hair will stay ok after wearing this"]),
          Armor(["Better gloves", "arms", 1, "Super warm and protective"]),
          Armor(["Greaves", "legs", 1, "Shins are important, this will protect them"]),
          Armor(["Breastplate", "torso", 1, "Shiny peace of metal to protect my torso"]),
          Armor(["Shield", "shield", 2, "Superior defence"])]

armor_names = [armor.name for armor in armors]


class PowerUps:
    def __init__(self, powerups_properties=None):
        if powerups_properties is None:
            powerups_properties = ["weapon", "torso", 0]
        self.name = powerups_properties[0]
        self.stat = powerups_properties[1]
        self.powerup = powerups_properties[2]
        self.status = powerups_properties[3]


# powerups_properties = [name, stat, add, status]
powerups = [PowerUps(["Health potion", "current_hp", 5, "Phial with red liquid (Hp + 5)"]),
            PowerUps(["Mana potion", "current_mana", 5, "Phial with blue liquid (Mana + 5)"])]

powerups_names = [powerup.name for powerup in powerups]


class CommonItem:
    def __init__(self, common_item_properties=None):
        self.name = common_item_properties[0]
        self.status = common_item_properties[1]


# common_item_properties = [name, stat, add, status]
common_items = [CommonItem(["Key", "Old rusty key."]),
                CommonItem(["Gold", "Money makes the world go round"]),
                CommonItem(["Leaf", "It is just beautiful"]),
                CommonItem(["Stone", "Nice geology"]),
                CommonItem(["Rope", "I could hang myself with this."])]

common_items_names = [common_item.name for common_item in common_items]


def main():
    potion = powerups[1]
    print(type(potion))
    type(potion)


if __name__ == "__main__":
    main()
