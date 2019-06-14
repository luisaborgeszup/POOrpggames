# Created by luisa at 06/06/2019
  @TestCharacter
Feature: Character functions
  Testing the functions from the Character class of my game
  
  Background: It will be used a character, an enemy or a friend for the scenarios
    Given a character, an enemy or a friend

  Scenario: Verify function get name from character
    When asked the name of the character
    Then the correct name of the character should be returned

  Scenario: Verify function set name of character
    When it is settled a name for the character
    Then the previous name of the character should change to this new one

  Scenario: Verify value returned from function get description from character
    When the description of the character is changed
    Then the value of the description should be changed to this new one

  Scenario: Verify function describe character
    When asked to describe this character
    Then the description of the character should be returned

  Scenario: Verify function set conversation for a character
    When it is not settled a conversation for a character yet
    Then the value of his conversation should be None
    And when it is settled a conversation for a character
    Then it should now have a conversation

  Scenario: Verify talk function with a character
    When asked to talk to a character
    Then the character should not respond if he has not a conversation settled
    And if he now does have a conversation settled
    Then he will now talk back


  Scenario: Verify fight function with a character
    When asked to fight with a character
    Then he will not fight you back

  Scenario: Verify set and get weakness function for an enemy
    When is not settled a weakness for an enemy yet
    Then the value of the weakness should be None
    And when it is settled one for the enemy
    Then he should now have a weakness

  Scenario: Verify fight function with an enemy
    When asked to fight an enemy
    And the combat item used is the one which can defeat the enemy
    Then the enemy is defeated
    And if the combat item used is not the right one
    Then the enemy wins
    And if there is no combat item
    Then nothing will happen

  Scenario: Verify set and get stolen item function from an enemy
    When is not settled a stolen item from an enemy yet
    Then the value of the stolen item should be None
    And when it is settled one from the enemy
    Then it should now have a stolen item from the enemy

  Scenario: Verify function steal from a enemy
    When the enemy has no items to be stolen
    Then it is returned that he does not have something to be stolen
    And if he now has something to be stolen
    Then the item should be successfully stolen

  Scenario: Verify defeated function
    When the enemy has been defeated
    Then he now should be interpreted as a None value

  Scenario: Verify get and set defeated enemies
    When an enemy is defeated, the number of defeated enemies increases
    And it is settled this number in a class variable
    Then when asked this number, it should be returned

  Scenario: Verify number of defeats
    When asked the number of defeats
    Then a string containing this number should be returned

  Scenario: Verify set and get greetings
    When the friend does not have a greeting yet
    Then the value of the greeting should be None
    And if he now has a greeting
    Then the greeting should be returned

  Scenario: Verify greets function
    When asked to greet a friend and he does not have a greeting yet
    Then he will not greet you back
    And if now he has a greeting settled
    Then he will greet you back

