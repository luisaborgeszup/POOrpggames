class Character:

    # Create a character
    def __init__(self):
        """Initialises the character with a name, a description and
        initiates the conversation with a non existing value."""
        self.name = None
        self.description = None
        self.conversation = None
        self.evaluation = None

    def get_name(self):
        return self.name

    def set_name(self, char_name):
        self.name = char_name

    def get_description(self):
        return self.description

    def set_description(self, char_description):
        self.description = char_description

    def describe(self):
        """Describes the character only if the character is in the game itself."""
        if self.name is not None:
            print( self.name + " is here!" )
            print( self.description )
            return not None
        else:
            print("")
            return None

    def get_conversation(self):
        return self.conversation

    def set_conversation(self, conversation):
        """Defines a character's response to when it is spoken to."""
        self.conversation = conversation

    def talk(self):
        """Talks to the character only if he has a response."""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
            return not None
        else:
            print(self.name + " doesn't want to talk to you")
            return None


class Enemy(Character):

    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        super().__init__()
        self.name = char_name
        self.description = char_description
        self.weakness = None
        self.stolen_item = None
        self.evaluation = True

    def set_weakness(self, item_weakness):
        """Sets the weakness of the enemy."""
        self.weakness = item_weakness

    def get_weakness(self):
        """Returns the weakness of the enemy."""
        return self.weakness

    def set_stolen_item(self, item_enemy):
        """Sets the stolen item from the enemy."""
        self.stolen_item = item_enemy

    def get_stolen_item(self):
        """Returns the stolen item from the enemy."""
        return self.stolen_item

    def steal(self):
        """Attempt of steal an item from the enemy if he has one."""
        print("You tried to steal from " + self.name)

        if self.stolen_item == "nothing":
            print("What a pity!")
            print(self.name + " had nothing to be stolen! Good luck next "
                              "time!")
            return False

        else:
            print("Congrats! You've just conquered a item! Let's see\n"
                  "what it is..")
            return True


class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__()
        self.name = char_name
        self.description = char_description
        self.greetings = None
        self.evaluation = False

    def set_greetings(self, char_greetings):
        """Sets a greeting for the friend character."""
        self.greetings = char_greetings

    def get_greetings(self):
        """Returns the friends's greeting."""
        return self.greetings

    def greets(self):
        """Let the friend greet the player."""
        if self.greetings is not None:
            print("[" + self.name + " greets you]: " + self.greetings)
            return not None

        else:
            print(self.name + " doesn't want greet you")
            return None
