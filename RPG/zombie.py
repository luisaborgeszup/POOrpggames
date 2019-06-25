
from map import Map


class Player(object):

    def __init__(self, first_room):
        self.current_room = first_room

    def move(self, destination_room):
        map = Map()
        if map.evaluate(self.current_room, destination_room):
            self.current_room = destination_room
        else:
            raise Exception("Invalid movement")

    
if __name__ == "__main__":
    player = Player("kitchen")
    print("Current room before move call - " + player.current_room)
    player.move("living room")
    print("Current room after move call - " + player.current_room)


       


