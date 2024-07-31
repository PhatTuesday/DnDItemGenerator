import random
from itemTables import itemAttributes

def randomnumber(min, max):
    return random.randint(min, max)

# define a variable here that I can record the item type I got at random

# Getting the peices we need here
def get_item_type():
    return itemAttributes['itemType'][randomnumber(0, 8)]


def get_weapon():
    return itemAttributes['weapon'][randomnumber(0, 22)]

def get_armor():
    return itemAttributes['armor'][randomnumber(0, 7)]

itemType = get_item_type()
weaponType = get_weapon()
armorType = get_armor()

if itemType == "weapon":
    print("You got a " + weaponType + "!")

elif itemType == "armor":
    print("You got a " + armorType + "!")

elif itemType == "potion":
    print("You got a " + itemAttributes['potion'][randomnumber(0, 25)] + " potion!")

elif itemType == "scroll":
    print("You got a scroll of " + itemAttributes['scroll'][randomnumber(0, 20)])

elif itemType == "ring":
    print("You got a ring of " + itemAttributes['ring'][randomnumber(0, 11)])

elif itemType == "necklace":
    print("You got a " + itemAttributes['necklace'][randomnumber(0, 11)] + " necklace!")

elif itemType == "wand":
    print("You got a wand of " + itemAttributes['wand'][randomnumber(0, 13)])

elif itemType == "component":
    print("You got a " + itemAttributes['component'][randomnumber(0, 15)] + " component!")

elif itemType == "gold":
    print("You found " + str(randomnumber(1, 250)) + " gold!")
else:
    print(itemType)