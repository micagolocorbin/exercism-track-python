"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    amount = dict()

    for item in items:
        num = items.count(item)
        amount[item] = num

    return amount


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    items_amount = create_inventory(items)

    for item in items_amount:
        if inventory.get(item):
            inventory[item] += items_amount[item]
        else:
            inventory[item] = items_amount[item]

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    items_amount = create_inventory(items)

    for item in inventory:
        if items_amount.get(item) and items_amount.get(item) <= inventory.get(item):
            inventory[item] -= items_amount[item]
        elif items_amount.get(item) is None:
            continue
        else:
            inventory[item] = 0

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item
    does not match.
    """

    inventory.pop(item, "not found")
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in
    inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    listing = []

    for key, value in inventory.items():
        if value != 0:
            listing.append((key, value))

    return listing
