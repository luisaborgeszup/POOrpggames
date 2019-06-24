from rpg import *
from ground import Ground


class Player:

    def __init__(self):
        self.current_room = None

    def set_current_room(self, first_room):
        self.current_room = first_room

    def get_current_room(self):
        return self.current_room

    def move(self, current_room, destination_room):
        if map1.evaluate(current_room, destination_room):
            self.set_current_room(destination_room)
        else:
            print("There's no possible way to go to that room from here..")
            return False


if __name__ == "__main__":
    player = Player()
    map1 = Ground()
    garden = Room("Garden")
    road = Room("Road")
    kitchen = Room("Kitchen")
    pool = Room("Pool")
    home = Room("Home")
    map1 = Ground()
    map1.link_rooms(garden, road)
    map1.link_rooms(garden, kitchen)
    map1.link_rooms(kitchen, garden)
    player.set_current_room(kitchen)
    map1.get_details_room(kitchen)
    print(map1.linked_rooms)
    print(map1.evaluate(kitchen, pool))
    print("Current room before move call - ", player.current_room.get_name())
    player.move(kitchen, home)
    print("Current room after move call - " + player.current_room.get_name())

