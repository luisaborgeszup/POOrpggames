import unittest2
from room import Room
from item import Item
from character import Character, Enemy, Friend



class ItemSteps2(unittest2.TestCase):


    def setUp(self):
        self.room = Room("Kitchen")
        self.room_two = Room("Asgard")
        self.direction = "north"
        self.character = Character("Dave", "a smelly zombie")
        self.item = Item("cheese")
        self.room.link_to_room(self.room_two, self.direction)


    def test_get_name(self):
        self.assertEqual(self.room.get_name(), "Kitchen", "The function isn't working correctly.")


    def test_set_name(self):
        self.room.set_name("University")
        self.assertEqual(self.room.name, "University", "The function isn't working correctly.")

    def test_get_description(self):
        self.assertEqual(self.room.get_description(), None, "The function isn't working correctly.")

    def test_set_description(self):
        self.room.set_description("The worst place in the world.")
        self.assertEqual(self.room.description, "The worst place in the world.", "The function isn't working correctly.")

    def test_get_description_after_set_description(self):
        self.room.set_description("The worst place in the world.")
        self.assertEqual(self.room.get_description(), "The worst place in the world.", "The function isn't working "
                                                                                       "correctly.")

    def test_describe_room_after_set_description(self):
        if self.room.name is not None:
            self.room.set_description("The worst place in the world.")
            self.assertEqual(self.room.describe(), not None, "The function isn't working correctly.")
        else:
            self.assertEqual(self.room.describe(), None, "The function isn't working correctly.")

    def test_set_and_get_character(self):
        self.assertEqual(self.room.get_character(), None, "The function isn't working correctly.")
        self.room.set_character(self.character)
        self.assertEqual(self.room.get_character(), self.character, "The function isn't working correctly.")


    def test_set_and_get_item(self):
        self.assertEqual(self.room.get_item(), None, "The function isn't working correctly.")
        self.room.set_item(self.item)
        self.assertEqual(self.room.get_item(), self.item, "The function isn't working correctly.")

    def test_taken_item(self):
        self.room.set_item(self.item)
        self.room.item_was_taken()
        self.assertEqual(self.room.get_item(), None, "The function isn't working correctly.")

    def test_link_to_room(self):
        self.assertEqual(self.room.linked_rooms[self.direction], self.room_two, "The function isn't working correctly.")
        
    def test_get_details(self):
        self.room.set_description("A place where I cook my meals.")
        self.room.set_item(self.item)
        self.room.set_character(self.character)
        self.assertEqual(self.room.get_details(), not None, "The function isn't working correctly.")

    def test_move(self):
        self.room.move(self.direction)
        self.assertEqual(self.room.move(self.direction), self.room_two, "The function isn't working correctly.")

if __name__ == "__main__":
    unittest2.main()