from rpg import *
import numpy as np
import pandas as pd

class Ground:

    def __init__(self):
        self.list = Room.rooms
        self.character = None
        self.linked_rooms = np.zeros(len(self.list)**2, dtype=int).reshape((len(self.list), len(self.list)))
        self.linked_rooms = pd.DataFrame(self.linked_rooms, index=self.list, columns=self.list)
        for i in range(self.linked_rooms.index.size):
            for j in range(self.linked_rooms.columns.size):
                if i == j:
                    self.linked_rooms.ix[i, j] = None

    def link_rooms(self, current_room, destination_room):
        for i in range(self.linked_rooms.index.size):
            for j in range(self.linked_rooms.columns.size):
                if (current_room.name == self.linked_rooms.index[i]) and (destination_room.name == self.linked_rooms.columns[j]):
                    self.linked_rooms.ix[i, j] = 1

    def evaluate(self, current_room, destination_room):
        for i in range(self.linked_rooms.index.size):
            for j in range(self.linked_rooms.columns.size):
                if (destination_room.get_name() == self.linked_rooms.columns[j]) and (current_room.get_name() == self.linked_rooms.columns[i]):
                    if self.linked_rooms.ix[i, j] == 1:
                        return True

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

    def defeated(self):
        self.character = None
        return None


if __name__ == "__main__":
    garden = Room("Garden")
    road = Room("Road")
    kitchen = Room("Kitchen")
    pool = Room("Pool")
    home = Room("Home")
    map1 = Ground()
    map1.link_rooms(garden, road)
    map1.link_rooms(garden, kitchen)
    map1.link_rooms(road, garden)
    map1.evaluate(pool)
    print(map1.linked_rooms)
