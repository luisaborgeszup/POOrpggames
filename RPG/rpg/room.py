class Room():

    def __init__(self, room_name):
        """Initialises the room with a name and a
        dictionary for the directions in which the rooms are linked.
        The description of the room, the character in it and the
        item also in it are initialised with non existing values."""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_character(self, new_character):
        """Sets a character in the room."""
        self.character = new_character

    def get_character(self):
        """Returns the character present in the room."""
        return self.character

    def set_description(self, room_description):
        """Sets a description for the room."""
        self.description = room_description

    def get_description(self):
        """Returns the description of the room."""
        return self.description

    def get_name(self):
        """Returns the name of the room."""
        return self.name

    def set_name(self, room_name):
        """Sets a name for the room."""
        self.name = room_name

    def set_item(self, item_name):
        """Sets a item in the room."""
        self.item = item_name

    def get_item(self):
        """Returns the item present in the room."""
        return self.item

    def item_was_taken(self):
        """Sets the item which was taken as a
        non existing value so it can be removed from the room."""
        self.item = None
        return None

    def describe(self):
        """Describes the room."""
        print(self.description)

    def link_to_room(self, room_to_link, direction):
        """Saves the direction, for which two rooms were linked, in the dictionary."""
        self.linked_rooms[direction] = room_to_link
        #print(self.name, "linked_rooms:", repr(self.linked_rooms))
        # ^ used to show how the dictionary gets built up

    def get_details(self):
        """Outputs the information of the room such as description and linked rooms to it."""
        if self.name is not None:
            print("The ", self.name)
            print('-----------------------------------------------------------------------')
            print(self.description, '\n')
            for direction in self.linked_rooms:
                rooms_around = self.linked_rooms[direction]
                print("The ", rooms_around.get_name(), " is ", direction)

            return not None

        else:
            return None

    def move(self, direction):
        """Allows the player to move towards rooms which exists."""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]

        else:
            print("There's nothing here asshole.")
            return self

