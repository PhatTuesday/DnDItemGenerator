import random
from data.itemTables import itemAttributes


def randomnumber(min, max):
    return random.randint(min, max)


def get_item_type(user_input):
    item_types = ['weapon', 'armor', 'potion', 'scroll', 'ring', 'necklace', 'wand', 'component', 'gold']
    if user_input in item_types:
        return user_input
    elif user_input == "random":
        return itemAttributes['itemType'][randomnumber(0, 8)]
    else:
        return "I'm sorry, I didn't understand that."


def get_weapon():
    return itemAttributes['weapon'][randomnumber(0, 22)]


def get_armor():
    return itemAttributes['armor'][randomnumber(0, 7)]


def generator(user_input):
    itemType = get_item_type(user_input)
    weaponType = get_weapon()
    armorType = get_armor()
    answer = "..."

    if itemType == "weapon":
        answer = "You got a " + weaponType + "!"

    elif itemType == "armor":
        answer = "You got a " + armorType + "!"

    elif itemType == "potion":
        answer = "You got a " + itemAttributes['potion'][randomnumber(0, 25)] + " potion!"

    elif itemType == "scroll":
        answer = "You got a scroll of " + itemAttributes['scroll'][randomnumber(0, 20)]

    elif itemType == "ring":
        answer = "You got a ring of " + itemAttributes['ring'][randomnumber(0, 11)]

    elif itemType == "necklace":
        answer = "You got a " + itemAttributes['necklace'][randomnumber(0, 11)] + " necklace!"

    elif itemType == "wand":
        answer = "You got a wand of " + itemAttributes['wand'][randomnumber(0, 13)]

    elif itemType == "component":
        answer = "You got a " + itemAttributes['component'][randomnumber(0, 15)] + " component!"

    elif itemType == "gold":
        answer = "You found " + str(randomnumber(1, 250)) + " gold!"
    else:
        answer = itemType

    return answer
