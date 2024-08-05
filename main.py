import randomizer
from data.itemTables import itemAttributes

item_types = ', '.join(itemAttributes['itemType'][:-1]) + ' or ' + itemAttributes['itemType'][-1]
print("What random item would you like to generate?")
print("You can choose from " + item_types + ", or type 'random' for a random item.")
user_input = input(": ")

print(randomizer.generator(user_input))
