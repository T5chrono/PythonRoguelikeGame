class Armor():
    def __init__(self, armor_properties=None):
        if armor_properties is None:
            armor_properties = ["weapon", "torso", 0]
        self.name = armor_properties[0]
        self.body_part = armor_properties[1]
        self.armor = armor_properties[2]
        self.status = armor_properties[3]

class ArmorsPool():

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