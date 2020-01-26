class PowerUps():
    def __init__(self, powerups_properties=None):
        if powerups_properties is None:
            powerups_properties = ["weapon", "torso", 0]
        self.name = powerups_properties[0]
        self.stat = powerups_properties[1]
        self.powerup = powerups_properties[2]
        self.status = powerups_properties[3]

class PowerUpsPool():

# powerups_properties = [name, stat, add, status]
    powerups = [PowerUps(["Health potion", "current_hp", 5, "Phial with red liquid (Hp + 5)"]),
            PowerUps(["Mana potion", "current_mana", 5, "Phial with blue liquid (Mana + 5)"])]

    powerups_names = [powerup.name for powerup in powerups]