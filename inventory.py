import character


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory.keys():
            inventory.update({item: inventory[item] + 1})
        else:
            inventory.update({item: 1})
    return inventory


def main():
    print(character.Keanu.inventory)


if __name__ == "__main__":
    main()
