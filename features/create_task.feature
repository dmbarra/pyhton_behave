Feature: Website Dashboard

  Scenario: Open manage tasks
    Given I open the page
    And I login
    Then I see "My Tasks"
    And I see message saying that list belongs to that user
    And I can create new task