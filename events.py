from random import choice

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

    events = [Event(["HP"], 0, 0, 0, 0, 5, "You hear DnD players singing 'Diggy, diggy hole'. You approach slowly and join their party. They share snacks with you. You regain 5 HP")]
