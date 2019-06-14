import unittest2
from character import Character, Enemy, Friend


class CharacterSteps2(unittest2.TestCase):

    def setUp(self):
        self.character = Character("Person", "an aleatory persona")
        self.enemy = Enemy("Dave", "a smelly zombie")
        self.friend = Friend("Catrina", "a friendly skeleton")
        self.defeated_enemies = 0

    def test_get_name(self):
        self.assertEqual(self.character.get_name(), "Person", "The function isn't working correctly.")

    def test_set_name(self):
        self.character.set_name("Hooman")
        self.assertEqual(self.character.name, "Hooman", "The function isn't working correctly.")

    def test_get_description(self):
        self.assertEqual(self.character.get_description(), "an aleatory persona",
                         "The function isn't working correctly.")

    def test_set_description(self):
        self.character.set_description("the best friend of a doggo")
        self.assertEqual(self.character.description, "the best friend of a doggo",
                         "The function isn't working correctly.")

    def test_describe_character(self):
        if self.character.name is not None:
            self.assertEqual(self.character.describe(), not None, "The function isn't working correctly.")
        else:
            self.assertEqual(self.character.describe(), None, "The function isn't working correctly.")

    def test_get_and_set_conversation(self):
        self.assertEqual(self.character.get_conversation(), None, "The function isn't working correctly.")
        self.character.set_conversation("I do nothing.")
        self.assertEqual(self.character.conversation, "I do nothing.", "The function isn't working correctly.")

    def test_talk(self):
        self.assertEqual(self.character.talk(), None, "The function isn't working correctly.")
        self.character.set_conversation("I do nothing.")
        self.assertEqual(self.character.talk(), not None, "The function isn't working correctly.")

    def test_fight_character(self):
        self.assertEqual(self.character.fight("cheese"), True, "The function isn't working correctly.")

    def test_get_and_set_wakness(self):
        self.assertEqual(self.enemy.get_weakness(), None, "The function isn't working correctly.")
        self.enemy.set_weakness("cheese")
        self.assertEqual(self.enemy.get_weakness(), "cheese", "The function isn't working correctly.")

    def test_fight_enemy(self):
        self.enemy.set_weakness("cheese")
        self.assertEqual(self.enemy.fight("cheese"), True, "The function isn't working correctly.")
        self.assertEqual(self.enemy.fight("dog"), False, "The function isn't working correctly.")
        self.assertEqual(self.enemy.fight(None), None, "The function isn't working correctly.")

    def test_set_and_get_stolen_item(self):
        self.assertEqual(self.enemy.get_stolen_item(), None, "The function isn't working correctly.")
        self.enemy.set_stolen_item("meat")
        self.assertEqual(self.enemy.get_stolen_item(), "meat", "The function isn't working correctly.")

    def test_steal_enemy(self):
        self.enemy.set_stolen_item("nothing")
        self.assertEqual(self.enemy.steal(), False, "The function isn't working correctly.")
        self.enemy.set_stolen_item("meat")
        self.assertEqual(self.enemy.steal(), True, "The function isn't working correctly.")

    def test_defeated_enemy(self):
        self.assertEqual(self.enemy.defeated(), None, "The function isn't working correctly.")

    def test_set_and_get_defeated_enemies(self):
        self.enemy.set_defeated_enemies(self.defeated_enemies)
        self.assertEqual(self.enemy.get_defeated_enemies(), 0, "The function isn't working correctly.")

    def test_number_of_defeats(self):
        self.enemy.set_defeated_enemies(1)
        self.assertEqual(self.enemy.number_of_defeats(), "1", "The function isn't "
                                                                                            "working correctly.")
    def test_get_and_set_greetings(self):
        self.assertEqual(self.friend.get_greetings(), None, "The function isn't working correctly.")
        self.friend.set_greetings("Why hello there!")
        self.assertEqual(self.friend.get_greetings(), "Why hello there!", "The function isn't working correctly.")

    def test_greets(self):
        self.assertEqual(self.friend.greets(), None, "The function isn't working correctly.")
        self.friend.set_greetings("Why hello there!")
        self.assertEqual(self.friend.greets(), not None, "The function isn't working correctly.")


if __name__ == "__main__":
    unittest2.main()
