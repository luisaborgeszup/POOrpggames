from behave import *
from character import Character, Enemy, Friend

use_step_matcher("re")


@given("a character, an enemy or a friend")
def step_impl(context):
    context.character = Character("Person", "an aleatory persona")
    context.enemy = Enemy("Dave", "a smelly zombie")
    context.friend = Friend("Catrina", "a friendly skeleton")


@when("asked the name of the character")
def step_impl(context):
    context.character_name = context.character.get_name()


@then("the correct name of the character should be returned")
def step_impl(context):
    assert context.character_name == "Person"


@when("it is settled a name for the character")
def step_impl(context):
    context.character.set_name("Human")


@then("the previous name of the character should change to this new one")
def step_impl(context):
    assert context.character.name == "Human"


@when("the description of the character is changed")
def step_impl(context):
    context.character.set_description("a person who breathes")


@then("the value of the description should be changed to this new one")
def step_impl(context):
    assert context.character.description == "a person who breathes"


@when("asked to describe this character")
def step_impl(context):
    context.describe_character = context.character.describe()


@then("the description of the character should be returned")
def step_impl(context):
    assert context.describe_character is not None


@when("it is not settled a conversation for a character yet")
def step_impl(context):
    context.character_desc = context.character.get_conversation()


@then("the value of his conversation should be None")
def step_impl(context):
    assert context.character_desc is None


@step("when it is settled a conversation for a character")
def step_impl(context):
    context.character.set_conversation("Greetings, I do nothing.")


@then("it should now have a conversation")
def step_impl(context):
    assert context.character.get_conversation() == "Greetings, I do nothing."


@when("asked to talk to a character")
def step_impl(context):
    context.talk = context.character.talk()


@then("the character should not respond if he has not a conversation settled")
def step_impl(context):
    assert context.talk is None


@step("if he now does have a conversation settled")
def step_impl(context):
    context.character.set_conversation("Greetings, I do nothing.")
    context.talk = context.character.talk()


@then("he will now talk back")
def step_impl(context):
    assert context.talk is not None


@when("asked to fight with a character")
def step_impl(context):
    context.fight = context.character.fight("cheese")


@then("he will not fight you back")
def step_impl(context):
    assert context.fight is True


@when("is not settled a weakness for an enemy yet")
def step_impl(context):
    context.weakness = context.enemy.get_weakness()


@then("the value of the weakness should be None")
def step_impl(context):
    assert context.weakness is None


@step("when it is settled one for the enemy")
def step_impl(context):
    context.enemy.set_weakness("cheese")


@then("he should now have a weakness")
def step_impl(context):
    assert context.enemy.get_weakness() == "cheese"


@when("asked to fight an enemy")
def step_impl(context):
    context.weakness = None
    context.enemy.set_weakness("cheese")
    context.enemy.fight(context.weakness)


@step("the combat item used is the one which can defeat the enemy")
def step_impl(context):
    context.weakness = context.enemy.get_weakness()


@then("the enemy is defeated")
def step_impl(context):
    assert context.enemy.fight(context.weakness) is True


@step("if the combat item used is not the right one")
def step_impl(context):
    context.enemy.set_weakness("dog")


@then("the enemy wins")
def step_impl(context):
    assert context.enemy.fight(context.weakness) is False


@step("if there is no combat item")
def step_impl(context):
    context.fight = context.enemy.fight(None)


@then("nothing will happen")
def step_impl(context):
    assert context.fight is None


@when("is not settled a stolen item from an enemy yet")
def step_impl(context):
    context.stolen_item = context.enemy.get_stolen_item()


@then("the value of the stolen item should be None")
def step_impl(context):
    assert context.stolen_item is None


@step("when it is settled one from the enemy")
def step_impl(context):
    context.enemy.set_stolen_item("meat")


@then("it should now have a stolen item from the enemy")
def step_impl(context):
    assert context.enemy.get_stolen_item() == "meat"


@when("the enemy has no items to be stolen")
def step_impl(context):
    context.enemy.set_stolen_item("nothing")


@then("it is returned that he does not have something to be stolen")
def step_impl(context):
    assert context.enemy.steal() is False


@step("if he now has something to be stolen")
def step_impl(context):
    context.enemy.set_stolen_item("meat")


@then("the item should be successfully stolen")
def step_impl(context):
    assert context.enemy.steal() is True


@when("the enemy has been defeated")
def step_impl(context):
    context.defeated_enemy = context.enemy.defeated()


@then("he now should be interpreted as a None value")
def step_impl(context):
    assert context.defeated_enemy is None


@when("an enemy is defeated, the number of defeated enemies increases")
def step_impl(context):
    context.enemy.set_weakness("cheese")
    context.enemy.fight("cheese")
    context.defeated_enemies = 1


@step("it is settled this number in a class variable")
def step_impl(context):
    context.enemy.set_defeated_enemies(context.defeated_enemies)


@then("when asked this number, it should be returned")
def step_impl(context):
    assert context.enemy.get_defeated_enemies() == 1


@when("asked the number of defeats")
def step_impl(context):
    context.enemy.set_defeated_enemies(1)
    context.number_of_defeats = context.enemy.number_of_defeats()


@then("a string containing this number should be returned")
def step_impl(context):
    assert context.number_of_defeats == "1"


@when("the friend does not have a greeting yet")
def step_impl(context):
    context.greetings = context.friend.get_greetings()


@then("the value of the greeting should be None")
def step_impl(context):
    assert context.greetings is None


@step("if he now has a greeting")
def step_impl(context):
    context.friend.set_greetings("Why hello there!")


@then("the greeting should be returned")
def step_impl(context):
    assert context.friend.get_greetings() == "Why hello there!"


@when("asked to greet a friend and he does not have a greeting yet")
def step_impl(context):
    context.greets = context.friend.greets()


@then("he will not greet you back")
def step_impl(context):
    assert context.greets is None


@step("if now he has a greeting settled")
def step_impl(context):
    context.friend.set_greetings("Why hello there!")


@then("he will greet you back")
def step_impl(context):
    assert context.friend.greets() is not None
