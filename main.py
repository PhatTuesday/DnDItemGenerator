from itemTables import itemAttributes
from randomizer import randomnumber

# I want to return a random item type

# I defined the function
def returnItem():
    return itemAttributes.itemType[randomnumber(0, 7)];
    # return itemAttributes.itemType[randomnumber(0, 7)];


# I called the function... In a print statement
# print(returnItem())



# Print the item type of and the weapon type of the item
# print(itemAttributes.itemType[randomnumber(0, 7)] + " of " + itemAttributes.weapon[0]);

print(itemAttributes["weapon"])