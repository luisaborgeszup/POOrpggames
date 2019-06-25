# Created by luisa at 06/06/2019
  @TestItem
Feature: Item functions
  Testing the functions from the Item class of my game

  Scenario: Verify function get name from item
    Given an item
    When asked the name of the item
    Then the correct name of the item should be returned

  Scenario: Verify function set name of item
    Given another item
    When it is settled a name for it
    Then the previous name should change to this new one

  Scenario: Verify if value returned from function get description from item
    Given that an item has a description
    When is not settled yet
    Then the value of it should be None
    And when it is settled one for the item
    Then the value of it should be not None

  Scenario: Verify function item stolen
    Given yet again another item
    When it is stolen
    Then the value returned from the function should be the name of the item

  Scenario: Verify function describe item
    Given a new item with a description
    When asked to describe this item
    Then the description of the object should be returned







