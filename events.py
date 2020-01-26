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

    events = [Event(["HP"], 0, 0, 0, 0, 5, "diggy.wav","\nYou hear DnD players singing '" + colors.INFO + "Diggy, diggy hole" + colors.RESET + "'. \n\nYou approach slowly and join their party. \n\nThey share snacks with you. You " + colors.PLAYER  + "regain 5 HP!" + colors.RESET),
            Event(["HP"], 0, 0, 0, 0, -2, "shout.wav", "\n" + colors.ACTION + "You fall asleep on the table." + colors.RESET + " A manager notices it and yells at you. You " + colors.ACTION + "loose 2 HP" + colors.RESET)]


