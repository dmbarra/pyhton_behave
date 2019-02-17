Feature: Create Task

  Background: Open and Login into app
    Given I open the page
    And I login on app

  Scenario: Open manage tasks
    Then I see "My Tasks"
    And I see message saying that list belongs to that user
    And I can create new task

  Scenario: Create new task
    When I add new task
    Then the new task is present on list
    And numbers of subtasks is zero

  @not_implemented
  Scenario: Create new task without required title
    When I add new task without required field
    Then the new task is present on list

  @not_implemented
  Scenario: Remove task
    When I remove a task
    Then the task is removed