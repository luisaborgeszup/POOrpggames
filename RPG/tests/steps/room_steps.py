from behave import *
from room import Room
from item import Item
from character import Character, Enemy, Friend

use_step_matcher("re")


@given("an empty room")
def step_impl(context):
    context.room = Room("kitchen")


@when("asked the name of the room")
def step_impl(context):
    context.room_name = context.room.get_name()


@then("the correct name of the room should be returned")
def step_impl(context):
    assert context.room_name == "kitchen"


@when("it is settled a name for the room")
def step_impl(context):
    context.room.set_name("Living Room")


@then("the previous name of the room should change to this new one")
def step_impl(context):
    assert context.room.name == "Living Room"


@when("the description of the room is not settled yet")
def step_impl(context):
    context.room_description = context.room.get_description()


@then("the value of the description should be None")
def step_impl(context):
    assert context.room_description is None


@step("when it is settled one for the room")
def step_impl(context):
    context.room.set_description("A place where I cook my meals.")


@then("the value of the description should be not None")
def step_impl(context):
    assert context.room.description == "A place where I cook my meals."


@given("that the room has a description")
def step_impl(context):
    context.room.set_description("A place where I cook my meals.")


@when("asked to describe this room")
def step_impl(context):
    context.describe_room = context.room.describe()


@then("the description of the room should be returned")
def step_impl(context):
    assert context.describe_room is not None


@when("is settled a character in it")
def step_impl(context):
    context.character = Enemy("Dave", "A smelly zombie")
    context.room.set_character(context.character)


@then("the room should now have inside a character")
def step_impl(context):
    assert context.room.get_character() == context.character


@when("is settled an item in it")
def step_impl(context):
    context.item = Item("space ship")
    context.room.set_item(context.item)


@then("the room should now have inside an item")
def step_impl(context):
    assert context.room.get_item() == context.item


@when("the room has now an item")
def step_impl(context):
    context.item = Item("yakult")
    context.room.set_item(context.item)


@step("the item is taken from the room")
def step_impl(context):
    context.room.item_was_taken()


@then("the room should be empty again")
def step_impl(context):
    assert context.room.get_item() is None


@given("another room")
def step_impl(context):
    context.room_two = Room("Bedroom")


@when("this last is located at a certain direction")
def step_impl(context):
    context.direction = "north"


@step("when applied the link between this two rooms")
def step_impl(context):
    context.room.link_to_room(context.room_two, context.direction)


@then("the new room should be linked to the old one at the right direction")
def step_impl(context):
    assert context.room.linked_rooms[context.direction] == context.room_two


@given("that the room has a description, a item, a character and other rooms around")
def step_impl(context):
    context.room.set_description("A place where I cook my meals.")
    context.room_two = Room("Nárnia")
    context.room_three = Room("Asgard")
    context.item = Item("mjolnir")
    context.character = Friend("Ragnar Lothbrok", "the most awesome viking")
    context.direction_one = "north"
    context.direction_two = "west"
    context.room.link_to_room(context.room_two, context.direction_one)
    context.room.link_to_room(context.room_three, context.direction_two)


@when("asked the details of the room")
def step_impl(context):
    context.details_room = context.room.get_details()


@then("it should be printed these information of it")
def step_impl(context):
    assert context.details_room is not None


@given("another room located at a certain direction")
def step_impl(context):
    context.room_two = Room("Basement")
    context.direction = "north"


@when("asked to move between them")
def step_impl(context):
    context.room.link_to_room(context.room_two, context.direction)
    context.move = context.room.move(context.direction)

@then("it be returned the room for which it is desired to go")
def step_impl(context):
    assert context.move == context.room_two