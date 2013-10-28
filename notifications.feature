Feature: Notifications
  
  Background:
    Given state "standard-spaces"
  
  Scenario: There should a button to invite others to a space.
    Given "Fred Carpenter" as the persona
    When we visit "/space/test_space_42"
    Then there should be a link "Invite People to Space"

  Scenario: Inviting someone to a space should result in them getting a message.
    Given "Fred Carpenter" as the persona
    When I visit "http://lightnet.is/space/test_space_42"
    And I click the link with text that contains "Invite People to Space"
    And I set "@Edward_Foobin_1" to the text of "share-recipients"
    And I press "Invite"
    Then I should not see an element with id "share-recipients"
    Given "Edward Foobin" as the persona
    When I visit "http://lightnet.is/messages/"
    Then I should see "Fred_Carpenter_1 has invited you to /space/test_space_42"

  Scenario: Inviting someone to a space they are already subscribed to
      Unsure this should be a special case or not

  Scenario: Sharing an item with another user
    Given "Fred Carpenter" as the persona
    When I visit "$item_1_url"
    And I click the link with text that contains "share"
    And I set "@Edward_Foobin_1" to the text of "share-recipients"
    And I press "Share"
    Then I should not see an element with id "share-recipients"
    Given "Edward Foobin" as the persona
    When I visit "http://lightnet.is/messages/"
    Then I should see "Fred_Carpenter_1 has shared a link with you!"

  Scenario: Sharing a comment with another user
    Given "Fred Carpenter" as the persona
    When I visit "$item_1_url"
    And I click the "share" link in the first comment
    And I set "@Edward_Foobin_1" to the text of "share-recipients"
    And I press "Share"
    Then I should not see an element with id "share-recipients"
    Given "Edward Foobin" as the persona
    When I visit "http://lightnet.is/messages/"
    Then I should see "Fred_Carpenter_1 has shared a comment with you!"

  Scenario: Sharing a comment with another user
    Given "Fred Carpenter" as the persona
    When I visit "$item_1_url"
    And I click the "share" link in the first comment
    And I set "@Edward_Foobin_1" to the text of "share-recipients"
    And I press "Share"
    Then I should not see an element with id "share-recipients"
    Given "Edward Foobin" as the persona
    When I visit "http://lightnet.is/messages/"
    Then I should see "Fred_Carpenter_1 has shared a link with you!"


