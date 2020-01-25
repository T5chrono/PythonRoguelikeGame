from random import choice
import colors


class Event():

    def __init__(self, type, dex, strt, exp, intl, hp, desc):
        self.type = type
        self.dexterity = dex
        self.strenght = strt
        self.exp = exp
        self.intelligence = intl
        self.hp = hp
        self.description = desc

    def get_random_event():
        event = choice(EventPool.events)
        return event


class EventPool():

    events = [Event(["HP"], 0, 0, 0, 0, 5, "\nYou hear DnD players singing '" + colors.INFO + "Diggy, diggy hole" + colors.RESET + "'. \n\nYou approach slowly and join their party. \n\nThey share snacks with you. You " + colors.PLAYER  + "regain 5 HP!" + colors.RESET)]
