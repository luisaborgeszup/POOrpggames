class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        """Initialises the character with a name, a description and
        initiates the conversation with a non existing value."""
        self.name = char_name
        self.description = char_description
        self.conversation = None

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
        else:
            print("")

    def set_conversation(self, conversation):
        """Defines a character's response to when it is spoken to."""
        self.conversation = conversation

    def talk(self):
        """Talks to the character only if he has a response."""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Fights with the character, but it only do so if the character is an enemy."""
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        """Initialises the enemy with the same attributes as a regular
        character plus a weakness and a stolen item, both with non existing values."""
        super().__init__(char_name,char_description)
        self.weakness = None
        self.stolen_item = None

    def fight(self, combat_item):
        """Fights with the enemy. If the enemy wins, the game ends. If the player wins,
        the game continues."""
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item + ", congrats!!")
            Enemy.enemies_defeated += 1

            return True

        elif combat_item == None:
            print("")

        else:
            print(self.name + " crushes you, puny adventurer!")
            return False

    def set_weakness(self, item_weakness):
        """Sets the weakness of the enemy."""
        self.weakness = item_weakness

    def get_weakness(self):
        """Returns the weakness of the enemy."""
        return self.weakness

    def get_defeated_enemies(self):
        """Returns the number of enemies whom were defeated by the player."""
        return Enemy.enemies_defeated

    def set_defeated_enemies(self, defeated_enemies):
        """Sets the number of enemies whom wherr defeated by the player."""
        Enemy.enemies_defeated = defeated_enemies

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

    def defeated(self):
        """Sets the enemy as a non existing value so he doesn't shows up
        in them game again if he has been defeated."""
        self.name = None
        return None

    def number_of_defeats(self):
        """Returns the string equivalent to the number of enemies whom
        were defeated by the player."""
        return str(self.get_defeated_enemies())



class Friend(Character):

    def __init__(self, char_name, char_description):
        """Initialises the enemy with the same attributes as a regular
                character plus greetings with a non existing value."""
        super().__init__(char_name,char_description)
        self.greetings = None

    def set_greetings(self, char_greetings):
        """Sets a greeting for the friend character."""
        self.greetings = char_greetings

    def get_greetings(self):
        """Returns the friends's greeting."""
        return self.greetings

    def greets(self):
        """Let the friend greet the player."""
        print("[" + self.name + " greets you]: " + self.greetings)




