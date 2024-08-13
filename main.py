import randomizer
from data.itemTables import itemAttributes

item_types = ', '.join(itemAttributes['itemType'][:-1]) + ' or ' + itemAttributes['itemType'][-1]

while True:
    print("")
    print("What random item would you like to generate?")
    print("You can choose from " + item_types + ", or type 'random' for a random item.")
    print("Type 'exit' to quit.")
    user_input = input(": ")

    if user_input.lower() == "exit":
        print("Thank you!")
        break

    print(randomizer.generator(user_input))
