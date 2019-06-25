from rpg import *
from ground import Ground


class Player:

    def __init__(self, first_room):
        self.current_room = Room(first_room)

    def move(self, current_room, destination_room):
        if map1.evaluate(current_room, destination_room):
            self.current_room = destination_room
        else:
            print("There's no possible way to go to that room from here..")
            return False

    def talk(self):
        current_character = self.current_room.get_character()
        if current_character.conversation is not None:
            print("[" + current_character.name + " says]: " + current_character.conversation)
            return not None
        else:
            print(current_character.name + " doesn't want to talk to you")
            return None

    def greets(self):
        current_character = self.current_room.get_character()
        if current_character.evaluation is True:
            if current_character.greetings is not None:
                print("[" + current_character.name + " greets you]: " + current_character.greetings)
                return not None

            else:
                print(current_character.name + " doesn't want greet you")
                return None

        elif current_character.evaluation is False:
            print(current_character.name + " doesn't look so friendly..")
            return None

        elif current_character.evaluation is None:
            print("There's no one here..")
            return None

    def fight(self, combat_item):
        if combat_item in map1.backpack:
            current_character = self.current_room.get_character()
            if current_character.evaluation is True:
                print("You can't fight " + current_character.name + ", he is a friend!")
                return False

            elif current_character.evaluation is False:
                if combat_item == current_character.weakness:
                    print("You fend " + current_character.name + " off with the " + combat_item + ", congrats!!")
                    map1.defeated()
                    Enemy.enemies_defeated += 1
                    return True

                elif combat_item is None:
                    print("")

                else:
                    print(current_character.name + " crushes you, puny adventurer!")
                    raise Exception("Press 'run' to restart the game!")

            elif current_character.evaluation is None:
                print("There's no one here..")
                return None

        else:
            print("You don't have this item in your backpack. Look around a little more..")
            return None

    def steal(self):
        current_character = self.current_room.get_character()
        if current_character.evaluation is True:
            print("You can't steal from " + current_character.name + "!")
            return None

        elif current_character.evaluation is False:
            print("You tried to steal from " + current_character.name)

            if current_character.stolen_item == "nothing":
                print("What a pity!")
                print(current_character.name + " had nothing to be stolen! Good luck next "
                                               "time!")
                return False

            else:
                print("Congrats! You've just conquered a item! Let's see\n"
                      "what it is..")
                print(map1.item_stolen())
                return True

    def number_of_defeats(self):
        print("Number of defeats: " + str(Enemy.enemies_defeated))


if __name__ == "__main__":
    player = Player("Kitchen")
    dave = Enemy("Dave", "a smelly zombie")
    map1 = Ground()
    garden = Room("Garden")
    garden.set_character(dave)
    road = Room("Road")
    kitchen = Room("Kitchen")
    pool = Room("Pool")
    home = Room("Home")
    map1 = Ground()
    map1.link_rooms(garden, road)
    map1.link_rooms(garden, kitchen)
    map1.link_rooms(kitchen, garden)
    print(map1.linked_rooms)
    print(map1.evaluate(kitchen, pool))
    print("Current room before move call - ", player.current_room.get_name())
    player.move(kitchen, home)
    print("Current room after move call - " + player.current_room.get_name())
    print(player.number_of_defeats())
