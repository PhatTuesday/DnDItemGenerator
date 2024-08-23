import random
from data.itemTables import itemAttributes
from data.skillTables import stats, skills, buffs


def randomnumber(min, max):
    return random.randint(min, max)


def get_item_type(user_input):
    if user_input in itemAttributes['itemType']:
        return generator(user_input)
    elif user_input == "random":
        fux_user_input = itemAttributes['itemType'][randomnumber(0, 8)]
        return generator(fux_user_input)
    else:
        return "Invalid input. Please try again."


def get_weapon():
    weapon = itemAttributes['weapon'][randomnumber(0, 22)]
    additions = stats[randomnumber(0, 5)] + " + " + str(randomnumber(1, 5))
    return weapon + " with " + additions


def get_armor():
    armor = itemAttributes['armor'][randomnumber(0, 7)]
    additions = skills[randomnumber(0, 5)] + " + " + str(randomnumber(1, 5))
    return armor + " with " + additions


def get_potion():
    potion = itemAttributes['potion'][randomnumber(0, 3)]
    additions = buffs[randomnumber(0, 9)]
    return potion + " potion of " + additions


def generator(user_input):
    item_type: str = user_input
    weapon_type: str = get_weapon()
    armor_type: str = get_armor()
    potion_type: str = get_potion()

    if item_type == "weapon":
        return "You got a " + weapon_type + "!"
    elif item_type == "armor":
        return "You got a " + armor_type + "!"
    elif item_type == "potion":
        return "You got a " + potion_type + "!"
    elif item_type == "scroll":
        return "You got a scroll of " + itemAttributes['scroll'][randomnumber(0, 20)]
    elif item_type == "ring":
        return "You got a ring of " + itemAttributes['ring'][randomnumber(0, 11)]
    elif item_type == "necklace":
        return "You got a " + itemAttributes['necklace'][randomnumber(0, 11)] + " necklace!"
    elif item_type == "wand":
        return "You got a wand of " + itemAttributes['wand'][randomnumber(0, 13)]
    elif item_type == "component":
        return "You got a " + itemAttributes['component'][randomnumber(0, 15)] + " component!"
    elif item_type == "gold":
        return "You found " + str(randomnumber(1, 250)) + " gold!"
    else:
        return "Invalid input. Please try again."
