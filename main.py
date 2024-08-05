import randomizer
from itemTables import itemAttributes
from randomizer import randomnumber


# Returns random ItemType
def return_item():
    return itemAttributes['itemType'][randomnumber(0, 7)]


# print(return_item())

print(randomizer.answer)