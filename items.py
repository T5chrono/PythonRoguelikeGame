class CommonItem():
    def __init__(self, common_item_properties=None):
        self.name = common_item_properties[0]
        self.status = common_item_properties[1]


class CommonItemsPool():


# common_item_properties = [name, stat, add, status]
    common_items = [CommonItem(["Pass card", "A card with an ugly picture"]),
                CommonItem(["Wallet", "Money makes the world go round"]),
                CommonItem(["Computer mouse", "It is just beautiful"]),
                CommonItem(["Cup", "A cup with cold tea"]),
                CommonItem(["Rope", "You could hang yourself with this."])]

    common_items_names = [common_item.name for common_item in common_items]