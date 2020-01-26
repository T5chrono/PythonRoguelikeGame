import battle
import ui


class Boss:
    def __init__(self):
        self.name = "Managers and directors and CEO"
        self.difficulty = 5
        self.current_hp = 10
        self.armor = 5
        self.attack = 10
        self.defeat_exp = 100
        self.speed = 10
        self.dodge_chance = 10


def boss_fight():
    ui.print_message(question1)
    user_input = user_answer()
    if user_input == '1':
        you_are_fired()
    elif user_input == '2':
        ui.print_message(question2)
        user_input = user_answer()
        if user_input == '1':
            you_are_fired()
        elif user_input == '2':
            ui.print_message(question3)
            user_input = user_answer()
            if user_input == '1':
                you_are_fired()
            elif user_input == '2':
                you_get_a_promotion()
            elif user_input == '3':
                fight_with_boss()
            else:
                remind_player_to_say_something()
        elif user_input == '3':
            fight_with_boss()
        else:
            remind_player_to_say_something()
    elif user_input == '3':
        fight_with_boss()
    else:
        remind_player_to_say_something()


def user_answer():
    return input("What is your answer?: ")


def remind_player_to_say_something():
    ui.print_message("You have to answer somehow ('1', '2' or '3'")


def you_are_fired():
    ui.print_message("You are fired!!! ")
    # TODO: negative end game screen


def you_get_a_promotion():
    ui.print_message("Well I guess it is ok.")
    # TODO positive end game screen


def fight_with_boss():
    pass  # TODO battle fight


question1 = "Aaa, it's you! Where is my report.\n 1. My dog ate it.\n 2. I will bring it tomorrow.\n 3. I don't care " \
            "about your report let's fight.\n "
question2 = "I need it now!\n 1. Time is just a construct.\n 2. Maybe I can offer you something else?\n 3. I don't " \
            "care about your report let's fight.\n "
question3 = "What do you have in mind?\n 1. Let's just forget about it? \n 2. Maybe you want a cake?\n 3. I don't " \
            "care about your report let's fight.\n "
