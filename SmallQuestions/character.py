from tabulate import tabulate


class Character:

    def __init__(self, inventory):
        """
        Creates a new instance of
        a character, and sets up
        their inventory
        """

        assert isinstance(inventory, list)
        self.inventory = inventory

    def display_inventory(self):
        """
        Displays the inventory with tabulate.
        """

        # First, convert the inventory list to a dictionary
        inventory = self.convert_inventory(self.inventory)

        # Now we can display the inventory!
        print(tabulate(inventory, headers="keys"))
        print("\n")

    def convert_inventory(self, inv):
        d = {}
        for i in inv:
            temp = i.split(":")
            if temp[1] in d.keys():
                d[temp[1]].append(temp[0])
            else:
                d[temp[1]] = [temp[0]]
        return d



inventory = [
    "lemon-flavored lemons:food",
    "apple-flavored lemons:food",
    "bbqdude's chicken:food",
    "bisk's magic stew:food",
    "metaclasses:magic",
    "recursion:magic",
    "abstract base classes:magic",
    "pantsuit:armor",
    "pony ears:armor",
    "joseph's ushanka:armor",
    "4.1513:bitcoins",
]

lucy = Character(inventory)
lucy.display_inventory()
