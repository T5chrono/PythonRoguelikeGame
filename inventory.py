import random

import character
from weapons_armor_items import weapon_names, armor_names, powerups_names


ITEMS = ['Gold', 'Key', 'Stone', 'Rope', "Leaf"] + weapon_names + armor_names + powerups_names


def random_item(lst):
    """Returns random item from the list -> ITEMS"""
    return [random.choice(lst)]


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory.keys():
            inventory.update({item: inventory[item] + 1})
        else:
            inventory.update({item: 1})
    return inventory


def print_table(inventory, order='empty'):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    column_widths = calculate_column_widths(inventory)
    inventory = sort_dictionary(inventory, order)

    print_line(column_widths)
    print('item name'.rjust(column_widths[0]) + ' | ' + 'count'.rjust(column_widths[1]))
    print_line(column_widths)
    for item in inventory:
        print(item.rjust(column_widths[0]) + ' | ' + str(inventory[item]).rjust(column_widths[1]))
    print_line(column_widths)


# ----- Helper functions for print_table START-----
def calculate_column_widths(inventory):
    """ Calculates the perfect widths of columns for printing purposes. """
    inventory.update({'item name': 'count'})
    key_lengths = [len(key) for key in inventory.keys()]
    value_lengths = [len(str(value)) for value in inventory.values()]
    column_widths = [max(key_lengths), max(value_lengths)]
    del inventory['item name']
    return column_widths


def sort_dictionary(inventory, order):
    """ Sorts the dictionary in a given order. """
    if order == 'count,asc':
        inventory = {k: v for k, v in sorted(inventory.items(), key=lambda inv_item: inv_item[1])}
    elif order == 'count,desc':
        inventory = {k: v for k, v in sorted(inventory.items(), key=lambda inv_item: inv_item[1], reverse=True)}
    return inventory


def print_line(column_widths):
    """ Prints straight line which length corresponds to column widths. """
    print("-" * (sum(column_widths) + len(column_widths) + 1))
# ----- Helper functions for print_table END -----


def main():
    Keanu = character.Character("Keanu")
    print(Keanu.inventory)
    print_table(Keanu.inventory)


if __name__ == "__main__":
    main()
