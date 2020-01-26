class Weapon():
    def __init__(self, weapon_properties=None):
        if weapon_properties is None:
            weapon_properties = ["weapon", 0, 0]
        self.name = weapon_properties[0]
        self.attack = weapon_properties[1]
        self.critical_chance = weapon_properties[2]
        self.status = weapon_properties[3]

class WeaponsPool():

# weapon_properties = [name, attack, critical_chance, status]
    weapons = [Weapon(["Fists", 1, 0, "Your own fists"]),
           Weapon(["Fork", 2, 0, "Shiny fork"]),
           Weapon(["Broom", 3, 1, "Sturdy piece of wood for punishing"]),
           Weapon(["Scissors", 3, 2, "You could chop monster in half with this"]),
           Weapon(["Boss badge", 4, 1, "Smashing machine"])]

    weapon_names = [weapon.name for weapon in weapons]