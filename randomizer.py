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

elif itemType == "gold":
    print("You found " + str(randomnumber(1, 250)) + " gold!")
else:
    print(itemType)