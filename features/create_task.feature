Feature: Website Dashboard

  Scenario: Open manage tasks
    Given I open the page
    Then I see "My Tasks"
    And I see message saying that list belongs to that user
    And I can create new task