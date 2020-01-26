import random
import ui
import weapons
import armors
import items
import powerups


class Inventory():
    ITEMS_NAMES = items.CommonItemsPool.common_items_names + weapons.WeaponsPool.weapon_names + powerups.PowerUpsPool.powerups_names + armors.ArmorsPool.armor_names

    def __init__(self):
        self.items = {}
        self.equipped_items = {}

    def get_random_item(self):
        return random.choice(Inventory.ITEMS_NAMES)


    def add_to_inventory(self):
        item = self.get_random_item()
        ui.display_added_item(item)

        if item in self.items.keys():
            self.items.update({item: self.items[item] + 1})
        else:
            self.items.update({item: 1})
  
    def remove_from_inventory(self, removed_item):
        if removed_item in self.items.keys():
            self.items.update({removed_item: self.items[removed_item] - 1})
            if self.items[removed_item] <= 0:
                del self.items[removed_item]
                    

    def print_table(self):
        column_widths = self.calculate_column_widths()
        blank_line = ""
        ui.UI.print_message(blank_line)
        self.print_line(column_widths)
        ui.UI.print_message('item name'.rjust(column_widths[0]) + ' | ' + 'count'.rjust(column_widths[1]))
        self.print_line(column_widths)
        for item in self.items:
            ui.UI.print_message(item.rjust(column_widths[0]) + ' | ' + str(self.items[item]).rjust(column_widths[1]))
        self.print_line(column_widths)

    def calculate_column_widths(self):
        self.items.update({'item name': 'count'})
        key_lengths = [len(key) for key in self.items.keys()]
        value_lengths = [len(str(value)) for value in self.items.values()]
        column_widths = [max(key_lengths), max(value_lengths)]
        del self.items['item name']
        return column_widths

    def print_line(self, column_widths):
        ui.UI.print_message("-" * (sum(column_widths) + len(column_widths) + 1))
