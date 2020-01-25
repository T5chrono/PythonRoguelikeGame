from random import choice
import colors


class Event():

    def __init__(self, type, dex, strt, exp, intl, hp, sound_file, desc):
        self.type = type
        self.dexterity = dex
        self.strenght = strt
        self.exp = exp
        self.intelligence = intl
        self.hp = hp
        self.description = desc
        self.sound_file = sound_file

    def get_random_event():
        event = choice(EventPool.events)
        return event


class EventPool():

    # events = [Event(["HP"], 0, 0, 0, 0, 5, "\nYou hear DnD players singing '" + colors.INFO + "Diggy, diggy hole" + colors.RESET + "'. \n\nYou approach slowly and join their party. \n\nThey share snacks with you. You " + colors.PLAYER  + "regain 5 HP!" + colors.RESET)]
    events = [Event(["HP"], 0, 0, 0, 0, 5, "diggy.wav","You hear DnD players singing 'Diggy, diggy hole'. You approach slowly and join their party. They share snacks with you. You regain 5 HP"),
                Event(["HP"], 0, 0, 0, 0, -2, "shout.wav", "You fall asleep on the table. A manager notices it and yells at you. You loose 2 HP")]


