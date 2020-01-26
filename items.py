class CommonItem():
    def __init__(self, common_item_properties=None):
        self.name = common_item_properties[0]
        self.status = common_item_properties[1]


class CommonItemsPool():


# common_item_properties = [name, stat, add, status]
    common_items = [CommonItem(["Key", "Old rusty key."]),
                CommonItem(["Gold", "Money makes the world go round"]),
                CommonItem(["Leaf", "It is just beautiful"]),
                CommonItem(["Stone", "Nice geology"]),
                CommonItem(["Rope", "I could hang myself with this."])]

    common_items_names = [common_item.name for common_item in common_items]