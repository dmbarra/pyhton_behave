Feature: Create SubTask

  Background: Open and Login into app
    Given I open the page
    And I login on app
    And I have task

  @not_implemented
  Scenario: Create new subtask
    Given I open manage subtask
    When I fill subtask description
    And I fill the subtask date
    And I submit subtask
    Then the new subtask is present on list of subtasks

  @not_implemented
  Scenario: Create new subtask without description requirement
    Given I open manage subtask
    When I fill the subtask date
    And I submit subtask
    Then the app returns is missing required field

  @not_implemented
  Scenario: Create new subtask without date requirement
    Given I open manage subtask
    When I fill subtask description
    And I submit subtask
    Then the app returns is missing required field

  @not_implemented
  Scenario: Remove a subtask
    Given I open manage subtask
    When I remove subtask from list
    Then the subtask is removed