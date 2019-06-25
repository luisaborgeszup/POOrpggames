# Created by luisa at 06/06/2019
  @TestRoom
Feature: Room functions
  Testing the functions from the Room class of my game
  
  Background: It will be used an empty room for the scenarios
    Given an empty room

  Scenario: Verify function get name from room
    When asked the name of the room
    Then the correct name of the room should be returned

  Scenario: Verify function set name of room
    When it is settled a name for the room
    Then the previous name of the room should change to this new one

  Scenario: Verify value returned from function get description from room
    When the description of the room is not settled yet
    Then the value of the description should be None
    And when it is settled one for the room
    Then the value of the description should be not None

  Scenario: Verify function describe room
    Given that the room has a description
    When asked to describe this room
    Then the description of the room should be returned

  Scenario: Verify function get and set character in the room
    When is settled a character in it
    Then the room should now have inside a character

  Scenario: Verify function get and set character in the room
    When is settled an item in it
    Then the room should now have inside an item

  Scenario: Verify function 'item was taken' from the room
    When the room has now an item
    And the item is taken from the room
    Then the room should be empty again

 Scenario: Verify function 'link to room'
   Given another room
   When this last is located at a certain direction
   And when applied the link between this two rooms
   Then the new room should be linked to the old one at the right direction

 Scenario: Verify function get details of the room
   Given that the room has a description, a item, a character and other rooms around
   When asked the details of the room
   Then it should be printed these information of it

 Scenario: Verify move function between rooms
   Given another room located at a certain direction
   When asked to move between them
   Then it be returned the room for which it is desired to go