from behave import *
from item import Item


use_step_matcher("re")



@given("an item")
def step_impl(context):
    context.item = Item("cheese")


@when("asked the name of the item")
def step_impl(context):
    context.item_name = context.item.get_name_item()


@then("the correct name of the item should be returned")
def step_impl(context):
    assert context.item_name == 'cheese'

@given("another item")
def step_impl(context):
    context.item = Item("dog")


@when("it is settled a name for it")
def step_impl(context):
    context.new_name = context.item.set_name_item("shoe")


@then("the previous name should change to this new one")
def step_impl(context):
    assert context.item != context.new_name


@given("that an item has a description")
def step_impl(context):
    context.item = Item("cheese")
    context.description = context.item.desc_item


@when("is not settled yet")
def step_impl(context):
    context.get_desc = context.item.get_desc_item()


@then("the value of it should be None")
def step_impl(context):
    assert context.get_desc == context.description


@step("when it is settled one for the item")
def step_impl(context):
    context.set_desc = context.item.set_desc_item('a large and smelly block of cheese')


@then("the value of it should be not None")
def step_impl(context):
    assert context.set_desc == context.description


@given("yet again another item")
def step_impl(context):
    context.item = Item("heart")


@when("it is stolen")
def step_impl(context):
    context.stolen_item = context.item.item_stolen()


@then("the value returned from the function should be the name of the item")
def step_impl(context):
    assert context.stolen_item == "heart"


@given("a new item with a description")
def step_impl(context):
    context.item = Item("ball")
    context.item.desc_item = "a ballsing red ball"

@when("asked to describe this item")
def step_impl(context):
    context.describe = context.item.describe_item()

@then("the description of the object should be returned")
def step_impl(context):
    assert context.describe is not None