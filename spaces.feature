Feature: Spaces

  @wip
  Scenario: Creating a space
    Given "Frank" as the persona
    And I visit "/"
    And I am logged in as the current persona
    When I click the link with text "Create your own space"
    And I fill in "name" with the current timestamp
    And I fill in "#title" with "test space"
    And I fill in "textarea[name=public_description]" with "test space"
    And I fill in "textarea[name=description]" with "test space"
    And I press "create"
    Then I should see "your space has been created" within 5 seconds
    And the browser's url should contain the timestamp


  Scenario: Editing a space
  Scenario: Deleting a space
  Scenario: subscribe to space
  Scenario: unsubscribe to space
  Scenario: private spaces
  Scenario: moderated spaces
  Scenario: wiki
  Scenario: searching by space
  Scenario: Creating a house
  Scenario: Creating a space within a house