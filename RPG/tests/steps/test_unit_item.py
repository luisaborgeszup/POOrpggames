import unittest2
from item import Item


class ItemSteps2(unittest2.TestCase):


    def setUp(self):
        self.item = Item("cheese")


    def test_get_name(self):
        self.assertEqual(self.item.get_name_item(), "cheese", "The function isn't working correctly.")


    def test_set_name(self):
        self.item.set_name_item("dog")
        self.assertEqual(self.item.name_item, "dog", "The function isn't working correctly.")

    def test_get_description(self):
        self.assertEqual(self.item.get_desc_item(), None, "The function isn't working correctly.")

    def test_set_description(self):
        self.item.set_desc_item("a smelly block of cheese")
        self.assertEqual(self.item.desc_item, "a smelly block of cheese", "The function isn't working correctly.")

    def test_get_description_after_set_description(self):
        self.item.set_desc_item("a smelly block of cheese")
        self.assertEqual(self.item.get_desc_item(), "a smelly block of cheese", "The function isn't working correctly.")

    def test_describe_item_after_set_description(self):
        if self.item.name_item is not None:
            self.item.set_desc_item("a smelly block of cheese")
            self.assertEqual(self.item.describe_item(), not None, "The function isn't working correctly.")
        else:
            self.assertEqual(self.item.describe_item(), None, "The function isn't working correctly.")

    def test_stolen_item(self):
        self.assertEqual(self.item.name_item, self.item.item_stolen(), "The function isn't working correctly.")


if __name__ == "__main__":
    unittest2.main()