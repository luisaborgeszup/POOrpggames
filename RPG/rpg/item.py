class Item():

    def __init__(self, item_name):
        """Initialises the room with a name and the item's description with
        a non existing value."""
        self.name_item= item_name
        self.desc_item = None

    def set_desc_item(self, item_desc):
        """Sets a description for the item."""
        self.desc_item = item_desc

    def get_desc_item(self):
        """Returns the description of the room."""
        return self.desc_item

    def set_name_item(self, item_name):
        """Sets a name for the item."""
        self.name_item = item_name

    def get_name_item(self):
        """Returns the name of the item."""
        return self.name_item

    def describe_item(self):
        """Describes the item only if it exists."""
        if self.name_item is not None:
            print("\nLook! It seems there is " + self.desc_item + "!")

        else:
            print("")

    def item_stolen(self):
        """Returns the name of the stolen item of the current room."""
        return self.name_item

