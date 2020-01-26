ALL_POSSIBLE_RACES = {
    # name : statistics
    "Corpo Rat": [2, 2, 2, 10, 10, 10, 10, "Your favorite color is grey."],
    "Mr Sandwich": [4, 1, 1, 15, 15, 5, 5, "Your favorite activity is 'eating'."],
    "Raising Star": [1, 4, 1, 5, 5, 15, 15, "Everyone around should know that you are awesome! At least that's what you think..."],
    "Android": [1, 1, 4, 5, 5, 15, 15, "Your favorite food is Apple."],
    "fsociety": [2, 2, 2, 15, 15, 5, 5, "You don't care what they think about you."]
}

ALL_POSSIBLE_CLASSES = {
    # name : statistics
    "Baby Boss": [2, 2, 2, 10, 10, 10, 10, "You shout to everyone 'Gimmie that report NOW!'"],
    "Sport Committee": [4, 1, 1, 15, 15, 5, 5, "You like to play it HARD!"],
    "Mr Robot": [1, 4, 1, 5, 5, 15, 15, "Your favorite song is 'Work, work, work, work, work'..."],
    "Geek": [1, 1, 4, 5, 5, 15, 15, "You love eating Apples!"],
    "Corpo Dinosaur": [2, 2, 2, 15, 15, 5, 5, "Eveyone knows you. You know everyone. Probably you were there before company started..."]
}


class CharacterRace():

    def __init__(self, race_name, race_properties):

        basic_race = 'Corpo Rat'
        if race_properties == "":
            race_properties = [basic_race] + ALL_POSSIBLE_RACES[basic_race]
        else:
            race_properties = [race_name] + ALL_POSSIBLE_RACES[race_name]

        self.name = race_properties[0]
        self.strength = race_properties[1]
        self.dexterity = race_properties[2]
        self.intelligence = race_properties[3]
        self.max_hp = race_properties[4]
        self.current_hp = race_properties[5]
        self.max_mana = race_properties[6]
        self.current_mana = race_properties[7]
        self.description = race_properties[8]


class CharacterClass():

    def __init__(self, class_name, class_properties):

        basic_class = 'Mr Robot'
        if class_properties == "":
            class_properties = [basic_class] + ALL_POSSIBLE_CLASSES[basic_class]
        else:
            class_properties = [class_name] + ALL_POSSIBLE_CLASSES[class_name]

        self.name = class_properties[0]
        self.strength = class_properties[1]
        self.dexterity = class_properties[2]
        self.intelligence = class_properties[3]
        self.max_hp = class_properties[4]
        self.current_hp = class_properties[5]
        self.max_mana = class_properties[6]
        self.current_mana = class_properties[7]
        self.description = class_properties[8]
