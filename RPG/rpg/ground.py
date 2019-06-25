from rpg import *
import numpy as np
import pandas as pd

class Ground:

    def __init__(self):
        self.room_list = Room.rooms
        self.backpack = {}
        self.character = None
        self.item = None
        self.linked_rooms = np.zeros(len(self.room_list)**2, dtype=int).reshape((len(self.room_list), len(self.room_list)))
        self.linked_rooms = pd.DataFrame(self.linked_rooms, index=self.room_list, columns=self.room_list)
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

    def defeated(self):
        Enemy.enemies_defeated += 1
        self.character = None
        return None

    def item_was_taken(self, stolen_item):
        self.backpack[stolen_item] = self.item
        self.item = None
        return None

    def item_stolen(self):
        return self.item


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
    map1.evaluate(kitchen, pool)
    print(map1.linked_rooms)
